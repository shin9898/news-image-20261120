"""Render the 20 November 2026 world-news front page to assets/entry.png.

Run at build time (needs Pillow and the macOS system fonts):
    .venv/bin/python build/render.py
The entry program (main.py) only copies the PNG this writes, so the graded
run needs no network, no fonts and no third-party packages.

Every fact on the page comes from build/stories.py, where each item lists
the reports it was checked against.
"""

from __future__ import annotations

import math
import sys
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "build"))
import stories as S  # noqa: E402

W = H = 1024
M = 26  # outer margin

PAPER = (247, 243, 234)
INK = (20, 20, 22)
GREY = (88, 88, 92)
RULE = (40, 40, 44)
RED = (178, 18, 27)
PANEL = (28, 28, 32)
PANEL_TXT = (245, 245, 245)
BLUE = (0, 51, 153)
GOLD = (255, 204, 0)

SUP = "/System/Library/Fonts/Supplemental/"
FONTS = {
    "mast": (SUP + "Georgia Bold.ttf", 0),
    "head": (SUP + "Arial Narrow Bold.ttf", 0),
    "body": (SUP + "Arial.ttf", 0),
    "bodyb": (SUP + "Arial Bold.ttf", 0),
    "serif": (SUP + "Georgia.ttf", 0),
    "seriti": (SUP + "Georgia Italic.ttf", 0),
}
_cache: dict[tuple[str, int], ImageFont.FreeTypeFont] = {}


def font(kind: str, size: int) -> ImageFont.FreeTypeFont:
    key = (kind, size)
    if key not in _cache:
        path, idx = FONTS[kind]
        _cache[key] = ImageFont.truetype(path, size, index=idx)
    return _cache[key]


def text_w(d: ImageDraw.ImageDraw, s: str, f) -> int:
    return int(math.ceil(d.textlength(s, font=f)))


def wrap(d, s: str, f, width: int) -> list[str]:
    words, lines, cur = s.split(), [], ""
    for w in words:
        t = w if not cur else cur + " " + w
        if text_w(d, t, f) <= width:
            cur = t
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def fit(d, s: str, kind: str, width: int, max_lines: int, start: int, minimum: int):
    """Largest size from start down to minimum whose wrap fits in max_lines."""
    for size in range(start, minimum - 1, -1):
        f = font(kind, size)
        lines = wrap(d, s, f, width)
        if len(lines) <= max_lines:
            return f, lines
    raise SystemExit(f"text does not fit: {s!r}")


def block(d, x: int, y: int, lines, f, fill, lead: float = 1.12) -> int:
    asc, desc = f.getmetrics()
    step = int((asc + desc) * lead)
    for ln in lines:
        d.text((x, y), ln, font=f, fill=fill)
        y += step
    return y


def kicker(d, x: int, y: int, s: str, color=RED) -> int:
    f = font("bodyb", 17)
    d.text((x, y), s.upper(), font=f, fill=color)
    return y + 24


# ---------- small pictograms (drawn, no external art) ----------

def icon_stars(d, cx: int, cy: int, r: int) -> None:
    d.ellipse((cx - r - 8, cy - r - 8, cx + r + 8, cy + r + 8), fill=BLUE)
    for i in range(12):
        a = -math.pi / 2 + i * math.pi / 6
        sx, sy = cx + r * math.cos(a), cy + r * math.sin(a)
        star(d, sx, sy, 6, GOLD)


def star(d, cx: float, cy: float, r: float, fill) -> None:
    pts = []
    for k in range(10):
        rr = r if k % 2 == 0 else r * 0.42
        a = -math.pi / 2 + k * math.pi / 5
        pts.append((cx + rr * math.cos(a), cy + rr * math.sin(a)))
    d.polygon(pts, fill=fill)


def icon_thermo(d, x: int, y: int, h: int) -> None:
    # thermometer with a high mercury level
    d.rounded_rectangle((x, y, x + 18, y + h), radius=9, outline=INK, width=3)
    d.ellipse((x - 9, y + h - 12, x + 27, y + h + 24), fill=RED, outline=INK, width=3)
    d.rectangle((x + 6, y + 14, x + 12, y + h), fill=RED)
    for k in range(5):
        yy = y + 12 + k * (h - 20) // 5
        d.line((x + 22, yy, x + 30, yy), fill=INK, width=2)


def icon_server(d, x: int, y: int, w: int, h: int) -> None:
    rows = 4
    rh = h // rows
    for k in range(rows):
        top = y + k * rh
        d.rounded_rectangle((x, top + 2, x + w, top + rh - 2), radius=4, fill=PANEL)
        d.ellipse((x + 8, top + rh // 2 - 4, x + 16, top + rh // 2 + 4), fill=(80, 220, 120))
        for j in range(3):
            lx = x + 26 + j * 12
            d.line((lx, top + 8, lx, top + rh - 8), fill=(150, 150, 155), width=3)


def icon_zeta(d, x: int, y: int) -> None:
    f = font("seriti", 46)
    d.text((x, y), "ζ(s)", font=f, fill=INK)
    f2 = font("body", 15)
    d.text((x + 2, y + 54), "Re(s) = ½", font=f2, fill=GREY)


def bar_chart(d, x: int, y: int, w: int, rows) -> int:
    """Horizontal bars for one-day % falls; rows = [(label, pct)]."""
    lab_f = font("bodyb", 18)
    val_f = font("head", 22)
    lab_w = max(text_w(d, r[0], lab_f) for r in rows) + 10
    val_w = 70
    span = w - lab_w - val_w
    worst = max(abs(p) for _, p in rows)
    bh, gap = 21, 7
    for label, pct in rows:
        d.text((x, y + 2), label, font=lab_f, fill=INK)
        bw = int(span * abs(pct) / worst)
        d.rectangle((x + lab_w, y, x + lab_w + bw, y + bh), fill=RED)
        d.text((x + lab_w + bw + 6, y - 1), f"−{abs(pct):.1f}%", font=val_f, fill=RED)
        y += bh + gap
    return y


# ---------- page ----------

def render() -> Image.Image:
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)

    # masthead
    d.line((M, 16, W - M, 16), fill=RULE, width=2)
    mf = font("mast", 60)
    d.text((M, 20), "WORLD NEWS", font=mf, fill=INK)
    tag = font("seriti", 18)
    tx = W - M - text_w(d, S.TAGLINE[0], tag)
    d.text((tx, 30), S.TAGLINE[0], font=tag, fill=GREY)
    d.text((W - M - text_w(d, S.TAGLINE[1], tag), 54), S.TAGLINE[1], font=tag, fill=GREY)

    # date band: the day this page sums up, as large as the masthead allows
    by = 90
    d.rectangle((M, by, W - M, by + 46), fill=RED)
    df = font("head", 38)
    dw = text_w(d, S.DATE_LINE, df)
    d.text(((W - dw) // 2, by + 2), S.DATE_LINE, font=df, fill=(255, 255, 255))

    # ----- lead story -----
    ly = by + 62
    lead = S.LEAD
    col_w = 610
    y = kicker(d, M, ly, lead["kicker"])
    hf, hl = fit(d, lead["headline"], "head", col_w, 3, 52, 44)
    y = block(d, M, y, hl, hf, INK, 1.0)
    y += 4
    bf, bl = fit(d, lead["body"], "body", col_w, 4, 21, 18)
    y = block(d, M, y, bl, bf, INK, 1.2)
    lead_bottom = y

    # stat panel
    px0 = M + col_w + 22
    px1 = W - M
    py0 = ly
    stats = lead["stats"]
    py1 = max(lead_bottom, py0 + 270)
    d.rectangle((px0, py0, px1, py1), fill=PANEL)
    sy = py0 + 10
    sf_big = font("head", 46)
    sf_lab = font("body", 18)
    for big, label in stats:
        d.text((px0 + 18, sy), big, font=sf_big, fill=(255, 92, 92))
        sy += 48
        ll = wrap(d, label, sf_lab, px1 - px0 - 36)
        sy = block(d, px0 + 18, sy, ll, sf_lab, PANEL_TXT, 1.1) + 8
    src_f = font("body", 14)
    d.text((px0 + 18, py1 - 24), lead["stat_note"], font=src_f, fill=(170, 170, 175))

    # ----- second row -----
    ry = py1 + 18
    d.line((M, ry - 9, W - M, ry - 9), fill=RULE, width=3)
    half = (W - 2 * M - 30) // 2
    # markets
    mk = S.MARKETS
    x = M
    y = kicker(d, x, ry, mk["kicker"])
    hf, hl = fit(d, mk["headline"], "head", half, 1, 36, 30)
    y = block(d, x, y, hl, hf, INK, 1.02) + 4
    y = bar_chart(d, x, y, half, mk["bars"])
    bf, bl = fit(d, mk["body"], "body", half, 2, 19, 16)
    y = block(d, x, y + 2, bl, bf, INK, 1.18)
    row2_bottom = y

    # UK-EU
    x2 = M + half + 30
    d.line((x2 - 15, ry, x2 - 15, row2_bottom), fill=(160, 160, 160), width=1)
    eu = S.UKEU
    y = kicker(d, x2, ry, eu["kicker"])
    icon_r = 34
    hw = half - (2 * icon_r + 34)
    hf, hl = fit(d, eu["headline"], "head", hw, 2, 36, 30)
    icon_stars(d, x2 + half - icon_r - 8, y + icon_r + 4, icon_r)
    y = block(d, x2, y, hl, hf, INK, 1.02) + 4
    bf, bl = fit(d, eu["body"], "body", half, 4, 19, 16)
    y = block(d, x2, y, bl, bf, INK, 1.18)
    row2_bottom = max(row2_bottom, y)

    # ----- third row -----
    r3 = row2_bottom + 16
    d.line((M, r3 - 8, W - M, r3 - 8), fill=RULE, width=3)
    third = (W - 2 * M - 2 * 26) // 3
    cards = [(S.COP, "thermo"), (S.DATACENTRES, "server"), (S.RIEMANN, "zeta")]
    bottoms = []
    for i, (st, ic) in enumerate(cards):
        cx = M + i * (third + 26)
        y = kicker(d, cx, r3, st["kicker"])
        iw = 62
        hf, hl = fit(d, st["headline"], "head", third - iw - 8, 3, 31, 26)
        if ic == "thermo":
            icon_thermo(d, cx + third - 40, y + 4, 62)
        elif ic == "server":
            icon_server(d, cx + third - 62, y + 4, 62, 84)
        else:
            icon_zeta(d, cx + third - 86, y - 4)
        y = block(d, cx, y, hl, hf, INK, 1.02) + 6
        bf, bl = fit(d, st["body"], "body", third, 4, 17, 15)
        y = block(d, cx, y, bl, bf, INK, 1.18)
        bottoms.append(y)
    for i in (1, 2):
        lx = M + i * (third + 26) - 13
        d.line((lx, r3, lx, max(bottoms)), fill=(160, 160, 160), width=1)

    # ----- also today ticker -----
    ty = max(bottoms) + 14
    d.line((M, ty - 6, W - M, ty - 6), fill=RULE, width=3)
    af = font("bodyb", 17)
    d.text((M, ty + 2), "ALSO ON 20 NOV:", font=af, fill=RED)
    ax = M + text_w(d, "ALSO ON 20 NOV:", af) + 10
    tf, tl = fit(d, "  •  ".join(S.ALSO), "body", W - M - ax, 2, 18, 15)
    ty = block(d, ax, ty + 2, tl, tf, INK, 1.15)

    # sources footer
    ff = font("body", 13)
    d.text((M, H - 22), S.SOURCES, font=ff, fill=GREY)
    if ty > H - 26:
        raise SystemExit(f"layout overflows: ticker ends at {ty}")
    return img


def main() -> None:
    out = ROOT / "assets" / "entry.png"
    out.parent.mkdir(exist_ok=True)
    img = render()
    img.save(out, format="PNG", optimize=True)
    print(out, out.stat().st_size, "bytes", img.size)


if __name__ == "__main__":
    main()
