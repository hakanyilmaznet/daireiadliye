import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('event_deck_modern.json', 'r', encoding='utf-8') as f:
    c = f.read()
    mod = json.loads(c[c.find('['):c.rfind(']')+1])

print('=== TR_VAKA_001 ===')
ev = mod[0]
print(ev['title'])
print(ev['desc'])
for i, o in enumerate(ev['options']):
    print(f"[{i+1}] {o['label']}")
    print(f"     effects: {o['effects']}")
    print(f"     log: {o['log']}")

print('\n=== TR_VAKA_002 ===')
ev = mod[1]
print(ev['title'])
print(ev['desc'])
for i, o in enumerate(ev['options']):
    print(f"[{i+1}] {o['label']}")
    print(f"     effects: {o['effects']}")
    print(f"     log: {o['log']}")

with open('event_deck.json', 'r', encoding='utf-8') as f:
    c = f.read()
    ott = json.loads(c[c.find('['):c.rfind(']')+1])

print('\n=== OTTOMAN EVENT 0 ===')
ev = ott[0]
print(ev['title'])
print(ev['desc'])
for i, o in enumerate(ev['options']):
    print(f"[{i+1}] {o['label']}")
    print(f"     effects: {o['effects']}")
    print(f"     log: {o['log']}")

print('\n=== OTTOMAN EVENT 1 ===')
ev = ott[1]
print(ev['title'])
print(ev['desc'])
for i, o in enumerate(ev['options']):
    print(f"[{i+1}] {o['label']}")
    print(f"     effects: {o['effects']}")
    print(f"     log: {o['log']}")
