import json

with open('event_deck_modern.json', 'r', encoding='utf-8') as f:
    text = f.read().strip()
if text.startswith('const EVENT_DECK_MODERN ='):
    text = text[len('const EVENT_DECK_MODERN ='):].strip()
if text.endswith(';'):
    text = text[:-1].strip()

events = json.loads(text)

with open('characters_modern.json', 'r', encoding='utf-8') as f:
    chars = json.load(f)

print(f'Total events: {len(events)}')
print(f'Total characters: {len(chars)}')

for b in range(100, 1000, 30):
    sample = events[b]
    chars_list = [c['id'] for c in sample['characters']]
    print(f"Batch {b+1}-{min(b+30, 1000)}: '{sample['title'][:40]}' -> {chars_list}")
