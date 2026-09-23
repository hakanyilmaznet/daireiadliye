# -*- coding: utf-8 -*-
"""
Test script to refine character assignments across all 1000 modern events
and generate updated characters_modern.json.
"""
import json
import re

with open('event_deck_modern.json', 'r', encoding='utf-8') as f:
    text = f.read().strip()
if text.startswith('const EVENT_DECK_MODERN ='):
    text = text[len('const EVENT_DECK_MODERN ='):].strip()
if text.endswith(';'):
    text = text[:-1].strip()

events = json.loads(text)

# Canonical names for characters in modern era
CANONICAL_NAMES = {
    "char_cumhurbaskani": "Cumhurbaşkanı",
    "char_basbakan": "Başbakan",
    "char_tbmm_baskani": "TBMM Başkanı",
    "char_milletvekili": "TBMM Grup Başkanvekili",
    "char_adalet_bakani": "Adalet Bakanı",
    "char_anayasa_mahkemesi_baskani": "Anayasa Mahkemesi Başkanı",
    "char_adli_yargi_hakimi": "Cumhuriyet Başsavcısı",
    "char_icisleri_bakani": "İçişleri Bakanı",
    "char_genelkurmay_baskani": "Genelkurmay Başkanı",
    "char_savunma_bakani": "Milli Savunma Bakanı",
    "char_savunma_sanayii_baskani": "Savunma Sanayii Başkanı",
    "char_diplomat": "Dışişleri Müsteşarı",
    "char_hazine_bakani": "Hazine ve Maliye Bakanı",
    "char_merkez_bankasi_baskani": "Merkez Bankası Başkanı",
    "char_ticaret_bakani": "Ticaret Bakanı",
    "char_sanayi_bakani": "Sanayi ve Teknoloji Bakanı",
    "char_tusiad_baskani": "İş Dünyası / TÜSİAD Başkanı",
    "char_esnaf_odasi_baskani": "Esnaf Odaları Başkanı",
    "char_tuketici_dernekleri_baskani": "Tüketici Hakları Temsilcisi",
    "char_afad_baskani": "AFAD / Kriz Masası Başkanı",
    "char_cevre_sehircilik_bakani": "Çevre ve Şehircilik Bakanı",
    "char_sehir_plancisi": "Mimarlar ve Şehir Plancıları Temsilcisi",
    "char_saglik_bakani": "Sağlık Bakanı",
    "char_goc_idaresi_baskani": "Göç İdaresi Başkanı"
}

# Specific overrides by event ID:
SPECIFIC_OVERRIDES = {
    # Göç ve Sınır Güvenliği Olayları -> char_goc_idaresi_baskani
    "tr_vaka_173": ("char_ticaret_bakani", "char_goc_idaresi_baskani"),
    "tr_vaka_286": ("char_adli_yargi_hakimi", "char_goc_idaresi_baskani"),
    "tr_vaka_814": ("char_sehir_plancisi", "char_goc_idaresi_baskani"),
    "tr_vaka_815": ("char_icisleri_bakani", "char_goc_idaresi_baskani"),
    "tr_vaka_954": ("char_icisleri_bakani", "char_goc_idaresi_baskani"),
    "tr_vaka_955": ("char_icisleri_bakani", "char_goc_idaresi_baskani"),
    "tr_vaka_956": ("char_icisleri_bakani", "char_goc_idaresi_baskani"),
    "tr_vaka_957": ("char_icisleri_bakani", "char_goc_idaresi_baskani"),
    "tr_vaka_958": ("char_savunma_bakani", "char_goc_idaresi_baskani"),
    "tr_vaka_969": ("char_icisleri_bakani", "char_goc_idaresi_baskani"),

    # TÜSİAD / İş Dünyası / Sermaye / Özelleştirme Olayları -> char_tusiad_baskani
    "tr_vaka_026": ("char_hazine_bakani", "char_tusiad_baskani"),
    "tr_vaka_052": ("char_hazine_bakani", "char_tusiad_baskani"),
    "tr_vaka_078": ("char_hazine_bakani", "char_tusiad_baskani"),
    "tr_vaka_134": ("char_adli_yargi_hakimi", "char_tusiad_baskani"),
    "tr_vaka_137": ("char_hazine_bakani", "char_tusiad_baskani"),
    "tr_vaka_143": ("char_hazine_bakani", "char_tusiad_baskani"),
    "tr_vaka_154": ("char_hazine_bakani", "char_tusiad_baskani"),
    "tr_vaka_155": ("char_hazine_bakani", "char_tusiad_baskani"),
    "tr_vaka_156": ("char_hazine_bakani", "char_tusiad_baskani"),
    "tr_vaka_182": ("char_hazine_bakani", "char_tusiad_baskani"),
    "tr_vaka_184": ("char_sanayi_bakani", "char_tusiad_baskani"),
    "tr_vaka_187": ("char_sanayi_bakani", "char_tusiad_baskani"),
    "tr_vaka_189": ("char_sanayi_bakani", "char_tusiad_baskani"),
    "tr_vaka_190": ("char_hazine_bakani", "char_tusiad_baskani"),
    "tr_vaka_274": ("char_adli_yargi_hakimi", "char_tusiad_baskani"),
    "tr_vaka_543": ("char_hazine_bakani", "char_tusiad_baskani"),
    "tr_vaka_548": ("char_hazine_bakani", "char_tusiad_baskani"),
    "tr_vaka_697": ("char_cumhurbaskani", "char_tusiad_baskani"),
    "tr_vaka_699": ("char_sehir_plancisi", "char_tusiad_baskani"),
    "tr_vaka_717": ("char_ticaret_bakani", "char_tusiad_baskani"),
    "tr_vaka_721": ("char_ticaret_bakani", "char_tusiad_baskani"),
    "tr_vaka_722": ("char_adalet_bakani", "char_tusiad_baskani"),
    "tr_vaka_824": ("char_hazine_bakani", "char_tusiad_baskani"),
    "tr_vaka_831": ("char_hazine_bakani", "char_tusiad_baskani"),
    "tr_vaka_832": ("char_hazine_bakani", "char_tusiad_baskani"),
    "tr_vaka_833": ("char_sanayi_bakani", "char_tusiad_baskani"),
    "tr_vaka_837": ("char_hazine_bakani", "char_tusiad_baskani"),
    "tr_vaka_838": ("char_hazine_bakani", "char_tusiad_baskani"),
    "tr_vaka_860": ("char_adalet_bakani", "char_tusiad_baskani"),
    "tr_vaka_988": ("char_ticaret_bakani", "char_tusiad_baskani"),
    "tr_vaka_994": ("char_sanayi_bakani", "char_tusiad_baskani"),
    "tr_vaka_995": ("char_hazine_bakani", "char_tusiad_baskani"),

    # Domain 3 (161-190) AB ve Hukuk Uyum Düzenlemeleri
    "tr_vaka_164": ("char_adalet_bakani", "char_basbakan"),
    "tr_vaka_167": ("char_adalet_bakani", "char_basbakan"),
    "tr_vaka_168": ("char_adalet_bakani", "char_adli_yargi_hakimi"),
    "tr_vaka_169": ("char_adalet_bakani", "char_adli_yargi_hakimi"),
    "tr_vaka_170": ("char_adalet_bakani", "char_adli_yargi_hakimi"),
    "tr_vaka_171": ("char_cumhurbaskani", "char_basbakan"),
    "tr_vaka_172": ("char_icisleri_bakani", "char_basbakan"),
    "tr_vaka_174": ("char_ticaret_bakani", "char_sanayi_bakani"),
    "tr_vaka_175": ("char_hazine_bakani", "char_esnaf_odasi_baskani"),
    "tr_vaka_176": ("char_saglik_bakani", "char_hazine_bakani"),
    "tr_vaka_177": ("char_milletvekili", "char_basbakan"),
    "tr_vaka_178": ("char_tbmm_baskani", "char_basbakan"),
    "tr_vaka_179": ("char_cevre_sehircilik_bakani", "char_sehir_plancisi"),
    "tr_vaka_180": ("char_adalet_bakani", "char_tuketici_dernekleri_baskani"),
    "tr_vaka_181": ("char_hazine_bakani", "char_merkez_bankasi_baskani"),
    "tr_vaka_183": ("char_cumhurbaskani", "char_adalet_bakani"),
    "tr_vaka_185": ("char_genelkurmay_baskani", "char_savunma_bakani"),
    "tr_vaka_186": ("char_adalet_bakani", "char_genelkurmay_baskani"),
    "tr_vaka_188": ("char_cevre_sehircilik_bakani", "char_sehir_plancisi"),

    # Domain 4 (191-220) E-Muhtıra, Mitingler ve Davalar
    "tr_vaka_194": ("char_genelkurmay_baskani", "char_basbakan"),
    "tr_vaka_195": ("char_basbakan", "char_genelkurmay_baskani"),
    "tr_vaka_196": ("char_icisleri_bakani", "char_cumhurbaskani"),
    "tr_vaka_198": ("char_cumhurbaskani", "char_tbmm_baskani"),
    "tr_vaka_206": ("char_icisleri_bakani", "char_adli_yargi_hakimi"),
    "tr_vaka_207": ("char_adalet_bakani", "char_adli_yargi_hakimi"),
    "tr_vaka_208": ("char_adli_yargi_hakimi", "char_icisleri_bakani"),
    "tr_vaka_209": ("char_adalet_bakani", "char_adli_yargi_hakimi"),
    "tr_vaka_210": ("char_icisleri_bakani", "char_adli_yargi_hakimi"),
    "tr_vaka_211": ("char_icisleri_bakani", "char_adli_yargi_hakimi"),
    "tr_vaka_212": ("char_icisleri_bakani", "char_adli_yargi_hakimi"),
    "tr_vaka_213": ("char_icisleri_bakani", "char_adli_yargi_hakimi"),
    "tr_vaka_214": ("char_adli_yargi_hakimi", "char_genelkurmay_baskani"),
    "tr_vaka_215": ("char_adli_yargi_hakimi", "char_genelkurmay_baskani"),
    "tr_vaka_216": ("char_adli_yargi_hakimi", "char_genelkurmay_baskani"),
    "tr_vaka_217": ("char_adli_yargi_hakimi", "char_genelkurmay_baskani"),
    "tr_vaka_218": ("char_adli_yargi_hakimi", "char_genelkurmay_baskani"),
    "tr_vaka_219": ("char_adli_yargi_hakimi", "char_genelkurmay_baskani"),
    "tr_vaka_220": ("char_adli_yargi_hakimi", "char_genelkurmay_baskani"),

    # Domain 2 (131-160) Bankacılık Operasyonları
    "tr_vaka_132": ("char_hazine_bakani", "char_adli_yargi_hakimi"),
    "tr_vaka_133": ("char_basbakan", "char_adli_yargi_hakimi"),
    "tr_vaka_135": ("char_hazine_bakani", "char_adli_yargi_hakimi"),
    "tr_vaka_136": ("char_icisleri_bakani", "char_adli_yargi_hakimi"),
    "tr_vaka_146": ("char_icisleri_bakani", "char_adli_yargi_hakimi"),
    "tr_vaka_147": ("char_icisleri_bakani", "char_adli_yargi_hakimi"),
    "tr_vaka_148": ("char_ticaret_bakani", "char_icisleri_bakani"),
    "tr_vaka_149": ("char_ticaret_bakani", "char_icisleri_bakani"),
    "tr_vaka_150": ("char_hazine_bakani", "char_adli_yargi_hakimi"),
    "tr_vaka_151": ("char_cevre_sehircilik_bakani", "char_adli_yargi_hakimi"),
    "tr_vaka_152": ("char_hazine_bakani", "char_adli_yargi_hakimi"),

    # Domain 18 (611-640) Eğitim, Üniversiteler, Gençlik
    "tr_vaka_611": ("char_tbmm_baskani", "char_basbakan"),
    "tr_vaka_612": ("char_anayasa_mahkemesi_baskani", "char_milletvekili"),
    "tr_vaka_614": ("char_anayasa_mahkemesi_baskani", "char_milletvekili"),
    "tr_vaka_616": ("char_basbakan", "char_tbmm_baskani"),
    "tr_vaka_617": ("char_icisleri_bakani", "char_savunma_bakani"),
    "tr_vaka_618": ("char_tbmm_baskani", "char_milletvekili"),
    "tr_vaka_619": ("char_basbakan", "char_milletvekili"),
    "tr_vaka_620": ("char_adli_yargi_hakimi", "char_icisleri_bakani"),
    "tr_vaka_621": ("char_adli_yargi_hakimi", "char_cumhurbaskani"),
    "tr_vaka_626": ("char_icisleri_bakani", "char_sehir_plancisi"),
    "tr_vaka_628": ("char_hazine_bakani", "char_tbmm_baskani"),
    "tr_vaka_629": ("char_sanayi_bakani", "char_hazine_bakani"),
    "tr_vaka_630": ("char_sanayi_bakani", "char_saglik_bakani"),
    "tr_vaka_632": ("char_icisleri_bakani", "char_cumhurbaskani"),
    "tr_vaka_633": ("char_sehir_plancisi", "char_cevre_sehircilik_bakani"),
    "tr_vaka_634": ("char_cumhurbaskani", "char_tbmm_baskani"),
    "tr_vaka_635": ("char_esnaf_odasi_baskani", "char_sanayi_bakani"),
    "tr_vaka_636": ("char_saglik_bakani", "char_hazine_bakani"),
    "tr_vaka_637": ("char_saglik_bakani", "char_adalet_bakani"),
    "tr_vaka_639": ("char_ticaret_bakani", "char_tuketici_dernekleri_baskani"),

    # Domain 20 (671-700) Spor ve Zaferler
    "tr_vaka_677": ("char_adli_yargi_hakimi", "char_adalet_bakani"),
    "tr_vaka_678": ("char_diplomat", "char_cumhurbaskani"),
    "tr_vaka_679": ("char_adli_yargi_hakimi", "char_adalet_bakani"),
    "tr_vaka_680": ("char_icisleri_bakani", "char_tuketici_dernekleri_baskani"),
    "tr_vaka_693": ("char_adli_yargi_hakimi", "char_icisleri_bakani"),
    "tr_vaka_695": ("char_diplomat", "char_cumhurbaskani"),
    "tr_vaka_700": ("char_esnaf_odasi_baskani", "char_cumhurbaskani"),

    # Domain 21 (701-730) Kültür ve Sanat
    "tr_vaka_706": ("char_diplomat", "char_sehir_plancisi"),
    "tr_vaka_707": ("char_diplomat", "char_sehir_plancisi"),
    "tr_vaka_708": ("char_diplomat", "char_sehir_plancisi"),
    "tr_vaka_713": ("char_cumhurbaskani", "char_diplomat"),
    "tr_vaka_714": ("char_cumhurbaskani", "char_diplomat"),
    "tr_vaka_715": ("char_cumhurbaskani", "char_diplomat"),
    "tr_vaka_720": ("char_adalet_bakani", "char_tuketici_dernekleri_baskani"),
    "tr_vaka_727": ("char_esnaf_odasi_baskani", "char_cumhurbaskani"),
    "tr_vaka_730": ("char_cevre_sehircilik_bakani", "char_sehir_plancisi"),

    # Domain 25 (821-850) Çalışma Hayatı
    "tr_vaka_839": ("char_ticaret_bakani", "char_esnaf_odasi_baskani"),

    # Domain 30 (971-1000) Türkiye Yüzyılı
    "tr_vaka_972": ("char_cumhurbaskani", "char_genelkurmay_baskani"),
    "tr_vaka_973": ("char_cumhurbaskani", "char_savunma_bakani"),
    "tr_vaka_977": ("char_anayasa_mahkemesi_baskani", "char_adalet_bakani"),
    "tr_vaka_978": ("char_adalet_bakani", "char_adli_yargi_hakimi"),
    "tr_vaka_981": ("char_cumhurbaskani", "char_genelkurmay_baskani"),
    "tr_vaka_982": ("char_cumhurbaskani", "char_genelkurmay_baskani"),
    "tr_vaka_983": ("char_sanayi_bakani", "char_cumhurbaskani"),
    "tr_vaka_984": ("char_savunma_sanayii_baskani", "char_savunma_bakani"),
    "tr_vaka_985": ("char_cevre_sehircilik_bakani", "char_sanayi_bakani"),
    "tr_vaka_986": ("char_cevre_sehircilik_bakani", "char_sanayi_bakani"),
    "tr_vaka_987": ("char_cevre_sehircilik_bakani", "char_sanayi_bakani"),
    "tr_vaka_989": ("char_sanayi_bakani", "char_cumhurbaskani"),
    "tr_vaka_990": ("char_sanayi_bakani", "char_cumhurbaskani"),
    "tr_vaka_991": ("char_sanayi_bakani", "char_cumhurbaskani"),
    "tr_vaka_992": ("char_savunma_sanayii_baskani", "char_savunma_bakani"),
    "tr_vaka_993": ("char_savunma_sanayii_baskani", "char_savunma_bakani"),
    "tr_vaka_996": ("char_diplomat", "char_sehir_plancisi"),
    "tr_vaka_997": ("char_diplomat", "char_cumhurbaskani"),
    "tr_vaka_998": ("char_diplomat", "char_cumhurbaskani"),
}

# Apply overrides
for ev in events:
    ev_id = ev['id']
    if ev_id in SPECIFIC_OVERRIDES:
        c1, c2 = SPECIFIC_OVERRIDES[ev_id]
        ev['characters'] = [
            {"id": c1, "name": CANONICAL_NAMES[c1]},
            {"id": c2, "name": CANONICAL_NAMES[c2]}
        ]
    else:
        # Standardize character names
        for ch in ev['characters']:
            cid = ch['id']
            # If DGM era (events < tr_vaka_170), keep DGM Başsavcısı for adli_yargi if already set
            if cid == "char_adli_yargi_hakimi":
                ev_num = int(re.sub(r'\D', '', ev_id))
                if ev_num <= 170:
                    ch['name'] = "DGM Başsavcısı"
                else:
                    ch['name'] = "Cumhuriyet Başsavcısı"
            elif cid in CANONICAL_NAMES:
                ch['name'] = CANONICAL_NAMES[cid]

# Count characters and build events list
char_counts = {cid: [] for cid in CANONICAL_NAMES}
for ev in events:
    for ch in ev['characters']:
        cid = ch['id']
        char_counts[cid].append(ev['id'])

print("Updated character counts:")
for cid, ev_list in sorted(char_counts.items(), key=lambda x: len(x[1]), reverse=True):
    print(f"  {cid} ({CANONICAL_NAMES[cid]}): {len(ev_list)} events")

total_char_refs = sum(len(v) for v in char_counts.values())
print(f"\nTotal character references across 1000 events: {total_char_refs} (Expected: 2000)")
