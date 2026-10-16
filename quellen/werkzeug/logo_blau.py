"""Färbt die roten Teile des Logos (Sonne, Pfeil) blau, die Kirschblüte bleibt rosa.
Aufruf: python3 -I quellen/werkzeug/logo_blau.py <logo-rot.png> <logo-blau.png>; danach node scripts/gen-icons.mjs"""
import sys, numpy as np
from PIL import Image
src, dst = sys.argv[1], sys.argv[2]
im = np.asarray(Image.open(src).convert('RGBA')).astype(np.float32) / 255
rgb, a = im[..., :3], im[..., 3:]
mx, mn = rgb.max(-1), rgb.min(-1); d = mx - mn + 1e-6
r, g, b = rgb[..., 0], rgb[..., 1], rgb[..., 2]
h = np.where(mx == r, ((g - b) / d) % 6, np.where(mx == g, (b - r) / d + 2, (r - g) / d + 4)) / 6
s = np.where(mx > 0, d / (mx + 1e-6), 0); v = mx
hd = np.minimum(np.abs(h), np.abs(h - 1))               # Abstand zu Rot
w = np.clip((0.05 - hd) / 0.02, 0, 1) * np.clip((s - 0.12) / 0.1, 0, 1)
# Sakura (hell, mittlere Sättigung) bleibt rosa: Bereich der Blüte bestimmen
blossom = (hd < 0.04) & (s > 0.45) & (s < 0.68) & (v > 0.93)
H_, W_ = w.shape
blossom[:, int(W_ * 0.35):] = False; blossom[:int(H_ * 0.4), :] = False  # Blüte sitzt links unten
ys, xs = np.nonzero(blossom)
y0, y1, x0, x1 = ys.min() - 20, ys.max() + 20, xs.min() - 20, xs.max() + 20
inbox = np.zeros_like(w, bool); inbox[y0:y1, x0:x1] = True
w = np.where(inbox & (v > 0.88), 0, w)
print('Blüte:', x0, y0, x1, y1)
H = 0.6  # Blau (216°)
nh = (h + w * (((H - h + 0.5) % 1) - 0.5)) % 1
i = np.floor(nh * 6); f = nh * 6 - i; p = v * (1 - s); q = v * (1 - f * s); t = v * (1 - (1 - f) * s)
i = i.astype(int) % 6
out = np.stack([np.choose(i, [v, q, p, p, t, v]), np.choose(i, [t, v, v, q, p, p]), np.choose(i, [p, p, t, v, v, q])], -1)
Image.fromarray((np.concatenate([out, a], -1) * 255).round().astype(np.uint8), 'RGBA').save(dst)
