import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('event_deck_modern.json', 'r', encoding='utf-8') as f:
    c = f.read()
    mod = json.loads(c[c.find('['):c.rfind(']')+1])

def dump_range(start, end):
    for i in range(start, end):
        ev = mod[i]
        print(f"[{i}] {ev['id']}: {ev['title']}")
        print(f"     {ev['desc']}")

if __name__ == '__main__':
    start = int(sys.argv[1]) if len(sys.argv) > 1 else 100
    end = int(sys.argv[2]) if len(sys.argv) > 2 else 130
    dump_range(start, end)
