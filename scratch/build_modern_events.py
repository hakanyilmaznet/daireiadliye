# -*- coding: utf-8 -*-
"""
Dâire-i Adliyye - Modern Türkiye Olay Destesi Oluşturucu (1000 Vaka)
Son 30 Yılın (1995-2026) Gerçek Olayları
"""

import json
import re
import os

# Karakterleri yükle
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
with open(os.path.join(BASE_DIR, 'characters_modern.json'), 'r', encoding='utf-8') as f:
    chars_data = json.load(f)

char_map = {c['id']: c['name'] for c in chars_data}

def format_preview(effects):
    stat_labels = {
        'justice': 'Adalet',
        'people': 'Halk',
        'treasury': 'Hazine',
        'military': 'Güvenlik',
        'authority': 'Otorite'
    }
    pos = []
    neg = []
    for k in ['justice', 'people', 'treasury', 'military', 'authority']:
        v = effects.get(k, 0)
        if v > 0:
            pos.append(f"{stat_labels[k]} +{v}")
        elif v < 0:
            neg.append(f"{stat_labels[k]} {v}")
    
    if pos and neg:
        return f"{', '.join(pos)} | {', '.join(neg)}"
    elif pos:
        return ', '.join(pos)
    elif neg:
        return ', '.join(neg)
    return ""

print(f"Toplam karakter sayısı: {len(char_map)}")
