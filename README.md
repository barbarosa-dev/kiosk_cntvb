# 🏫 Recepția Digitală — C.N. „Tudor Vladimirescu” București

Un **kiosk interactiv** pentru prezentarea liceului: ecran de așteptare, detectarea mâinii, navigare fără mouse, informații despre colegiu, joc educațional și tur virtual 360° accesibil pe laptop, proiector și telefon.

> **Pitch pentru prezentare:** „Am transformat site-ul clasic al liceului într-o recepție digitală: vizitatorul este întâmpinat, poate naviga prin gesturi, poate afla informații despre liceu și poate explora spațiile în 360° de pe telefon. Recunoașterea mâinii rulează local în browser; imaginile camerei nu părăsesc dispozitivul.”

## Obiectivul proiectului

Proiectul este gândit ca o experiență reutilizabilă la porți deschise, în recepția liceului sau la evenimente. Are trei moduri de utilizare:

1. **Kiosk pe ecran/proiector** — `kiosk.html`, cu fallback automat la mouse dacă nu există cameră sau internet.
2. **Tur virtual** — `tur.html`, cu panorame demo care pot fi înlocuite pe rând cu fotografii reale.
3. **Distribuire pe telefon** — publicare prin GitHub Pages și acces rapid printr-un link sau cod QR.

## Fișiere

```text
kiosk_cntvb/
├── kiosk.html
├── tur.html
├── aframe.min.js
├── panorame/
│   ├── hol.jpg
│   ├── laborator.jpg
│   ├── biblioteca.jpg
│   └── curte.jpg
├── tools/
│   └── genereaza_panorame.py
└── README.md
```

## Rulare și testare

### Laptop / proiector

Deschide proiectul prin GitHub Pages sau printr-un server local. Pentru camera web, un context HTTPS sau `localhost` este mai sigur decât deschiderea directă cu `file://`.

```bash
python3 -m http.server 8000
```

Apoi accesează `http://localhost:8000/kiosk.html`. Pentru prezentare, folosește Chrome în ecran complet sau:

```bash
chrome --kiosk http://localhost:8000/kiosk.html
```

Înainte de prezentare verifică: sunetul, camera, lumina din sală, conexiunea la internet și modul mouse. Dacă MediaPipe nu pornește, aplicația continuă să funcționeze cu mouse-ul.

### Telefon

Publică repository-ul prin **Settings → Pages → Deploy from branch → main/root** și distribuie adresa `.../tur.html`. Pentru iPhone, prima atingere a ecranului poate fi necesară pentru permisiunea giroscopului. Un QR către tur este ideal lângă proiector.

## Poze reale pentru tur

Înlocuiește treptat imaginile din `panorame/`, păstrând numele fișierelor. Pentru un tur 360° autentic, imaginile trebuie să fie equirectangulare, raport **2:1** (de exemplu 4096×2048). Cere acordul liceului înainte de publicarea fotografiilor și evită elevii identificabili în cadru fără acord.

Pentru panorame demo poți rula:

```bash
python3 tools/genereaza_panorame.py
python3 tools/genereaza_panorame.py --width 4096
```

Generatorul creează automat folderul `panorame/` și salvează JPEG progresive optimizate. Pentru telefoane și proiector, este recomandat să păstrezi imaginile sub aproximativ 4–6 MB fiecare.

Ordinea recomandată pentru fotografii: **exterior → intrare → hol → laborator → bibliotecă → curte**. Fiecare cameră poate primi descriere și hotspot-uri în obiectul `CAMERE` din `tur.html`.

## Cum funcționează

- `kiosk.html` este un automat de stări: `idle → meniu → pagină/joc`.
- MediaPipe identifică 21 de puncte ale mâinii; arătătorul devine cursor, ciupirea face click, iar staționarea de 1,5 secunde activează un buton.
- Fără cameră, internet sau permisiuni, aplicația revine la mouse fără să blocheze demo-ul.
- `tur.html` folosește A-Frame și o sferă texturată cu panorama equirectangulară.
- Hotspot-urile sunt poziționate cu trigonometrie: `x = r·sin(θ)`, `z = −r·cos(θ)`.
- Recordul jocului este păstrat local, nu pe un server.

## Prezentare recomandată în clasă

1. Pornește `kiosk.html` în modul ecran complet.
2. Arată ecranul idle și activează meniul printr-un gest sau click.
3. Demonstrează o pagină de conținut și fallback-ul la mouse.
4. Deschide turul virtual și navighează între două camere.
5. Afișează QR-ul și lasă colegii să deschidă turul pe telefon.
6. Explică faptul că imaginile demo sunt înlocuibile cu fotografii reale și că proiectul poate deveni un kiosk permanent pentru porți deschise.

## Siguranță și confidențialitate

Camera este folosită numai pentru detectarea mâinii în browser. Nu salva și nu încărca cadre video. Pentru fotografiile reale, obține acordul liceului, nu publica fețe identificabile fără consimțământ și păstrează datele de contact verificate înainte de prezentare.

## Iterații

| Versiune | Rezultat |
|---|---|
| v1 | site clasic cu mouse |
| v2 | HandWave și jocul cu coșul |
| v3 | kiosk cu detectare, meniu și fallback |
| v4 | tur virtual 360° și distribuire pe telefon |
| v5 | fotografii reale, QR, mod prezentare și utilizare la porți deschise |

*Proiect realizat cu ajutorul AI ca prototip de pornire; fiecare componentă trebuie înțeleasă, testată și personalizată de echipă.*
