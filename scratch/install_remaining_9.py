# -*- coding: utf-8 -*-
"""
Download remaining 9 characters from Wikimedia with proper rate-limiting and User-Agent.
"""

import urllib.request
import urllib.parse
import json
import io
import os
import time
from PIL import Image

TARGET_DIR = r"c:\Users\muker\Downloads\daireiadliye\assets\characters"

remaining_files = {
    "char_merkez_bankasi_baskani": "File:Portrait of David Ricardo by Thomas Phillips (cropped).jpg",
    "char_ticaret_bakani": "File:A Baltimore Shipowner by Joshua Johnson.jpg",
    "char_sanayi_bakani": "File:Framed Oil Portrait on Canvas of James B. Eads - DPLA - 8feceec24d485d9f2681407bc068b556.jpg",
    "char_tusiad_baskani": "File:F. Ambrose Clark.jpg",
    "char_esnaf_odasi_baskani": "File:Charles Willson Peale - David Rittenhouse - Google Art Project (3x4 cropped).jpg",
    "char_afad_baskani": "File:Midshipman Augustus Brine.jpg",
    "char_sehir_plancisi": "File:Charles Thevenin - Portrait of an Architect.jpg",
    "char_saglik_bakani": "File:Portrait of a Physician in His Library.jpg",
    "char_goc_idaresi_baskani": "File:Posthumous Portrait of Herman Willem Daendels, Governor-General of the Dutch East Indies - Rd Saleh.jpg"
}

HEADERS = {
    'User-Agent': 'DaireiAdliyyeEducationalProject/1.0 (https://github.com/muker/daireiadliyye; muker@example.org) Python-urllib'
}

def get_wikimedia_url(file_title):
    url = 'https://commons.wikimedia.org/w/api.php?action=query&titles=' + urllib.parse.quote(file_title) + '&prop=imageinfo&iiprop=url|size&format=json'
    req = urllib.request.Request(url, headers=HEADERS)
    try:
        with urllib.request.urlopen(req) as resp:
            data = json.loads(resp.read().decode('utf-8'))
            pages = data.get('query', {}).get('pages', {})
            for pid, pinfo in pages.items():
                info = pinfo.get('imageinfo', [{}])[0]
                return info.get('url')
    except Exception as e:
        print(f"Error fetching URL for {file_title}: {e}")
    return None

for cid, file_title in remaining_files.items():
    print(f"Processing {cid}...")
    time.sleep(3)  # Respectful 3-second delay between requests
    direct_url = get_wikimedia_url(file_title)
    if not direct_url:
        print(f"  Failed to get URL for {cid}")
        continue
    
    time.sleep(2)
    try:
        req = urllib.request.Request(direct_url, headers=HEADERS)
        with urllib.request.urlopen(req) as resp:
            raw_data = resp.read()
        
        img = Image.open(io.BytesIO(raw_data)).convert('RGB')
        w, h = img.size
        side = min(w, h)
        # Crop square centered on upper body / head
        crop_box = ((w - side) // 2, 0, (w + side) // 2, side)
        cropped = img.crop(crop_box).resize((1024, 1024), Image.LANCZOS)
        
        dest_png = os.path.join(TARGET_DIR, f"{cid}.png")
        dest_jpg = os.path.join(TARGET_DIR, f"{cid}.jpg")
        cropped.save(dest_png, format="PNG")
        cropped.save(dest_jpg, format="JPEG", quality=95)
        print(f"  SUCCESS: Installed {cid} (1024x1024)")
    except Exception as e:
        print(f"  Failed to download/process {cid}: {e}")

print("Completed processing remaining characters.")
