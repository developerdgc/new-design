// ---- Afaq Mines importer runtime (runs inside Figma as a development plugin) ----
const BASE = 'https://raw.githubusercontent.com/developerdgc/new-design/claude/elegant-noether-jrww02/afaq-mines/';
const FAMILY = 'Plus Jakarta Sans';
const WEIGHTS = { 100: 'ExtraLight', 200: 'ExtraLight', 300: 'Light', 400: 'Regular', 500: 'Medium', 600: 'SemiBold', 700: 'Bold', 800: 'ExtraBold', 900: 'ExtraBold' };
const styleOf = (w, i) => { const s = WEIGHTS[w] || 'Regular'; return i ? (s === 'Regular' ? 'Italic' : s + ' Italic') : s; };
const hexToRgb = h => ({ r: parseInt(h.slice(1, 3), 16) / 255, g: parseInt(h.slice(3, 5), 16) / 255, b: parseInt(h.slice(5, 7), 16) / 255 });
const imageCache = {};
let imgFail = 0;

async function imageHash(src) {
  if (src in imageCache) return imageCache[src];
  try {
    const res = await fetch(BASE + src.replace(/^\.?\//, ''));
    if (!res.ok) throw new Error(res.status);
    const buf = await res.arrayBuffer();
    imageCache[src] = figma.createImage(new Uint8Array(buf)).hash;
  } catch (e) { imageCache[src] = null; imgFail++; }
  return imageCache[src];
}

function gradientTransform(angle) {
  const t = angle * Math.PI / 180, dx = Math.sin(t), dy = -Math.cos(t), L = Math.abs(dx) + Math.abs(dy);
  return [[dx / L, dy / L, 0.5 - (0.5 * dx + 0.5 * dy) / L], [-dy, dx, 0.5 + 0.5 * dy - 0.5 * dx]];
}

async function paints(list) {
  const out = [];
  for (const f of list || []) {
    if (f[0] === 's') out.push({ type: 'SOLID', color: hexToRgb(f[1]), opacity: f[2] });
    else if (f[0] === 'g') out.push({ type: 'GRADIENT_LINEAR', gradientTransform: gradientTransform(f[1]), gradientStops: f[2].map(s => ({ color: { ...hexToRgb(s[0]), a: s[1] }, position: Math.min(1, Math.max(0, s[2])) })) });
    else if (f[0] === 'i') {
      const h = await imageHash(f[1]);
      out.push(h ? { type: 'IMAGE', imageHash: h, scaleMode: 'FILL' } : { type: 'SOLID', color: { r: .85, g: .85, b: .85 } });
    }
  }
  return out;
}

function applyBox(node, n) {
  if (n.r) {
    if (Array.isArray(n.r)) { node.topLeftRadius = n.r[0]; node.topRightRadius = n.r[1]; node.bottomRightRadius = n.r[2]; node.bottomLeftRadius = n.r[3]; }
    else node.cornerRadius = n.r;
  }
  if (n.st) {
    node.strokes = [{ type: 'SOLID', color: hexToRgb(n.st[0]), opacity: n.st[1] }];
    node.strokeAlign = 'INSIDE';
    if (n.sd) { node.strokeTopWeight = n.sd[0]; node.strokeRightWeight = n.sd[1]; node.strokeBottomWeight = n.sd[2]; node.strokeLeftWeight = n.sd[3]; }
    else node.strokeWeight = n.st[2];
  }
  if (n.sh) node.effects = [{ type: n.sh[5] ? 'INNER_SHADOW' : 'DROP_SHADOW', color: { ...hexToRgb(n.sh[0]), a: n.sh[1] }, offset: { x: n.sh[2], y: n.sh[3] }, radius: n.sh[4], spread: n.sh[6] || 0, visible: true, blendMode: 'NORMAL' }];
  if (n.o != null && n.o < 1) node.opacity = n.o;
}

const ALIGN = { left: 'LEFT', start: 'LEFT', center: 'CENTER', right: 'RIGHT', end: 'RIGHT', justify: 'JUSTIFIED' };
let count = 0;

async function build(n, parent, px, py) {
  let node;
  if (n.k === 'f' || n.k === 'b') {
    node = n.k === 'f' ? figma.createFrame() : figma.createRectangle();
    node.name = n.n || (n.k === 'f' ? 'Frame' : 'Box');
    parent.appendChild(node);
    node.resize(Math.max(n.w, 0.01), Math.max(n.h, 0.01));
    node.fills = await paints(n.f);
    if (n.k === 'f') node.clipsContent = true;
    applyBox(node, n);
  } else if (n.k === 't') {
    node = figma.createText();
    parent.appendChild(node);
    const first = n.g[0];
    node.fontName = { family: FAMILY, style: styleOf(first[2], first[3]) };
    node.characters = n.g.map(s => s[0]).join('');
    let pos = 0;
    for (const s of n.g) {
      const end = pos + s[0].length;
      if (end > pos) {
        node.setRangeFontName(pos, end, { family: FAMILY, style: styleOf(s[2], s[3]) });
        node.setRangeFontSize(pos, end, s[1]);
        if (s[5] > 0) node.setRangeFills(pos, end, [{ type: 'SOLID', color: hexToRgb(s[4]), opacity: s[5] }]);
        else node.setRangeFills(pos, end, []);
      }
      pos = end;
    }
    node.lineHeight = { unit: 'PIXELS', value: n.lh };
    if (n.ls) node.letterSpacing = { unit: 'PIXELS', value: n.ls };
    node.textAlignHorizontal = ALIGN[n.al] || 'LEFT';
    if (n.ts) { node.strokes = [{ type: 'SOLID', color: hexToRgb(n.ts[0]) }]; node.strokeWeight = n.ts[1]; node.strokeAlign = 'CENTER'; }
    const single = n.h <= n.lh * 1.5;
    const extra = single ? 8 : 2;
    node.textAutoResize = 'HEIGHT';
    node.resize(Math.max(n.w + extra, 1), node.height);
    node.name = n.g.map(s => s[0]).join('').slice(0, 40);
    if (n.o != null && n.o < 1) node.opacity = n.o;
    n = { ...n, x: n.x - (node.textAlignHorizontal === 'CENTER' ? extra / 2 : node.textAlignHorizontal === 'RIGHT' ? extra : 0) };
  } else if (n.k === 's') {
    try { node = figma.createNodeFromSvg(ICONS[n.v]); } catch (e) { node = figma.createFrame(); node.fills = []; }
    parent.appendChild(node);
    node.name = 'icon';
    node.resize(Math.max(n.w, 1), Math.max(n.h, 1));
    if (n.o != null && n.o < 1) node.opacity = n.o;
  } else if (n.k === 'r') {
    node = figma.createEllipse(); parent.appendChild(node); node.name = 'radio';
    node.resize(n.w, n.h); node.fills = [{ type: 'SOLID', color: { r: 1, g: 1, b: 1 } }];
    node.strokes = [{ type: 'SOLID', color: n.on ? hexToRgb(n.c) : { r: .6, g: .6, b: .6 } }]; node.strokeWeight = n.on ? 5 : 1.5; node.strokeAlign = 'INSIDE';
  } else return;
  node.x = n.x - px; node.y = n.y - py;
  count++;
  if (n.k === 'f' && n.c) for (const c of n.c) await build(c, node, n.x, n.y);
}

async function main() {
  const styles = new Set(['Regular', 'Medium', 'SemiBold', 'Bold', 'ExtraBold', 'Light', 'Italic']);
  await Promise.all([...styles].map(s => figma.loadFontAsync({ family: FAMILY, style: s }).catch(() => null)));
  await figma.loadFontAsync({ family: 'Inter', style: 'Bold' });
  let page = figma.root.children.find(p => p.name === 'Afaq Mines – Desktop');
  if (!page) { page = figma.createPage(); page.name = 'Afaq Mines – Desktop'; }
  await figma.setCurrentPageAsync(page);
  let x = 0;
  const frames = [];
  for (let i = 0; i < PAGES.length; i++) {
    const P = PAGES[i];
    figma.notify(`Building ${P.title} (${i + 1}/${PAGES.length})…`, { timeout: 1500 });
    const label = figma.createText(); page.appendChild(label);
    label.fontName = { family: 'Inter', style: 'Bold' }; label.fontSize = 40; label.characters = P.title; label.x = x; label.y = -90;
    const frame = figma.createFrame(); page.appendChild(frame);
    frame.name = P.title; frame.resize(P.w, P.h); frame.x = x; frame.y = 0; frame.clipsContent = true;
    frame.fills = [{ type: 'SOLID', color: { r: 1, g: 1, b: 1 } }];
    for (const n of P.tree) await build(n, frame, 0, 0);
    frames.push(frame);
    x += P.w + 240;
  }
  figma.viewport.scrollAndZoomIntoView(frames.slice(0, 1));
  return frames.length;
}

main().then(nf => {
  figma.closePlugin(`Afaq Mines: ${nf} pages, ${count} layers created` + (imgFail ? ` (${imgFail} images failed to load)` : ''));
}).catch(e => figma.closePlugin('Import failed: ' + e.message));
