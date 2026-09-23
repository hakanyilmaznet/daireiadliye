import re
from deck_utils import make_preview

def evaluate_option_effects(event, opt_idx, opt):
    """
    Evaluates contextual, balanced, and realistic stat effects for an option
    based on the event's context and the specific option's action prose.
    
    Stats:
      justice: Adalet / Hukuk devleti
      people: Halk / Toplumsal refah & huzur
      treasury: Hazine / Maliye & Bütçe
      military: Güvenlik / Ordu / Polis
      authority: Otorite / Devlet gücü & İstikrar
    """
    title = event.get('title', '').lower()
    desc = event.get('desc', '').lower()
    label = opt.get('label', '').lower()
    log = opt.get('log', '').lower()
    full_text = f"{title} {desc} {label} {log}"
    
    # -------------------------------------------------------------
    # 1. Identify Domain & Thematic Tags
    # -------------------------------------------------------------
    is_economic = any(w in full_text for w in [
        'enflasyon', 'faiz', 'döviz', 'kur ', 'imf', 'banka', 'bddk', 'spk', 'borsa', 'kredi', 
        'tahvil', 'mevduat', 'devalüasyon', 'merkez bankası', 'cari açık', 'rezerv', 'ihracat', 
        'ithalat', 'bütçe', 'özelleştirme', 'vergi', 'para politikası', 'kıdem tazminatı'
    ])
    is_security_terror = any(w in full_text for w in [
        'terör', 'pkk', 'fetö', 'deaş', 'dhkp', 'sınır ötesi', 'harekat', 'hendek', 'tsk', 'mehmetçik',
        'askeri', 'karakol', 'şehit', 'bomba', 'çatışma', 'savunma sanayii', 'iha', 'siha', 'roket',
        'kardak', 'fırat kalkanı', 'zeytin dalı', 'barış pınarı', 'pençe', 'darbe', 'muhtıra', 'komando'
    ])
    is_disaster = any(w in full_text for w in [
        'deprem', 'fay', 'afad', 'sel ', 'yangın', 'maden faciası', 'enkaz', 'afet', 'kızılay',
        'arama-kurtarma', 'heyelan', 'çığ ', 'pandemi', 'koronavirüs', 'karantina', 'aşı'
    ])
    is_corruption_crime = any(w in full_text for w in [
        'yolsuzluk', 'rüşvet', 'mafya', 'çete', 'kara para', 'vurgun', 'zimmet', 'hortumlama',
        'kaçakçılık', 'zehir tacir', 'sahte içki', 'suç örgütü', 'suikast', 'cinayet', 'susurluk',
        'metil alkol', 'paravan', 'ihaleye fesat'
    ])
    is_diplomacy = any(w in full_text for w in [
        'ab ', 'avrupa birliği', 'nato', 'diplomat', 'dışişleri', 'elçi', 'kıbrıs', 'yunanistan',
        'türk devletleri', 'uluslararası', 'müzakere', 'zirve', 'antlaşma', 'koridor', 'kalkınma yolu',
        'zengezur', 'fav limanı', 'vize muafiyeti', 'avrupa konseyi', 'aihm'
    ])
    is_social_civic = any(w in full_text for w in [
        'sendika', 'grev', 'işçi', 'asgari ücret', 'eğitim', 'öğretmen', 'üniversite',
        'öğrenci', 'sağlık', 'doktor', 'hastane', 'eczacı', 'esnaf', 'sanat', 'sinema', 'kültür',
        'kadın', 'baro', 'eylem', 'protesto', 'gezi parkı', 'altın palmiye', 'nobel', 'müze'
    ])

    # -------------------------------------------------------------
    # 2. Strategy Slot (0: Adli, 1: Sulh, 2: Mali, 3: Otorite, 4: Nizam)
    # -------------------------------------------------------------
    slot = opt_idx % 5
    eff = {'justice': 0, 'people': 0, 'treasury': 0, 'military': 0, 'authority': 0}

    # =============================================================
    # SLOT 0: HUKUK / ADALET / YARGI & MEŞRUİYET
    # =============================================================
    if slot == 0:
        eff['justice'] = 8
        eff['people'] = 5
        eff['authority'] = 2
        eff['treasury'] = -2
        eff['military'] = 0

        if is_corruption_crime:
            # Prosecuting corrupt networks / confiscating ill-gotten wealth
            eff['justice'] = 9
            eff['people'] = 7
            eff['treasury'] = 5   # Seizing black money, recovering stolen public treasury
            eff['authority'] = 3
        elif is_disaster:
            # Prosecuting rogue builders, corrupt zoning officials
            eff['justice'] = 9
            eff['people'] = 8
            eff['authority'] = 3
            eff['treasury'] = -2
        elif is_diplomacy:
            # International law, treaties, maritime rights
            eff['justice'] = 8
            eff['authority'] = 6
            eff['people'] = 5
            eff['treasury'] = 2
        elif is_security_terror:
            # Independent trials for captured terrorists/conspirators
            eff['justice'] = 8
            eff['military'] = 4
            eff['authority'] = 5
            eff['people'] = 4
            eff['treasury'] = -2
        elif is_economic:
            # Regulatory enforcement by BDDK, SPK, MASAK against manipulation
            eff['justice'] = 8
            eff['treasury'] = 4
            eff['people'] = 5
            eff['authority'] = 4
        else:
            eff['justice'] = 8
            eff['people'] = 6
            eff['authority'] = 2
            eff['treasury'] = -2

    # =============================================================
    # SLOT 1: SULH / MASLAHAT / İSTİŞARE & UZLAŞI
    # =============================================================
    elif slot == 1:
        # Core philosophy: Social harmony, de-escalation, dialog
        eff['people'] = 8
        eff['authority'] = 5
        eff['treasury'] = -2
        eff['justice'] = 2
        eff['military'] = 0

        # Does the choice involve an unprincipled backroom concession / coverup?
        if any(w in label for w in ['affet', 'örtbas', 'hasıraltı', 'taviz ver', 'yok say', 'göz yum']):
            eff['justice'] = -4
            eff['people'] = 5
            eff['authority'] = 4
            eff['treasury'] = 0
        elif is_social_civic or 'sendika' in full_text or 'grev' in full_text or 'esnaf' in full_text:
            # Resolving strike / social tension with agreement
            eff['people'] = 9
            eff['authority'] = 6
            eff['treasury'] = -4  # Wage hikes or social benefits package
            eff['justice'] = 3
        elif is_diplomacy:
            # Diplomatic dialogue / Turkish States / bilateral agreements
            eff['people'] = 6
            eff['authority'] = 7
            eff['treasury'] = 3   # Trade and investment opportunities
            eff['justice'] = 3
        elif is_economic:
            # Consultation with business leaders, unions, banks
            eff['people'] = 7
            eff['treasury'] = 4
            eff['authority'] = 6
            eff['justice'] = 2
        elif is_disaster:
            # Mobilizing civil society, voluntary aid, blood donations, NGOs
            eff['people'] = 9
            eff['authority'] = 5
            eff['treasury'] = 4   # Civil solidarity covers immediate relief expenses
            eff['military'] = 2

    # =============================================================
    # SLOT 2: MALİYE / HAZİNE / İKTİSADİ RASYONELLİK
    # =============================================================
    elif slot == 2:
        # Does this choice spend money (investment, relief, subsidies) OR generate/save money?
        spends_money = any(w in label for w in [
            'ödenek ayır', 'bütçe tahsis', 'finanse et', 'destek sağla', 'fon tahsis', 'kredi ver',
            'yatırım yap', 'tazminat öde', 'sübvanse', 'yardım paketi', 'inşa et', 'harca', 'fon kur',
            'finansman sağla', 'kaynak aktar'
        ])
        brings_large_revenue = any(w in label for w in [
            'gelir sağla', 'ihracat', 'transit gelir', 'milyar dolar', 'vergi kaçağını önle',
            'turizm geliri', 'kara paraya el koy', 'özelleştirme geliri', 'tasarruf'
        ])

        if brings_large_revenue:
            # Large positive revenue generation (e.g. Development Road, energy transit, cracking tax evasion)
            eff['treasury'] = 8
            eff['authority'] = 5
            eff['people'] = 4 if not any(w in label for w in ['ek vergi', 'harç artır']) else -4
            eff['justice'] = 3 if any(w in label for w in ['vergi kaçağı', 'kara para', 'usulsüz']) else 1
            eff['military'] = 0
        elif spends_money:
            # State expenditure for disaster reconstruction, social aid, infrastructure
            eff['treasury'] = -6
            eff['people'] = 8
            eff['authority'] = 4
            eff['justice'] = 2
            eff['military'] = 2 if is_security_terror or is_disaster else 0
        else:
            # Traditional fiscal austerity, strict monetary policy, reserve accumulation
            eff['treasury'] = 8
            eff['authority'] = 4
            eff['people'] = -5  # Tight budget belts squeeze households
            eff['justice'] = 0

    # =============================================================
    # SLOT 3: GÜVENLİK / ASAYİŞ / OPERASYONEL MÜDAHALE
    # =============================================================
    elif slot == 3:
        # Check target of enforcement: Is it criminals/terrorists OR civilians/protesters?
        is_protective_raid = any(w in label for w in [
            'terör', 'hücre', 'zehir tacir', 'sahte içki', 'kaçakçı', 'çete', 'mafya', 'rant odak',
            'istismar', 'çocuk emeği', 'kom', 'tem', 'baskın', 'mehmetçik', 'sat komando', 'sabotaj',
            'sit alanı', 'kaçak yapı', 'kaçak etil alkol', 'sınır ötesi'
        ])
        is_crackdown_on_civilians = any(w in label for w in [
            'eylem', 'protesto', 'yürüyüş', 'grev', 'sokak', 'gösteri', 'barikat', 'tazyikli su', 'yasakla'
        ])

        if is_protective_raid:
            # Operation against armed groups, cartels, illegal syndicates
            eff['military'] = 9
            eff['authority'] = 8
            eff['people'] = 5     # Public is grateful for security
            eff['justice'] = 5    # Criminals brought to justice
            eff['treasury'] = -5  # Operational fuel, ammo, overtime costs
        elif is_disaster:
            # Military and police deployed to disaster zone for search-rescue and anti-looting
            eff['military'] = 6
            eff['people'] = 8     # Troops digging survivors out of ruins!
            eff['authority'] = 6
            eff['treasury'] = -4
            eff['justice'] = 2
        elif is_crackdown_on_civilians:
            # Heavy-handed police intervention in civic protests
            eff['authority'] = 8
            eff['military'] = 5
            eff['people'] = -7    # Public outrage
            eff['justice'] = -4   # Repression of constitutional right
            eff['treasury'] = -2
        else:
            # Routine administrative enforcement / inspections with police
            eff['authority'] = 7
            eff['military'] = 4
            eff['people'] = -2
            eff['justice'] = 3
            eff['treasury'] = -3

    # =============================================================
    # SLOT 4: YAPISAL REFORM / YASAMA & KURUMSAL DÖNÜŞÜM
    # =============================================================
    elif slot == 4:
        # Legislation, constitutional amendments, institutional modernization
        eff['authority'] = 6
        eff['justice'] = 7
        eff['treasury'] = -4  # Institutional restructuring and setup costs
        eff['people'] = 5

        if is_economic:
            # Economic / banking reform (BDDK, Central Bank, SPK legislation)
            eff['justice'] = 6
            eff['treasury'] = 5   # Long-term investment confidence & capital inflow
            eff['people'] = 4
            eff['authority'] = 6
            eff['military'] = 0
        elif is_security_terror:
            # Defense industry law, cyber security law, anti-terror legislation
            eff['military'] = 7
            eff['authority'] = 7
            eff['justice'] = 5
            eff['treasury'] = -4
            eff['people'] = 3
        elif is_disaster:
            # DASK, earthquake building codes, civil protection reform
            eff['justice'] = 8
            eff['people'] = 8
            eff['authority'] = 6
            eff['treasury'] = -4
            eff['military'] = 1
        elif is_social_civic:
            # Labor law, education reform, healthcare system, cultural protection
            eff['people'] = 8
            eff['justice'] = 7
            eff['authority'] = 5
            eff['treasury'] = -4
            eff['military'] = 0

    # -------------------------------------------------------------
    # 3. Micro-tuning based on explicit text triggers
    # -------------------------------------------------------------
    if 'uluslararası deniz hukuku' in label or 'anayasa mahkemesi' in label or 'aihm' in label:
        eff['justice'] = max(eff['justice'], 7)
    if 'milyar dolar' in label or 'ihracat rekoru' in label or 'transit gelir' in label:
        eff['treasury'] = max(eff['treasury'], 7)
    if 'mehmetçik' in label or 'sat komandoları' in label or 'hava harekatı' in label:
        eff['military'] = max(eff['military'], 7)
        eff['treasury'] = min(eff['treasury'], -3) # Real operations always cost money

    # -------------------------------------------------------------
    # 4. Bounds Clamping & Sanity Check [-12, +12]
    # -------------------------------------------------------------
    for k in eff:
        eff[k] = max(-12, min(12, eff[k]))

    return eff
