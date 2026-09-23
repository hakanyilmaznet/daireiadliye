import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('event_deck_modern.json', 'r', encoding='utf-8') as f:
    c = f.read()
    mod = json.loads(c[c.find('['):c.rfind(']')+1])

for idx in [100, 102, 130, 131, 160]:
    ev = mod[idx]
    print(f"\n=== {ev['id']}: {ev['title']} ===")
    for j, o in enumerate(ev['options']):
        print(f"[{j+1}] {o['label']}")
        print(f"     log: {o['log']}")
        print(f"     preview: {o['preview']}")
