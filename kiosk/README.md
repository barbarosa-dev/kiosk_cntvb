# 🏫 Recepția Digitală — C.N. „Tudor Vladimirescu” București

Un **kiosk interactiv** pentru holul liceului: ecranul stă în așteptare (ceas + carusel),
**te vede când ridici mâna**, te întâmpină, te lasă să navighezi prin informațiile colegiului
**fără mouse** (arăți cu degetul și ciupești), iar dacă nu te-ai hotărât te distrezi cu
**🧺 Prinzătorul de gânduri** — iar în bara laterală rulează meniul. Include și un
**Tur Virtual 360°** (VR pe telefon, fără cască).

> **Pitch-ul pentru profesoară (20 de secunde):**
> *„Am transformat site-ul clasic al liceului într-o experiență de recepție: ecranul te
> detectează prin cameră, navighezi cu mâna fără mouse, iar liceul se poate explora în 360°
> direct de pe telefon. Toată recunoașterea mâinii rulează local, în browser — imaginiile
> nu părăsesc niciodată dispozitivul.”*

---

## 🧭 Povestea proiectului (prezintă asta — iterațiile contează!)

| Versiune | Ce e | Unde e |
|---|---|---|
| v1 | site clasic, control cu mouse-ul | punct de plecare demonstrativ |
| v2 | **HandWave** — mâna în 2D, jocul cu coșul | folderul `../handwave/` |
| v3 | **Recepția Digitală** — kiosk: detectare → întâmpinare → meniu cu mâna → joc | `kiosk.html` |
| v4 | **Tur Virtual 360°** — VR pe telefon, fără cască | `tur.html` + `panorame/` |

Fiecare versiune adaugă un strat. Asta e dezvoltare software reală: cercetare → prototip → iterație.

---

## 📂 Fișierele

```
kiosk/
├── kiosk.html        ← ecranul principal (kiosk-ul cu toate stările)
├── tur.html          ← turul virtual VR (A-Frame)
├── aframe.min.js     ← biblioteca VR, salvată local (merge și fără internet)
├── panorame/
│   ├── hol.jpg           ← înlocuiește cu poze REALE de pe telefon
│   ├── laborator.jpg
│   ├── biblioteca.jpg
│   └── curte.jpg
├── tools/
│   └── genereaza_panorame.py  ← regenerează panoramele demo (python3 tools/genereaza_panorame.py)
└── README.md         ← acest ghid
```

---

## 🚀 Cum rulezi

### Pe laptop
1. Descarci tot folderul `kiosk/`.
2. Deschizi `kiosk.html` în Chrome → permiți camera → ridici mâna. 🖐️
3. `tur.html` se deschide din meniu ( „🕶️ Tur Virtual 360°”) sau direct.
   - Laptop: tragi cu mouse-ul ca să te uiți în jur, click pe 🔵 ca să mergi.
   - Funcționează **offline** (A-Frame e local); doar recunoașterea mâinii are nevoie de
     internet la prima încărcare (apoi rămâne în cache-ul browserului).

### Pe telefon (VR „magic window”, fără cască)
Telefonul nu poate deschide fișiere locale ușor → publici proiectul **gratuit pe GitHub Pages**:
1. Îți faci cont pe github.com (dacă nu ai).
2. Repository nou → „uploading an existing file” → urci tot folderul.
3. Settings → Pages → Source: `main` / root → Save.
4. După ~1 minut ai adresa `https://numetau.github.io/nume-repo/kiosk.html`.
5. O deschizi pe telefon → miști telefonul și „ești” în liceu. 🤳
   - iPhone: apasă o dată pe ecran la început (iOS cere permisiunea pentru giroscop).
   - Bonus: generează un cod QR cu adresa (gratuit, caută „qr code generator”) și lipește-l
     lângă ecranul kiosk-ului — „scanează și ia turul cu tine”.

### Ca kiosk adevărat (la ușile deschise)
- Chrome pe ecranul din hol: **F11** (ecran complet) sau lansezi cu
  `chrome --kiosk https://.../kiosk.html` — dispare și bara browserului.

---

## 🖼️ Cum pui pozele REALE în tur

1. **Panorame cu telefonul:** modul „Panorama” din camera telefonului NU face 360° complet —
   pentru demo e ok, dar ideal e o aplicație de 360° (ex. „Google Street View” → Crează → 360°).
   Reguli de aur: **pivotăm pe loc** (nu pășim), lumină bună, cât mai puțini oameni în cadru.
2. Poza trebuie să fie **360° equirectangulară** = raport **2:1** (ex. 4096×2048). Aplicațiile
   de 360° exportă așa automat.
3. Redenumire simplă: `hol.jpg`, `laborator.jpg`, `biblioteca.jpg`, `curte.jpg` → le copiezi
   în `panorame/` (le suprascrii pe cele demo). Ține pozele sub ~4 MB.
4. Cameră nouă? Adaugă în `tur.html` în obiectul `CAMERE` o intrare nouă + o linie în `<a-assets>`,
   cu `imagine: '#pano-numenou'` și unghiurile destinațiilor (0 = în față, 90 = dreapta etc.).

## ✏️ Cum schimbi textele din kiosk
Tot conținutul (meniu + carusel + pagini) e în obiectul **`PAGINI`** din `kiosk.html` —
edictezi acolo. Datele actuale sunt cele reale de pe cntvb.ro (sept. 2026): specializări,
medii de admitere 2025–2026, contact, program secretariat. **Verificați-le înainte de
prezentare** — mai ales dacă se publică date noi de admitere.

---

## 🧠 Cum funcționează (pentru întrebări)

### Kiosk (`kiosk.html`)
- **Stări:** `idle` (ceas + carusel) → `meniu` (întâmpinare) → `pag` (conținut) / `joc`.
  Un automat de stări — noțiune de informatică reală.
- **Detectarea ta:** MediaPipe găsește 21 de puncte pe mâna ta, de ~30 de ori pe secundă.
  Prima „mână văzută” scoate kiosk-ul din așteptare → mesaj de întâmpinare.
- **Cursorul:** vârful arătătorului (punctul 8) devine cursor pe ecran (oglindit, ca o selfie).
- **Click fără mouse:** (a) **ciupești** = click instant; (b) **stai 1,5s** peste un buton („dwell”)
  = click automat. Ambele sunt tehnici folosite în instalații reale.
- **Inactivitate:** 25s fără nimeni în meniu → intră jocul; 45s într-o pagină → înapoi la meniu.
- **Degradare grațioasă:** fără cameră/internet → totul merge cu mouse-ul, zero erori.

### Tur virtual (`tur.html`)
- **A-Frame** (Mozilla) construiește scena 3D; panorama e o „sferă” (`a-sky`) în jurul tău.
- **Proiecția equirectangulară:** poza 2:1 se „împachetează” pe sferă — trigonometrie reală
  (ce se întâmplă la unghi θ pe sferă ajunge la x = θ/360 × lățimea pozei).
- **Giroscopul** telefonului rotește camera (look-controls) — de-aia „ești acolo”.
- **Hotspot-uri:** inelele 🔵 sunt la poziția `(r·sin θ, h, −r·cos θ)` și se rotesc cu `-θ`
  ca să fie cu fața spre tine — iarăși trigonometrie de clasa a XI-a.
- **Două cursoare:** privire (fuse 1,5s — pentru telefon/laptop) + mouse (click direct).

### Întrebări probabile
1. **„De ce VR fără cască?”** → WebXR funcționează cu orice dispozitiv; „magic window” =
   telefonul devine o „fereastră” în spațiu prin giroscop. Cardboard (20 lei) o transformă
   în VR stereo complet.
2. **„Ce matematică e aici?”** → proiecție equirectangulară, trigonometrie pentru poziționarea
   hotspot-urilor, vectori și interpolare pentru cursor și coș.
3. **„Ce se întâmplă cu imaginile?”** → totul local; camera nu trimite nimic nicăieri.
4. **„Ce e mai greu de făcut?”** → reglajul interacțiunii: pragul „ciupirii”, timpul de dwell,
   netezirea mișcării — adică UX, nu doar cod.

---

## 📅 Plan pe 7 zile

| Zi | Cine | Ce face |
|---|---|---|
| 1 | amândoi | Rulați tot pe laptop și pe telefon (GitHub Pages). Împărțiți rolurile. |
| 2 | amândoi | **Pozele reale 360°** în liceu (cu acord!) + înlocuite în `panorame/`. |
| 3 | colegul | O cameră nouă în tur + un hotspot nou în `CAMERE`. |
| 3 | tu | Corectezi/îmbogățești textele din `PAGINI` cu vocele voastre. |
| 4 | amândoi | Teste de rezistență: camera acoperită, fără internet, lumină slabă. |
| 5 | amândoi | Repetiția prezentării + QR code pentru telefoanele din public. |
| 6–7 | amândoi | Surpriza finală (ex: la scor 25 în joc, ecranul face confetti 🎉) + rezervă. |

**Roluri sugerate:** tu = conținut, poze, prezentare; colegul = customizări în `CAMERE`/joc.
Regula rămâne: **oricare poate explica orice linie.**

---

## ⚠️ Capcane & salvări

| Problemă | Salvarea |
|---|---|
| Camera blocată pe laptopul din laborator | Mod șoarece automat — și-l arătați ca feature |
| Internet slab (MediaPipe nu se încarcă) | Deschideți o dată acasă → rămâne în cache; turul e deja 100% offline |
| Panorama arată „curbată” | Poza nu e 2:1 sau nu e 360° complet — refă cu o aplicație de 360° |
| iPhone nu rotește imaginea | Apasă o dată pe ecran (permisiunea de giroscop e cerută de iOS) |
| Mâna „sare” | 50–80 cm de cameră, fundal simplu, lumină din față |

## 💡 Extensii pentru nota mare
- **QR code** pe ecranul kiosk: „ia turul pe telefonul tău”.
- **Recunoaștere de față** în loc de mână pentru detectarea vizitatorului (MediaPipe are și FaceLandmarker).
- **Mod prezentare:** schimbi slide-urile la tablă fluturând mâna.
- **Statistici locale**: de câte ori a fost deschisă fiecare pagină (localStorage) — „analiză de trafic” de kiosk.

---

*Proiect realizat cu ajutorul AI-ului ca prototip de pornire — fiecare linie a fost înțeleasă,
explicată și personalizată de echipă. Fii sincer(ă) când ești întrebat(ă): onestitatea + înțelegerea
= cea mai puternică combinație la prezentare.*
