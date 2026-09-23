# -*- coding: utf-8 -*-
import json

with open('event_deck_modern.json', 'r', encoding='utf-8') as f:
    text = f.read().strip()
if text.startswith('const EVENT_DECK_MODERN ='):
    text = text[len('const EVENT_DECK_MODERN ='):].strip()
if text.endswith(';'):
    text = text[:-1].strip()

events = json.loads(text)

keywords = ['göç', 'mülteci', 'sığınmacı', 'geri kabul', 'hudut', 'iltica', 'yabancılar', 'vize', 'pasaport', 'ikamet', 'sınır', 'kaçak göçmen', 'insan kaçakçılığı', 'afgan', 'suriyeli']

matched = []
for ev in events:
    content = (ev['title'] + " " + ev['desc'] + " " + ev['source']).lower()
    for kw in keywords:
        if kw in content:
            matched.append((ev['id'], ev['title'], [c['id'] for c in ev['characters']], kw))
            break

print(f"Total matching migration/border keywords: {len(matched)}")
for ev_id, title, chars, kw in matched:
    print(f"  {ev_id} [{kw}]: {title} -> {chars}")
