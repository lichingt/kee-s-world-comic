# Kee’s World Comics RSS Feed

This repository scrapes the daily **Kee’s World** comics from [The Star](https://www.thestar.com.my/lifestyle/comics) and generates an RSS feed (`comics.xml`) that can be used in any RSS reader, such as NetNewsWire.

The feed includes:

- Comic date as the RSS title
- Comic image embedded in the feed
- Proper `pubDate` with AEDT timezone for correct chronological sorting

---

## 🛠 Features

- Scrapes daily comics automatically
- Generates a lightweight RSS feed
- Hosted on GitHub Pages for easy access
- Works with all standard RSS readers

---

## ⚡ Setup & Usage

### 1. Clone the repo

```bash
git clone https://github.com/YOUR-USERNAME/kee-s-world-comic.git
cd kee-s-world-comic
```

### 2. Create a Python virtual environment

```bash
python3 -m venv venv
source venv/bin/activate   # macOS/Linux
# OR
venv\Scripts\activate      # Windows
```

### 3. Install dependencies

```bash
pip install requests beautifulsoup4 feedgen
```

###  4. Run the scraper
```bash
python scrape.py
```
This generates comics.xml.

### 5. Host on GitHub Pages
Upload comics.xml to your repository
Enable GitHub Pages from the repository settings
Your feed will be available at:
```
https://YOUR-USERNAME.github.io/kee-s-world-comic/comics.xml
```

### 6. Add to your RSS reader

Subscribe to the feed URL in your preferred RSS reader, e.g., NetNewsWire.

## 🔄 Automation

You can use GitHub Actions to run `scrape.py` daily and automatically update the feed.

## 📌 Notes
The scraper only extracts the image URL and date — images remain hosted on The Star's CDN.
Timezone is set to AEDT (UTC+11).

If The Star updates their HTML layout, selectors in scrape.py may need updating.

## ©️ Copyright & Attribution

The **Kee's World** comic artwork and content are the property of [The Star Media Group](https://www.thestar.com.my/). This tool only aggregates and distributes the feed—images remain hosted on The Star's CDN. Please support the original creators by visiting [The Star's comics page](https://www.thestar.com.my/lifestyle/comics).
