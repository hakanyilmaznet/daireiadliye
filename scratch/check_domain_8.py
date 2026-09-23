# -*- coding: utf-8 -*-
import json

with open('event_deck_modern.json', 'r', encoding='utf-8') as f:
    text = f.read().strip()
if text.startswith('const EVENT_DECK_MODERN ='):
    text = text[len('const EVENT_DECK_MODERN ='):].strip()
if text.endswith(';'):
    text = text[:-1].strip()

events = json.loads(text)

print("Domain 8 (311-340):")
for ev in events[310:340]:
    print(f"  {ev['id']}: {ev['title']} -> {[c['id'] for c in ev['characters']]}")
