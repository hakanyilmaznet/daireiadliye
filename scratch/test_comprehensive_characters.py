# -*- coding: utf-8 -*-
"""
Comprehensive Character Mapping Refinement for Modern Turkey Event Deck (1000 Events).
Ensures all 24 characters are meaningfully, authentically, and accurately represented.
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

SPECIFIC_OVERRIDES = {
    # -------------------------------------------------------------
    # GÖÇ VE SINIR YÖNETİMİ -> char_goc_idaresi_baskani
    # -------------------------------------------------------------
    "tr_vaka_173": ("char_ticaret_bakani", "char_goc_idaresi_baskani"),
    "tr_vaka_286": ("char_adli_yargi_hakimi", "char_goc_idaresi_baskani"),
    "tr_vaka_353": ("char_diplomat", "char_goc_idaresi_baskani"),
    "tr_vaka_554": ("char_icisleri_bakani", "char_goc_idaresi_baskani"),
    "tr_vaka_814": ("char_sehir_plancisi", "char_goc_idaresi_baskani"),
    "tr_vaka_815": ("char_icisleri_bakani", "char_goc_idaresi_baskani"),
    "tr_vaka_954": ("char_icisleri_bakani", "char_goc_idaresi_baskani"),
    "tr_vaka_955": ("char_icisleri_bakani", "char_goc_idaresi_baskani"),
    "tr_vaka_956": ("char_icisleri_bakani", "char_goc_idaresi_baskani"),
    "tr_vaka_957": ("char_icisleri_bakani", "char_goc_idaresi_baskani"),
    "tr_vaka_958": ("char_savunma_bakani", "char_goc_idaresi_baskani"),
    "tr_vaka_969": ("char_icisleri_bakani", "char_goc_idaresi_baskani"),

    # -------------------------------------------------------------
    # İŞ DÜNYASI, HOLDİNGLER, ÖZELLEŞTİRME -> char_tusiad_baskani
    # -------------------------------------------------------------
    "tr_vaka_026": ("char_hazine_bakani", "char_tusiad_baskani"),
    "tr_vaka_052": ("char_hazine_bakani", "char_tusiad_baskani"),
    "tr_vaka_078": ("char_hazine_bakani", "char_tusiad_baskani"),
    "tr_vaka_130": ("char_hazine_bakani", "char_tusiad_baskani"),
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
    "tr_vaka_662": ("char_hazine_bakani", "char_tusiad_baskani"),
    "tr_vaka_667": ("char_saglik_bakani", "char_tusiad_baskani"),
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
    "tr_vaka_861": ("char_adalet_bakani", "char_tusiad_baskani"),
    "tr_vaka_988": ("char_ticaret_bakani", "char_tusiad_baskani"),
    "tr_vaka_994": ("char_sanayi_bakani", "char_tusiad_baskani"),
    "tr_vaka_995": ("char_hazine_bakani", "char_tusiad_baskani"),

    # -------------------------------------------------------------
    # ANAYASA MAHKEMESİ VE TEMEL HAKLAR -> char_anayasa_mahkemesi_baskani
    # -------------------------------------------------------------
    "tr_vaka_123": ("char_anayasa_mahkemesi_baskani", "char_tbmm_baskani"),
    "tr_vaka_251": ("char_anayasa_mahkemesi_baskani", "char_adalet_bakani"),
    "tr_vaka_252": ("char_anayasa_mahkemesi_baskani", "char_adalet_bakani"),
    "tr_vaka_253": ("char_anayasa_mahkemesi_baskani", "char_adalet_bakani"),
    "tr_vaka_254": ("char_anayasa_mahkemesi_baskani", "char_adalet_bakani"),
    "tr_vaka_270": ("char_anayasa_mahkemesi_baskani", "char_adalet_bakani"),
    "tr_vaka_271": ("char_anayasa_mahkemesi_baskani", "char_adalet_bakani"),
    "tr_vaka_327": ("char_adalet_bakani", "char_anayasa_mahkemesi_baskani"),
    "tr_vaka_329": ("char_anayasa_mahkemesi_baskani", "char_adli_yargi_hakimi"),
    "tr_vaka_610": ("char_anayasa_mahkemesi_baskani", "char_adli_yargi_hakimi"),
    "tr_vaka_612": ("char_anayasa_mahkemesi_baskani", "char_milletvekili"),
    "tr_vaka_614": ("char_anayasa_mahkemesi_baskani", "char_milletvekili"),
    "tr_vaka_857": ("char_anayasa_mahkemesi_baskani", "char_tbmm_baskani"),
    "tr_vaka_977": ("char_anayasa_mahkemesi_baskani", "char_adalet_bakani"),

    # -------------------------------------------------------------
    # YASAMA VE PARLAMENTO -> char_milletvekili & char_tbmm_baskani
    # -------------------------------------------------------------
    "tr_vaka_112": ("char_adalet_bakani", "char_tbmm_baskani"),
    "tr_vaka_113": ("char_adalet_bakani", "char_tbmm_baskani"),
    "tr_vaka_119": ("char_tbmm_baskani", "char_milletvekili"),
    "tr_vaka_122": ("char_adalet_bakani", "char_tbmm_baskani"),
    "tr_vaka_124": ("char_adalet_bakani", "char_tbmm_baskani"),
    "tr_vaka_177": ("char_milletvekili", "char_basbakan"),
    "tr_vaka_178": ("char_tbmm_baskani", "char_basbakan"),
    "tr_vaka_315": ("char_tbmm_baskani", "char_milletvekili"),
    "tr_vaka_328": ("char_tbmm_baskani", "char_milletvekili"),
    "tr_vaka_338": ("char_tbmm_baskani", "char_milletvekili"),
    "tr_vaka_339": ("char_cumhurbaskani", "char_milletvekili"),
    "tr_vaka_340": ("char_cumhurbaskani", "char_milletvekili"),
    "tr_vaka_595": ("char_tbmm_baskani", "char_adli_yargi_hakimi"),
    "tr_vaka_618": ("char_tbmm_baskani", "char_milletvekili"),
    "tr_vaka_619": ("char_basbakan", "char_milletvekili"),
    "tr_vaka_851": ("char_tbmm_baskani", "char_adalet_bakani"),
    "tr_vaka_852": ("char_tbmm_baskani", "char_hazine_bakani"),
    "tr_vaka_853": ("char_tbmm_baskani", "char_adalet_bakani"),
    "tr_vaka_854": ("char_hazine_bakani", "char_tbmm_baskani"),
    "tr_vaka_855": ("char_hazine_bakani", "char_tbmm_baskani"),
    "tr_vaka_866": ("char_adalet_bakani", "char_tbmm_baskani"),
    "tr_vaka_867": ("char_adalet_bakani", "char_tbmm_baskani"),
    "tr_vaka_880": ("char_tbmm_baskani", "char_milletvekili"),

    # -------------------------------------------------------------
    # SAĞLIK VE TIP REFORMLARI -> char_saglik_bakani
    # -------------------------------------------------------------
    "tr_vaka_176": ("char_saglik_bakani", "char_hazine_bakani"),
    "tr_vaka_325": ("char_saglik_bakani", "char_savunma_bakani"),
    "tr_vaka_583": ("char_adli_yargi_hakimi", "char_saglik_bakani"),
    "tr_vaka_584": ("char_adli_yargi_hakimi", "char_saglik_bakani"),
    "tr_vaka_585": ("char_adli_yargi_hakimi", "char_saglik_bakani"),
    "tr_vaka_630": ("char_sanayi_bakani", "char_saglik_bakani"),
    "tr_vaka_636": ("char_saglik_bakani", "char_hazine_bakani"),
    "tr_vaka_637": ("char_saglik_bakani", "char_adalet_bakani"),
    "tr_vaka_641": ("char_saglik_bakani", "char_hazine_bakani"),
    "tr_vaka_642": ("char_saglik_bakani", "char_hazine_bakani"),
    "tr_vaka_643": ("char_saglik_bakani", "char_hazine_bakani"),
    "tr_vaka_644": ("char_saglik_bakani", "char_hazine_bakani"),
    "tr_vaka_646": ("char_saglik_bakani", "char_sanayi_bakani"),
    "tr_vaka_647": ("char_saglik_bakani", "char_sanayi_bakani"),
    "tr_vaka_648": ("char_saglik_bakani", "char_sehir_plancisi"),
    "tr_vaka_649": ("char_saglik_bakani", "char_sehir_plancisi"),
    "tr_vaka_650": ("char_saglik_bakani", "char_sehir_plancisi"),
    "tr_vaka_651": ("char_saglik_bakani", "char_afad_baskani"),
    "tr_vaka_652": ("char_saglik_bakani", "char_ticaret_bakani"),
    "tr_vaka_653": ("char_saglik_bakani", "char_ticaret_bakani"),
    "tr_vaka_654": ("char_saglik_bakani", "char_cumhurbaskani"),
    "tr_vaka_655": ("char_saglik_bakani", "char_cumhurbaskani"),
    "tr_vaka_659": ("char_saglik_bakani", "char_esnaf_odasi_baskani"),
    "tr_vaka_660": ("char_saglik_bakani", "char_sanayi_bakani"),
    "tr_vaka_661": ("char_saglik_bakani", "char_sanayi_bakani"),
    "tr_vaka_663": ("char_saglik_bakani", "char_adalet_bakani"),
    "tr_vaka_664": ("char_saglik_bakani", "char_adalet_bakani"),
    "tr_vaka_665": ("char_saglik_bakani", "char_hazine_bakani"),
    "tr_vaka_666": ("char_saglik_bakani", "char_hazine_bakani"),
    "tr_vaka_668": ("char_saglik_bakani", "char_tuketici_dernekleri_baskani"),
    "tr_vaka_670": ("char_saglik_bakani", "char_adli_yargi_hakimi"),
    "tr_vaka_877": ("char_saglik_bakani", "char_adalet_bakani"),
    "tr_vaka_878": ("char_saglik_bakani", "char_adli_yargi_hakimi"),

    # -------------------------------------------------------------
    # SAVUNMA SANAYİİ VE MİLLİ TEKNOLOJİ -> char_savunma_sanayii_baskani
    # -------------------------------------------------------------
    "tr_vaka_477": ("char_savunma_sanayii_baskani", "char_savunma_bakani"),
    "tr_vaka_984": ("char_savunma_sanayii_baskani", "char_savunma_bakani"),
    "tr_vaka_992": ("char_savunma_sanayii_baskani", "char_savunma_bakani"),
    "tr_vaka_993": ("char_savunma_sanayii_baskani", "char_savunma_bakani"),

    # -------------------------------------------------------------
    # ASKERİ, MİLLİ GÜVENLİK VE DIŞ POLİTİKA
    # -------------------------------------------------------------
    "tr_vaka_120": ("char_genelkurmay_baskani", "char_diplomat"),
    "tr_vaka_121": ("char_diplomat", "char_cumhurbaskani"),
    "tr_vaka_125": ("char_adalet_bakani", "char_diplomat"),
    "tr_vaka_185": ("char_genelkurmay_baskani", "char_savunma_bakani"),
    "tr_vaka_186": ("char_adalet_bakani", "char_genelkurmay_baskani"),
    "tr_vaka_194": ("char_genelkurmay_baskani", "char_basbakan"),
    "tr_vaka_195": ("char_basbakan", "char_genelkurmay_baskani"),
    "tr_vaka_311": ("char_icisleri_bakani", "char_genelkurmay_baskani"),
    "tr_vaka_312": ("char_icisleri_bakani", "char_cumhurbaskani"),
    "tr_vaka_314": ("char_icisleri_bakani", "char_cumhurbaskani"),
    "tr_vaka_316": ("char_genelkurmay_baskani", "char_savunma_bakani"),
    "tr_vaka_317": ("char_genelkurmay_baskani", "char_icisleri_bakani"),
    "tr_vaka_323": ("char_savunma_bakani", "char_genelkurmay_baskani"),
    "tr_vaka_324": ("char_savunma_bakani", "char_genelkurmay_baskani"),
    "tr_vaka_972": ("char_cumhurbaskani", "char_genelkurmay_baskani"),
    "tr_vaka_973": ("char_cumhurbaskani", "char_savunma_bakani"),
    "tr_vaka_981": ("char_cumhurbaskani", "char_genelkurmay_baskani"),
    "tr_vaka_982": ("char_cumhurbaskani", "char_genelkurmay_baskani"),
    "tr_vaka_997": ("char_diplomat", "char_cumhurbaskani"),
    "tr_vaka_998": ("char_diplomat", "char_cumhurbaskani"),

    # -------------------------------------------------------------
    # HUKUK, YARGI VE SORUŞTURMALAR
    # -------------------------------------------------------------
    "tr_vaka_114": ("char_icisleri_bakani", "char_adalet_bakani"),
    "tr_vaka_115": ("char_adli_yargi_hakimi", "char_adalet_bakani"),
    "tr_vaka_116": ("char_adli_yargi_hakimi", "char_adalet_bakani"),
    "tr_vaka_126": ("char_adalet_bakani", "char_adli_yargi_hakimi"),
    "tr_vaka_127": ("char_adalet_bakani", "char_adli_yargi_hakimi"),
    "tr_vaka_128": ("char_icisleri_bakani", "char_adalet_bakani"),
    "tr_vaka_129": ("char_adalet_bakani", "char_basbakan"),
    "tr_vaka_132": ("char_hazine_bakani", "char_adli_yargi_hakimi"),
    "tr_vaka_133": ("char_basbakan", "char_adli_yargi_hakimi"),
    "tr_vaka_135": ("char_hazine_bakani", "char_adli_yargi_hakimi"),
    "tr_vaka_136": ("char_icisleri_bakani", "char_adli_yargi_hakimi"),
    "tr_vaka_146": ("char_icisleri_bakani", "char_adli_yargi_hakimi"),
    "tr_vaka_147": ("char_icisleri_bakani", "char_adli_yargi_hakimi"),
    "tr_vaka_150": ("char_hazine_bakani", "char_adli_yargi_hakimi"),
    "tr_vaka_151": ("char_cevre_sehircilik_bakani", "char_adli_yargi_hakimi"),
    "tr_vaka_152": ("char_hazine_bakani", "char_adli_yargi_hakimi"),
    "tr_vaka_168": ("char_adalet_bakani", "char_adli_yargi_hakimi"),
    "tr_vaka_169": ("char_adalet_bakani", "char_adli_yargi_hakimi"),
    "tr_vaka_170": ("char_adalet_bakani", "char_adli_yargi_hakimi"),
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
    "tr_vaka_255": ("char_basbakan", "char_adli_yargi_hakimi"),
    "tr_vaka_256": ("char_basbakan", "char_adli_yargi_hakimi"),
    "tr_vaka_257": ("char_tbmm_baskani", "char_basbakan"),
    "tr_vaka_260": ("char_icisleri_bakani", "char_adli_yargi_hakimi"),
    "tr_vaka_261": ("char_icisleri_bakani", "char_adli_yargi_hakimi"),
    "tr_vaka_262": ("char_basbakan", "char_cumhurbaskani"),
    "tr_vaka_264": ("char_icisleri_bakani", "char_basbakan"),
    "tr_vaka_265": ("char_icisleri_bakani", "char_genelkurmay_baskani"),
    "tr_vaka_267": ("char_sanayi_bakani", "char_adli_yargi_hakimi"),
    "tr_vaka_268": ("char_sanayi_bakani", "char_adli_yargi_hakimi"),
    "tr_vaka_269": ("char_sanayi_bakani", "char_icisleri_bakani"),
    "tr_vaka_273": ("char_hazine_bakani", "char_adli_yargi_hakimi"),
    "tr_vaka_280": ("char_icisleri_bakani", "char_adalet_bakani"),
    "tr_vaka_326": ("char_adalet_bakani", "char_cumhurbaskani"),
    "tr_vaka_334": ("char_adli_yargi_hakimi", "char_cumhurbaskani"),
    "tr_vaka_335": ("char_adli_yargi_hakimi", "char_cumhurbaskani"),
    "tr_vaka_336": ("char_adli_yargi_hakimi", "char_cumhurbaskani"),
    "tr_vaka_337": ("char_icisleri_bakani", "char_adli_yargi_hakimi"),
    "tr_vaka_581": ("char_adli_yargi_hakimi", "char_icisleri_bakani"),
    "tr_vaka_582": ("char_adli_yargi_hakimi", "char_icisleri_bakani"),
    "tr_vaka_586": ("char_adli_yargi_hakimi", "char_icisleri_bakani"),
    "tr_vaka_587": ("char_adli_yargi_hakimi", "char_icisleri_bakani"),
    "tr_vaka_588": ("char_adli_yargi_hakimi", "char_icisleri_bakani"),
    "tr_vaka_596": ("char_adli_yargi_hakimi", "char_adalet_bakani"),
    "tr_vaka_597": ("char_adli_yargi_hakimi", "char_adalet_bakani"),
    "tr_vaka_601": ("char_adli_yargi_hakimi", "char_sehir_plancisi"),
    "tr_vaka_602": ("char_adli_yargi_hakimi", "char_sanayi_bakani"),
    "tr_vaka_603": ("char_adli_yargi_hakimi", "char_sanayi_bakani"),
    "tr_vaka_604": ("char_adli_yargi_hakimi", "char_sanayi_bakani"),
    "tr_vaka_605": ("char_adli_yargi_hakimi", "char_sanayi_bakani"),
    "tr_vaka_606": ("char_adli_yargi_hakimi", "char_icisleri_bakani"),
    "tr_vaka_620": ("char_adli_yargi_hakimi", "char_icisleri_bakani"),
    "tr_vaka_621": ("char_adli_yargi_hakimi", "char_cumhurbaskani"),
    "tr_vaka_677": ("char_adli_yargi_hakimi", "char_adalet_bakani"),
    "tr_vaka_679": ("char_adli_yargi_hakimi", "char_adalet_bakani"),
    "tr_vaka_693": ("char_adli_yargi_hakimi", "char_icisleri_bakani"),
    "tr_vaka_858": ("char_adalet_bakani", "char_adli_yargi_hakimi"),
    "tr_vaka_859": ("char_adalet_bakani", "char_adli_yargi_hakimi"),
    "tr_vaka_864": ("char_sanayi_bakani", "char_adalet_bakani"),
    "tr_vaka_868": ("char_adalet_bakani", "char_icisleri_bakani"),
    "tr_vaka_869": ("char_adalet_bakani", "char_icisleri_bakani"),
    "tr_vaka_874": ("char_sanayi_bakani", "char_adalet_bakani"),
    "tr_vaka_978": ("char_adalet_bakani", "char_adli_yargi_hakimi"),

    # -------------------------------------------------------------
    # ÇEVRE, ŞEHİRCİLİK VE BELEDİYELER
    # -------------------------------------------------------------
    "tr_vaka_179": ("char_cevre_sehircilik_bakani", "char_sehir_plancisi"),
    "tr_vaka_188": ("char_cevre_sehircilik_bakani", "char_sehir_plancisi"),
    "tr_vaka_626": ("char_icisleri_bakani", "char_sehir_plancisi"),
    "tr_vaka_633": ("char_sehir_plancisi", "char_cevre_sehircilik_bakani"),
    "tr_vaka_706": ("char_diplomat", "char_sehir_plancisi"),
    "tr_vaka_707": ("char_diplomat", "char_sehir_plancisi"),
    "tr_vaka_708": ("char_diplomat", "char_sehir_plancisi"),
    "tr_vaka_730": ("char_cevre_sehircilik_bakani", "char_sehir_plancisi"),
    "tr_vaka_985": ("char_cevre_sehircilik_bakani", "char_sanayi_bakani"),
    "tr_vaka_986": ("char_cevre_sehircilik_bakani", "char_sanayi_bakani"),
    "tr_vaka_987": ("char_cevre_sehircilik_bakani", "char_sanayi_bakani"),

    # -------------------------------------------------------------
    # TİCARET, ESNAF VE TÜKETİCİ
    # -------------------------------------------------------------
    "tr_vaka_148": ("char_ticaret_bakani", "char_icisleri_bakani"),
    "tr_vaka_149": ("char_ticaret_bakani", "char_icisleri_bakani"),
    "tr_vaka_174": ("char_ticaret_bakani", "char_sanayi_bakani"),
    "tr_vaka_180": ("char_adalet_bakani", "char_tuketici_dernekleri_baskani"),
    "tr_vaka_635": ("char_esnaf_odasi_baskani", "char_sanayi_bakani"),
    "tr_vaka_639": ("char_ticaret_bakani", "char_tuketici_dernekleri_baskani"),
    "tr_vaka_680": ("char_icisleri_bakani", "char_tuketici_dernekleri_baskani"),
    "tr_vaka_700": ("char_esnaf_odasi_baskani", "char_cumhurbaskani"),
    "tr_vaka_720": ("char_adalet_bakani", "char_tuketici_dernekleri_baskani"),
    "tr_vaka_727": ("char_esnaf_odasi_baskani", "char_cumhurbaskani"),
    "tr_vaka_839": ("char_ticaret_bakani", "char_esnaf_odasi_baskani"),
    "tr_vaka_906": ("char_ticaret_bakani", "char_esnaf_odasi_baskani"),

    # -------------------------------------------------------------
    # BİLİM, SANAYİ VE DİJİTAL
    # -------------------------------------------------------------
    "tr_vaka_629": ("char_sanayi_bakani", "char_hazine_bakani"),
    "tr_vaka_713": ("char_cumhurbaskani", "char_diplomat"),
    "tr_vaka_714": ("char_cumhurbaskani", "char_diplomat"),
    "tr_vaka_715": ("char_cumhurbaskani", "char_diplomat"),
    "tr_vaka_983": ("char_sanayi_bakani", "char_cumhurbaskani"),
    "tr_vaka_989": ("char_sanayi_bakani", "char_cumhurbaskani"),
    "tr_vaka_990": ("char_sanayi_bakani", "char_cumhurbaskani"),
    "tr_vaka_991": ("char_sanayi_bakani", "char_cumhurbaskani"),
    "tr_vaka_996": ("char_diplomat", "char_sehir_plancisi"),
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
            # If DGM era (events <= tr_vaka_170), keep DGM Başsavcısı for adli_yargi if already set
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
    print(f"  {cid:32s} ({CANONICAL_NAMES[cid]}): {len(ev_list):3d} events")

total_char_refs = sum(len(v) for v in char_counts.values())
print(f"\nTotal character references across 1000 events: {total_char_refs} (Expected: 2000)")
