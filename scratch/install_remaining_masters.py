# -*- coding: utf-8 -*-
"""
Resolve and download master oil portraits for the 13 modern characters.
"""

import urllib.request
import urllib.parse
import json
import io
import os
from PIL import Image

TARGET_DIR = r"c:\Users\muker\Downloads\daireiadliye\assets\characters"

selected_files = {
    # 1. Dışişleri Müsteşarı / Diplomat: Philip de László masterpiece
    "char_diplomat": "File:Philip Alexius de László - Portrait of Myron Herrick.jpg",

    # 2. Hazine ve Maliye Bakanı: Henri Fantin-Latour portrait of financier/banker
    "char_hazine_bakani": "File:Henri Fantin-Latour - Portrait of Leon Maitre, 1886.jpg",

    # 3. Merkez Bankası Başkanı: Classical economist David Ricardo by Thomas Phillips
    "char_merkez_bankasi_baskani": "File:Portrait of David Ricardo by Thomas Phillips (cropped).jpg",

    # 4. Ticaret Bakanı: Merchant / Shipowner by Joshua Johnson
    "char_ticaret_bakani": "File:A Baltimore Shipowner by Joshua Johnson.jpg",

    # 5. Sanayi ve Teknoloji Bakanı: Great engineer James B. Eads
    "char_sanayi_bakani": "File:Framed Oil Portrait on Canvas of James B. Eads - DPLA - 8feceec24d485d9f2681407bc068b556.jpg",

    # 6. İş Dünyası / TÜSİAD Başkanı: High society industrialist / gentleman F. Ambrose Clark by Sir Alfred Munnings
    "char_tusiad_baskani": "File:F. Ambrose Clark.jpg",

    # 7. Esnaf Odaları Başkanı: Master craftsman / scientist David Rittenhouse by Charles Willson Peale
    "char_esnaf_odasi_baskani": "File:Charles Willson Peale - David Rittenhouse - Google Art Project (3x4 cropped).jpg",

    # 8. Tüketici Hakları Temsilcisi: Jean-Baptiste Perronneau portrait of jurist Daniel Jousse
    "char_tuketici_dernekleri_baskani": "File:Jean-Baptiste Perronneau - Portrait of the Lawyer Daniel Jousse - WGA17217.jpg",

    # 9. AFAD / Kriz Masası Başkanı: Resolute commander / governor
    "char_afad_baskani": "File:Midshipman Augustus Brine.jpg",

    # 10. Çevre ve Şehircilik Bakanı: Alexander von Humboldt (founder of physical geography & ecology)
    "char_cevre_sehircilik_bakani": "File:Stieler, Joseph Karl - Alexander von Humboldt - 1843.jpg",

    # 11. Mimarlar ve Şehir Plancıları Temsilcisi: Charles Thévenin - Portrait of an Architect
    "char_sehir_plancisi": "File:Charles Thevenin - Portrait of an Architect.jpg",

    # 12. Sağlık Bakanı: Master painting Portrait of a Physician in His Library
    "char_saglik_bakani": "File:Portrait of a Physician in His Library.jpg",

    # 13. Göç İdaresi Başkanı: Border and customs governance by Raden Saleh
    "char_goc_idaresi_baskani": "File:Posthumous Portrait of Herman Willem Daendels, Governor-General of the Dutch East Indies - Rd Saleh.jpg"
}

def get_wikimedia_url(file_title):
    url = 'https://commons.wikimedia.org/w/api.php?action=query&titles=' + urllib.parse.quote(file_title) + '&prop=imageinfo&iiprop=url|size&format=json'
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})
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

for cid, file_title in selected_files.items():
    print(f"Resolving {cid}: {file_title}...")
    direct_url = get_wikimedia_url(file_title)
    if not direct_url:
        print(f"  FAILED to resolve direct URL for {cid}")
        continue
    
    try:
        req = urllib.request.Request(direct_url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})
        with urllib.request.urlopen(req) as resp:
            raw_data = resp.read()
        
        img = Image.open(io.BytesIO(raw_data)).convert('RGB')
        w, h = img.size
        side = min(w, h)
        # Crop square centered on upper body / face
        crop_box = ((w - side) // 2, 0, (w + side) // 2, side)
        cropped = img.crop(crop_box).resize((1024, 1024), Image.LANCZOS)
        
        dest_png = os.path.join(TARGET_DIR, f"{cid}.png")
        dest_jpg = os.path.join(TARGET_DIR, f"{cid}.jpg")
        cropped.save(dest_png, format="PNG")
        cropped.save(dest_jpg, format="JPEG", quality=95)
        print(f"  SUCCESS: Installed {cid} (1024x1024)")
    except Exception as e:
        print(f"  FAILED to process {cid}: {e}")
