import json
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from deck_utils import load_modern_deck, save_modern_deck, make_preview
from contextual_scorer import evaluate_option_effects

def run():
    deck = load_modern_deck()
    print(f"Loaded {len(deck)} events from modern deck.")
    
    total_options_updated = 0
    stat_deltas_sum = {'justice': 0, 'people': 0, 'treasury': 0, 'military': 0, 'authority': 0}
    stat_deltas_count = {'justice': 0, 'people': 0, 'treasury': 0, 'military': 0, 'authority': 0}

    for ev in deck:
        options = ev.get('options', [])
        for idx, opt in enumerate(options):
            new_eff = evaluate_option_effects(ev, idx, opt)
            new_prev = make_preview(new_eff)
            
            opt['effects'] = new_eff
            opt['preview'] = new_prev
            total_options_updated += 1

            for k, v in new_eff.items():
                stat_deltas_sum[k] += v
                stat_deltas_count[k] += 1

    print(f"Successfully re-evaluated {total_options_updated} options across {len(deck)} events.")
    print("Average deltas per option:")
    for k in stat_deltas_sum:
        avg = stat_deltas_sum[k] / stat_deltas_count[k]
        print(f"  {k:10s}: {avg:+.2f}")

    save_modern_deck(deck)
    print("Deck successfully saved to both event_deck_modern.json and event_deck_modern.js.")

if __name__ == '__main__':
    run()
