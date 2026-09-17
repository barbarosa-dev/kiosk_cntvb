#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generează panorame DEMO (equirectangulare 2:1) pentru turul virtual.
Rulează din folderul kiosk/:   python3 tools/genereaza_panorame.py
Când aveți poze reale, înlocuiți fișierele din panorame/ păstrând numele:
  hol.jpg, laborator.jpg, biblioteca.jpg, curte.jpg
"""
from PIL import Image, ImageDraw, ImageFont
import os

W, H = 2048, 1024          # raport 2:1 = format equirectangular (360°x180°)
HORIZON = 512               # linia orizontului (nivelul ochiului)

def font(marime):
    for drum in ('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf',
                 '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'):
        if os.path.exists(drum):
            return ImageFont.truetype(drum, marime)
    return ImageFont.load_default()

def amestec(c1, c2, k):
    return tuple(int(a + (b - a) * k) for a, b in zip(c1, c2))

def genereaza(fisier, titlu, subtitlu, baza, piloni=True, usi=True, ferestre=False):
    img = Image.new('RGB', (W, H))
    d = ImageDraw.Draw(img)
    negru = (14, 16, 28)
    # gradient vertical: tavan deschis -> perete (culoarea bazei) -> podea inchisa
    for y in range(H):
        if y < HORIZON:
            k = y / HORIZON
            cul = amestec(amestec((255, 255, 255), baza, 0.25), baza, k)
        else:
            k = (y - HORIZON) / (H - HORIZON)
            cul = amestec(baza, negru, min(1.0, k * 1.25))
        d.line([(0, y), (W, y)], fill=cul)
    perete_gri = amestec(baza, (10, 10, 20), 0.45)
    if piloni:  # coloane verticale pe pereti
        for x in range(0, W, 256):
            d.rectangle([x + 120, HORIZON - 170, x + 136, HORIZON + 180], fill=perete_gri)
    if usi:  # usi
        for x0 in (420, 1500):
            d.rectangle([x0, HORIZON - 80, x0 + 200, HORIZON + 180],
                        fill=amestec(baza, (0, 0, 0), 0.55),
                        outline=amestec((255, 255, 255), baza, 0.4), width=4)
    if ferestre:  # ferestre (pentru curte)
        for x0 in (200, 700, 1200, 1650):
            d.rectangle([x0, HORIZON - 220, x0 + 240, HORIZON - 20],
                        fill=amestec((255, 255, 255), (140, 200, 255), 0.35),
                        outline=(90, 90, 110), width=6)
    # lampi pe tavan
    for x0 in (350, 1024, 1700):
        d.ellipse([x0 - 70, HORIZON - 330, x0 + 70, HORIZON - 230],
                  fill=amestec((255, 255, 240), baza, 0.15), outline=(120, 120, 140))
    # plinta
    d.rectangle([0, HORIZON + 180, W, HORIZON + 205], fill=amestec(baza, (0, 0, 0), 0.6))
    # etichete mari (cu umbra)
    f_titlu, f_sub = font(110), font(44)
    def text_centrat(y, text, f):
        lat = d.textlength(text, font=f)
        x = (W - lat) // 2
        d.text((x + 4, y + 4), text, font=f, fill=(0, 0, 0))
        d.text((x, y), text, font=f, fill=(255, 255, 255))
    text_centrat(HORIZON - 290, titlu, f_titlu)
    text_centrat(HORIZON - 130, subtitlu, f_sub)
    img.save(os.path.join('panorame', fisier), quality=78)
    print('am generat panorame/' + fisier)

CAMERE = [
    ('hol.jpg',         'HOLUL COLEGIULUI',       'panorama demo - inlocuieste cu o poza reala', (99, 102, 241)),
    ('laborator.jpg',   'LABORATOR DE INFORMATIC\u0102', 'panorama demo - inlocuieste cu o poza reala', (34, 197, 94)),
    ('biblioteca.jpg',  'BIBLIOTECA',             'panorama demo - inlocuieste cu o poza reala', (234, 179, 8)),
    ('curte.jpg',       'CURTEA COLEGIULUI',      'panorama demo - inlocuieste cu o poza reala', (96, 165, 250)),
]
for fisier, titlu, sub, baza in CAMERE:
    genereaza(fisier, titlu, sub, baza,
              piloni=(fisier != 'curte.jpg'),
              usi=(fisier != 'curte.jpg'),
              ferestre=(fisier == 'curte.jpg'))
print('Gata! Total:', sum(os.path.getsize(os.path.join('panorame', f)) for f in os.listdir('panorame')) // 1024, 'KB')
