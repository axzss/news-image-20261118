#!/usr/bin/env python3
"""Render the 18 Nov 2026 world-news summary image, 1024x1024 PNG.
Programmatic typography only — no generated imagery, so no garbled text.
Deterministic: no timestamps, no randomness.

Caveat: built early on 18 Nov 2026 (~02:20 UTC) from what had been
reported so far; the day's later news is not in it. Refresh before the
20 Nov deadline if a bigger story lands.
"""
from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
PAPER = (248, 244, 236)
INK = (25, 25, 25)
RED = (163, 22, 33)
MUTED = (90, 86, 78)
RULE = (201, 194, 180)
WHITE = (255, 255, 255)

DJ_SERIF = "/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf"
DJ_SERIF_B = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
LIB_SANS = "/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf"
LIB_SANS_B = "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf"
DJ_SANS_B = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"

def font(path, size):
    return ImageFont.truetype(path, size)

def wrap(draw, text, fnt, max_w):
    words = text.split()
    lines, cur = [], ""
    for w in words:
        trial = (cur + " " + w).strip()
        if draw.textlength(trial, font=fnt) <= max_w:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines

def draw_lines(draw, lines, x, y, fnt, fill, leading):
    for ln in lines:
        draw.text((x, y), ln, font=fnt, fill=fill)
        y += leading
    return y

def text_w(draw, text, fnt):
    return draw.textlength(text, font=fnt)

def main():
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)
    M = 44
    CW = W - 2 * M

    # ---- Masthead ----
    f_mast = font(DJ_SERIF_B, 92)
    title = "THE WORLD"
    d.text(((W - text_w(d, title, f_mast)) / 2, 30), title, font=f_mast, fill=INK)

    f_date = font(LIB_SANS_B, 21)
    date = "WEDNESDAY, 18 NOVEMBER 2026"
    tag = "SEVEN STORIES  ·  ONE DAY"
    y = 138
    d.text((M, y), date, font=f_date, fill=INK)
    d.text((W - M - text_w(d, tag, f_date), y), tag, font=f_date, fill=RED)

    d.line([(M, 172), (W - M, 172)], fill=INK, width=3)
    d.line([(M, 178), (W - M, 178)], fill=INK, width=1)

    # ---- Top story ----
    y = 196
    f_tag = font(DJ_SANS_B, 17)
    tag_txt = "  TOP STORY  "
    tw = text_w(d, tag_txt, f_tag)
    d.rectangle([M, y, M + tw, y + 28], fill=RED)
    d.text((M, y + 3), tag_txt, font=f_tag, fill=WHITE)
    f_kick = font(LIB_SANS_B, 18)
    d.text((M + tw + 14, y + 4), "MIDDLE EAST — GULF", font=f_kick, fill=RED)

    f_head = font(DJ_SERIF_B, 43)
    head = "Iran drones target U.S. radar in Bahrain"
    lines = wrap(d, head, f_head, CW - 210)
    y2 = draw_lines(d, lines, M, y + 44, f_head, INK, 52)

    f_sum = font(LIB_SANS, 21)
    summ = "Bahrain intercepts the drones; Kuwait reports its own interceptions."
    slines = wrap(d, summ, f_sum, CW - 210)
    draw_lines(d, slines, M, y2 + 8, f_sum, MUTED, 30)

    # small radar motif, right side of top band
    bx, by = W - M - 185, y + 52
    cx, cy = bx + 92, by + 55
    d.ellipse([cx - 58, cy - 58, cx + 58, cy + 58], outline=INK, width=4)
    d.ellipse([cx - 32, cy - 32, cx + 32, cy + 32], outline=INK, width=3)
    d.line([(cx, cy), (cx + 40, cy - 40)], fill=INK, width=3)
    d.ellipse([cx + 34, cy - 46, cx + 46, cy - 34], fill=RED)
    d.ellipse([cx - 4, cy - 4, cx + 4, cy + 4], fill=INK)

    d.line([(M, 392), (W - M, 392)], fill=RULE, width=2)

    # ---- Grid: 6 stories, 2 cols x 3 rows ----
    stories = [
        ("01", "UKRAINE — WAR",
         "Ukraine hits Crimea bridge for a second day",
         "Kyiv targets the bridge again as Russia keeps pounding Kyiv\u2019s bridges."),
        ("02", "BUSINESS — TECH",
         "Nvidia revenue jumps 103% as Huang stays out",
         "The chipmaker reports $115.8 billion in quarterly sales and will not reinstate its ex-CEO."),
        ("03", "ASIA — DIPLOMACY",
         "Trump in Manila for Quad talks ahead of China trip",
         "Praises Australia\u2019s Albanese as leaders gather before the APEC summit in Shenzhen."),
        ("04", "MIDDLE EAST — SANCTIONS",
         "Britain and Australia sanction settlement firms",
         "London and Canberra target companies building Israeli settlements in the West Bank."),
        ("05", "TRADE — CHINA / CANADA",
         "Canada and China extend trade deals",
         "Xi meets Carney ahead of the APEC summit as Ottawa and Beijing deepen cooperation."),
        ("06", "SPACE",
         "Voyager 1 nears one light-day from Earth",
         "NASA\u2019s probe is about to become the first human-made object a full light-day away."),
    ]
    f_num = font(DJ_SERIF_B, 30)
    f_gkick = font(LIB_SANS_B, 15)
    f_ghead = font(DJ_SERIF_B, 25)
    f_gsum = font(LIB_SANS, 19)

    gx0, gy0 = M, 412
    col_w = (CW - 28) // 2
    row_h = 178
    for i, (num, kick, head, summ) in enumerate(stories):
        col, row = i % 2, i // 2
        x = gx0 + col * (col_w + 28)
        y = gy0 + row * row_h
        if row > 0:
            d.line([(M, y - 12), (W - M, y - 12)], fill=RULE, width=1)
        d.text((x, y), num, font=f_num, fill=RED)
        d.text((x + 52, y + 8), kick, font=f_gkick, fill=RED)
        hlines = wrap(d, head, f_ghead, col_w)
        y2 = draw_lines(d, hlines, x, y + 44, f_ghead, INK, 30)
        sl = wrap(d, summ, f_gsum, col_w)
        draw_lines(d, sl, x, y2 + 6, f_gsum, MUTED, 24)

    # ---- Footer ----
    fy = 968
    d.line([(M, fy), (W - M, fy)], fill=INK, width=2)
    f_foot = font(LIB_SANS, 15)
    left = "Sources: Reuters · AP · Times of India · The West Australian · AppiSToS"
    right = "All headlines verified from reporting on 18 November 2026"
    d.text((M, fy + 10), left, font=f_foot, fill=MUTED)
    d.text((W - M - text_w(d, right, f_foot), fy + 10), right, font=f_foot, fill=MUTED)

    img.save("/home/hatch/workspace/makefun/news-image-20261118/assets/entry.png", "PNG")
    print("saved")

if __name__ == "__main__":
    main()
