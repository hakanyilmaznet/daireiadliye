# -*- coding: utf-8 -*-
"""
Apply Character Updates to:
1. characters_modern.json
2. event_deck_modern.json
3. event_deck_modern.js

Ensures 100% synchronization and valid schema across all files.
"""

import json
import os
import re

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODERN_JSON_PATH = os.path.join(BASE_DIR, 'event_deck_modern.json')
MODERN_JS_PATH = os.path.join(BASE_DIR, 'event_deck_modern.js')
CHARS_MODERN_PATH = os.path.join(BASE_DIR, 'characters_modern.json')

# 1. Canonical Modern Character Titles
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

# 2. Targeted Event Overrides for Authentic Representation
EVENT_OVERRIDES = {
    # Göç ve Sınır Güvenliği -> char_goc_idaresi_baskani
    "tr_vaka_173": ("char_ticaret_bakani", "char_goc_idaresi_baskani"),
    "tr_vaka_286": ("char_adli_yargi_hakimi", "char_goc_idaresi_baskani"),
    "tr_vaka_290": ("char_icisleri_bakani", "char_goc_idaresi_baskani"),
    "tr_vaka_350": ("char_diplomat", "char_goc_idaresi_baskani"),
    "tr_vaka_353": ("char_diplomat", "char_goc_idaresi_baskani"),
    "tr_vaka_354": ("char_savunma_bakani", "char_goc_idaresi_baskani"),
    "tr_vaka_355": ("char_savunma_bakani", "char_goc_idaresi_baskani"),
    "tr_vaka_356": ("char_savunma_bakani", "char_goc_idaresi_baskani"),
    "tr_vaka_370": ("char_diplomat", "char_goc_idaresi_baskani"),
    "tr_vaka_554": ("char_icisleri_bakani", "char_goc_idaresi_baskani"),
    "tr_vaka_752": ("char_ticaret_bakani", "char_goc_idaresi_baskani"),
    "tr_vaka_814": ("char_sehir_plancisi", "char_goc_idaresi_baskani"),
    "tr_vaka_815": ("char_icisleri_bakani", "char_goc_idaresi_baskani"),
    "tr_vaka_946": ("char_icisleri_bakani", "char_goc_idaresi_baskani"),
    "tr_vaka_954": ("char_icisleri_bakani", "char_goc_idaresi_baskani"),
    "tr_vaka_955": ("char_icisleri_bakani", "char_goc_idaresi_baskani"),
    "tr_vaka_956": ("char_icisleri_bakani", "char_goc_idaresi_baskani"),
    "tr_vaka_957": ("char_icisleri_bakani", "char_goc_idaresi_baskani"),
    "tr_vaka_958": ("char_savunma_bakani", "char_goc_idaresi_baskani"),
    "tr_vaka_959": ("char_icisleri_bakani", "char_goc_idaresi_baskani"),
    "tr_vaka_960": ("char_icisleri_bakani", "char_goc_idaresi_baskani"),
    "tr_vaka_968": ("char_ticaret_bakani", "char_goc_idaresi_baskani"),
    "tr_vaka_969": ("char_icisleri_bakani", "char_goc_idaresi_baskani"),

    # TÜSİAD, Özel Sektör, Sermaye Piyasaları ve Özelleştirme -> char_tusiad_baskani
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

    # Anayasa Mahkemesi ve Yüksek Yargı -> char_anayasa_mahkemesi_baskani
    "tr_vaka_123": ("char_anayasa_mahkemesi_baskani", "char_tbmm_baskani"),
    "tr_vaka_204": ("char_anayasa_mahkemesi_baskani", "char_milletvekili"),
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

    # Meclis ve Milletvekilleri -> char_milletvekili & char_tbmm_baskani
    "tr_vaka_107": ("char_basbakan", "char_milletvekili"),
    "tr_vaka_108": ("char_tbmm_baskani", "char_milletvekili"),
    "tr_vaka_112": ("char_adalet_bakani", "char_tbmm_baskani"),
    "tr_vaka_113": ("char_adalet_bakani", "char_tbmm_baskani"),
    "tr_vaka_117": ("char_tbmm_baskani", "char_milletvekili"),
    "tr_vaka_118": ("char_basbakan", "char_milletvekili"),
    "tr_vaka_119": ("char_tbmm_baskani", "char_milletvekili"),
    "tr_vaka_122": ("char_adalet_bakani", "char_tbmm_baskani"),
    "tr_vaka_124": ("char_adalet_bakani", "char_tbmm_baskani"),
    "tr_vaka_177": ("char_milletvekili", "char_basbakan"),
    "tr_vaka_178": ("char_tbmm_baskani", "char_basbakan"),
    "tr_vaka_192": ("char_tbmm_baskani", "char_milletvekili"),
    "tr_vaka_197": ("char_tbmm_baskani", "char_milletvekili"),
    "tr_vaka_201": ("char_tbmm_baskani", "char_milletvekili"),
    "tr_vaka_315": ("char_tbmm_baskani", "char_milletvekili"),
    "tr_vaka_321": ("char_cumhurbaskani", "char_milletvekili"),
    "tr_vaka_328": ("char_tbmm_baskani", "char_milletvekili"),
    "tr_vaka_330": ("char_cumhurbaskani", "char_milletvekili"),
    "tr_vaka_332": ("char_tbmm_baskani", "char_milletvekili"),
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
    "tr_vaka_974": ("char_cumhurbaskani", "char_milletvekili"),
    "tr_vaka_976": ("char_tbmm_baskani", "char_milletvekili"),
    "tr_vaka_979": ("char_tbmm_baskani", "char_milletvekili"),
    "tr_vaka_1000": ("char_cumhurbaskani", "char_milletvekili"),

    # Sağlık, Hastaneler ve Pandemi -> char_saglik_bakani
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

    # Savunma Sanayii -> char_savunma_sanayii_baskani
    "tr_vaka_477": ("char_savunma_sanayii_baskani", "char_savunma_bakani"),
    "tr_vaka_984": ("char_savunma_sanayii_baskani", "char_savunma_bakani"),
    "tr_vaka_992": ("char_savunma_sanayii_baskani", "char_savunma_bakani"),
    "tr_vaka_993": ("char_savunma_sanayii_baskani", "char_savunma_bakani"),

    # Güvenlik, Askeriye ve Diplomasi
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

    # Yargı, Hukuk ve Soruşturmalar
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
    "tr_vaka_164": ("char_adalet_bakani", "char_basbakan"),
    "tr_vaka_167": ("char_adalet_bakani", "char_basbakan"),
    "tr_vaka_168": ("char_adalet_bakani", "char_adli_yargi_hakimi"),
    "tr_vaka_169": ("char_adalet_bakani", "char_adli_yargi_hakimi"),
    "tr_vaka_170": ("char_adalet_bakani", "char_adli_yargi_hakimi"),
    "tr_vaka_171": ("char_cumhurbaskani", "char_basbakan"),
    "tr_vaka_172": ("char_icisleri_bakani", "char_basbakan"),
    "tr_vaka_175": ("char_hazine_bakani", "char_esnaf_odasi_baskani"),
    "tr_vaka_181": ("char_hazine_bakani", "char_merkez_bankasi_baskani"),
    "tr_vaka_183": ("char_cumhurbaskani", "char_adalet_bakani"),
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
    "tr_vaka_678": ("char_diplomat", "char_cumhurbaskani"),
    "tr_vaka_679": ("char_adli_yargi_hakimi", "char_adalet_bakani"),
    "tr_vaka_693": ("char_adli_yargi_hakimi", "char_icisleri_bakani"),
    "tr_vaka_695": ("char_diplomat", "char_cumhurbaskani"),
    "tr_vaka_858": ("char_adalet_bakani", "char_adli_yargi_hakimi"),
    "tr_vaka_859": ("char_adalet_bakani", "char_adli_yargi_hakimi"),
    "tr_vaka_864": ("char_sanayi_bakani", "char_adalet_bakani"),
    "tr_vaka_868": ("char_adalet_bakani", "char_icisleri_bakani"),
    "tr_vaka_869": ("char_adalet_bakani", "char_icisleri_bakani"),
    "tr_vaka_874": ("char_sanayi_bakani", "char_adalet_bakani"),
    "tr_vaka_978": ("char_adalet_bakani", "char_adli_yargi_hakimi"),

    # Çevre, Şehircilik ve Mimarlık
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

    # Ticaret, Tüketici ve Esnaf
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

    # Teknoloji, Sanayi ve Bilim
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

# 3. Process Events
with open(MODERN_JSON_PATH, 'r', encoding='utf-8') as f:
    raw_content = f.read().strip()

clean_json = re.sub(r'^(const|var|let)\s+EVENT_DECK_MODERN\s*=\s*', '', raw_content)
clean_json = re.sub(r';\s*$', '', clean_json)
events = json.loads(clean_json)

for ev in events:
    ev_id = ev['id']
    if ev_id in EVENT_OVERRIDES:
        c1, c2 = EVENT_OVERRIDES[ev_id]
        ev['characters'] = [
            {"id": c1, "name": CANONICAL_NAMES[c1]},
            {"id": c2, "name": CANONICAL_NAMES[c2]}
        ]
    else:
        # Standardize character names across existing assignments
        for ch in ev['characters']:
            cid = ch['id']
            if cid == "char_adli_yargi_hakimi":
                ev_num = int(re.sub(r'\D', '', ev_id))
                if ev_num <= 170:
                    ch['name'] = "DGM Başsavcısı"
                else:
                    ch['name'] = "Cumhuriyet Başsavcısı"
            elif cid in CANONICAL_NAMES:
                ch['name'] = CANONICAL_NAMES[cid]

# 4. Compute index for characters_modern.json
char_events_map = {cid: [] for cid in CANONICAL_NAMES}
for ev in events:
    for ch in ev['characters']:
        cid = ch['id']
        if cid in char_events_map:
            char_events_map[cid].append(ev['id'])
        else:
            print(f"UYARI: Tanımlanmamış karakter ID: {cid}")

# Maintain the original order of characters in characters_modern.json
with open(CHARS_MODERN_PATH, 'r', encoding='utf-8') as f:
    orig_chars = json.load(f)

updated_chars = []
for oc in orig_chars:
    cid = oc['id']
    ev_list = char_events_map.get(cid, [])
    updated_chars.append({
        "id": cid,
        "name": CANONICAL_NAMES.get(cid, oc['name']),
        "image": f"assets/characters/{cid}.png",
        "eventCount": len(ev_list),
        "events": ev_list
    })

# Verify any new characters not in original
orig_ids = {oc['id'] for oc in orig_chars}
for cid in CANONICAL_NAMES:
    if cid not in orig_ids:
        ev_list = char_events_map.get(cid, [])
        updated_chars.append({
            "id": cid,
            "name": CANONICAL_NAMES[cid],
            "image": f"assets/characters/{cid}.png",
            "eventCount": len(ev_list),
            "events": ev_list
        })

# 5. Write characters_modern.json
with open(CHARS_MODERN_PATH, 'w', encoding='utf-8') as f:
    json.dump(updated_chars, f, ensure_ascii=False, indent=2)
print(f"characters_modern.json başarıyla güncellendi ({len(updated_chars)} karakter).")

# 6. Write event_deck_modern.json and event_deck_modern.js
deck_code = "const EVENT_DECK_MODERN = " + json.dumps(events, ensure_ascii=False, indent=2) + ";\n"

with open(MODERN_JSON_PATH, 'w', encoding='utf-8') as f:
    f.write(deck_code)
print(f"event_deck_modern.json başarıyla güncellendi ({len(events)} olay).")

with open(MODERN_JS_PATH, 'w', encoding='utf-8') as f:
    f.write(deck_code)
print(f"event_deck_modern.js başarıyla güncellendi ({len(events)} olay).")

# 7. Print summary of character counts
print("\n--- GÜNCEL KARAKTER DAĞILIMI (1000 OLAY) ---")
for c in sorted(updated_chars, key=lambda x: x['eventCount'], reverse=True):
    print(f"  {c['name']:36s} [{c['id']}]: {c['eventCount']:3d} olay")
