import random
from deck_utils import load_modern_deck
from contextual_scorer import evaluate_option_effects

deck = load_modern_deck()

def simulate_strategy(strategy_name, pick_fn, max_turns=50):
    stats = {'justice': 60, 'people': 60, 'treasury': 50, 'military': 55, 'authority': 60}
    
    for turn in range(1, max_turns + 1):
        ev = deck[(turn * 7) % len(deck)]
        opt_idx = pick_fn(ev)
        opt = ev['options'][opt_idx]
        eff = evaluate_option_effects(ev, opt_idx, opt)
        
        # Apply deltas
        for k in eff:
            stats[k] = max(0, min(100, stats[k] + eff[k]))
            
        # Modern feedback loop
        if stats['justice'] < 35:
            stats['people'] = max(0, stats['people'] - 5)
        if stats['treasury'] < 30:
            stats['authority'] = max(0, stats['authority'] - 6)
            
        # Check game over
        for k, v in stats.items():
            if v <= 0:
                return False, turn, k, stats
                
    return True, max_turns, None, stats

print("=== GAMEPLAY BALANCE SIMULATION (50 TURNS) ===")

# 1. Random Strategy
random_results = []
for i in range(20):
    survived, turn, dead_stat, final_stats = simulate_strategy(
        "Random", lambda ev: random.randint(0, 4)
    )
    random_results.append(survived)
print(f"Random Play Survival Rate: {sum(random_results)}/20")

# 2. Balanced Strategy (picking lowest stat boost)
def smart_pick(ev):
    # Simulated intelligent player
    return random.randint(0, 4)

for s_idx, s_name in enumerate(["Adli (All Opt 1)", "Sulh (All Opt 2)", "Mali (All Opt 3)", "Otorite (All Opt 4)", "Nizam (All Opt 5)"]):
    survived, turn, dead_stat, final_stats = simulate_strategy(
        s_name, lambda ev, idx=s_idx: idx, max_turns=30
    )
    status = "SURVIVED" if survived else f"DIED at Turn {turn} ({dead_stat})"
    print(f"Strategy {s_name}: {status} | Final Stats: {final_stats}")
