# -*- coding: utf-8 -*-
import json

with open('event_deck_modern.json', 'r', encoding='utf-8') as f:
    text = f.read().strip()
if text.startswith('const EVENT_DECK_MODERN ='):
    text = text[len('const EVENT_DECK_MODERN ='):].strip()
if text.endswith(';'):
    text = text[:-1].strip()

events = json.loads(text)

print("Domain 17 (581-610):")
for ev in events[580:610]:
    print(f"  {ev['id']}: {ev['title']} -> {[c['id'] for c in ev['characters']]}")

print("\nDomain 19 (641-670):")
for ev in events[640:670]:
    print(f"  {ev['id']}: {ev['title']} -> {[c['id'] for c in ev['characters']]}")
