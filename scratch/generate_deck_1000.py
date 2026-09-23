# -*- coding: utf-8 -*-
"""
Dâire-i Adliyye - Generator for complete 1000 Modern Turkish History Events
tr_vaka_001 to tr_vaka_1000
"""
import json
import os
import re

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODERN_JSON_PATH = os.path.join(BASE_DIR, 'event_deck_modern.json')
MODERN_JS_PATH = os.path.join(BASE_DIR, 'event_deck_modern.js')
CHARS_PATH = os.path.join(BASE_DIR, 'characters_modern.json')

with open(CHARS_PATH, 'r', encoding='utf-8') as f:
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

def load_existing_100():
    with open(MODERN_JSON_PATH, 'r', encoding='utf-8') as f:
        content = f.read().strip()
    content = re.sub(r'^(const|var|let)\s+EVENT_DECK_MODERN\s*=\s*', '', content)
    content = re.sub(r';\s*$', '', content)
    deck = json.loads(content)
    print(f"Loaded existing events: {len(deck)}")
    return deck[:100]

print("Script template ready.")
