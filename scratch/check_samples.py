import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('event_deck_modern.json', 'r', encoding='utf-8') as f:
    c = f.read()
    mod = json.loads(c[c.find('['):c.rfind(']')+1])

def check_indices(indices):
    for idx in indices:
        ev = mod[idx]
        print(f"\n=== [{idx}] {ev['id']}: {ev['title']} ===")
        for j, o in enumerate(ev['options']):
            print(f"[{j+1}] {o['label']}")
            print(f"     log: {o['log']}")
            print(f"     preview: {o['preview']}")

if __name__ == '__main__':
    indices = [int(x) for x in sys.argv[1:]] if len(sys.argv) > 1 else [190, 220, 254, 264, 279]
    check_indices(indices)
