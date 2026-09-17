# 🖐️ HandWave — site-ul care te vede

Proiect de informatică: un site pe care **NU-l controlezi cu mouse-ul**. Ridici mâna
în fața camerei web, iar un model de inteligență artificială (MediaPipe, de la Google)
îți urmărește mâna în timp real: miști palma ca să prinzi obiectele care cad și
**ciupești** (deget mare + arătător) ca să apeși „start”.

> **Pe scurt, pentru profesoară:** *„Am făcut un site interactiv controlat prin gesturi,
> cu recunoaștere a mâinii în timp real, care rulează 100% local în browser — fără
> server și fără ca imaginile să părăsească laptopul.”* — asta e ideea care diferențiază
> proiectul de un site clasic.

---

## 🚀 Cum îl rulezi (30 de secunde)

1. Descarcă **`index.html`** și deschide-l în **Chrome** sau **Edge** (dublu-click pe el).
2. Apasă **„▶ Începe”** → browserul întreabă despre cameră → apeși **„Permite”**.
3. Ridică mâna la ~50–80 cm de cameră și mut-o stânga-dreapta. Coșul te ascultă. 🧺
4. Ca să reîncepi jocul: **ciupește** degetele sau apasă **Space**.

**Important pentru ziua prezentării:** modelul AI se descarcă de pe internet **o singură
dată**, apoi rămâne în memoria cache a browserului. Deschide site-ul o dată acasă, cu
internet, înainte de prezentare — la școală va porni instant chiar dacă internetul e slab.

### Merge fără cameră? Da!
Dacă camera e refuzată, lipsește sau nu ai internet, site-ul **comută automat în mod
șoarece** și joci normal. Nicio eroare, nicio pagină stricată — asta se numește
**degradare grațioasă** și e un argument de notă mare: „ne-am gândit și la ce poate merge prost”.

---

## 🧠 Cum funcționează (ca să poți explica ORICE)

`index.html` conține două scripturi separate — asta e arhitectura proiectului:

```
┌─────────────────┐   21 de puncte   ┌──────────────────────┐
│ SCRIPTUL 2      │ ───────────────► │ SCRIPTUL 1           │
│ Camera+MediaPipe│  (de ~30 ori/s)  │ Jocul (canvas)       │
│ (modul separat) │                  │ coș, obiecte, scor   │
└─────────────────┘                  └──────────────────────┘
        are fallback                      merge și singur
     (mod șoarece)                      (cu mouse-ul)
```

1. **Camera** — `getUserMedia()` îți accesează webcam-ul exact ca într-un apel video.
   Video-ul **nu se trimite nicăieri**, rămâne în pagină.
2. **MediaPipe Tasks Vision** — un model AI antrenat de Google găsește **21 de puncte
   (landmark-uri)** pe mână: încheietura și toate articulațiile degetelor. Rulează
   local, pe placa video / procesorul tău, prin WebAssembly.
3. **Jocul** primește punctele și le traduce în comenzi:
   - poziția palmei = **media a 3 puncte** din palmă (0, 5, 17) → devine coordonata X a coșului;
   - distanța deget mare–arătător ÷ lungimea palmei = **„ciupirea”** → funcționează ca un click.

### Explicații pe înțelesul tuturor (de memorat)
- **Landmark** = un punct-cheie pe imagine (ca o articulație a degetului). 21 de puncte = toată mâna.
- **Interpolare** = coșul nu „sare” exact unde e mâna, ci alună lin spre țintă — de asta mișcarea pare naturală. E linia `joc.cosX += (joc.tintaX - joc.cosX) * dt * 10`.
- **Fallback / degradare grațioasă** = dacă o funcționalitate eșuează (camera, internetul), aplicația continuă să funcționeze în mod redus, nu se blochează.
- **localStorage** = memoria mică a browserului; aici se salvează recordul tău între sesiuni.

### Unde e ceva în cod ( CTRL+F după nume )
| Vrei să schimbi... | Caută în `index.html` |
|---|---|
| viteza, numărul de vieți, șansa de 📱, emoji-urile care cad | `CONFIG` (începutul Scriptului 1) |
| culorile site-ului | `:root` (începutul CSS-ului) |
| cum se desenează mâna în panoul din colț | `deseneazaMana` |
| cum se calculează poziția palmei și ciupirea | `onHandLandmarks` |
| spawn-ul obiectelor și dificultatea | `vitezaCurenta`, `intervalSpawnCurent`, `spawnObiect` |
| sunetele (generate în cod, fără fișiere!) | `bip`, `sunetBun`, `sunetRau`, `sunetNivel` |

---

## 🔧 Personalizare rapidă (ca să devină „al vostru”)

Profa va întreba „ați scris voi asta?”. Cel mai bun răspuns e onestitatea + dovada că
înțelegeți fiecare parte: **modificați-l zgomotos.** Idei de 10 minute fiecare:

- schimbă emoji-urile din `CONFIG` (ex: tema haloween 🎃👻💀 vs 🕷️);
- schimbă viteza și numărul de vieți până simți că e „jocul vostru”;
- redenumește proiectul (titlul `<h1>` și `<title>`);
- puneți numele voastre în footer;
- **power-up nou** (nivel mediu): un ⭐ rar care dă +1 viață — copiază logica din
  `prinde()` și adaugă `emoji: '⭐'` în `obiecteBune`.

### Extensii pentru nota mare (dacă rămâne timp)
1. **Gesturi de navigare** —Swipe cu palma să schimbe secțiunile site-ului (nu doar jocul!).
2. **Două mâini** — `numHands: 2` în Scriptul 2 → mod 2 jucători pe același ecran.
3. **Tabel de recorduri** cu nume (cere numele la game over, salvează în `localStorage`).
4. **Mod „prezentare”** — schimbi slide-urile la tablă fluturând mâna. 🤯

---

## 📅 Plan pe 7 zile (împărțit pe doi)

> **Regula de aur:** la final, **oricare dintre voi poate explica orice linie**.
> Schimbați-vă rolurile la repetiție — profa întreabă aleatoriu.

| Zi | Cine | Ce face |
|---|---|---|
| 1 | amândoi | Fiecare rulează proiectul acasă, joacă 15 min, citește acest README. Alegeți numele proiectului. |
| 2 | amândoi | Personalizare: emoji, culori, viteze, texte. Fiecare face cel puțin o modificare în cod. |
| 3 | colegul (mai avansat) | Adaugă o funcție nouă (ex: power-up ⭐). **Tu:** rescrie cu vorbele voastre secțiunea „Cum funcționează” din site. |
| 4 | amândoi | Testare pe ambele laptopuri + telefon. Lista de bug-uri și micile reparări. |
| 5 | amândoi | Repetiția prezentării (scriptul de mai jos) + testul camerei în condițiile de la școală (lumină, unghi, distanță). |
| 6–7 | amândoi | Rezervă pentru fixuri + o „surpriză” de final (ex: la scor 25, o furtună de 📚). |

**Sugestie de roluri:** tu = design, branding, textele din site, prezentarea;
colegul = logica jocului și tuning-ul dificultății. Dar amândoi înțelegeți tot.

---

## 🎤 Script de prezentare (3 minute)

- **0:00–0:20 — Hook:** *„Ce-ar fi dacă nu ai avea nevoie de mouse ca să folosești un site?”*
  Stați amândoi cu mâinile ridicate. Zâmbet. Publicul e deja curios.
- **0:20–1:00 — Demo live:** unul joacă, celălalt comentează. **Invitați profa să joace!**
  (lasă-o pe ea, arată-i ciupirea). Prezentarea care își lasă profesoara să joace nu se uită.
- **1:00–1:40 — Cum funcționează:** arătați panoul cu camera din colț și punctele verzi
  pe mână. „Camera → model AI cu 21 de puncte → două numere: poziția palmei și ciupirea.”
- **1:40–2:20 — Codul:** deschideți `index.html`: arătați `CONFIG` („aici am decis
  dificultatea”), funcția `onHandLandmarks` („aici se traduc punctele în mișcare”),
  interpolarea coșului („aici se netezește mișcarea”).
- **2:20–3:00 — Finalul:** degradare grațioasă (opriți camera din browser și arătați că
  trece singură pe mouse!), confidențialitate („video-ul nu iese din laptop”), extensiile
  planificate. „Întrebări?”

### Întrebări probabile + răspunsuri
1. **„Ați scris tot codul voi?”** → *„Am pornit de la un prototip generat cu ajutorul
   AI-ului, apoi l-am studiat, înțeles și modificat linie cu linie — uitați, aici se
   calculează poziția palmei, aici am schimbat noi vitelele și am adăugat funcția X.”*
   Onestitatea + înțelegerea = cea mai puternică combinație.
2. **„Ce bibliotecă de AI folosiți?”** → MediaPipe Tasks Vision (Google), rulează local prin WebAssembly.
3. **„Cum știe unde e mâna?”** → modelul e antrenat pe milioane de imagini de mâini;
   întoarce 21 de puncte; noi folosim media a 3 puncte din palmă.
4. **„Ce se întâmplă cu imaginile?”** → nimic — totul local; putem tăia internetul după încărcare.
5. **„De ce merge și cu mouse-ul?”** → detectăm orice eroare (try/catch) și comutăm pe fallback.
6. **„Care a fost partea grea?”** → netezirea mișcării (interpolarea) și reglarea
   pragului de „ciupire” ca să nu declanșeze din greșeală.

---

## ⚠️ Capcane & salvări

| Problemă | Salvarea |
|---|---|
| Camera blocată de browser/sistem | Mod șoarece automat + explicați degradarea grațioasă (punct forte!) |
| Internet slab la școală | Deschideți site-ul o dată acasă înainte (modelul rămâne în cache) |
| Lumină slabă în laborator | Mâna se detectează greu — testați înainte; apropiați-vă de fereastră |
| Mâna „sare” | Țineți mâna la 50–80 cm, fundal cât mai simplu, lumină din față |
| Laptopul de la școală e slab | Modelul încearcă GPU, apoi trece singur pe CPU |

## 📂 Fișierele proiectului
- `index.html` — **tot proiectul într-un singur fișier** (HTML + CSS + JS). Ușor de trimis, ușor de deschis.
- `README.md` — acest ghid.

Mult succes! 🚀
