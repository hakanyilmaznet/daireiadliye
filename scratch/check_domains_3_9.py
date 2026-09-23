# -*- coding: utf-8 -*-
import json

with open('event_deck_modern.json', 'r', encoding='utf-8') as f:
    text = f.read().strip()
if text.startswith('const EVENT_DECK_MODERN ='):
    text = text[len('const EVENT_DECK_MODERN ='):].strip()
if text.endswith(';'):
    text = text[:-1].strip()

events = json.loads(text)

# Let's inspect domain 3 (161-190) and domain 9 (341-370)
print("Domain 3 cases (161-190):")
for ev in events[160:190]:
    print(f"  {ev['id']}: {ev['title']} -> {[c['id'] for c in ev['characters']]}")

print("\nDomain 9 cases (341-370):")
for ev in events[340:370]:
    print(f"  {ev['id']}: {ev['title']} -> {[c['id'] for c in ev['characters']]}")
