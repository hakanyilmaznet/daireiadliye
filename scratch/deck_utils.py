import json
import os

def make_preview(eff):
    pos = []
    neg = []
    order = [('Adalet', 'justice'), ('Halk', 'people'), ('Hazine', 'treasury'), ('Güvenlik', 'military'), ('Otorite', 'authority')]
    for tr, k in order:
        v = eff.get(k, 0)
        if v > 0:
            pos.append(f"{tr} +{v}")
        elif v < 0:
            neg.append(f"{tr} {v}")
    pos_str = ", ".join(pos)
    neg_str = ", ".join(neg)
    if pos_str and neg_str:
        return f"{pos_str} | {neg_str}"
    elif pos_str:
        return pos_str
    elif neg_str:
        return neg_str
    return "Etkisiz"

def load_modern_deck():
    with open('event_deck_modern.json', 'r', encoding='utf-8') as f:
        c = f.read()
    start = c.find('[')
    end = c.rfind(']') + 1
    return json.loads(c[start:end])

def save_modern_deck(deck):
    # write to both event_deck_modern.json and event_deck_modern.js
    content = "const EVENT_DECK_MODERN = " + json.dumps(deck, ensure_ascii=False, indent=2) + ";\n"
    with open('event_deck_modern.json', 'w', encoding='utf-8') as f:
        f.write(content)
    with open('event_deck_modern.js', 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Successfully saved {len(deck)} events to event_deck_modern.json and event_deck_modern.js")

def apply_options_to_deck(deck, options_map):
    applied = 0
    for ev in deck:
        eid = ev['id']
        if eid in options_map:
            raw_opts = options_map[eid]
            formatted_opts = []
            for o in raw_opts:
                eff = o['effects']
                prev = make_preview(eff)
                formatted_opts.append({
                    "label": o['label'],
                    "preview": prev,
                    "effects": eff,
                    "log": o['log']
                })
            ev['options'] = formatted_opts
            applied += 1
    print(f"Applied realistic options to {applied} events.")
    return deck
