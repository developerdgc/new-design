// Figma builder: decodes the layout tree from the data PNG and builds editable layers.
// Params replaced before sending: __DATA__ (data rect id), __HOLDER__ (assets frame id), __WRAP__ (wrapper id or ''), __SECS__ (section indexes), __NAME__, __X__
const holder = await figma.getNodeByIdAsync('__HOLDER__');
const dataRect = holder.findOne(n => n.name === '__DATA__');
const bytes = await figma.getImageByHash(dataRect.fills[0].imageHash).getBytesAsync();
let p = 8, parts = [], W = 0, H = 0;
while (p < bytes.length) {
  const len = (bytes[p] << 24 | bytes[p + 1] << 16 | bytes[p + 2] << 8 | bytes[p + 3]) >>> 0;
  const t = String.fromCharCode(bytes[p + 4], bytes[p + 5], bytes[p + 6], bytes[p + 7]);
  if (t === 'IHDR') { W = (bytes[p + 8] << 24 | bytes[p + 9] << 16 | bytes[p + 10] << 8 | bytes[p + 11]) >>> 0; H = (bytes[p + 12] << 24 | bytes[p + 13] << 16 | bytes[p + 14] << 8 | bytes[p + 15]) >>> 0; }
  if (t === 'IDAT') parts.push(bytes.subarray(p + 8, p + 8 + len));
  p += 12 + len;
}
const z = new Uint8Array(parts.reduce((a, c) => a + c.length, 0)); let o = 0; for (const c of parts) { z.set(c, o); o += c.length; }
// zlib stored blocks -> raw scanlines
const raw = new Uint8Array((W + 1) * H); let zi = 2, ri = 0;
while (true) { const fin = z[zi] & 1; const L = z[zi + 1] | z[zi + 2] << 8; zi += 5; raw.set(z.subarray(zi, zi + L), ri); ri += L; zi += L; if (fin) break; }
const flat = new Uint8Array(W * H); for (let y = 0; y < H; y++) flat.set(raw.subarray(y * (W + 1) + 1, (y + 1) * (W + 1)), y * W);
const n0 = (flat[0] << 24 | flat[1] << 16 | flat[2] << 8 | flat[3]) >>> 0;
let s = ''; for (let i = 4; i < 4 + n0; i += 8192) s += String.fromCharCode.apply(null, flat.subarray(i, Math.min(4 + n0, i + 8192)));
const TREE = JSON.parse(s);

const hashes = {}; for (const r of holder.children) if (r.name.startsWith('img:') && r.fills.length) hashes[r.name.slice(4)] = r.fills[0].imageHash;
const STY = { 100: 'Thin', 200: 'ExtraLight', 300: 'Light', 400: 'Regular', 500: 'Medium', 600: 'SemiBold', 700: 'Bold', 800: 'ExtraBold', 900: 'Black' };
const font = st => ({ family: st.f === 'U' ? 'Unbounded' : 'Manrope', style: STY[Math.min(st.f === 'U' ? 900 : 800, Math.max(200, st.w || 400))] });
const fonts = new Set();
(function scan(n) { if (n.t === 'T') n.r.forEach(r => fonts.add(JSON.stringify(font(r[2])))); (n.ch || []).forEach(scan); })({ ch: __SECS__.map(i => TREE.sections[i]) });
await Promise.all([...fonts].map(f => figma.loadFontAsync(JSON.parse(f))));

const rgb = c => ({ r: c[0], g: c[1], b: c[2] });
const stops = s => s.map(([c, q]) => ({ position: q, color: { r: c[0], g: c[1], b: c[2], a: c[3] } }));
function paint(f) {
  if (f.k === 'S') return { type: 'SOLID', color: rgb(f.c), opacity: f.c[3] };
  if (f.k === 'L') { const a = (f.a - 90) * Math.PI / 180, c = Math.cos(a), sn = Math.sin(a); return { type: 'GRADIENT_LINEAR', gradientStops: stops(f.s), gradientTransform: [[c, sn, 0.5 - 0.5 * c - 0.5 * sn], [-sn, c, 0.5 + 0.5 * sn - 0.5 * c]] }; }
  if (f.k === 'R') return { type: 'GRADIENT_RADIAL', gradientStops: stops(f.s), gradientTransform: [[1 / (2 * f.rx), 0, 0.5 - f.cx / (2 * f.rx)], [0, 1 / (2 * f.ry), 0.5 - f.cy / (2 * f.ry)]] };
  if (f.k === 'C') return { type: 'GRADIENT_ANGULAR', gradientStops: stops(f.s), gradientTransform: [[0, 1, 0], [-1, 0, 1]] };
  if (f.k === 'U' && hashes[f.key]) return { type: 'IMAGE', imageHash: hashes[f.key], scaleMode: 'FILL' };
  return null;
}
function radius(n, r) { if (!r) return; if (typeof r === 'number') n.cornerRadius = r; else { n.topLeftRadius = r[0]; n.topRightRadius = r[1]; n.bottomRightRadius = r[2]; n.bottomLeftRadius = r[3]; } }
function effects(d) {
  const e = (d.fx || []).map(x => ({ type: x.i ? 'INNER_SHADOW' : 'DROP_SHADOW', color: { r: x.c[0], g: x.c[1], b: x.c[2], a: x.c[3] }, offset: { x: x.x, y: x.y }, radius: x.b, spread: x.s, visible: true, blendMode: 'NORMAL' }));
  if (d.bb) e.push({ type: 'BACKGROUND_BLUR', radius: d.bb, visible: true });
  if (d.lb) e.push({ type: 'LAYER_BLUR', radius: d.lb, visible: true });
  return e;
}
const BM = { multiply: 'MULTIPLY', screen: 'SCREEN', overlay: 'OVERLAY', 'soft-light': 'SOFT_LIGHT', lighten: 'LIGHTEN', darken: 'DARKEN', 'color-dodge': 'COLOR_DODGE', 'plus-lighter': 'LINEAR_DODGE' };
let count = 0;
function build(d, parent) {
  let n;
  if (d.t === 'F' || d.t === 'G') {
    n = figma.createFrame(); n.name = d.n || 'frame';
    n.resize(Math.max(d.w, 0.01), Math.max(d.h, 0.01));
    n.fills = (d.fl || []).map(paint).filter(Boolean);
    if (d.st) { n.strokes = [{ type: 'SOLID', color: rgb(d.st.c), opacity: d.st.c[3] }]; n.strokeAlign = 'INSIDE';
      if (d.st.ws) { n.strokeTopWeight = d.st.ws[0]; n.strokeRightWeight = d.st.ws[1]; n.strokeBottomWeight = d.st.ws[2]; n.strokeLeftWeight = d.st.ws[3]; } else n.strokeWeight = d.st.w; }
    radius(n, d.rad);
    const e = effects(d); if (e.length) n.effects = e;
    n.clipsContent = !!d.clip;
    parent.appendChild(n); n.x = d.x; n.y = d.y;
    for (const c of d.ch || []) build(c, n);
  } else if (d.t === 'T') {
    n = figma.createText();
    n.fontName = font(d.r[0] ? d.r[0][2] : { f: 'M', w: 400 });
    n.characters = d.tx;
    n.lineHeight = { unit: 'PIXELS', value: d.lh };
    for (const [a, b, st] of d.r) {
      n.setRangeFontName(a, b, font(st)); n.setRangeFontSize(a, b, Math.max(1, st.z));
      if (st.ls) n.setRangeLetterSpacing(a, b, { unit: 'PIXELS', value: st.ls });
      if (st.u) n.setRangeTextDecoration(a, b, 'UNDERLINE');
      let fp = st.g ? paint(st.g) : st.c ? paint({ k: 'S', c: st.c }) : null;
      if (!fp && st.sk && st.sk[0]) fp = { type: 'SOLID', color: rgb(st.sk[0]), opacity: st.sk[0][3] };
      n.setRangeFills(a, b, fp ? [fp] : []);
    }
    n.textAlignHorizontal = { L: 'LEFT', C: 'CENTER', R: 'RIGHT', J: 'JUSTIFIED' }[d.al] || 'LEFT';
    parent.appendChild(n);
    if (d.ml) { n.resize(Math.max(d.w, 1), Math.max(d.h, 1)); n.textAutoResize = 'HEIGHT'; } else n.textAutoResize = 'WIDTH_AND_HEIGHT';
    n.name = d.n; n.x = d.x; n.y = d.y;
  } else if (d.t === 'S') {
    try { n = figma.createNodeFromSvg(d.svg); } catch (e) { return; }
    n.name = 'icon'; parent.appendChild(n); n.resize(Math.max(d.w, 0.01), Math.max(d.h, 0.01)); n.x = d.x; n.y = d.y; n.fills = [];
  } else if (d.t === 'I') {
    n = figma.createRectangle(); n.name = d.n || 'image';
    n.resize(Math.max(d.w, 0.01), Math.max(d.h, 0.01));
    n.fills = hashes[d.k] ? [{ type: 'IMAGE', imageHash: hashes[d.k], scaleMode: d.fit === 'FIT' ? 'FIT' : 'FILL' }] : [{ type: 'SOLID', color: { r: .8, g: .8, b: .8 } }];
    radius(n, d.rad); parent.appendChild(n); n.x = d.x; n.y = d.y;
  }
  if (!n) return;
  if (d.op != null && d.op < 1) n.opacity = d.op;
  if (d.bm && BM[d.bm] && 'blendMode' in n) n.blendMode = BM[d.bm];
  count++;
  return n;
}

let wrap = '__WRAP__' ? await figma.getNodeByIdAsync('__WRAP__') : null;
if (!wrap) {
  wrap = figma.createFrame(); wrap.name = '__NAME__'; wrap.resize(TREE.W, TREE.H); wrap.x = __X__; wrap.y = 0;
  wrap.fills = [{ type: 'SOLID', color: { r: 1, g: 1, b: 1 } }]; wrap.clipsContent = true;
}
const made = [];
for (const i of __SECS__) {
  const d = TREE.sections[i];
  wrap.findChildren(c => c.name === d.n && Math.abs(c.y - d.y) < 2).forEach(c => c.remove()); // retry-safe
  const n = build(d, wrap); made.push({ id: n.id, name: n.name, y: n.y, h: n.height });
}
return { wrap: wrap.id, made, nodes: count };
