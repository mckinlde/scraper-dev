# scraper-dev

Fully reproducible, Nix-flake-based Selenium webscraping starter project.

## 📦 Features

- Python 3.11 + Selenium
- Headless and windowed Chrome web scraping
- Chromium + Chromedriver fully managed by Nix
- No global package installs needed
- Clean dev environment using `nix develop`

---

## 🚀 Quick Start

### 1. Install Nix

If you don't have Nix installed:

```bash
curl -L https://nixos.org/nix/install | sh
```

Then open a **new terminal window**.

---

### 2. Clone this repo

```bash
git clone git@github.com:mckinlde/scraper-dev.git
cd scraper-dev
```

(Or if you prefer HTTPS:  
`git clone https://github.com/mckinlde/scraper-dev.git`)

---

### 3. Enter the Nix dev environment

```bash
nix develop
```

✅ This spawns a shell with:
- Python 3.11
- Selenium
- Chromium
- Chromedriver
already available.

---

### 4. Run the test scraper

```bash
python3 -m scraper.hello_world
```

You should see:

```
Headless Chrome: PASS
Windowed Chrome: PASS
```

meaning scraping works headless and windowed.

---

## 🛠 Project Structure

```
scraper-dev/
├── .gitignore
├── flake.nix        # Nix environment definition
├── flake.lock       # Locked versions
└── scraper/         # Python scraping package
    ├── __init__.py
    ├── browser.py
    ├── headless_browser.py
    └── hello_world.py (test runner)
```

---

## ✨ Notes

- No need for pip, virtualenv, or system package managers.
- Nix ensures full reproducibility across machines.
- Best used with VSCode/VSCodium + manual `nix develop` shell.

---

## 📜 License

MIT License.

