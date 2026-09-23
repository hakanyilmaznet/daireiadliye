import json
import sys

# Force utf-8 stdout
sys.stdout.reconfigure(encoding='utf-8')

with open("event_deck.json", "r", encoding="utf-8") as f:
    c = f.read()
    ott = json.loads(c[c.find("["):c.rfind("]")+1])

print(f"=== OTTOMAN EVENTS (Sample) ===")
for idx in [0, 1, 2]:
    ev = ott[idx]
    print(f"\n[Ottoman Event {idx}: {ev['title']}]")
    print("Desc:", ev['desc'])
    for i, o in enumerate(ev["options"]):
        print(f"  Option {i+1} ({o.get('label')}): {o.get('log')}")
        print(f"    preview: {o.get('preview')}")
        print(f"    effects: {o.get('effects')}")

with open("event_deck_modern.json", "r", encoding="utf-8") as f:
    c = f.read()
    mod = json.loads(c[c.find("["):c.rfind("]")+1])

print(f"\n=== MODERN EVENTS (Sample) ===")
for idx in [0, 50, 100, 101, 102, 200, 500]:
    ev = mod[idx]
    print(f"\n[Modern Event {idx} ({ev['id']}): {ev['title']}]")
    print("Desc:", ev['desc'])
    for i, o in enumerate(ev["options"]):
        print(f"  Option {i+1} ({o.get('label')}): {o.get('log')}")
        print(f"    preview: {o.get('preview')}")
        print(f"    effects: {o.get('effects')}")
