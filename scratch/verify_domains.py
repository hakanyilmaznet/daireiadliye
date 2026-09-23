import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('event_deck_modern.json', 'r', encoding='utf-8') as f:
    c = f.read()
    mod = json.loads(c[c.find('['):c.rfind(']')+1])

print(f'Total events: {len(mod)}')
for d in range(30):
    start_idx = 100 + d * 30
    end_idx = start_idx + 30
    first_ev = mod[start_idx]
    last_ev = mod[end_idx - 1]
    print(f"Domain {d+1}: [{start_idx}..{end_idx-1}] ({first_ev['id']} - {last_ev['id']})")
    print(f"   Start: {first_ev['title']}")
    print(f"   End:   {last_ev['title']}")
