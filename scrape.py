import requests
from bs4 import BeautifulSoup
from feedgen.feed import FeedGenerator
from datetime import datetime, timezone, timedelta
import re

URL = "https://www.thestar.com.my/lifestyle/comics"
HEADERS = {"User-Agent": "Mozilla/5.0"}

# AEDT timezone (UTC+11)
AEDT = timezone(timedelta(hours=11), name="AEDT")

def scrape():
    res = requests.get(URL, headers=HEADERS)
    soup = BeautifulSoup(res.text, "html.parser")

    comics = []

    # Get the latest 5 comics
    blocks = soup.select("div.comic-wrapper")[:5]

    for block in blocks:
        date_tag = block.select_one("h4.date")
        img_tag = block.select_one("div.comic-strips img")

        if not date_tag or not img_tag:
            continue

        date_str = date_tag.get_text(strip=True)  # e.g., "Saturday, 28th March 2026"

        # Parse date string into datetime
        # Remove ordinal suffixes (st, nd, rd, th) from the date string
        date_str_clean = re.sub(r'(\d+)(st|nd|rd|th)', r'\1', date_str)
        pub_date = datetime.strptime(date_str_clean, "%A, %d %B %Y")

        pub_date = pub_date.replace(tzinfo=AEDT)

        comics.append({
            "title": date_str,
            "image": img_tag["src"],
            "pubDate": pub_date
        })

    return comics

def generate_rss(comics):
    fg = FeedGenerator()
    fg.title("Kee's World Comics")
    fg.link(href=URL)
    fg.description("Daily comics from The Star")

    for c in comics:
        fe = fg.add_entry()
        fe.title(c["title"])
        fe.link(href=c["image"])
        fe.description(f'<img src="{c["image"]}"/>')
        fe.pubDate(c["pubDate"])  # AEDT timezone

    fg.rss_file("comics.xml")

if __name__ == "__main__":
    comics = scrape()
    generate_rss(comics)
    print(f"Generated {len(comics)} comics in comics.xml")