# -*- coding: utf-8 -*-
"""
Part 1 Events Generator (tr_vaka_101 to tr_vaka_400: 300 Events)
Domains 1 to 10:
1. 1990'lar Koalisyonlar ve Siyasi Krizler (1995-2002)
2. Bankacılık Krizleri, Hortumlama ve TMSF Operasyonları (1998-2006)
3. 2007-2012 Siyasi Gerilimler, Yargı ve Referandumlar
4. Kumpas Davaları, Yargı Çatışması ve 17-25 Aralık (2010-2015)
5. Terörle Mücadele, Barış Arayışları ve Hendek Olayları (2005-2017)
6. 15 Temmuz Darbe Girişimi, OHAL ve Yeni Hükümet Sistemi (2016-2023)
7. Dış Politika, Doğu Akdeniz, Mavi Vatan & Sınır Ötesi Harekâtlar
8. Savunma Sanayii, Havacılık ve Uzay Çağı Atılımları
9. Büyük Doğal Afetler, Kriz Masaları ve Çevre Krizleri
10. Mega Ulaşım, Altyapı ve Enerji Projeleri
"""

import json
import os

with open(os.path.join(os.path.dirname(__file__), '..', 'characters_modern.json'), 'r', encoding='utf-8') as f:
    chars = json.load(f)
char_map = {c['id']: c['name'] for c in chars}

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

def make_options(title, opt1_t, opt2_t, opt3_t, opt4_t, opt5_t,
                 opt1_log, opt2_log, opt3_log, opt4_log, opt5_log,
                 e1=(8, 7, -2, 0, -2), e2=(-7, 8, -2, 0, 7), e3=(-2, -7, 8, 0, 3), e4=(-3, -8, 0, 8, 7), e5=(8, 3, -7, 0, 7)):
    eff1 = {'justice': e1[0], 'people': e1[1], 'treasury': e1[2], 'military': e1[3], 'authority': e1[4]}
    eff2 = {'justice': e2[0], 'people': e2[1], 'treasury': e2[2], 'military': e2[3], 'authority': e2[4]}
    eff3 = {'justice': e3[0], 'people': e3[1], 'treasury': e3[2], 'military': e3[3], 'authority': e3[4]}
    eff4 = {'justice': e4[0], 'people': e4[1], 'treasury': e4[2], 'military': e4[3], 'authority': e4[4]}
    eff5 = {'justice': e5[0], 'people': e5[1], 'treasury': e5[2], 'military': e5[3], 'authority': e5[4]}

    return [
        {'label': opt1_t, 'preview': format_preview(eff1), 'effects': eff1, 'log': opt1_log},
        {'label': opt2_t, 'preview': format_preview(eff2), 'effects': eff2, 'log': opt2_log},
        {'label': opt3_t, 'preview': format_preview(eff3), 'effects': eff3, 'log': opt3_log},
        {'label': opt4_t, 'preview': format_preview(eff4), 'effects': eff4, 'log': opt4_log},
        {'label': opt5_t, 'preview': format_preview(eff5), 'effects': eff5, 'log': opt5_log}
    ]

# We will populate domains 1 to 10
domains_data = []

# DOMAIN 1: 1990'lar Koalisyonlar ve Siyasi Krizler (1995-2002)
d1_cases = [
    (
        "Refahyol Hükümeti Protokolü ve Güvenoyu Çalkantısı",
        "Başbakanlık & TBMM",
        "char_basbakan", "char_milletvekili",
        "54. Hükümetin kurulması sürecinde partiler arası protokol pazarlıkları ve güvenoyu oylaması meclis kulislerinde büyük gerilim yarattı.",
        "Koalisyon protokolünü şeffaflıkla kamuoyuna açıkla; milletvekili transferi iddialarına karşı Meclis Soruşturması aç.",
        "Liderler arası uzlaşıyı koru; kabine içi dengeleri gözeterek meclis aritmetiğini sakinleştir.",
        "Bütçe disiplininden taviz verme; koalisyon ortaklarının popülist harcama taleplerini Hazine adına frenle.",
        "Güvenlik bürokrasisinin hükümet programına yönelik itirazlarını kararlı bir devlet iradesiyle sınırla.",
        "'Siyasi Partiler ve Koalisyonlar Kanunu' çıkararak güvenoyu süreçlerini anayasal güvencelere bağla.",
        "Yargı ve denetim yolu işletildi; siyaset üzerindeki şaibeler dağıtıldı.",
        "Siyasi uzlaşı korundu; hükümet güvenoyu alarak göreve başladı.",
        "Hazine dengesi muhafaza edildi; koalisyon pazarlıklarının maliyeti önlendi.",
        "Sivil otorite pekiştirildi; bürokratik vesayet baskısı kırıldı.",
        "Yasal reform ile koalisyon protokolleri kurumsal güvenceye bağlandı."
    ),
    (
        "Aydınlık İçin Bir Dakika Karanlık Eylemleri ve Sivil Tepki",
        "İçişleri Bakanlığı",
        "char_icisleri_bakani", "char_adli_yargi_hakimi",
        "Susurluk skandalı sonrası her akşam saat 21.00'de evlerde ışıkların kapatılmasıyla başlayan eylem, milyonların katıldığı bir sivil itaatsizliğe dönüştü.",
        "Eylemcilerin 'temiz toplum' talebini esas al; devlet-çete irtibatı iddialarını derhal DGM Başsavcılığı'na taşı.",
        "Toplumsal tansiyonu düşür; sivil toplum kuruluşlarıyla diyalog kurarak meclis araştırması başlat.",
        "Karanlık eylemleri sırasında sokak güvenliğini sağlayan kolluk kuvvetlerine ek bütçe ve donanım aktar.",
        "Kamu düzenini bozduğu ve trafiği aksattığı gerekçesiyle izinsiz gösterilere kolluk marifetiyle müdahale et.",
        "'Sivil Toplum ve Gösteri Yürüyüşleri Reform Paketi' hazırlayarak barışçıl protesto hakkını yasal teminata al.",
        "Halkın adalet talebi karşılık buldu; yargı çetelerin üzerine kararlılıkla gitti.",
        "Diyalog yoluyla gerilim düşürüldü; sokaktaki öfke meclis zeminine taşındı.",
        "Güvenlik bütçesi takviye edildi; şehir asayişi korundu.",
        "Kamu nizamı tavizsiz sağlandı; devletin otoritesi hissettirildi.",
        "Yeni mevzuat ile toplantı ve gösteri hakkı demokratik güvenceye kavuşturuldu."
    ),
    (
        "28 Şubat 1997 MGK Bildirisi ve İrtica Raporu",
        "Milli Güvenlik Kurulu (MGK)",
        "char_genelkurmay_baskani", "char_basbakan",
        "9 saat süren tarihi MGK toplantısında askeri kanat, hükümete 18 maddelik tedbir paketini imzalama çağrısında bulundu.",
        "Anayasal hukuk devleti ilkelerine bağlı kal; bildirideki talepleri bağımsız yargı ve anayasa süzgecinden geçir.",
        "Siyasi krizi yumuşat; MGK tavsiye kararlarını hükümet içinde kademeli bir takvime bağlayarak imza krizini aş.",
        "Kararların kamu maliyesine ve vakıf gelirlerine etkisini araştır; bütçe gelirlerini koruyacak tedbirler al.",
        "Askeri kanadın brifinglerine ve talimatlarına karşı hükümetin yürütme gücünü ve devlet otoritesini net bir dille savun.",
        "'Milli Güvenlik Kurulu Teşkilat Kanunu'nda reform yaparak kurulun görevini salt sivil danışma organı olarak sınırla.",
        "Hukukun üstünlüğü gözetildi; anayasal sınırlara riayet sağlandı.",
        "Zamana yayılan uzlaşıyla hükümet krizi geçici olarak donduruldu.",
        "Mali tedbirlerle vakıf ve dernek hesapları denetime alındı.",
        "Sivil irade dik duruş sergiledi; askeri vesayete karşı devlet heybeti korundu.",
        "Kurumsal reform ile MGK'nın sivil niteliği yasal zemine oturtuldu."
    ),
    (
        "Batı Çalışma Grubu (BÇG) Fişleme Belgeleri Kriz",
        "Adalet Bakanlığı & DGM",
        "char_adalet_bakani", "char_adli_yargi_hakimi",
        "Deniz Kuvvetleri Komutanlığı bünyesinde kurulan BÇG'nin binlerce kamu görevlisini ve siyasetçiyi fişlediği belgelerin sızması ortalığı karıştırdı.",
        "Fişleme belgelerini askeri savcılıktan adli yargıya al; kişisel verileri ihlal eden sorumlular hakkında dava aç.",
        "Bürokrasideki gerilimi yatıştırmak için Meclis İnceleme Heyeti kur; askeriye ile sivil idareyi karşı karşıya getirme.",
        "Yasadışı fişleme faaliyetlerine harcanan gizli ödenek ve kamu kaynaklarını Sayıştay denetimine aç.",
        "Askeri istihbaratın iç güvenlik konusundaki hassasiyetini koru; gizli bilgi sızdıran köstebekleri derhal cezalandır.",
        "'Kamu Görevlilerinin Korunması ve Fişlemenin Yasaklanması Kanunu' çıkararak benzer yapıları müebbet hapse bağla.",
        "Kişisel hak ihlallerine yargı dur dedi; hukuk devletine güven pekişti.",
        "Siyasi dengeler korundu; ordu-hükümet çatışması engellendi.",
        "Gizli harcamalar denetlendi; kamu bütçesinin suistimali önlendi.",
        "Gizli bilgi sızdıran klikler dağıtıldı; askeri disiplin tesis edildi.",
        "Yeni kanun ile fişleme suçu ilk kez TCK'da en ağır yaptırımlara bağlandı."
    ),
    (
        "Sincan'da Kudüs Gecesi ve Tankların Yürütülmesi",
        "İçişleri Bakanlığı & Genelkurmay",
        "char_icisleri_bakani", "char_genelkurmay_baskani",
        "Sincan Belediyesi'nin düzenlediği gecedeki konuşmalar sonrası Etimesgut Zırhlı Birlikler Okulu'na ait tanklar Sincan caddelerinden geçti.",
        "Kudüs Gecesi'nde Anayasa'ya aykırı konuşma yapanlar ve tankları tatbikat bahanesiyle şehre sokanlar hakkında eşzamanlı adli soruşturma aç.",
        "Belediye başkanını görevden uzaklaştırarak gerilimi düşür; askeriye ile polemiğe girmeden krizi idari kararla çöz.",
        "Sincan'da yaşanan gerilimin piyasalara etkisini sınırlamak için Merkez Bankası likidite desteğini artır.",
        "Tankların sokaktan geçmesini 'demokrasiye balans ayarı' olarak niteleyen askeri yetkililere sert idari yaptırım uygula.",
        "'Askeri Birliklerin İntikali ve Meskun Mahal Güvenliği Kanunu' çıkararak her türlü askeri konvoyu sivil izne bağla.",
        "Çifte soruşturma ile hukukun tarafsızlığı sağlandı; her iki tarafa da hesap soruldu.",
        "İdari tasarrufla tansiyon düşürüldü; koalisyon ömrü uzatıldı.",
        "Piyasalara güven verildi; faiz dalgalanmasının önüne geçildi.",
        "Hükümetin sivil otoritesi tavizsiz gösterildi.",
        "Yasal düzenleme ile kışladan sivil izinsiz palet dahi çıkması kanunen yasaklandı."
    ),
    (
        "Fazilet Partisi'nin Kurulması ve Kapatılması Davası",
        "Anayasa Mahkemesi",
        "char_anayasa_mahkemesi_baskani", "char_tbmm_baskani",
        "Refah Partisi'nin kapatılmasının ardından kurulan Fazilet Partisi hakkında Yargıtay Cumhuriyet Başsavcılığı 'odak olma' gerekçesiyle kapatma davası açtı.",
        "AİHM içtihatları ve Venedik Komisyonu ilkeleri doğrultusunda karar ver; parti kapatma yerine odak olan kişilere ceza ver.",
        "Mecliste grubu bulunan partilerle uzlaş; Anayasa'nın 69. maddesini değiştirerek parti kapatmayı zorlaştıracak formül üret.",
        "Kapatılması talep edilen partinin Hazine yardımına bloke koy; kamu kaynağının amaç dışı kullanımını engelle.",
        "Cumhuriyetin temel niteliklerine aykırı odaklaşmaya karşı AYM'nin mutlak kapatma yetkisini tavizsiz kullan.",
        "'Siyasi Partiler Kanunu Reformu' yaparak parti kapatma kararlarını sadece şiddet ve terör odağı olma şartına bağla.",
        "Hukuki standartlar yükseltildi; evrensel hukuk normlarına bağlı kalındı.",
        "Mecliste uzlaşı arandı; anayasal kriz yumuşatıldı.",
        "Hazine kaynağı korundu; bütçeden gereksiz harcama kesildi.",
        "Anayasal düzen korundu; devletin kırmızı çizgileri hissettirildi.",
        "Yasal reform ile parti kapatma rejiminde köklü ve modern bir dönemeç açıldı."
    ),
    (
        "18 Nisan 1999 Erken Seçimleri ve 57. Hükümet Protokolü",
        "TBMM & Başbakanlık",
        "char_basbakan", "char_tbmm_baskani",
        "DSP, MHP ve ANAP'ın oluşturduğu 57. Hükümet kurulurken koalisyon ortakları arasında bakanlık paylaşımları ve Meclis Başkanlığı pazarlığı kızıştı.",
        "Bakanlıkların teşkilat yapılarını liyakat esasına göre düzenle; koalisyon kadrolaşmasına yargı ve Danıştay denetimi getir.",
        "Üç partili koalisyon liderleri zirvesi topla; bakanlıkları adilce dağıtıp istikrarlı bir hükümet protokolü imzala.",
        "Kamu bankaları ve KİT'lerin koalisyon partileri arasında 'arpalık' olarak paylaşılmasını kesinlikle yasakla.",
        "Koalisyon uyumsuzluğu çıkaran bakanları Başbakanlık yetkisini kullanarak derhal görevden al.",
        "'Koalisyon Hükümetleri Çalışma Usulü ve Kamu Yönetimi Reformu Kanunu' çıkararak bakanlık yetki çakışmalarını bitir.",
        "Liyakat sağlandı; kadrolaşma ve usulsüz atamaların önüne geçildi.",
        "Koalisyon uyumu sağlandı; Meclis tatile girmeden güvenoyu tamamlandı.",
        "Kamu bankaları tasalluttan kurtarıldı; Hazine açıkları sınırlandı.",
        "Başbakanlık otoritesi hissettirildi; hükümet disiplini korundu.",
        "Yasal mevzuat ile bakanlıkların görev sınırları kalıcı olarak netleştirildi."
    ),
    (
        "Merve Kavakçı'nın TBMM Yemin Töreni Gerilimi",
        "TBMM Genel Kurulu",
        "char_tbmm_baskani", "char_milletvekili",
        "21. Dönem ilk birleşiminde başörtüsüyle genel kurula gelen milletvekiline yönelik protestolar meclisi kilitledi; vatandaşlık tartışmaları patlak verdi.",
        "Milletin iradesine saygı duy; Anayasa ve Meclis İçtüzüğü'nde başörtüsü yasağı bulunmadığını belirterek yemini yaptır.",
        "Genel kurula ara ver; grup başkanvekilleriyle kapalı toplantı yaparak yeminin sonraki bir oturumda yapılması için uzlaş.",
        "Milletvekilinin çifte vatandaşlık ve ABD pasaportu işlemlerini İçişleri ve Dışişleri incelemesine aç.",
        "İçtüzük kurallarını ve devlet geleneklerini gerekçe göstererek milletvekilinin genel kurul salonundan çıkarılmasını sağla.",
        "'Milletvekili Dokunulmazlığı ve Meclis İçtüzüğü Kılık Kıyafet Reformu' hazırlayarak kıyafet dayatmalarını kanunen kaldır.",
        "Milli irade korundu; seçilmiş milletvekilinin hakları teslim edildi.",
        "Gerilim büyümeden yatıştırıldı; genel kurul çalışmaları devam etti.",
        "Vatandaşlık mevzuatı incelendi; yasal gereklilikler yerine getirildi.",
        "Devlet teamülleri tavizsiz korundu; meclis otoritesi sergilendi.",
        "İçtüzük reformu ile kılık kıyafet yasaklarının gelecekte hortlaması önlendi."
    ),
    (
        "Çankaya Köşkü'nde Anayasa Kitapçığı Fırlatılması (Şubat 2001)",
        "Cumhurbaşkanlığı & Başbakanlık",
        "char_cumhurbaskani", "char_basbakan",
        "MGK toplantısında Cumhurbaşkanı Sezer'in Başbakan Ecevit'e anayasa kitapçığını fırlatması sonrası gecelik faizler %7500'e fırladı ve borsa çöktü.",
        "Devlet Denetleme Kurulu'nun kamu bankaları yolsuzluk raporlarını bağımsız savcılara teslim et; yargı sürecini başlat.",
        "Köşk ve Başbakanlık arasında acil uzlaşı zirvesi düzenle; ortak basın toplantısıyla 'devlet çarkları işliyor' mesajı ver.",
        "Merkez Bankası döviz rezervlerini piyasaya sürmeyi durdur; dalgalı kur rejimine geçerek Hazine nakit açığını yönet.",
        "Krizin sorumlusu olarak spekülatif sermaye hareketlerine ve piyasa dedikodularına karşı olağanüstü denetim uygula.",
        "'Devlet Organları Arası İletişim ve Kriz Yönetimi Yasası' çıkararak zirve toplantılarının gizlilik ve usulünü yasal takvime bağla.",
        "Yolsuzluk dosyaları adliyeye intikal etti; hesap verilebilirlik sağlandı.",
        "Siyasi güven tazelendi; devletin tepesindeki kavga sona erdirildi.",
        "Dalgalı kura geçilerek milyarlarca dolarlık döviz rezervi erimesi önlendi.",
        "Spekülatörlere gözdağı verildi; devlet ciddiyeti hissettirildi.",
        "Kurumsal reform ile yüksek devlet makamları arasındaki temas protokolü kanunlaştı."
    ),
    (
        "Abdullah Öcalan'ın Kenya'da Yakalanması ve Getirilişi",
        "Başbakanlık & MİT",
        "char_basbakan", "char_genelkurmay_baskani",
        "Nairobi'deki Yunanistan Büyükelçiliği'nden çıkarılan terör elebaşı, bordo berelilerin operasyonuyla Türkiye'ye getirildi; sokaklarda bayram havası esti.",
        "Yargılamayı İmralı Adası'nda kurulan özel mahkemede, uluslararası hukuka ve Türk Ceza Kanunu'na tam uygun şekilde canlı yürüt.",
        "TBMM'de tüm partilerin temsilcileriyle ortak milli birlik deklarasyonu yayınla; toplumsal barışı güçlendir.",
        "Operasyonun ve İmralı güvenliğinin getirdiği ek masrafları Hazine yedek ödeneğinden şeffafça karşıla.",
        "Terör örgütünün misilleme ve sokak eylemleri tehdidine karşı 81 ilde teyakkuza geç; en ufak provokasyona sert müdahale et.",
        "'Terörle Mücadele ve Pişmanlık Kanunu'nu baştan sona yenileyerek dağdaki örgüt üyelerinin çözülmesini hızlandır.",
        "Hukuka tam bağlı yargılama ile dünya kamuoyunda Türkiye'nin haklılığı perçinlendi.",
        "Milli birlik duygusu zirveye çıktı; toplumsal dayanışma güçlendi.",
        "Hazine bütçesi sarsılmadan operasyon lojistiği tamamlandı.",
        "Sokak hakimiyeti sağlandı; terör örgütünün kaos planları boşa çıkarıldı.",
        "Yapısal reform ile örgütün tabanındaki çözülme hızlandı."
    )
]

# We will generate remaining cases for domains 1 to 10
# To ensure all 300 events are realistic and high quality, let's define the catalog of titles and themes!
print("make_part1.py base setup complete.")
