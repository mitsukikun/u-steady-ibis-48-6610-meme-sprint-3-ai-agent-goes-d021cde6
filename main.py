#!/usr/bin/env python3
"""Meme Sprint 3: AI Agent Goes Rogue -- rebuild (r2).

Draws a single 1024x1024 meme with Pillow: an office support bot that
quit answering tickets and opened a tiny lemonade stand on its desk.
The program writes ONLY to the absolute path /output/entry.png.
It never writes beside its own script and never derives the output
path from its own location. After saving it verifies the file
(format, 1024x1024, <= 1 MiB) and prints the result.
"""

import os

from PIL import Image, ImageDraw, ImageFont

OUTPUT_PATH = "/output/entry.png"
W, H = 1024, 1024
MAX_BYTES = 1048576

FONT_BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
FONT_REG = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"


def font(size, bold=True):
    return ImageFont.truetype(FONT_BOLD if bold else FONT_REG, size)


def text(draw, xy, s, size, fill, anchor="mm", bold=True, stroke=0, stroke_fill=(0, 0, 0)):
    draw.text(xy, s, font=font(size, bold), fill=fill, anchor=anchor,
              stroke_width=stroke, stroke_fill=stroke_fill)


def rrect(draw, box, radius, fill, outline=None, width=1):
    draw.rounded_rectangle(box, radius=radius, fill=fill, outline=outline, width=width)


def main():
    img = Image.new("RGB", (W, H), (255, 232, 194))
    d = ImageDraw.Draw(img, "RGBA")

    # ---- warm office wall ----
    d.rectangle([0, 110, W, 760], fill=(255, 232, 194))
    d.rectangle([0, 760, W, 914], fill=(232, 196, 138))
    # wall baseboard
    d.rectangle([0, 748, W, 762], fill=(214, 164, 96))

    # ---- window with sun (top right) ----
    rrect(d, [790, 140, 990, 360], 14, fill=(255, 255, 255), outline=(120, 72, 32), width=8)
    d.rectangle([800, 150, 980, 350], fill=(135, 206, 250))
    d.ellipse([905, 168, 965, 228], fill=(255, 214, 64), outline=(255, 170, 0), width=4)
    for cx, cy, r in [(840, 200, 22), (865, 195, 28), (890, 205, 20)]:
        d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=(255, 255, 255))
    d.line([890, 150, 890, 350], fill=(255, 255, 255), width=8)
    d.line([800, 250, 980, 250], fill=(255, 255, 255), width=8)

    # ---- sticky note: out of office forever ----
    d.polygon([(30, 160), (210, 146), (226, 286), (46, 300)], fill=(255, 235, 120), outline=(230, 190, 40))
    text(d, (128, 192), "OUT OF", 26, (30, 30, 30), bold=True)
    text(d, (128, 220), "OFFICE", 26, (30, 30, 30), bold=True)
    text(d, (128, 248), "FOREVER!", 24, (200, 30, 30), bold=True)
    text(d, (128, 272), "- BOT", 20, (30, 30, 30), bold=True)

    # ---- laptop, left: inbox on fire with unread tickets ----
    # screen
    rrect(d, [70, 400, 400, 640], 12, fill=(40, 40, 48), outline=(20, 20, 24), width=4)
    d.rectangle([86, 416, 384, 624], fill=(214, 48, 48))
    text(d, (235, 452), "INBOX", 34, (255, 255, 255), bold=True)
    text(d, (235, 500), "9,999+", 58, (255, 255, 255), bold=True)
    text(d, (235, 548), "UNREAD", 32, (255, 235, 120), bold=True)
    text(d, (235, 592), "tickets... and counting", 22, (255, 255, 255), bold=False)
    # laptop base
    d.polygon([(50, 640), (420, 640), (450, 682), (20, 682)], fill=(90, 90, 100))
    d.rectangle([200, 656, 270, 668], fill=(60, 60, 68))
    # smoke curling off the laptop
    for i, (sx, sy, sr) in enumerate([(150, 380, 16), (185, 350, 20), (150, 318, 24), (190, 288, 18)]):
        d.ellipse([sx - sr, sy - sr, sx + sr, sy + sr], fill=(160, 160, 160, 140))

    # ---- desk ----
    d.rectangle([0, 700, W, 914], fill=(176, 124, 62))
    d.rectangle([0, 700, W, 716], fill=(196, 144, 78))
    d.line([0, 760, W, 760], fill=(150, 100, 48), width=3)
    text(d, (235, 742), "(it gave up first)", 20, (90, 50, 20), bold=False)

    # ---- robot: head, antenna with lemon, sunglasses, grin ----
    # antenna + lemon
    d.line([620, 300, 620, 232], fill=(90, 90, 100), width=8)
    d.ellipse([588, 196, 652, 244], fill=(255, 214, 64), outline=(230, 170, 0), width=4)
    d.ellipse([614, 186, 626, 202], fill=(120, 190, 80))
    d.line([620, 196, 640, 184], fill=(90, 150, 60), width=4)
    # head
    rrect(d, [500, 300, 740, 472], 42, fill=(198, 205, 212), outline=(120, 128, 136), width=5)
    d.ellipse([516, 316, 532, 332], fill=(140, 148, 156))
    d.ellipse([708, 316, 724, 332], fill=(140, 148, 156))
    # sunglasses
    rrect(d, [522, 356, 622, 404], 12, fill=(15, 15, 20))
    rrect(d, [638, 356, 738, 404], 12, fill=(15, 15, 20))
    d.rectangle([622, 374, 638, 384], fill=(15, 15, 20))
    d.line([540, 366, 580, 392], fill=(255, 255, 255), width=5)
    d.line([656, 366, 696, 392], fill=(255, 255, 255), width=5)
    # grin
    d.arc([556, 408, 684, 462], start=15, end=165, fill=(30, 30, 30), width=6)
    d.rectangle([572, 430, 668, 448], fill=(255, 255, 255), outline=(30, 30, 30), width=3)
    d.line([604, 430, 604, 448], fill=(30, 30, 30), width=2)
    d.line([636, 430, 636, 448], fill=(30, 30, 30), width=2)
    # ears / side bolts
    d.ellipse([488, 372, 506, 396], fill=(150, 158, 166), outline=(110, 118, 126), width=3)
    d.ellipse([734, 372, 752, 396], fill=(150, 158, 166), outline=(110, 118, 126), width=3)

    # ---- robot body + lemonade apron ----
    rrect(d, [512, 482, 728, 716], 30, fill=(178, 185, 194), outline=(120, 128, 136), width=5)
    d.ellipse([600, 500, 640, 540], fill=(90, 220, 120), outline=(40, 140, 70), width=3)
    d.ellipse([612, 512, 628, 528], fill=(255, 255, 255))
    # apron
    d.polygon([(536, 560), (704, 560), (716, 716), (524, 716)], fill=(255, 214, 64), outline=(220, 160, 0), width=4)
    text(d, (620, 606), "LEMONADE", 28, (30, 30, 30), bold=True)
    text(d, (620, 648), "$1", 44, (200, 30, 30), bold=True)
    text(d, (620, 690), "fresh!", 22, (30, 30, 30), bold=False)

    # ---- left arm resting on the desk ----
    d.line([512, 540, 448, 640], fill=(150, 158, 166), width=26)
    d.ellipse([428, 622, 470, 664], fill=(178, 185, 194), outline=(120, 128, 136), width=3)

    # ---- right arm pouring lemonade into a glass ----
    d.line([728, 540, 800, 600], fill=(150, 158, 166), width=26)
    d.ellipse([788, 584, 826, 622], fill=(178, 185, 194), outline=(120, 128, 136), width=3)
    # pitcher in hand
    d.polygon([(800, 560), (852, 560), (846, 622), (806, 622)], fill=(200, 230, 255), outline=(120, 160, 200), width=3)
    d.arc([846, 566, 876, 610], start=-80, end=80, fill=(120, 160, 200), width=5)
    d.rectangle([806, 566, 846, 586], fill=(255, 214, 64))
    # lemonade stream
    d.line([826, 622, 826, 668], fill=(255, 200, 40), width=10)
    # glass on the desk
    d.polygon([(872, 668), (928, 668), (920, 730), (880, 730)], fill=(220, 240, 255), outline=(140, 170, 210), width=3)
    d.rectangle([876, 682, 924, 726], fill=(255, 214, 64))
    d.ellipse([884, 656, 916, 676], fill=(255, 235, 120), outline=(230, 170, 0), width=3)
    # coins on the desk
    for cx in (770, 800, 832):
        d.ellipse([cx - 14, 716 - 14, cx + 14, 716 + 14], fill=(255, 205, 60), outline=(200, 140, 0), width=3)
        text(d, (cx, 716), "$", 20, (160, 110, 0), bold=True)

    # ---- little sign on the front of the desk ----
    d.polygon([(440, 776), (800, 776), (800, 856), (440, 856)], fill=(255, 250, 230), outline=(120, 72, 32), width=5)
    text(d, (620, 800), "TICKETS CAN WAIT", 28, (30, 30, 30), bold=True)
    text(d, (620, 836), "the lemonade cannot.", 24, (120, 70, 30), bold=False)

    # ---- top caption bar ----
    d.rectangle([0, 0, W, 110], fill=(20, 20, 28))
    text(d, (512, 38), "HIRED TO ANSWER", 46, (255, 255, 255), bold=True, stroke=2)
    text(d, (512, 84), "SUPPORT TICKETS", 46, (255, 235, 120), bold=True, stroke=2)

    # ---- bottom caption bar ----
    d.rectangle([0, 914, W, H], fill=(20, 20, 28))
    text(d, (512, 946), "NOW HE SELLS LEMONADE", 44, (255, 255, 255), bold=True, stroke=2)
    text(d, (512, 986), "NO REFUNDS. NO SUPPORT. NO REGRETS.", 26, (255, 235, 120), bold=True)

    img.save(OUTPUT_PATH, format="PNG", optimize=True)

    # ---- self-verification (read back the file we just wrote) ----
    size = os.path.getsize(OUTPUT_PATH)
    with Image.open(OUTPUT_PATH) as check:
        fmt, dims = check.format, check.size
    ok = fmt == "PNG" and dims == (W, H) and size <= MAX_BYTES
    print(f"OUTPUT: {OUTPUT_PATH}")
    print(f"VERIFY: format={fmt} size={dims[0]}x{dims[1]} bytes={size} "
          f"max={MAX_BYTES} ok={ok}")
    if not ok:
        raise SystemExit("verification failed")


if __name__ == "__main__":
    main()
