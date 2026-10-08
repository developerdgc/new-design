// Walks the rendered homepage and writes a compact layout tree for the Figma builder.
// Usage: W=1440 OUT=tree-desktop.json node extract.js
const { chromium } = require('playwright');
const path = require('path');
const GF = path.join(__dirname, '..', 'gf');

(async () => {
  const W = +(process.env.W || 1440);
  const b = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium' });
  const p = await b.newPage({ viewport: { width: W, height: 900 }, deviceScaleFactor: 2 });
  await p.route(/fonts\.googleapis\.com/, r => r.fulfill({ path: GF + '/gf.css', contentType: 'text/css' }));
  await p.route(/fonts\.gstatic\.com/, r => r.fulfill({ path: GF + '/' + r.request().url().split('/').pop(), contentType: 'font/woff2' }));
  await p.goto('http://localhost:8765/portfolio-artifact.html', { waitUntil: 'load' });
  await p.addStyleTag({ content: '*{animation-play-state:paused!important;transition:none!important} .site-head{position:absolute!important;transform:none!important} .cursor{display:none!important} .__nopse::before,.__nopse::after{content:none!important}' });
  const tree = await p.evaluate(async () => {
    for (const i of document.images) i.loading = 'eager';
    const H0 = document.body.scrollHeight;
    for (let y = 0; y < H0; y += 400) { scrollTo(0, y); await new Promise(r => setTimeout(r, 50)); }
    scrollTo(0, 0);
    document.querySelectorAll('body *').forEach(e => { if (getComputedStyle(e).opacity === '0' && !e.closest('dialog')) e.style.opacity = 1; });
    await Promise.all([...document.images].map(i => i.complete ? 0 : new Promise(r => { i.onload = i.onerror = r; })));
    await document.fonts.ready;
    await new Promise(r => setTimeout(r, 500));

    // Turn ::before / ::after into real elements so they get boxes.
    const pseudo = [];
    document.querySelectorAll('body *').forEach(el => {
      if (el.closest('dialog,script,style,svg')) return;
      for (const which of ['::before', '::after']) {
        const cs = getComputedStyle(el, which);
        if (!cs.content || cs.content === 'none' || cs.content === 'normal' || cs.display === 'none') continue;
        pseudo.push([el, which, cs]);
      }
    });
    for (const [el, which, cs] of pseudo) {
      const s = document.createElement('span');
      s.dataset.pseudo = which.slice(2);
      for (let i = 0; i < cs.length; i++) { const k = cs[i]; s.style.setProperty(k, cs.getPropertyValue(k)); }
      let txt = '';
      if (/counter\(/.test(cs.content)) {
        const sib = [...el.parentElement.children].filter(x => x.tagName === el.tagName && x.className === el.className);
        const idx = sib.indexOf(el) + 1;
        txt = cs.content.split(/\s+(?=(?:[^"]*"[^"]*")*[^"]*$)/).map(t => t.startsWith('"') ? t.slice(1, -1) : /counter\(/.test(t) ? String(idx) : '').join('');
      } else { const m = cs.content.match(/^"(.*)"$/s); txt = m ? m[1] : ''; }
      s.textContent = txt;
      s.__cls = (el.className && el.className.baseVal === undefined ? el.className : '') + ' ' + which;
      if (which === '::before') el.insertBefore(s, el.firstChild); else el.appendChild(s);
    }
    pseudo.forEach(([el]) => el.classList.add('__nopse'));
    await new Promise(r => setTimeout(r, 200));

    const VW = document.documentElement.clientWidth;
    const num = v => parseFloat(v) || 0;
    function col(s) {
      if (!s || s === 'transparent') return null;
      let m = s.match(/rgba?\(([^)]+)\)/);
      let a = 1, r, g, bb;
      if (m) { const q = m[1].split(/[ ,/]+/).filter(Boolean).map(parseFloat); [r, g, bb] = q; if (q.length > 3) a = q[3]; r /= 255; g /= 255; bb /= 255; }
      else if ((m = s.match(/color\(srgb ([^)]+)\)/))) { const q = m[1].split(/[ /]+/).filter(Boolean).map(parseFloat); [r, g, bb] = q; if (q.length > 3) a = q[3]; }
      else return null;
      if (a <= 0.003) return null;
      return [+r.toFixed(4), +g.toFixed(4), +bb.toFixed(4), +(+a).toFixed(3)];
    }
    function splitTop(s) { const out = []; let d = 0, cur = ''; for (const ch of s) { if (ch === '(') d++; if (ch === ')') d--; if (ch === ',' && d === 0) { out.push(cur.trim()); cur = ''; } else cur += ch; } if (cur.trim()) out.push(cur.trim()); return out; }
    function stops(parts, lenPx) {
      const st = []; for (const part of parts) {
        const cm = part.match(/^(rgba?\([^)]*\)|color\([^)]*\)|transparent)\s*(.*)$/); if (!cm) continue;
        const c = cm[1] === 'transparent' ? [0, 0, 0, 0] : (col(cm[1]) || [0, 0, 0, 0]);
        const poss = cm[2].trim().split(/\s+/).filter(Boolean).map(x => x.endsWith('%') ? num(x) / 100 : (lenPx ? num(x) / lenPx : 0));
        if (!poss.length) st.push([c, null]); else poss.forEach(q => st.push([c, q]));
      }
      if (!st.length) return null;
      if (st[0][1] == null) st[0][1] = 0; if (st[st.length - 1][1] == null) st[st.length - 1][1] = 1;
      for (let i = 1; i < st.length - 1; i++) if (st[i][1] == null) { let j = i; while (st[j][1] == null) j++; const a = st[i - 1][1], z = st[j][1]; for (let k = i; k < j; k++) st[k][1] = a + (z - a) * (k - i + 1) / (j - i + 1); }
      // transparent stops take the neighbour's colour at zero alpha (CSS premultiplied look)
      st.forEach((s, i) => { if (s[0][3] === 0) { const n = st[i + 1] && st[i + 1][0][3] ? st[i + 1] : st[i - 1]; if (n) s[0] = [n[0][0], n[0][1], n[0][2], 0]; } });
      return st.map(([c, q]) => [c, Math.max(0, Math.min(1, +q.toFixed(4)))]);
    }
    function grads(bi, w, h) {
      if (!bi || bi === 'none') return [];
      const out = [];
      for (const layer of splitTop(bi)) {
        let m;
        if ((m = layer.match(/^(repeating-)?linear-gradient\((.*)\)$/s))) {
          if (m[1]) continue;
          const parts = splitTop(m[2]); let ang = 180;
          if (/deg|turn|rad/.test(parts[0]) || /^to /.test(parts[0])) {
            const a = parts.shift();
            if (a.endsWith('deg')) ang = num(a); else if (a.endsWith('turn')) ang = num(a) * 360; else if (a.endsWith('rad')) ang = num(a) * 180 / Math.PI;
            else { const t = a.slice(3).trim(); ang = { 'top': 0, 'right': 90, 'bottom': 180, 'left': 270, 'top right': 45, 'right top': 45, 'bottom right': 135, 'right bottom': 135, 'bottom left': 225, 'left bottom': 225, 'top left': 315, 'left top': 315 }[t] ?? 180; }
          }
          const s = stops(parts, Math.abs(w * Math.sin(ang * Math.PI / 180)) + Math.abs(h * Math.cos(ang * Math.PI / 180)));
          if (s) out.push({ k: 'L', a: ang, s });
        } else if ((m = layer.match(/^radial-gradient\((.*)\)$/s))) {
          const parts = splitTop(m[1]); let shape = parts[0], cx = w / 2, cy = h / 2, rx = null, ry = null;
          if (!/^(rgba?|color|transparent)/.test(shape)) {
            parts.shift();
            const [sz, at] = shape.split(/\s+at\s+/);
            if (at) { const q = at.trim().split(/\s+/); const px = (v, L) => v === 'left' || v === 'top' ? 0 : v === 'right' || v === 'bottom' ? L : v === 'center' ? L / 2 : v.endsWith('%') ? num(v) / 100 * L : num(v); cx = px(q[0], w); cy = px(q[1] || 'center', h); }
            const dims = (sz || '').trim().split(/\s+/).filter(x => /px|%/.test(x));
            if (dims.length === 2) { rx = dims[0].endsWith('%') ? num(dims[0]) / 100 * w : num(dims[0]); ry = dims[1].endsWith('%') ? num(dims[1]) / 100 * h : num(dims[1]); }
            else if (dims.length === 1) { rx = ry = num(dims[0]); }
            else if (/closest-side/.test(sz)) { const circ = /circle/.test(sz); rx = Math.min(cx, w - cx); ry = Math.min(cy, h - cy); if (circ) rx = ry = Math.min(rx, ry); }
            else { const fx = Math.max(cx, w - cx), fy = Math.max(cy, h - cy); if (/circle/.test(sz)) rx = ry = Math.hypot(fx, fy); else { rx = fx * Math.SQRT2; ry = fy * Math.SQRT2; } }
          } else { const fx = Math.max(cx, w - cx), fy = Math.max(cy, h - cy); rx = fx * Math.SQRT2; ry = fy * Math.SQRT2; }
          const s = stops(parts, rx);
          if (s) out.push({ k: 'R', cx: +(cx / w).toFixed(4), cy: +(cy / h).toFixed(4), rx: +(rx / w).toFixed(4), ry: +(ry / h).toFixed(4), s });
        } else if ((m = layer.match(/^conic-gradient\((.*)\)$/s))) {
          const parts = splitTop(m[1]); let from = 0;
          if (/^from/.test(parts[0])) { from = num(parts.shift().replace('from', '')); }
          const s = stops(parts.map(x => x.replace(/(\d+(\.\d+)?)deg/g, (_, d) => (d / 3.6) + '%')), 0);
          if (s) out.push({ k: 'C', from, s });
        } else if ((m = layer.match(/^url\("?(.*?)"?\)$/))) {
          out.push({ k: 'U', src: m[1] });
        }
      }
      return out;
    }
    function shadows(v) {
      if (!v || v === 'none') return [];
      return splitTop(v).map(sh => {
        const cm = sh.match(/(rgba?\([^)]*\)|color\([^)]*\))/); const c = cm ? col(cm[1]) : null; if (!c) return null;
        const rest = sh.replace(cm[1], '').trim(); const q = rest.split(/\s+/).filter(x => x !== 'inset').map(num);
        return { c, x: q[0] || 0, y: q[1] || 0, b: q[2] || 0, s: q[3] || 0, i: /inset/.test(sh) ? 1 : 0 };
      }).filter(Boolean);
    }
    function radii(cs, w, h) {
      const g = k => { const v = cs[k]; const parts = v.split(' '); const x = parts[0].endsWith('%') ? num(parts[0]) / 100 * w : num(parts[0]); return Math.min(x, w / 2, h / 2); };
      const r = [g('borderTopLeftRadius'), g('borderTopRightRadius'), g('borderBottomRightRadius'), g('borderBottomLeftRadius')].map(x => +x.toFixed(2));
      return r.every(x => x === 0) ? 0 : (r.every(x => x === r[0]) ? r[0] : r);
    }
    const fam = f => /unbounded/i.test(f) ? 'U' : 'M';
    const isHidden = (el, cs) => cs.display === 'none' || cs.visibility === 'hidden' || +cs.opacity === 0 || el.hidden;
    const SKIP = 'script,style,noscript,dialog,template,link,meta,.cursor';
    function nameOf(el) {
      if (el.__cls) return el.__cls.trim();
      const c = typeof el.className === 'string' ? el.className.split(' ').filter(x => x && x !== '__nopse')[0] : '';
      const tag = el.tagName.toLowerCase();
      if (/^h[1-6]$/.test(tag)) return tag + (c ? ' .' + c : '');
      return c || tag;
    }
    const tt = (s, cs) => { const t = cs.textTransform; if (t === 'uppercase') return s.toUpperCase(); if (t === 'lowercase') return s.toLowerCase(); if (t === 'capitalize') return s.replace(/\b\w/g, x => x.toUpperCase()); return s; };
    function runStyle(cs) {
      const fs = num(cs.fontSize);
      const st = { f: fam(cs.fontFamily), w: Math.round(num(cs.fontWeight) / 100) * 100, z: +fs.toFixed(2) };
      const ls = cs.letterSpacing === 'normal' ? 0 : num(cs.letterSpacing); if (ls) st.ls = +ls.toFixed(2);
      const clipText = cs.webkitBackgroundClip === 'text' || cs.backgroundClip === 'text';
      const tf = cs.webkitTextFillColor;
      if (clipText && (tf === 'transparent' || /, 0\)$/.test(tf))) { const g = grads(cs.backgroundImage, 100, 40); if (g.length) st.g = g[0]; }
      if (!st.g) { let c = col(tf && !/, 0\)$/.test(tf) && tf !== cs.color ? tf : cs.color); if (tf === 'transparent' || /rgba\(.*, 0\)$/.test(tf)) c = null; st.c = c; }
      const sw = num(cs.webkitTextStrokeWidth); if (sw) st.sk = [col(cs.webkitTextStrokeColor), sw];
      if (/underline/.test(cs.textDecorationLine)) st.u = 1;
      if (cs.fontStyle === 'italic') st.it = 1;
      return st;
    }
    // Is this element a pure inline text container (text + plain inline children only)?
    function pureInline(el) {
      for (const ch of el.childNodes) {
        if (ch.nodeType === 3) continue;
        if (ch.nodeType !== 1) continue;
        if (ch.matches(SKIP)) continue;
        const cs = getComputedStyle(ch);
        if (isHidden(ch, cs)) continue;
        if (ch.tagName === 'BR') continue;
        if (ch.tagName === 'svg' || ch.tagName === 'IMG' || ch.tagName === 'VIDEO') return false;
        if (cs.display !== 'inline') return false;
        if (col(cs.backgroundColor) || cs.backgroundImage !== 'none' && !(cs.webkitBackgroundClip === 'text' || cs.backgroundClip === 'text')) return false;
        if (num(cs.borderTopWidth) || num(cs.borderBottomWidth) || num(cs.borderLeftWidth)) return false;
        if (cs.position === 'absolute' || cs.position === 'fixed') return false;
        if (!pureInline(ch)) return false;
      }
      return true;
    }
    function textRuns(el, big, ovs) {
      const runs = []; let txt = ''; let lastTop = null;
      const walk = (n, pcs) => {
        for (const ch of n.childNodes) {
          if (ch.nodeType === 3) {
            const st = runStyle(pcs);
            if (st.sk && !st.c && !st.g && ovs) { const rg = document.createRange(); rg.selectNodeContents(ch); const q = rg.getBoundingClientRect(); if (q.width) ovs.push({ q, tx: tt(ch.textContent.trim(), pcs), st: { ...st } }); }
            let s;
            if (big) {
              s = ''; const raw = ch.textContent; const rg = document.createRange();
              for (let i = 0; i < raw.length; i++) {
                const c = raw[i];
                if (/\s/.test(c)) { if (!(txt + s).endsWith(' ') && !(txt + s).endsWith('\n')) s += ' '; continue; }
                rg.setStart(ch, i); rg.setEnd(ch, i + 1); const q = rg.getBoundingClientRect();
                if (lastTop !== null && q.height && q.top > lastTop + q.height * 0.5) { if (s.endsWith(' ')) s = s.slice(0, -1) + '\n'; else if ((txt + s).endsWith(' ') && !s) { txt = txt.slice(0, -1); s = '\n'; } else s += '\n'; }
                if (q.height) lastTop = q.top;
                s += c;
              }
              s = tt(s, pcs);
            } else {
              s = ch.textContent.replace(/\s+/g, ' ');
              if (pcs.whiteSpace.startsWith('pre')) s = ch.textContent;
              s = tt(s, pcs);
            }
            if (!s) continue;
            runs.push([txt.length, txt.length + s.length, st]); txt += s;
          } else if (ch.nodeType === 1) {
            if (ch.tagName === 'BR') { txt += '\n'; continue; }
            const cs = getComputedStyle(ch); if (isHidden(ch, cs)) continue;
            walk(ch, cs);
          }
        }
      };
      walk(el, getComputedStyle(el));
      // trim, keeping run offsets aligned
      const lead = txt.length - txt.replace(/^[ \n]+/, '').length; const t2 = txt.trim();
      const out = runs.map(([a, z, s]) => [Math.max(0, a - lead), Math.min(t2.length, z - lead), s]).filter(([a, z]) => z > a);
      return { t: t2.replace(/ \n/g, '\n').replace(/\n /g, '\n'), r: out };
    }
    function textNode(el, x0, y0, cs) {
      const big = num(cs.fontSize) >= 26; const ovs = [];
      const { t, r } = textRuns(el, big, ovs); if (!t) return null;
      const rg = document.createRange(); rg.selectNodeContents(el);
      const rects = [...rg.getClientRects()].filter(q => q.width > 0.5 && q.height > 0.5);
      if (!rects.length) return null;
      const bb = rg.getBoundingClientRect();
      const fs = num(cs.fontSize); const lh = cs.lineHeight === 'normal' ? fs * 1.25 : num(cs.lineHeight);
      const tops = [...new Set(rects.map(q => Math.round(q.top / 3)))];
      const multi = tops.length > 1 || t.includes('\n');
      const er = el.getBoundingClientRect();
      const padL = num(cs.paddingLeft) + num(cs.borderLeftWidth), padR = num(cs.paddingRight) + num(cs.borderRightWidth);
      const first = rects[0];
      const y = first.top - (lh - first.height) / 2;
      const node = { t: 'T', n: t.slice(0, 40), tx: t, r, lh: +lh.toFixed(2), y: +(y - y0 + scrollY).toFixed(1) };
      const al = cs.textAlign; node.al = al === 'center' ? 'C' : (al === 'right' || al === 'end') ? 'R' : al === 'justify' ? 'J' : 'L';
      if (big) {
        node.x = +(bb.left - x0).toFixed(1); node.w = +(bb.width).toFixed(1); node.ml = 0;
      } else if (multi && cs.display !== 'inline') {
        node.x = +(er.left + padL - x0).toFixed(1); node.w = +(er.width - padL - padR + 1).toFixed(1); node.ml = 1;
      } else if (multi) {
        node.x = +(bb.left - x0).toFixed(1); node.w = +(bb.width + 1).toFixed(1); node.ml = 1;
      } else {
        node.x = +(bb.left - x0).toFixed(1); node.w = +(bb.width).toFixed(1); node.al = 'L';
      }
      node.h = +(bb.bottom - y + (lh - first.height) / 2).toFixed(1);
      if (node.ml) { const extra = 2; node.w = +(node.w + extra).toFixed(1); if (node.al === 'C') node.x -= extra / 2; else if (node.al === 'R') node.x -= extra; }
      if (ovs.length) node.ov = ovs.map(o => ({ x: +(o.q.left - x0).toFixed(1), y: +(o.q.top - (lh - o.q.height) / 2 - y0).toFixed(1), tx: o.tx, st: o.st, lh: node.lh }));
      return node;
    }
    function svgNode(el, x0, y0) {
      const r = el.getBoundingClientRect(); if (r.width < 1 || r.height < 1) return null;
      const c = el.cloneNode(true);
      const color = getComputedStyle(el).color;
      // inline computed paint for every shape so CSS-driven colours survive
      const src = [el, ...el.querySelectorAll('*')], dst = [c, ...c.querySelectorAll('*')];
      src.forEach((s, i) => { const cs = getComputedStyle(s); const d = dst[i];
        ['fill', 'stroke', 'stroke-width', 'opacity', 'stroke-linecap', 'stroke-linejoin'].forEach(k => { const v = cs.getPropertyValue(k); if (v && !(k === 'opacity' && v === '1')) d.setAttribute(k, v.replace('currentcolor', color)); });
        d.removeAttribute('class'); d.removeAttribute('style'); });
      c.setAttribute('width', r.width); c.setAttribute('height', r.height);
      if (!c.getAttribute('viewBox')) c.setAttribute('viewBox', `0 0 ${r.width} ${r.height}`);
      c.setAttribute('xmlns', 'http://www.w3.org/2000/svg');
      let s = new XMLSerializer().serializeToString(c).replace(/currentColor/gi, color);
      return { t: 'S', n: 'icon', x: +(r.left - x0).toFixed(1), y: +(r.top + scrollY - y0).toFixed(1), w: +r.width.toFixed(1), h: +r.height.toFixed(1), svg: s };
    }
    function walk(el, x0, y0, isRoot) {
      if (el.nodeType !== 1 || el.matches(SKIP)) return [];
      const cs = getComputedStyle(el);
      if (isHidden(el, cs)) return [];
      let r = el.getBoundingClientRect(); let rot = 0, restore = null;
      if (cs.transform && cs.transform !== 'none' && el.tagName !== 'svg') {
        const m = cs.transform.match(/matrix\(([^)]+)\)/);
        if (m) { const [a, bq] = m[1].split(',').map(parseFloat); const deg = Math.atan2(bq, a) * 180 / Math.PI;
          if (Math.abs(deg) > 0.5) { const cx = r.left + r.width / 2, cy = r.top + r.height / 2; restore = el.style.transform; el.style.setProperty('transform', 'none', 'important'); el.style.setProperty('rotate', 'none', 'important');
            const r2 = el.getBoundingClientRect(); rot = deg; r = { left: cx - r2.width / 2, top: cy - r2.height / 2, width: r2.width, height: r2.height, right: cx + r2.width / 2, bottom: cy + r2.height / 2 };
            const dx = r.left - r2.left, dy = r.top - r2.top; el.__shift = [dx, dy]; } }
      }
      const X = r.left, Y = r.top + scrollY;
      if (!isRoot && (r.right < -50 || r.left > VW + 50) && cs.position !== 'static') return [];
      if (el.tagName === 'svg') {
        if (el.querySelector('text,textPath,foreignObject,image')) { const id = 'r' + (window.__shots = (window.__shots || 0) + 1); el.setAttribute('data-figshot', id); return [{ t: 'I', n: 'graphic', x: +(r.left - x0).toFixed(1), y: +(r.top + scrollY - y0).toFixed(1), w: +r.width.toFixed(1), h: +r.height.toFixed(1), src: 'shot:' + id, fit: 'FILL', rad: 0 }]; }
        const s = svgNode(el, x0, y0); if (!s) return [];
        const sbg = col(cs.backgroundColor);
        if (sbg) {
          const pl = num(cs.paddingLeft), pt = num(cs.paddingTop), pr = num(cs.paddingRight), pb = num(cs.paddingBottom);
          const f = { t: 'F', n: 'icon bg', x: s.x, y: s.y, w: s.w, h: s.h, fl: [{ k: 'S', c: sbg }], rad: radii(cs, r.width, r.height), ch: [s] };
          s.x = pl; s.y = pt; s.w = +(s.w - pl - pr).toFixed(1); s.h = +(s.h - pt - pb).toFixed(1);
          s.svg = s.svg.replace(/width="[^"]*"/, `width="${s.w}"`).replace(/height="[^"]*"/, `height="${s.h}"`);
          return [f];
        }
        return [s];
      }
      // tiled / masked decorative textures -> raster
      if (!el.children.length && !el.textContent.trim() && ((cs.maskImage && cs.maskImage !== 'none') || (cs.webkitMaskImage && cs.webkitMaskImage !== 'none') || /repeating-/.test(cs.backgroundImage) || (/gradient/.test(cs.backgroundImage) && cs.backgroundSize !== 'auto' && cs.backgroundSize !== 'auto auto' && !/100%/.test(cs.backgroundSize)))) {
        if (r.width < 1 || r.height < 1) return [];
        const id = 'r' + (window.__shots = (window.__shots || 0) + 1); el.setAttribute('data-figshot', id);
        return [{ t: 'I', n: 'texture', x: +(r.left - x0).toFixed(1), y: +(r.top + scrollY - y0).toFixed(1), w: +r.width.toFixed(1), h: +r.height.toFixed(1), src: 'shot:' + id, fit: 'FILL', rad: 0, z: cs.position !== 'static' && cs.zIndex !== 'auto' ? +cs.zIndex : 0 }];
      }
      const box = { x: +(X - x0).toFixed(1), y: +(Y - y0).toFixed(1), w: +r.width.toFixed(1), h: +r.height.toFixed(1) };
      if (el.tagName === 'IMG' || el.tagName === 'VIDEO') {
        const src = el.tagName === 'IMG' ? (el.currentSrc || el.src) : el.poster;
        if (!src || r.width < 1) return [];
        if (rot) { el.style.transform = restore || ''; el.style.removeProperty('rotate'); }
        return [{ t: 'I', n: el.alt || nameOf(el), ...box, src, fit: cs.objectFit === 'contain' ? 'FIT' : 'FILL', rad: radii(cs, r.width, r.height), op: +cs.opacity < 1 ? +cs.opacity : undefined, pos: cs.objectPosition, rot: rot ? +rot.toFixed(2) : undefined }];
      }
      const fills = [];
      const bg = col(cs.backgroundColor); if (bg) fills.push({ k: 'S', c: bg });
      const clipText = cs.webkitBackgroundClip === 'text' || cs.backgroundClip === 'text';
      if (!clipText) for (const g of grads(cs.backgroundImage, r.width, r.height).reverse()) fills.push(g);
      const bw = ['Top', 'Right', 'Bottom', 'Left'].map(s => cs['border' + s + 'Style'] !== 'none' ? num(cs['border' + s + 'Width']) : 0);
      const bcol = ['Top', 'Right', 'Bottom', 'Left'].map(s => col(cs['border' + s + 'Color']));
      const hasB = bw.some((w, i) => w > 0 && bcol[i]);
      const fx = shadows(cs.boxShadow);
      const bf = cs.backdropFilter && cs.backdropFilter !== 'none' ? num((cs.backdropFilter.match(/blur\(([\d.]+)px/) || [0, 0])[1]) : 0;
      const lb = cs.filter && /blur\(/.test(cs.filter) ? num(cs.filter.match(/blur\(([\d.]+)px/)[1]) : 0;
      const clip = cs.overflow !== 'visible' || cs.overflowX !== 'visible';
      const visual = fills.length || hasB || fx.length || bf || isRoot || clip || Math.abs(rot) > 0.5;
      const rad = radii(cs, r.width, r.height);
      let kids = [];
      const hasText = [...el.childNodes].some(n => n.nodeType === 3 && n.textContent.trim());
      const sh = el.__shift || [0, 0];
      const nx = visual || rot ? X - sh[0] : x0, ny = visual || rot ? Y - sh[1] : y0;
      if ((hasText || el.dataset.pseudo) && pureInline(el)) {
        const t = textNode(el, nx, ny - scrollY, cs); if (t) kids.push(t);
      } else {
        for (const ch of el.childNodes) {
          if (ch.nodeType === 3) {
            if (!ch.textContent.trim()) continue;
            // stray text next to elements: wrap in a temp span to measure
            const sp = document.createElement('fig-t'); ch.replaceWith(sp); sp.appendChild(ch);
            const t = textNode(sp, nx, ny - scrollY, cs); if (t) kids.push(t);
          } else kids.push(...walk(ch, nx, ny, false));
        }
      }
      kids = kids.map((k, i) => [k, i]).sort((a, b) => ((a[0].z || 0) - (b[0].z || 0)) || (a[1] - b[1])).map(a => a[0]);
      const op = +cs.opacity < 1 ? +cs.opacity : undefined;
      const blend = cs.mixBlendMode !== 'normal' ? cs.mixBlendMode : undefined;
      if (visual) {
        const n = { t: 'F', n: nameOf(el), ...box, ch: kids };
        if (cs.position !== 'static' && cs.zIndex !== 'auto' && +cs.zIndex) n.z = +cs.zIndex;
        if (fills.length) n.fl = fills;
        if (hasB) { const same = bw.every(w => w === bw[0]) && bcol.every(c => JSON.stringify(c) === JSON.stringify(bcol[0])); n.st = same ? { w: bw[0], c: bcol[0] } : { ws: bw, c: bcol.find(Boolean) }; }
        if (rad) n.rad = rad;
        if (fx.length) n.fx = fx;
        if (bf) n.bb = bf;
        if (lb) n.lb = lb;
        if (clip && !isRoot) n.clip = 1;
        if (isRoot) n.clip = 1;
        if (op) n.op = op;
        if (blend) n.bm = blend;
        if (rot) { n.rot = +rot.toFixed(2); el.style.transform = restore || ''; el.style.removeProperty('rotate'); }
        return [n];
      }
      if ((op || blend) && kids.length) kids.forEach(k => { if (op) k.op = (k.op || 1) * op; });
      // keep structure: group 2+ children of a structural element
      const zz = cs.position !== 'static' && cs.zIndex !== 'auto' ? +cs.zIndex : 0;
      if (zz && kids.length < 2) kids.forEach(k => { k.z = zz; });
      if (kids.length >= 2 && !isRoot) return [{ t: 'G', n: nameOf(el), z: zz || undefined, ...box, ch: kids.map(k => ({ ...k, x: +(k.x - box.x).toFixed(1), y: +(k.y - box.y).toFixed(1), ov: k.ov && k.ov.map(v => ({ ...v, x: +(v.x - box.x).toFixed(1), y: +(v.y - box.y).toFixed(1) })) })) }];
      return kids;
    }
    const roots = [...document.querySelectorAll('body > .site-head, body > main > section, body > section, body > footer, main > section, .site-head, footer.foot')];
    const uniq = [...new Set(roots)].filter(e => !roots.some(o => o !== e && o.contains(e)));
    uniq.sort((a, b) => a.getBoundingClientRect().top - b.getBoundingClientRect().top);
    const H = document.documentElement.scrollHeight;
    return { W: VW, H, sections: uniq.map(el => { const [n] = walk(el, 0, 0, true); return n; }) };
  });
  const shots = await p.$$eval('[data-figshot]', els => els.map(e => e.getAttribute('data-figshot')));
  await p.addStyleTag({ content: 'html,body{background:transparent!important} body *{visibility:hidden!important} [data-figshot],[data-figshot] *{visibility:visible!important}' });
  for (const id of shots) await p.locator(`[data-figshot="${id}"]`).screenshot({ path: path.join(__dirname, 'shots', id + '.png'), omitBackground: true, scale: (await p.locator(`[data-figshot="${id}"]`).boundingBox()).height > 1900 ? 'css' : 'device' });
  require('fs').writeFileSync(process.env.OUT, JSON.stringify(tree));
  const count = n => 1 + (n.ch || []).reduce((a, c) => a + count(c), 0);
  console.log('sections', tree.sections.map(s => s.n + ':' + count(s)).join(' '), 'H', tree.H);
  await b.close();
})();
