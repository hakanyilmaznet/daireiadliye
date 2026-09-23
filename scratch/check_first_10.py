import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('event_deck_modern.json', 'r', encoding='utf-8') as f:
    c = f.read()
    mod = json.loads(c[c.find('['):c.rfind(']')+1])

print('Checking events 0 to 9:')
for i in range(10):
    ev = mod[i]
    print(f"\nEvent {i+1} ({ev['id']}): {ev['title']}")
    for j, o in enumerate(ev['options']):
        print(f"  Opt {j+1}: {o['label']}")
