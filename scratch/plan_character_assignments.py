# -*- coding: utf-8 -*-
"""
Inspect all cases in event_deck_modern.json and plan accurate character assignments.
"""
import json

with open('event_deck_modern.json', 'r', encoding='utf-8') as f:
    text = f.read().strip()
if text.startswith('const EVENT_DECK_MODERN ='):
    text = text[len('const EVENT_DECK_MODERN ='):].strip()
if text.endswith(';'):
    text = text[:-1].strip()

events = json.loads(text)

# Let's inspect cases by batch
for idx, ev in enumerate(events):
    # Print every 20th or interesting event
    pass

print(f"Total events: {len(events)}")
