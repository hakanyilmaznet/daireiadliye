import json
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from deck_utils import load_modern_deck, make_preview
from contextual_scorer import evaluate_option_effects

deck = load_modern_deck()

test_ids = [
    'tr_vaka_001', # Susurluk
    'tr_vaka_002', # Kardak
    'tr_vaka_004', # 1999 Depremi
    'tr_vaka_121', # Annan Planı
    'tr_vaka_211', # 2001 Krizinde IMF Standby
    'tr_vaka_551', # Kobani / Hendek
    'tr_vaka_711', # Cannes Kış Uykusu
    'tr_vaka_831', # Kıdem Tazminatı & Grev
    'tr_vaka_941', # Sahte İçki KOM Baskını
    'tr_vaka_996', # Kalkınma Yolu Projesi
]

print("=== TESTING CONTEXTUAL SCORER ===")
for eid in test_ids:
    ev = next((x for x in deck if x['id'] == eid), None)
    if not ev:
        continue
    print(f"\n[{ev['id']}] {ev['title']}")
    for i, opt in enumerate(ev['options']):
        new_eff = evaluate_option_effects(ev, i, opt)
        new_prev = make_preview(new_eff)
        old_eff = opt.get('effects', {})
        old_prev = opt.get('preview', '')
        print(f"  Opt {i+1}: {opt['label'][:75]}...")
        print(f"    OLD: {old_prev} -> {old_eff}")
        print(f"    NEW: {new_prev} -> {new_eff}")
