# 🔍 Google SERP Keyword Searcher (Česká verze)

Spolehlivá full-stack webová aplikace ve Flasku pro vyhledávání klíčových slov přes SerpAPI s exportem dat do formátu JSON.

## ✨ Klíčové vlastnosti
- **Integrace externího REST API:** Vyhledávání výsledků přes SerpAPI s lokalizací pro ČR (`gl=cz`, `hl=cs`).
- **Robustní síťová vrstva:** Ošetření výpadků spojení a chybových stavů API (`timeout=10` a odchytávání `requests.RequestException`).
- **Bezpečnost (Zero Leak):** API klíč není součástí kódu, načítá se bezpečně z proměnných prostředí (`os.getenv("SERPAPI_KEY")`).
- **Optimalizované UX:** 
  - Indikátor načítání (loader) při čekání na odpověď ze serveru.
  - Ochrana proti vícenásobnému odeslání (deaktivace tlačítka po kliknutí).
  - Ochrana proti znovuposlání formuláře při obnovení stránky (`window.history.replaceState`).
- **Efektivní export dat:** Výsledky jsou předávány do `/download` bez opakovaného (placeného) volání externího API. Stažení v JSON formátu s nastavenou hlavičkou `Content-Disposition: attachment`.
- **Testovací pokrytí (Unit Testing):** Automatizované testy s využitím `unittest.mock` (testování úspěšného parsování i síťového selhání bez reálného volání sítě a spotřeby kreditů).

---

## 🚀 Jak aplikaci spustit lokálně

### 1. Klonování a instalace závislostí
```bash
git clone https://github.com/TVUJ-NICK/google-serp-searcher.git
cd google-serp-searcher
pip install -r requirements.txt
```

### 2. Nastavení API klíče
Získej bezplatný klíč na [serpapi.com](https://serpapi.com) a nastav ho do proměnné prostředí:
```bash
export SERPAPI_KEY="tvuj_api_klic"
```

### 3. Spuštění serveru
```bash
python app.py
```
Aplikace poběží na adrese: `http://localhost:5000`

---

## 🧪 Spuštění testů
Testy jsou nezávislé na připojení k internetu a nevyžadují platný API klíč:
```bash
python -m unittest test_app.py
```
