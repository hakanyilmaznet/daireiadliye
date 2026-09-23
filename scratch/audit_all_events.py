import json
import re
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from deck_utils import load_modern_deck, make_preview

def audit():
    deck = load_modern_deck()
    print(f"Total events in deck: {len(deck)}")
    assert len(deck) == 1000, f"Expected 1000, got {len(deck)}"

    bad_templates = [
        "bağımsız teftiş ve yargı sürecini tavizsiz işlet",
        "krizinde taraflar ve ilgili kurumlarla istişare masası kur",
        "Kurumsal Düzenleme Kanunu",
        "Kriz Masası Kur",
        "{title}",
        "bağımsız teftiş ve denetim sürecini başlat",
    ]

    bad_counts = {t: 0 for t in bad_templates}
    title_matches_in_options = 0
    preview_mismatches = 0
    total_options = 0

    for i, ev in enumerate(deck):
        title = ev.get('title', '')
        options = ev.get('options', [])
        if len(options) != 5:
            print(f"Warning: Event {ev.get('id')} has {len(options)} options!")
        for opt in options:
            total_options += 1
            txt = opt.get('label', '')
            log = opt.get('log', '')
            preview = opt.get('preview', '')
            effects = opt.get('effects', {})

            for t in bad_templates:
                if t.lower() in txt.lower():
                    bad_counts[t] += 1

            # Check if entire title was clumsily injected into option text (only for events > 100)
            if len(title) > 6 and title.lower() in txt.lower() and i >= 100:
                title_matches_in_options += 1
                if title_matches_in_options <= 5:
                    print(f"Title match notice in ev {ev.get('id')}: '{title}' in '{txt}'")

            # Check preview math
            expected = make_preview(effects)
            if preview != expected:
                preview_mismatches += 1
                if preview_mismatches <= 3:
                    print(f"Preview mismatch in {ev.get('id')}: got '{preview}', expected '{expected}'")

    print("\n--- AUDIT RESULTS ---")
    print(f"Total events: {len(deck)}")
    print(f"Total options: {total_options}")
    print(f"Bad template counts: {bad_counts}")
    print(f"Clumsy Title matches in options: {title_matches_in_options}")
    print(f"Preview mismatches: {preview_mismatches}")

    # Inspect samples across batches
    print("\n--- SAMPLE INSPECTION ---")
    sample_indices = [120, 245, 360, 480, 595, 710, 830, 940, 995]
    for idx in sample_indices:
        ev = deck[idx]
        print(f"\n[{ev['id']}] {ev['title']} ({ev.get('characters', '')})")
        print(f"  Desc: {ev['desc'][:90]}...")
        for opt_idx, opt in enumerate(ev['options']):
            print(f"    Opt {opt_idx+1}: {opt['label']}")
            print(f"           Preview: {opt['preview']}")
            print(f"           Log: {opt['log'][:80]}...")

if __name__ == '__main__':
    audit()
