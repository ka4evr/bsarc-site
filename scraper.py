import os
import requests
from bs4 import BeautifulSoup
import html2text
import time

BASE_URL = "https://www.n4gm.org/"
CONTENT_DIR = "content/"
STATIC_DIR = "static/"

files_to_grab = ["", "N4GM.html", "UUNAA.html", "ares.html"]

def download_file(url_path):
    full_url = BASE_URL + url_path
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
        'Accept-Encoding': 'gzip, deflate' # Keep it simple for decompression
    }

    try:
        r = requests.get(full_url, headers=headers, timeout=15)
        r.raise_for_status()
        
        # This line is key: it uses requests' built-in decoder 
        # to turn binary "garbage" back into readable HTML text
        html_content = r.text 

        if url_path.endswith(".html") or url_path == "":
            local_path = os.path.join(CONTENT_DIR, url_path.replace(".html", ".md") or "_index.md")
            soup = BeautifulSoup(html_content, 'html.parser')
            
            # Remove scripts/styles
            for s in soup(['script', 'style']):
                s.decompose()

            converter = html2text.HTML2Text()
            converter.body_width = 0
            markdown = converter.handle(str(soup.body))

            with open(local_path, "w", encoding="utf-8") as f:
                clean_title = url_path.replace(".html", "").capitalize() or "Home"
                f.write(f"---\ntitle: '{clean_title}'\ndraft: false\n---\n\n")
                f.write(markdown)
            print(f"Fixed and Saved: {local_path}")

    except Exception as e:
        print(f"Error on {url_path}: {e}")

for item in files_to_grab:
    download_file(item)
    time.sleep(1)
