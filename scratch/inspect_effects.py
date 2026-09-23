import json
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from deck_utils import load_modern_deck

deck = load_modern_deck()
print("=== EVENTS 1 TO 5 ===")
for ev in deck[:5]:
    print(f"[{ev['id']}] {ev['title']}")
    for i, opt in enumerate(ev['options']):
        print(f"  Opt {i+1}: {opt['effects']} | {opt['label'][:60]}")

print("\n=== OTTOMAN DECK SAMPLE ===")
with open('event_deck.json', 'r', encoding='utf-8') as f:
    c = f.read()
start = c.find('[')
end = c.rfind(']') + 1
ott_deck = json.loads(c[start:end])
for ev in ott_deck[:5]:
    print(f"[{ev['id']}] {ev['title']}")
    for i, opt in enumerate(ev['options']):
        print(f"  Opt {i+1}: {opt['effects']} | {opt['label'][:60]}")
