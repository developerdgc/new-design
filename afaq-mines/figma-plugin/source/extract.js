// Walk the rendered DOM of each page and emit a Figma-ready node list (absolute layout, editable).
const { chromium } = require('playwright');
const fs = require('fs');
const [,, htmlPath, outDir, exe] = process.argv;
const PAGES = ['home','about','why-afaq','team','global','why-pakistan','regions','metallic','industrial','gemstones','products','processing','inquiry','contact'];

function walker() {
  const out = [];
  let uid = 0;
  const symbols = {};
  document.querySelectorAll('symbol').forEach(s => symbols[s.id] = s);
  const num = v => parseFloat(v) || 0;
  const parseColor = c => {
    const m = c && c.match(/rgba?\(([^)]+)\)/);
    if (!m) return null;
    const p = m[1].split(/[ ,\/]+/).filter(Boolean).map(Number);
    return { r: p[0] / 255, g: p[1] / 255, b: p[2] / 255, a: p.length > 3 ? p[3] : 1 };
  };
  function splitTop(s) { // split by commas not inside parens
    const r = []; let d = 0, cur = '';
    for (const ch of s) { if (ch === '(') d++; if (ch === ')') d--; if (ch === ',' && d === 0) { r.push(cur.trim()); cur = ''; } else cur += ch; }
    if (cur.trim()) r.push(cur.trim()); return r;
  }
  function parseBgImage(bi) {
    if (!bi || bi === 'none') return [];
    const layers = splitTop(bi);
    const res = [];
    for (const L of layers) {
      let m = L.match(/^url\("?(.*?)"?\)$/);
      if (m) { res.push({ t: 'img', src: m[1].replace(location.href.split('#')[0].replace(/[^/]*$/, ''), '') }); continue; }
      m = L.match(/^(?:linear-gradient)\((.*)\)$/);
      if (m) {
        const parts = splitTop(m[1]); let angle = 180;
        if (/deg$/.test(parts[0])) { angle = parseFloat(parts.shift()); }
        else if (/^to /.test(parts[0])) { const t = parts.shift(); angle = { 'to right': 90, 'to left': 270, 'to bottom': 180, 'to top': 0 }[t] ?? 180; }
        const stops = parts.map((p, i) => {
          const c = parseColor(p); const pm = p.match(/\)\s+([\d.]+)%/);
          return { c, p: pm ? parseFloat(pm[1]) / 100 : null };
        }).filter(s => s.c);
        stops.forEach((s, i) => { if (s.p == null) s.p = stops.length === 1 ? 0 : i / (stops.length - 1); });
        res.push({ t: 'lg', angle, stops });
        continue;
      }
      m = L.match(/^radial-gradient\((.*)\)$/);
      if (m) { const cs = splitTop(m[1]).map(parseColor).filter(Boolean); if (cs.length) res.push({ t: 'solid', c: cs[cs.length - 1], weak: true }); }
    }
    return res;
  }
  function radius(cs, w, h) {
    const f = v => v.includes('%') ? Math.min(w, h) * parseFloat(v) / 100 : num(v);
    return [f(cs.borderTopLeftRadius), f(cs.borderTopRightRadius), f(cs.borderBottomRightRadius), f(cs.borderBottomLeftRadius)];
  }
  function shadow(cs) {
    const s = cs.boxShadow; if (!s || s === 'none') return null;
    const first = splitTop(s)[0]; const c = parseColor(first); if (!c) return null;
    const nums = first.replace(/rgba?\([^)]*\)/, '').trim().split(/\s+/).map(num);
    return { c, x: nums[0] || 0, y: nums[1] || 0, b: nums[2] || 0, s: nums[3] || 0, inset: /inset/.test(first) };
  }
  function boxProps(cs, w, h) {
    const fills = [];
    const bg = parseColor(cs.backgroundColor);
    if (bg && bg.a > 0.01) fills.push({ t: 'solid', c: bg });
    const imgs = parseBgImage(cs.backgroundImage).reverse(); // css first layer is on top
    fills.push(...imgs);
    let stroke = null, sides = null;
    const bw = [cs.borderTopWidth, cs.borderRightWidth, cs.borderBottomWidth, cs.borderLeftWidth].map(num);
    const bcs = [cs.borderTopColor, cs.borderRightColor, cs.borderBottomColor, cs.borderLeftColor].map(parseColor);
    const vis = bw.map((v, i) => v > 0 && bcs[i] && bcs[i].a > 0.01 && cs['border' + ['Top', 'Right', 'Bottom', 'Left'][i] + 'Style'] !== 'none');
    if (vis.some(Boolean)) {
      const i = vis.indexOf(true);
      stroke = { c: bcs[i], w: bw[i] };
      if (!vis.every(Boolean)) sides = vis.map((v, k) => v ? bw[k] : 0);
    }
    return { fills, stroke, sides, r: radius(cs, w, h), sh: shadow(cs), op: num(cs.opacity) };
  }
  const visible = (el, cs) => cs.display !== 'none' && cs.visibility !== 'hidden' && num(cs.opacity) > 0.01;
  const isClip = cs => ['hidden', 'clip'].includes(cs.overflowX) || ['hidden', 'clip'].includes(cs.overflowY);
  const SKIP = new Set(['SCRIPT', 'STYLE', 'TITLE', 'LINK', 'META', 'NOSCRIPT', 'TEMPLATE', 'OPTION', 'OPTGROUP']);
  const fontOf = cs => ({ s: num(cs.fontSize), w: Math.round(num(cs.fontWeight) / 100) * 100, i: cs.fontStyle === 'italic', c: parseColor(cs.color), stroke: num(cs.webkitTextStrokeWidth) ? { w: num(cs.webkitTextStrokeWidth), c: parseColor(cs.webkitTextStrokeColor) } : null });
  function isTextLeaf(el) {
    let hasText = false;
    for (const n of el.childNodes) {
      if (n.nodeType === 3) { if (n.textContent.trim()) hasText = true; }
      else if (n.nodeType === 1) {
        if (n.tagName === 'BR') continue;
        const cs = getComputedStyle(n);
        if (cs.display === 'none') continue;
        if (cs.display !== 'inline' || ['svg', 'IMG', 'INPUT', 'SELECT', 'TEXTAREA', 'BUTTON'].includes(n.tagName)) return false;
        const bg = parseColor(cs.backgroundColor);
        if (bg && bg.a > 0.01) return false;
        if (!isTextLeaf(n) && n.textContent.trim()) return false;
        if (n.textContent.trim()) hasText = true;
      }
    }
    return hasText;
  }
  function segments(el, acc) {
    for (const n of el.childNodes) {
      if (n.nodeType === 3) acc.push({ t: n.textContent.replace(/\s+/g, ' '), f: fontOf(getComputedStyle(el)), tt: getComputedStyle(el).textTransform });
      else if (n.nodeType === 1) {
        if (n.tagName === 'BR') { acc.push({ t: '\n', f: fontOf(getComputedStyle(el)) }); continue; }
        if (getComputedStyle(n).display === 'none') continue;
        segments(n, acc);
      }
    }
    return acc;
  }
  function cleanSegs(segs) {
    // collapse whitespace across boundaries, trim ends
    let prevSpace = true;
    for (const s of segs) {
      if (s.t === '\n') { prevSpace = true; continue; }
      if (prevSpace) s.t = s.t.replace(/^ /, '');
      if (s.t.length) prevSpace = s.t.endsWith(' ');
      if (s.tt === 'uppercase') s.t = s.t.toUpperCase();
    }
    for (let i = segs.length - 1; i >= 0; i--) { const s = segs[i]; if (s.t === '\n') continue; s.t = s.t.replace(/ $/, ''); if (s.t.length) break; }
    // remove spaces before newline
    for (let i = 0; i < segs.length - 1; i++) if (segs[i + 1].t === '\n') segs[i].t = segs[i].t.replace(/ $/, '');
    return segs.filter(s => s.t.length);
  }
  function textNode(rect, cs, segs, base) {
    const lh = cs.lineHeight === 'normal' ? num(cs.fontSize) * 1.25 : num(cs.lineHeight);
    return { k: 'text', x: rect.x, y: rect.y, w: rect.w, h: rect.h, segs, lh, ls: cs.letterSpacing === 'normal' ? 0 : num(cs.letterSpacing), al: cs.textAlign, op: num(cs.opacity), ...base };
  }
  function svgString(el, cs) {
    const c = el.cloneNode(true);
    c.querySelectorAll('use').forEach(u => {
      const id = (u.getAttribute('href') || u.getAttribute('xlink:href') || '').slice(1);
      const s = symbols[id]; if (!s) return;
      if (s.getAttribute('viewBox') && !c.getAttribute('viewBox')) c.setAttribute('viewBox', s.getAttribute('viewBox'));
      const g = document.createElementNS('http://www.w3.org/2000/svg', 'g'); g.innerHTML = s.innerHTML; u.replaceWith(g);
    });
    const r = el.getBoundingClientRect();
    if (!c.getAttribute('viewBox')) c.setAttribute('viewBox', `0 0 ${r.width} ${r.height}`);
    c.setAttribute('width', r.width); c.setAttribute('height', r.height);
    c.setAttribute('xmlns', 'http://www.w3.org/2000/svg');
    const col = cs.color;
    const fill = cs.fill === 'none' ? 'none' : (cs.fill.startsWith('rgb') ? cs.fill : col);
    const stroke = cs.stroke === 'none' ? 'none' : (cs.stroke.startsWith('rgb') ? cs.stroke : col);
    c.setAttribute('fill', fill); c.setAttribute('stroke', stroke);
    c.setAttribute('stroke-width', cs.strokeWidth || '1.8'); c.setAttribute('stroke-linecap', cs.strokeLinecap); c.setAttribute('stroke-linejoin', cs.strokeLinejoin);
    c.removeAttribute('class'); c.removeAttribute('style');
    return c.outerHTML.replace(/currentColor/g, col);
  }
  const SY = window.scrollY;
  function abs(r) { return { x: r.left, y: r.top + SY, w: r.width, h: r.height }; }

  function pseudoBox(el, which, er) {
    const cs = getComputedStyle(el, which);
    if (!cs.content || cs.content === 'none' || cs.display === 'none') return null;
    const p = boxProps(cs, num(cs.width), num(cs.height));
    if (!p.fills.length && !p.stroke) return null;
    let x = er.x, y = er.y, w = num(cs.width), h = num(cs.height);
    if (cs.position === 'absolute') {
      const L = cs.left, R = cs.right, T = cs.top, B = cs.bottom;
      x = L !== 'auto' ? er.x + num(L) : er.x + er.w - num(R) - w;
      y = T !== 'auto' ? er.y + num(T) : er.y + er.h - num(B) - h;
    } else return null;
    if (w < 1 || h < 1) return null;
    return { k: 'box', name: (el.className && typeof el.className === 'string' ? el.className.split(' ')[0] : el.tagName.toLowerCase()) + which, x, y, w, h, ...p, z: num(cs.zIndex) };
  }

  function visit(el, parentClip, list) {
    if (SKIP.has(el.tagName)) return;
    const cs = getComputedStyle(el);
    if (!visible(el, cs)) return;
    if (el.tagName === 'symbol' || el.tagName === 'defs') return;
    const rr = el.getBoundingClientRect();
    const r = abs(rr);
    const name = (typeof el.className === 'string' && el.className ? el.className.split(' ')[0] : el.tagName.toLowerCase());
    if (el.tagName === 'svg') {
      if (r.w < 2 || r.h < 2) return;
      list.push({ k: 'svg', name: 'icon', ...r, svg: svgString(el, cs), op: num(cs.opacity) });
      return;
    }
    if (el.tagName === 'IMG') {
      if (r.w < 2 || r.h < 2) return;
      const p = boxProps(cs, r.w, r.h);
      list.push({ k: 'box', name: 'image', ...r, ...p, fills: [{ t: 'img', src: el.getAttribute('src') }], z: cs.zIndex === 'auto' ? 0 : num(cs.zIndex) });
      return;
    }
    const zero = r.w < 0.5 || r.h < 0.5;
    if (zero && !isClip(cs) && el.children.length === 0) return;
    const p = boxProps(cs, r.w, r.h);
    const clip = isClip(cs) && !zero && el.tagName !== 'BODY' && el.tagName !== 'HTML';
    const node = { k: clip ? 'frame' : 'box', name, ...r, ...p, z: cs.zIndex === 'auto' ? 0 : num(cs.zIndex), kids: [] };
    const hasBox = p.fills.length || p.stroke || p.sh;
    // form controls
    if (['INPUT', 'SELECT', 'TEXTAREA'].includes(el.tagName)) {
      if (el.type === 'radio' || el.type === 'checkbox') {
        const ch = el.checked; const ac = parseColor(cs.accentColor) || { r: .75, g: .54, b: .16, a: 1 };
        list.push({ k: 'radio', name: 'radio', ...r, on: ch, c: ac });
        return;
      }
      list.push({ ...node, k: 'box', kids: undefined });
      let t = el.tagName === 'SELECT' ? (el.options[el.selectedIndex] || {}).text || '' : (el.value || el.placeholder || '');
      if (t) {
        const ph = !el.value && el.tagName !== 'SELECT';
        const f = fontOf(cs); if (ph) { const pc = parseColor(getComputedStyle(el, '::placeholder').color); if (pc) f.c = pc; }
        const pl = num(cs.paddingLeft), pt = num(cs.paddingTop), pr = num(cs.paddingRight);
        const lh = cs.lineHeight === 'normal' ? f.s * 1.3 : num(cs.lineHeight);
        const ty = el.tagName === 'TEXTAREA' ? r.y + pt : r.y + (r.h - lh) / 2;
        list.push(textNode({ x: r.x + pl, y: ty, w: r.w - pl - pr, h: lh }, cs, [{ t, f }], { name: 'field-text' }));
      }
      return;
    }
    const target = clip ? node.kids : list;
    if (clip) list.push(node); else if (hasBox) list.push({ ...node, kids: undefined });
    // children incl pseudos, ordered by z
    const items = [];
    const b = pseudoBox(el, '::before', r); if (b) items.push({ z: b.z, ord: 0, pseudo: b });
    let ord = 1;
    if (isTextLeaf(el)) {
      const segs = cleanSegs(segments(el, []));
      if (segs.length) {
        const pl = num(cs.paddingLeft), pr = num(cs.paddingRight), pt = num(cs.paddingTop), pb = num(cs.paddingBottom);
        const bl = num(cs.borderLeftWidth), bt = num(cs.borderTopWidth);
        let tr;
        if (cs.display === 'inline') {
          const rg = document.createRange(); rg.selectNodeContents(el); const q = rg.getBoundingClientRect(); tr = abs(q);
        } else tr = { x: r.x + pl + bl, y: r.y + pt + bt, w: r.w - pl - pr - 2 * bl, h: r.h - pt - pb - 2 * bt };
        // for flex/grid centered single text, measure actual text range
        if (/flex|grid/.test(cs.display)) { const rg = document.createRange(); rg.selectNodeContents(el); tr = abs(rg.getBoundingClientRect()); }
        items.push({ z: 0, ord: ord++, node: textNode(tr, cs, segs, { name: 'text' }) });
      }
    } else {
      for (const ch of el.childNodes) {
        if (ch.nodeType === 3 && ch.textContent.trim()) {
          const rg = document.createRange(); rg.selectNodeContents(ch); const q = abs(rg.getBoundingClientRect());
          const segs = cleanSegs([{ t: ch.textContent.replace(/\s+/g, ' '), f: fontOf(cs), tt: cs.textTransform }]);
          if (segs.length && q.w > 0) items.push({ z: 0, ord: ord++, node: textNode(q, cs, segs, { name: 'text' }) });
        } else if (ch.nodeType === 1) {
          const ccs = getComputedStyle(ch);
          const z = ccs.position !== 'static' && ccs.zIndex !== 'auto' ? num(ccs.zIndex) : 0;
          items.push({ z, ord: ord++, el: ch });
        }
      }
    }
    const a = pseudoBox(el, '::after', r); if (a) items.push({ z: a.z, ord: ord++, pseudo: a });
    items.sort((x, y) => (x.z - y.z) || (x.ord - y.ord));
    for (const it of items) {
      if (it.pseudo) target.push(it.pseudo);
      else if (it.node) target.push(it.node);
      else visit(it.el, clip ? node : parentClip, target);
    }
  }
  const root = [];
  visit(document.body, null, root);
  return root;
}

(async () => {
  const b = await chromium.launch({ args: ['--no-sandbox'], executablePath: exe });
  const p = await b.newPage({ viewport: { width: 1440, height: 900 } });
  await p.goto('file://' + htmlPath);
  await p.addStyleTag({ content: '*,*::before,*::after{animation:none!important;transition:none!important}.ticker .track{transform:none!important}' });
  await p.waitForTimeout(2500);
  for (const pg of PAGES) {
    await p.evaluate(h => { location.hash = h; }, pg);
    await p.waitForTimeout(900);
    await p.evaluate(() => window.scrollTo(0, 0));
    await p.waitForTimeout(400);
    const H = await p.evaluate(() => document.documentElement.scrollHeight);
    const tree = await p.evaluate(walker);
    fs.writeFileSync(`${outDir}/${pg}.json`, JSON.stringify({ page: pg, w: 1440, h: H, tree }));
    console.log(pg, H, JSON.stringify(tree).length);
  }
  await b.close();
})();
