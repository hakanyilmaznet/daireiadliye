# -*- coding: utf-8 -*-
"""
Dâire-i Adliyye - Complete 1000 Modern Turkey Event Generator
Generates exactly 1000 events (tr_vaka_001 to tr_vaka_1000)
Preserves original 100 events, generates 900 authentic events from 1995-2026.
"""

import json
import os
import re

from scratch.data_domains_1_to_10 import DOMAINS_1_TO_10
from scratch.data_domains_11_to_20 import DOMAINS_11_TO_20
from scratch.data_domains_21_to_30 import DOMAINS_21_TO_30

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODERN_JSON_PATH = os.path.join(BASE_DIR, 'event_deck_modern.json')
MODERN_JS_PATH = os.path.join(BASE_DIR, 'event_deck_modern.js')
CHARS_PATH = os.path.join(BASE_DIR, 'characters_modern.json')

with open(CHARS_PATH, 'r', encoding='utf-8') as f:
    chars_data = json.load(f)
char_map = {c['id']: c['name'] for c in chars_data}

def format_preview(effects):
    stat_labels = {
        'justice': 'Adalet',
        'people': 'Halk',
        'treasury': 'Hazine',
        'military': 'Güvenlik',
        'authority': 'Otorite'
    }
    pos = []
    neg = []
    for k in ['justice', 'people', 'treasury', 'military', 'authority']:
        v = effects.get(k, 0)
        if v > 0:
            pos.append(f"{stat_labels[k]} +{v}")
        elif v < 0:
            neg.append(f"{stat_labels[k]} {v}")
    if pos and neg:
        return f"{', '.join(pos)} | {', '.join(neg)}"
    elif pos:
        return ', '.join(pos)
    elif neg:
        return ', '.join(neg)
    return ""

def load_existing_100():
    with open(MODERN_JSON_PATH, 'r', encoding='utf-8') as f:
        content = f.read().strip()
    content = re.sub(r'^(const|var|let)\s+EVENT_DECK_MODERN\s*=\s*', '', content)
    content = re.sub(r';\s*$', '', content)
    deck = json.loads(content)
    print(f"Mevcut desteden yüklenen olay sayısı: {len(deck[:100])}")
    return deck[:100]

def build_new_900():
    all_domains = DOMAINS_1_TO_10 + DOMAINS_11_TO_20 + DOMAINS_21_TO_30
    events = []
    current_id = 101

    for domain in all_domains:
        d_name = domain["name"]
        d_source = domain["source"]
        d_char1 = domain["char1"]
        d_char2 = domain["char2"]
        cases = domain["cases"]

        for idx, item in enumerate(cases):
            eff_mod = (current_id + idx) % 5

            j1 = 7 + (eff_mod % 3)
            p1 = 8 - (eff_mod % 2)
            t1 = -2 - (eff_mod % 2)
            a1 = -2 - (eff_mod % 3)

            j2 = -7 - (eff_mod % 2)
            p2 = 7 + (eff_mod % 3)
            t2 = -2 - (eff_mod % 2)
            a2 = 7 + (eff_mod % 2)

            j3 = -2 - (eff_mod % 2)
            p3 = -7 - (eff_mod % 3)
            t3 = 8 + (eff_mod % 2)
            a3 = 3 + (eff_mod % 2)

            j4 = -3 - (eff_mod % 2)
            p4 = -7 - (eff_mod % 3)
            m4 = 8 + (eff_mod % 2)
            a4 = 7 + (eff_mod % 2)

            j5 = 7 + (eff_mod % 3)
            p5 = 3 + (eff_mod % 2)
            t5 = -7 - (eff_mod % 2)
            a5 = 7 + (eff_mod % 2)

            eff1 = {'justice': j1, 'people': p1, 'treasury': t1, 'military': 0, 'authority': a1}
            eff2 = {'justice': j2, 'people': p2, 'treasury': t2, 'military': 0, 'authority': a2}
            eff3 = {'justice': j3, 'people': p3, 'treasury': t3, 'military': 0, 'authority': a3}
            eff4 = {'justice': j4, 'people': p4, 'treasury': 0, 'military': m4, 'authority': a4}
            eff5 = {'justice': j5, 'people': p5, 'treasury': t5, 'military': 0, 'authority': a5}

            if len(item) == 12:
                # Custom detailed options
                title, desc, o1_l, o1_g, o2_l, o2_g, o3_l, o3_g, o4_l, o4_g, o5_l, o5_g = item
            else:
                title, desc = item
                o1_l = f"{title} konusunda bağımsız teftiş ve yargı sürecini tavizsiz işlet; sorumluları adalet önüne çıkarıp şeffaflık sağla."
                o1_g = f"{title} hakkında adli tahkikat şeffaflıkla işletildi; adaletin tecellisi halk nezdinde devlete olan güveni tazeledi."
                
                o2_l = f"{title} krizinde taraflar ve ilgili kurumlarla istişare masası kur; gerilimi düşürerek idari dengeyi ve uzlaşıyı sağla."
                o2_g = f"{title} hadisesinde maslahat gözetilerek toplumsal uzlaşı sağlandı; taraflar teskin edildi ancak hesap sorma süreci sınırlı kaldı."

                o3_l = f"{title} meselesinde kamu kaynaklarını ve Hazine kasasını koru; şüpheli varlıklara el koyup tasarruf tedbirlerini tavizsiz uygula."
                o3_g = f"{title} kapsamında mali disiplin sağlandı; Hazine kasası güçlendirildi ve kamu zararı sorumlulardan tahsil edildi."

                o4_l = f"{title} karşısında kolluk ve güvenlik bürokrasisini harekete geçir; kamu nizamını bozan unsurlara karşı devletin mutlak heybetini hissettir."
                o4_g = f"{title} karşısında kararlı güvenlik tedbirleri uygulandı; kamu düzeni tesis edilerek devletin sarsılmaz otoritesi gösterildi."

                o5_l = f"TBMM'den '{title} ve Kurumsal Düzenleme Kanunu' çıkararak köklü bir reform paketiyle benzer krizlerin tekerrürünü önle."
                o5_g = f"Yürürlüğe konan reform ve yeni mevzuat ile kurumsal nizam sağlandı; benzer krizlerin tekerrürü yasal teminatla önlendi."

            options = [
                {'label': o1_l, 'preview': format_preview(eff1), 'effects': eff1, 'log': o1_g},
                {'label': o2_l, 'preview': format_preview(eff2), 'effects': eff2, 'log': o2_g},
                {'label': o3_l, 'preview': format_preview(eff3), 'effects': eff3, 'log': o3_g},
                {'label': o4_l, 'preview': format_preview(eff4), 'effects': eff4, 'log': o4_g},
                {'label': o5_l, 'preview': format_preview(eff5), 'effects': eff5, 'log': o5_g}
            ]

            ev_id = f"tr_vaka_{current_id:03d}" if current_id < 1000 else f"tr_vaka_{current_id}"
            
            c1_name = char_map.get(d_char1, "Cumhurbaşkanı")
            c2_name = char_map.get(d_char2, "Adalet Bakanı")

            ev = {
                'id': ev_id,
                'characters': [
                    {'id': d_char1, 'name': c1_name},
                    {'id': d_char2, 'name': c2_name}
                ],
                'source': d_source,
                'title': title,
                'desc': desc,
                'options': options
            }
            events.append(ev)
            current_id += 1

    print(f"Oluşturulan yeni vaka sayısı: {len(events)} (İlk: {events[0]['id']}, Son: {events[-1]['id']})")
    return events

def main():
    existing_100 = load_existing_100()
    new_900 = build_new_900()

    full_1000 = existing_100 + new_900
    print(f"Toplam deste boyutu: {len(full_1000)}")
    assert len(full_1000) == 1000, f"Hata: Toplam vaka 1000 değil ({len(full_1000)})"

    # Validation checks
    for idx, ev in enumerate(full_1000):
        expected_id = f"tr_vaka_{idx+1:03d}" if (idx+1) < 1000 else f"tr_vaka_{idx+1}"
        assert ev['id'] == expected_id, f"ID uyuşmazlığı: beklenen {expected_id}, bulunan {ev['id']}"
        assert len(ev['options']) == 5, f"{ev['id']} options sayısı 5 değil ({len(ev['options'])})"
        assert ev['title'], f"{ev['id']} title boş"
        assert ev['desc'], f"{ev['id']} desc boş"
        assert len(ev['characters']) >= 1, f"{ev['id']} characters boş"

        for opt in ev['options']:
            assert opt['label'], f"{ev['id']} option label boş"
            assert opt['log'], f"{ev['id']} option log boş"
            assert 'effects' in opt, f"{ev['id']} option effects yok"
            for k in ['justice', 'people', 'treasury', 'military', 'authority']:
                assert k in opt['effects'], f"{ev['id']} effects {k} eksik"

    print("Tüm 1000 vaka doğrulama testlerini başarıyla geçti!")

    # Format JSON
    json_body = json.dumps(full_1000, ensure_ascii=False, indent=2)
    file_content = f"const EVENT_DECK_MODERN = {json_body};\n"

    # Write event_deck_modern.json
    with open(MODERN_JSON_PATH, 'w', encoding='utf-8') as f:
        f.write(file_content)
    print(f"{MODERN_JSON_PATH} başarıyla güncellendi ({os.path.getsize(MODERN_JSON_PATH):,} bayt).")

    # Write event_deck_modern.js
    with open(MODERN_JS_PATH, 'w', encoding='utf-8') as f:
        f.write(file_content)
    print(f"{MODERN_JS_PATH} başarıyla güncellendi ({os.path.getsize(MODERN_JS_PATH):,} bayt).")

if __name__ == '__main__':
    main()
