# -*- coding: utf-8 -*-
"""
Validation script to ensure complete integrity of:
1. characters_modern.json
2. event_deck_modern.json
3. event_deck_modern.js
"""

import json
import os
import re

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODERN_JSON = os.path.join(BASE_DIR, 'event_deck_modern.json')
MODERN_JS = os.path.join(BASE_DIR, 'event_deck_modern.js')
CHARS_PATH = os.path.join(BASE_DIR, 'characters_modern.json')

# 1. Check identical content of event_deck_modern.json and event_deck_modern.js
with open(MODERN_JSON, 'rb') as f1, open(MODERN_JS, 'rb') as f2:
    b1 = f1.read()
    b2 = f2.read()
assert b1 == b2, "HATA: event_deck_modern.json ve event_deck_modern.js birebir aynı değil!"
print(f"PASS: JSON ve JS dosyaları birebir aynı (Boyut: {len(b1):,} bayt)")

# 2. Check parsing of event deck
text = b1.decode('utf-8').strip()
assert text.startswith('const EVENT_DECK_MODERN = '), "HATA: Dosya 'const EVENT_DECK_MODERN = ' ile başlamıyor!"
assert text.endswith(';'), "HATA: Dosya ';' ile bitmiyor!"

json_str = text[len('const EVENT_DECK_MODERN = '):-1].strip()
events = json.loads(json_str)
assert len(events) == 1000, f"HATA: Beklenen 1000 olay, bulunan: {len(events)}"
print("PASS: 1000 olay başarıyla yüklendi.")

# 3. Check characters_modern.json
with open(CHARS_PATH, 'r', encoding='utf-8') as f:
    chars = json.load(f)

assert len(chars) == 24, f"HATA: Beklenen 24 karakter, bulunan: {len(chars)}"
char_ids = {c['id'] for c in chars}
print(f"PASS: 24 karakter tanımlı.")

# 4. Check character mapping consistency
total_events_in_chars = sum(c['eventCount'] for c in chars)
assert total_events_in_chars == 2000, f"HATA: Beklenen 2000 referans, bulunan: {total_events_in_chars}"
print(f"PASS: Karakter toplam olay referansı tam 2000.")

event_id_set = {ev['id'] for ev in events}
assert len(event_id_set) == 1000, "HATA: Tekrarlayan olay ID'si var!"

for c in chars:
    assert c['eventCount'] == len(c['events']), f"HATA: {c['id']} eventCount ({c['eventCount']}) ile events uzunluğu ({len(c['events'])}) uyuşmuyor!"
    assert c['eventCount'] > 0, f"HATA: {c['id']} hiç olayda kullanılmamış!"
    for ev_id in c['events']:
        assert ev_id in event_id_set, f"HATA: {c['id']} içindeki {ev_id} olay destesinde yok!"

# 5. Check all events character references
for ev in events:
    assert len(ev['characters']) == 2, f"HATA: {ev['id']} 2 karaktere sahip değil!"
    for ch in ev['characters']:
        assert ch['id'] in char_ids, f"HATA: {ev['id']} içindeki {ch['id']} characters_modern.json'da yok!"
        assert ch['name'], f"HATA: {ev['id']} içindeki karakterin adı boş!"

# 6. Verify options schema
for ev in events:
    assert len(ev['options']) == 5, f"HATA: {ev['id']} 5 seçeneğe sahip değil!"
    for opt in ev['options']:
        assert 'label' in opt and opt['label'], f"HATA: {ev['id']} seçeneğinde label eksik!"
        assert 'preview' in opt and opt['preview'], f"HATA: {ev['id']} seçeneğinde preview eksik!"
        assert 'effects' in opt, f"HATA: {ev['id']} seçeneğinde effects eksik!"
        assert 'log' in opt and opt['log'], f"HATA: {ev['id']} seçeneğinde log eksik!"

print("TÜM KONTROLLER BAŞARIYLA GEÇTİ! (100% VALIDATED)")
