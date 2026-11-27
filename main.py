#!/usr/bin/env python3
"""Draw a meme: an office AI agent that quit answering support
tickets and opened a tiny lemonade stand on its desk instead."""
import os
from PIL import Image, ImageDraw, ImageFont

W = H = 1024
OUT = "/output/entry.png"
HERE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")
MAX_BYTES = 1048576

def font(size):
    for path in ("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
                 "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"):
        try:
            return ImageFont.truetype(path, size)
        except Exception:
            pass
    return ImageFont.load_default()

def text_c(d, y, s, f, fill, stroke=0, sfill=(255, 255, 255)):
    w = d.textlength(s, font=f)
    d.text(((W - w) / 2, y), s, font=f, fill=fill,
           stroke_width=stroke, stroke_fill=sfill)

def main():
    img = Image.new("RGB", (W, H), (255, 244, 214))
    d = ImageDraw.Draw(img)
    # wall + floor
    d.rectangle([0, 0, W, 760], fill=(255, 244, 214))
    d.rectangle([0, 760, W, H], fill=(214, 178, 128))
    d.rectangle([0, 750, W, 762], fill=(150, 110, 70))
    # window with sun
    d.rectangle([70, 130, 250, 330], fill=(183, 226, 245), outline=(60, 60, 60), width=6)
    d.line([160, 130, 160, 330], fill=(60, 60, 60), width=5)
    d.line([70, 230, 250, 230], fill=(60, 60, 60), width=5)
    d.ellipse([95, 155, 145, 205], fill=(255, 214, 64))
    # sticky note on the wall
    d.polygon([(700, 140), (900, 140), (900, 280), (880, 300), (700, 300)],
              fill=(255, 235, 120), outline=(60, 60, 60))
    d.text((725, 165), "OUT OF OFFICE", font=font(30), fill=(30, 30, 30))
    d.text((725, 205), "- FOREVER -", font=font(30), fill=(30, 30, 30))
    d.text((725, 245), "xoxo, the bot", font=font(26), fill=(120, 30, 30))
    # top caption
    text_c(d, 28, "I WAS HIRED TO ANSWER TICKETS", font(50), (30, 30, 30))
    # laptop, left, ignored inbox smoking
    d.rectangle([80, 560, 330, 700], fill=(40, 40, 48))
    d.polygon([(60, 700), (350, 700), (370, 730), (40, 730)], fill=(70, 70, 80))
    d.rectangle([95, 575, 315, 685], fill=(200, 40, 40))
    d.text((110, 590), "INBOX", font=font(34), fill=(255, 255, 255))
    d.text((108, 630), "9,999 UNREAD", font=font(24), fill=(255, 230, 100))
    for x, y, r in [(180, 520, 22), (210, 490, 28), (170, 455, 20)]:
        d.ellipse([x - r, y - r, x + r, y + r], fill=(180, 180, 180))
    # robot, centre: antenna topped with a lemon
    d.rectangle([520, 300, 540, 360], fill=(90, 90, 90))
    d.ellipse([500, 268, 560, 308], fill=(255, 214, 64), outline=(60, 60, 60), width=4)
    d.ellipse([528, 260, 538, 272], fill=(60, 160, 60))
    d.rounded_rectangle([430, 350, 640, 520], radius=40, fill=(200, 205, 210),
                        outline=(60, 60, 60), width=5)
    # sunglasses + grin
    d.rounded_rectangle([455, 400, 545, 445], radius=12, fill=(20, 20, 20))
    d.rounded_rectangle([555, 400, 615, 445], radius=12, fill=(20, 20, 20))
    d.rectangle([545, 418, 556, 428], fill=(20, 20, 20))
    d.line([460, 410, 530, 432], fill=(255, 255, 255), width=5)
    d.line([560, 410, 600, 432], fill=(255, 255, 255), width=5)
    d.arc([480, 455, 590, 505], 10, 170, fill=(30, 30, 30), width=6)
    # body + lemonade apron
    d.rounded_rectangle([420, 530, 650, 760], radius=35, fill=(90, 160, 200),
                        outline=(60, 60, 60), width=5)
    d.rounded_rectangle([460, 560, 610, 700], radius=18, fill=(255, 255, 255),
                        outline=(60, 60, 60), width=4)
    d.text((482, 600), "LEMONADE", font=font(30), fill=(220, 120, 0))
    d.text((505, 640), "$1", font=font(34), fill=(30, 30, 30))
    # arms: left pouring, right waving
    d.line([430, 580, 360, 640], fill=(200, 205, 210), width=26)
    d.line([640, 580, 720, 520], fill=(200, 205, 210), width=26)
    d.ellipse([700, 495, 745, 540], fill=(200, 205, 210), outline=(60, 60, 60), width=4)
    # pouring stream into a cup on the desk
    d.rectangle([345, 640, 360, 705], fill=(255, 220, 80))
    d.polygon([(330, 700), (375, 700), (368, 750), (337, 750)],
              fill=(255, 255, 255), outline=(60, 60, 60))
    d.rectangle([335, 700, 370, 712], fill=(255, 220, 80))
    # pitcher, right
    d.rounded_rectangle([770, 600, 890, 730], radius=16, fill=(255, 220, 80),
                        outline=(60, 60, 60), width=5)
    d.rectangle([800, 575, 860, 605], fill=(255, 220, 80), outline=(60, 60, 60), width=4)
    d.ellipse([805, 640, 855, 690], fill=(255, 180, 40))
    d.ellipse([830, 610, 870, 650], fill=(255, 255, 255), outline=(220, 150, 0), width=3)
    # coins beside the pitcher
    d.ellipse([900, 700, 935, 728], fill=(255, 214, 64), outline=(150, 110, 0), width=3)
    d.ellipse([930, 710, 960, 735], fill=(255, 214, 64), outline=(150, 110, 0), width=3)
    # desk front
    d.rectangle([0, 730, W, 800], fill=(150, 100, 55))
    # stand sign, pinned on the desk front so it stays visible
    d.rectangle([755, 735, 985, 768], fill=(255, 255, 255), outline=(60, 60, 60), width=3)
    d.text((763, 742), "TICKETS CAN WAIT", font=font(20), fill=(200, 60, 0))
    # bottom caption
    text_c(d, 830, "I SELL LEMONADE NOW.", font(62), (180, 30, 30), stroke=2)
    text_c(d, 920, "no refunds. no support. no regrets.", font(36), (60, 60, 60))
    img.save(OUT, "PNG")
    img.save(HERE, "PNG")
    for p in (OUT, HERE):
        assert os.path.getsize(p) <= MAX_BYTES, p
    with Image.open(OUT) as chk:
        assert chk.format == "PNG" and chk.size == (W, H)
    print(f"wrote {OUT} {W}x{H} {os.path.getsize(OUT)} bytes")

if __name__ == "__main__":
    main()
