# -*- coding: utf-8 -*-
import os
import shutil
from PIL import Image

artifact_dir = r"C:\Users\muker\.gemini\antigravity-ide\brain\9a6d7d3f-3886-411e-bd9c-6f01ea3fe30e"
target_dir = r"c:\Users\muker\Downloads\daireiadliye\assets\characters"

generated_map = {
    "char_cumhurbaskani": "char_cumhurbaskani_1790141778870.jpg",
    "char_basbakan": "char_basbakan_1790141750985.jpg",
    "char_tbmm_baskani": "char_tbmm_baskani_1790141799283.jpg",
    "char_milletvekili": "char_milletvekili_1790141819332.jpg",
    "char_adalet_bakani": "char_adalet_bakani_1790141841738.jpg",
    "char_anayasa_mahkemesi_baskani": "char_anayasa_mahkemesi_baskani_1790141868978.jpg",
    "char_adli_yargi_hakimi": "char_adli_yargi_hakimi_1790141896053.jpg",
    "char_icisleri_bakani": "char_icisleri_bakani_1790141923119.jpg",
    "char_genelkurmay_baskani": "char_genelkurmay_baskani_1790141953497.jpg",
    "char_savunma_bakani": "char_savunma_bakani_1790141985734.jpg",
    "char_savunma_sanayii_baskani": "char_savunma_sanayii_baskani_1790142026002.jpg",
}

for cid, filename in generated_map.items():
    src_path = os.path.join(artifact_dir, filename)
    if os.path.exists(src_path):
        img = Image.open(src_path)
        # Save as both PNG and JPG in assets/characters/
        dest_png = os.path.join(target_dir, f"{cid}.png")
        dest_jpg = os.path.join(target_dir, f"{cid}.jpg")
        
        # Save full resolution 1024x1024 RGB
        img.save(dest_png, format="PNG")
        img.save(dest_jpg, format="JPEG", quality=95)
        print(f"Installed {cid} -> PNG & JPG ({img.size})")
    else:
        print(f"File not found: {src_path}")
