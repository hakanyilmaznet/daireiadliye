# -*- coding: utf-8 -*-
"""
Part 1: Domains 1 to 10 (300 events: tr_vaka_101 to tr_vaka_400)
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

def build_event(id_num, title, source, char1, char2, desc,
                opt1_lbl, opt1_log,
                opt2_lbl, opt2_log,
                opt3_lbl, opt3_log,
                opt4_lbl, opt4_log,
                opt5_lbl, opt5_log,
                eff_mod=0):
    
    # Slight deterministic variations based on id_num / eff_mod
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

    return {
        'id': f'tr_vaka_{id_num:03d}' if id_num < 1000 else f'tr_vaka_{id_num}',
        'characters': [
            {'id': char1, 'name': char_map.get(char1, "Devlet Temsilcisi")},
            {'id': char2, 'name': char_map.get(char2, "Bürokrasi Temsilcisi")}
        ],
        'source': source,
        'title': title,
        'desc': desc,
        'options': [
            {'label': opt1_lbl, 'preview': format_preview(eff1), 'effects': eff1, 'log': opt1_log},
            {'label': opt2_lbl, 'preview': format_preview(eff2), 'effects': eff2, 'log': opt2_log},
            {'label': opt3_lbl, 'preview': format_preview(eff3), 'effects': eff3, 'log': opt3_log},
            {'label': opt4_lbl, 'preview': format_preview(eff4), 'effects': eff4, 'log': opt4_log},
            {'label': opt5_lbl, 'preview': format_preview(eff5), 'effects': eff5, 'log': opt5_log}
        ]
    }

# Definitions of domains 1 to 10
# 30 items per domain
domains = []

# Domain 1: 1990'lar Koalisyonlar ve Siyasi Krizler
d1 = [
    ("Refahyol Hükümeti Protokolü ve Güvenoyu Çalkantısı", "TBMM & Başbakanlık", "char_basbakan", "char_milletvekili",
     "54. Hükümetin kurulması sürecinde partiler arası protokol pazarlıkları ve güvenoyu oylaması meclis kulislerinde büyük gerilim yarattı.",
     "Milletvekili transferi iddialarına karşı Meclis Araştırması aç ve süreci bağımsız yargıya sevk et.", "Hukuki süreç işletildi; siyaset üzerindeki şaibeler yargı marifetiyle dağıtıldı.",
     "Koalisyon liderleri arasında uzlaşı sağla; kabine içi dengeleri gözeterek meclis aritmetiğini sakinleştir.", "Siyasi uzlaşı sağlandı; hükümet güvenoyu alarak göreve başladı.",
     "Bütçe disiplininden taviz verme; koalisyon ortaklarının popülist harcama taleplerini Hazine adına frenle.", "Hazine dengesi muhafaza edildi; popülist harcamalar durduruldu.",
     "Güvenlik bürokrasisinin hükümet programına yönelik itirazlarını kararlı bir devlet iradesiyle sınırla.", "Sivil otorite pekiştirildi; bürokratik vesayet baskısı kırıldı.",
     "'Siyasi Partiler ve Koalisyonlar Kanunu' çıkararak güvenoyu süreçlerini anayasal güvencelere bağla.", "Yasal reform ile koalisyon protokolleri kurumsal güvenceye bağlandı."),

    ("Aydınlık İçin Bir Dakika Karanlık Eylemleri", "İçişleri Bakanlığı", "char_icisleri_bakani", "char_adli_yargi_hakimi",
     "Susurluk kazası sonrası her akşam saat 21.00'de evlerde ışıkların kapatılmasıyla başlayan eylem, milyonların katıldığı bir sivil itaatsizliğe dönüştü.",
     "Eylemcilerin 'temiz toplum' talebini esas al; devlet-çete irtibatı iddialarını derhal DGM Başsavcılığı'na taşı.", "Halkın adalet talebi karşılık buldu; yargı çetelerin üzerine kararlılıkla gitti.",
     "Toplumsal tansiyonu düşür; sivil toplum kuruluşlarıyla diyalog kurarak meclis araştırması başlat.", "Diyalog yoluyla gerilim düşürüldü; sokaktaki öfke meclis zeminine taşındı.",
     "Karanlık eylemleri sırasında sokak güvenliğini sağlayan kolluk kuvvetlerine ek bütçe ve donanım aktar.", "Güvenlik bütçesi takviye edildi; şehir asayişi korundu.",
     "Kamu düzenini bozduğu ve trafiği aksattığı gerekçesiyle izinsiz gösterilere kolluk marifetiyle müdahale et.", "Kamu nizamı tavizsiz sağlandı; devletin otoritesi hissettirildi.",
     "'Sivil Toplum ve Gösteri Yürüyüşleri Reform Paketi' hazırlayarak barışçıl protesto hakkını yasal teminata al.", "Yeni mevzuat ile toplantı ve gösteri hakkı demokratik güvenceye kavuşturuldu."),

    ("28 Şubat 1997 MGK Bildirisi ve 18 Maddelik Talimat Listesi", "Milli Güvenlik Kurulu (MGK)", "char_genelkurmay_baskani", "char_basbakan",
     "9 saat süren tarihi MGK toplantısında askeri kanat, hükümete 18 maddelik tedbir paketini imzalama çağrısında bulundu.",
     "Anayasal hukuk devleti ilkelerine bağlı kal; bildirideki talepleri bağımsız yargı ve anayasa süzgecinden geçir.", "Hukukun üstünlüğü gözetildi; anayasal sınırlara riayet sağlandı.",
     "Siyasi krizi yumuşat; MGK tavsiye kararlarını hükümet içinde kademeli bir takvime bağlayarak imza krizini aş.", "Zamana yayılan uzlaşıyla hükümet krizi geçici olarak donduruldu.",
     "Kararların kamu maliyesine ve vakıf gelirlerine etkisini araştır; bütçe gelirlerini koruyacak tedbirler al.", "Mali tedbirlerle vakıf ve dernek hesapları denetime alındı.",
     "Askeri kanadın brifinglerine ve talimatlarına karşı hükümetin yürütme gücünü ve devlet otoritesini net bir dille savun.", "Sivil irade dik duruş sergiledi; askeri vesayete karşı devlet heybeti korundu.",
     "'Milli Güvenlik Kurulu Teşkilat Kanunu'nda reform yaparak kurulun görevini salt sivil danışma organı olarak sınırla.", "Kurumsal reform ile MGK'nın sivil niteliği yasal zemine oturtuldu."),

    ("Batı Çalışma Grubu (BÇG) Fişleme Belgeleri", "Adalet Bakanlığı & DGM", "char_adalet_bakani", "char_adli_yargi_hakimi",
     "Deniz Kuvvetleri Komutanlığı bünyesinde kurulan BÇG'nin binlerce kamu görevlisini ve siyasetçiyi fişlediği belgelerin sızması ortalığı karıştırdı.",
     "Fişleme belgelerini askeri savcılıktan adli yargıya al; kişisel verileri ihlal eden sorumlular hakkında dava aç.", "Kişisel hak ihlallerine yargı dur dedi; hukuk devletine güven pekişti.",
     "Bürokrasideki gerilimi yatıştırmak için Meclis İnceleme Heyeti kur; askeriye ile sivil idareyi karşı karşıya getirme.", "Siyasi dengeler korundu; ordu-hükümet çatışması engellendi.",
     "Yasadışı fişleme faaliyetlerine harcanan gizli ödenek ve kamu kaynaklarını Sayıştay denetimine aç.", "Gizli harcamalar denetlendi; kamu bütçesinin suistimali önlendi.",
     "Askeri istihbaratın iç güvenlik konusundaki hassasiyetini koru; gizli bilgi sızdıran köstebekleri derhal cezalandır.", "Gizli bilgi sızdıran klikler dağıtıldı; askeri disiplin tesis edildi.",
     "'Kamu Görevlilerinin Korunması ve Fişlemenin Yasaklanması Kanunu' çıkararak benzer yapıları müebbet hapse bağla.", "Yeni kanun ile fişleme suçu ilk kez TCK'da en ağır yaptırımlara bağlandı."),

    ("Sincan'da Kudüs Gecesi ve Tankların Yürütülmesi", "İçişleri Bakanlığı & Genelkurmay", "char_icisleri_bakani", "char_genelkurmay_baskani",
     "Sincan Belediyesi'nin düzenlediği gecedeki konuşmalar sonrası Etimesgut Zırhlı Birlikler Okulu'na ait tanklar Sincan caddelerinden geçti.",
     "Kudüs Gecesi'nde Anayasa'ya aykırı konuşma yapanlar ve tankları şehre sokanlar hakkında eşzamanlı adli soruşturma aç.", "Çifte soruşturma ile hukukun tarafsızlığı sağlandı; her iki tarafa da hesap soruldu.",
     "Belediye başkanını görevden uzaklaştırarak gerilimi düşür; askeriye ile polemiğe girmeden krizi idari kararla çöz.", "İdari tasarrufla tansiyon düşürüldü; koalisyon ömrü uzatıldı.",
     "Sincan'da yaşanan gerilimin piyasalara etkisini sınırlamak için Merkez Bankası likidite desteğini artır.", "Piyasalara güven verildi; faiz dalgalanmasının önüne geçildi.",
     "Tankların sokaktan geçmesini 'demokrasiye balans ayarı' olarak niteleyen askeri yetkililere sert idari yaptırım uygula.", "Hükümetin sivil otoritesi tavizsiz gösterildi.",
     "'Askeri Birliklerin İntikali ve Meskun Mahal Güvenliği Kanunu' çıkararak her türlü askeri konvoyu sivil izne bağla.", "Yasal düzenleme ile kışladan sivil izinsiz palet dahi çıkması kanunen yasaklandı."),

    ("Fazilet Partisi'nin Kurulması ve Kapatılması Davası", "Anayasa Mahkemesi", "char_anayasa_mahkemesi_baskani", "char_tbmm_baskani",
     "Refah Partisi'nin kapatılmasının ardından kurulan Fazilet Partisi hakkında Yargıtay Cumhuriyet Başsavcılığı 'odak olma' gerekçesiyle kapatma davası açtı.",
     "AİHM içtihatları ve Venedik Komisyonu ilkeleri doğrultusunda karar ver; parti kapatma yerine odak olan kişilere ceza ver.", "Hukuki standartlar yükseltildi; evrensel hukuk normlarına bağlı kalındı.",
     "Mecliste grubu bulunan partilerle uzlaş; Anayasa'nın 69. maddesini değiştirerek parti kapatmayı zorlaştıracak formül üret.", "Mecliste uzlaşı arandı; anayasal kriz yumuşatıldı.",
     "Kapatılması talep edilen partinin Hazine yardımına bloke koy; kamu kaynağının amaç dışı kullanımını engelle.", "Hazine kaynağı korundu; bütçeden gereksiz harcama kesildi.",
     "Cumhuriyetin temel niteliklerine aykırı odaklaşmaya karşı AYM'nin mutlak kapatma yetkisini tavizsiz kullan.", "Anayasal düzen korundu; devletin kırmızı çizgileri hissettirildi.",
     "'Siyasi Partiler Kanunu Reformu' yaparak parti kapatma kararlarını sadece şiddet ve terör odağı olma şartına bağla.", "Yasal reform ile parti kapatma rejiminde köklü ve modern bir dönemeç açıldı."),

    ("18 Nisan 1999 Seçimleri ve 57. Hükümet Protokolü", "TBMM & Başbakanlık", "char_basbakan", "char_tbmm_baskani",
     "DSP, MHP ve ANAP'ın oluşturduğu 57. Hükümet kurulurken koalisyon ortakları arasında bakanlık paylaşımları ve Meclis Başkanlığı pazarlığı kızıştı.",
     "Bakanlıkların teşkilat yapılarını liyakat esasına göre düzenle; koalisyon kadrolaşmasına yargı ve Danıştay denetimi getir.", "Liyakat sağlandı; kadrolaşma ve usulsüz atamaların önüne geçildi.",
     "Üç partili koalisyon liderleri zirvesi topla; bakanlıkları adilce dağıtıp istikrarlı bir hükümet protokolü imzala.", "Koalisyon uyumu sağlandı; Meclis tatile girmeden güvenoyu tamamlandı.",
     "Kamu bankaları ve KİT'lerin koalisyon partileri arasında paylaşılmasını kesinlikle yasakla; Hazine harcamalarını kıs.", "Kamu bankaları tasalluttan kurtarıldı; Hazine açıkları sınırlandı.",
     "Koalisyon uyumsuzluğu çıkaran bakanları Başbakanlık yetkisini kullanarak derhal görevden al.", "Başbakanlık otoritesi hissettirildi; hükümet disiplini korundu.",
     "'Koalisyon Hükümetleri Çalışma Usulü ve Kamu Yönetimi Reformu Kanunu' çıkararak bakanlık yetki çakışmalarını bitir.", "Yasal mevzuat ile bakanlıkların görev sınırları kalıcı olarak netleştirildi."),

    ("Merve Kavakçı'nın TBMM Yemin Töreni Gerilimi", "TBMM Genel Kurulu", "char_tbmm_baskani", "char_milletvekili",
     "21. Dönem ilk birleşiminde başörtüsüyle genel kurula gelen milletvekiline yönelik protestolar meclisi kilitledi; vatandaşlık tartışmaları patlak verdi.",
     "Milletin iradesine saygı duy; Anayasa ve Meclis İçtüzüğü'nde başörtüsü yasağı bulunmadığını belirterek yemini yaptır.", "Milli irade korundu; seçilmiş milletvekilinin hakları teslim edildi.",
     "Genel kurula ara ver; grup başkanvekilleriyle kapalı toplantı yaparak yeminin sonraki oturumda yapılması için uzlaş.", "Gerilim büyümeden yatıştırıldı; genel kurul çalışmaları devam etti.",
     "Milletvekilinin çifte vatandaşlık ve ABD pasaportu bildirim işlemlerini İçişleri incelemesine aç.", "Vatandaşlık mevzuatı incelendi; yasal gereklilikler yerine getirildi.",
     "İçtüzük kurallarını ve devlet geleneklerini gerekçe göstererek genel kurul salonundaki intizamı kollukla sağla.", "Devlet teamülleri tavizsiz korundu; meclis otoritesi sergilendi.",
     "'Milletvekili Dokunulmazlığı ve Meclis İçtüzüğü Kılık Kıyafet Reformu' hazırlayarak kıyafet dayatmalarını kanunen kaldır.", "İçtüzük reformu ile kılık kıyafet yasaklarının gelecekte hortlaması önlendi."),

    ("Çankaya Köşkü'nde Anayasa Kitapçığı Fırlatılması (Şubat 2001)", "Cumhurbaşkanlığı & Başbakanlık", "char_cumhurbaskani", "char_basbakan",
     "MGK toplantısında Cumhurbaşkanı Sezer'in Başbakan Ecevit'e anayasa kitapçığını fırlatması sonrası gecelik faizler %7500'e fırladı ve borsa çöktü.",
     "Devlet Denetleme Kurulu'nun kamu bankaları yolsuzluk raporlarını bağımsız savcılara teslim et; yargı sürecini başlat.", "Yolsuzluk dosyaları adliyeye intikal etti; hesap verilebilirlik sağlandı.",
     "Köşk ve Başbakanlık arasında acil uzlaşı zirvesi düzenle; ortak basın toplantısıyla 'devlet çarkları işliyor' mesajı ver.", "Siyasi güven tazelendi; devletin tepesindeki kavga sona erdirildi.",
     "Merkez Bankası döviz rezervlerini piyasaya sürmeyi durdur; dalgalı kur rejimine geçerek Hazine nakit açığını yönet.", "Dalgalı kura geçilerek milyarlarca dolarlık döviz rezervi erimesi önlendi.",
     "Krizin sorumlusu olarak spekülatif sermaye hareketlerine ve piyasa dedikodularına karşı olağanüstü denetim uygula.", "Spekülatörlere gözdağı verildi; devlet ciddiyeti hissettirildi.",
     "'Devlet Organları Arası İletişim ve Kriz Yönetimi Yasası' çıkararak zirve toplantılarının gizlilik ve usulünü yasal takvime bağla.", "Kurumsal reform ile yüksek devlet makamları arasındaki temas protokolü kanunlaştı."),

    ("Abdullah Öcalan'ın Kenya'da Yakalanması ve Getirilişi", "Başbakanlık & MİT", "char_basbakan", "char_genelkurmay_baskani",
     "Nairobi'deki Yunanistan Büyükelçiliği'nden çıkarılan terör elebaşı, bordo berelilerin operasyonuyla Türkiye'ye getirildi; sokaklarda bayram havası esti.",
     "Yargılamayı İmralı Adası'nda kurulan özel mahkemede, uluslararası hukuka ve Türk Ceza Kanunu'na tam uygun şekilde canlı yürüt.", "Hukuka tam bağlı yargılama ile dünya kamuoyunda Türkiye'nin haklılığı perçinlendi.",
     "TBMM'de tüm partilerin temsilcileriyle ortak milli birlik deklarasyonu yayınla; toplumsal barışı güçlendir.", "Milli birlik duygusu zirveye çıktı; toplumsal dayanışma güçlendi.",
     "Operasyonun ve İmralı güvenliğinin getirdiği ek masrafları Hazine yedek ödeneğinden şeffafça karşıla.", "Hazine bütçesi sarsılmadan operasyon lojistiği tamamlandı.",
     "Terör örgütünün misilleme ve sokak eylemleri tehdidine karşı 81 ilde teyakkuza geç; en ufak provokasyona sert müdahale et.", "Sokak hakimiyeti sağlandı; terör örgütünün kaos planları boşa çıkarıldı.",
     "'Terörle Mücadele ve Pişmanlık Kanunu'nu baştan sona yenileyerek dağdaki örgüt üyelerinin çözülmesini hızlandır.", "Yapısal reform ile örgütün tabanındaki çözülme hızlandı."),

    ("İmralı Duruşmaları ve Ağırlaştırılmış Müebbet Kararı", "Adalet Bakanlığı & DGM", "char_adalet_bakani", "char_adli_yargi_hakimi",
     "Şehit ailelerinin ve yerli-yabancı basının izlediği İmralı duruşmalarında Ankara 2 No'lu DGM, sanığı Türk Ceza Kanunu'nun 125. maddesi uyarınca idama mahkum etti.",
     "Yargı kararını titizlikle infaza hazırla; temyiz sürecini Yargıtay Ceza Genel Kurulu'nda açık duruşmayla tamamla.", "Yargı kararı tam hukuki kesinlik kazandı.",
     "Şehit aileleri dernekleri ile sivil toplum temsilcilerini kabul et; infaz konusundaki hassasiyetleri Meclis'te değerlendir.", "Toplumsal teselli sağlandı; acılı ailelerin devlete güveni korundu.",
     "İmralı cezaevi güvenliği ve ada lojistiği için Adalet Bakanlığı bütçesinden özel ödenek tahsis et.", "Ada güvenliği bütçelendirildi; güvenlik zafiyeti yaşanmadı.",
     "Adadaki duruşmalar sırasında sınır boylarında ve cezaevi etrafında askeri teyakkuz seviyesini en üste çıkar.", "Cezaevi ve ada güvenliği çelik bir zırhla tahkim edildi.",
     "'Ağırlaştırılmış Müebbet Hapis İnfaz Rejimi Kanunu' hazırlayarak infaz koşullarını uluslararası standartlara bağla.", "Modern infaz rejimi yasalaştı; uluslararası platformlarda Türkiye'nin eli güçlendi."),

    ("1999 Topluma Kazandırma Kanunu (Pişmanlık Yasası)", "İçişleri Bakanlığı & TBMM", "char_icisleri_bakani", "char_tbmm_baskani",
     "Terör örgütünden kopmaları hızlandırmak amacıyla hazırlanan Pişmanlık Yasası, şartları ve kapsamı bakımından mecliste hararetli tartışmalara sahne oldu.",
     "Silahlı eyleme karışmamış örgüt mensuplarının adli incelemesini titizlikle yap; suça bulaşanları kesinlikle affetme.", "Hukukun adalet terazisi korundu; masum ile suçlu titizlikle ayrıldı.",
     "Meclisteki tüm siyasi partilerin onay vereceği ortak bir af ve topluma kazandırma metninde uzlaş.", "Geniş bir meclis mutabakatı sağlandı; kanun kabul edildi.",
     "Pişmanlık yasasından yararlanıp topluma dönen gençlerin meslek edinmesi için İŞKUR ve KOSGEB hibeleri tahsis et.", "Sosyal rehabilitasyon fonu kuruldu; eski militanların üretici olması sağlandı.",
     "Yasayı istismar edip şehirlere sızmaya çalışan şüphelilere karşı istihbarat ve emniyet takibini aralıksız sürdür.", "Güvenlik açığı oluşması engellendi; istismar girişimleri boşa çıkarıldı.",
     "'Terör Mağdurları ve Toplumsal Rehabilitasyon Kanunu' çıkararak hem şehit yakınlarını koru hem dağdan inişi teşvik et.", "Dengeli reform ile hem mağdurların hakkı korundu hem de örgütten kopuş hızlandı."),

    ("Şartlı Salıverme Yasası (Rahşan Affı) ve Cezaevi Tahliyeleri", "Adalet Bakanlığı", "char_adalet_bakani", "char_milletvekili",
     "Cezaevlerindeki doluluğu azaltmak amacıyla çıkarılan yasa sonrası binlerce adli suçlunun tahliye olması kamuoyunda adalet duygusunu sarstı.",
     "Anayasa Mahkemesi'ne taşınan eşitlik ilkesi itirazlarını bekle; af kapsamının tecavüz ve cinayet suçlarına genişlemesini engelle.", "Hukuki sınırlar korundu; ağır suçluların salıverilmesinin önüne geçildi.",
     "Koalisyon ortakları ve mağdur ailelerle görüşerek tepkileri dindirecek ek bir düzeltme protokolü hazırla.", "Siyasi gerginlik hafifletildi; hükümet içindeki çatlaklar onarıldı.",
     "Tahliye olanların yeniden suça bulaşmasını önlemek için denetimli serbestlik birimlerine Hazine ödeneği aktar.", "Denetim altyapısı finanse edildi; mükerrer suç oranı düşürüldü.",
     "Sokaklarda güvenliği artır; cezaevinden çıkan sabıkalıları emniyet asayiş şubeleri marifetiyle yakın takibe al.", "Sokak suçlarına karşı polis teyakkuzu artırıldı; asayiş sağlandı.",
     "'Ceza ve Güvenlik Tedbirlerinin İnfazı Hakkında Temel Kanun' hazırlayarak keyfi afları anayasal olarak yasakla.", "İnfaz rejiminde kalıcı reform yapıldı; af beklentileri sona erdirildi."),

    ("Hayata Dönüş Operasyonu ve F Tipi Cezaevleri", "İçişleri Bakanlığı & Ceza Tevkifevleri", "char_icisleri_bakani", "char_adalet_bakani",
     "20 cezaevinde eşzamanlı başlatılan ölüm oruçlarını kırmak ve koğuş sisteminden oda sistemine geçmek amacıyla düzenlenen operasyonda 32 kişi hayatını kaybetti.",
     "Operasyon sırasında meydana gelen ölüm ve yaralanmalar hakkında tarafsız savcılık ve tabip odası soruşturması başlat.", "Adli tahkikat başlatıldı; sorumluların yargılanması süreci işletildi.",
     "Aydınlar, yazarlar ve baro temsilcilerinden oluşan arabulucu heyetiyle ölüm oruçlarını bitirecek bir müzakere yürüt.", "Sivil toplumla temas kuruldu; can kayıplarının artması önlendi.",
     "F tipi cezaevlerinin modern rehabilitasyon ve atölye imkanlarını tamamlamak için mali bütçeyi iki katına çıkar.", "Modern cezaevi altyapısı finanse edildi.",
     "Cezaevlerindeki örgüt hakimiyetine son vermek için jandarma ve gardiyanların mutlak kontrolünü sağla.", "Devletin cezaevlerindeki mutlak hakimiyeti yeniden kuruldu.",
     "'Ceza İnfaz Kurumları İnfaz ve Koruma Kanunu'nu Avrupa İşkencenin Önlenmesi Komitesi standartlarına tam uyumlu hale getir.", "Yasal güvenceler getirildi; F tipi sistem uluslararası denetime açıldı."),

    ("Manisa Davası ve Polis İşkencesi İddiaları", "Adalet Bakanlığı & Emniyet", "char_adalet_bakani", "char_icisleri_bakani",
     "Manisa'da duvarlara yazı yazdıkları gerekçesiyle gözaltına alınan 16 liseli gence işkence yapıldığı iddiası Türkiye gündemini sarstı.",
     "İşkenceyle suçlanan polis memurlarını derhal açığa al ve ağır ceza mahkemesinde kamu davası açtır.", "İşkence iddiaları cezasız kalmadı; yargı adaleti tecelli ettirdi.",
     "Gençlerin aileleri ve insan hakları heyetleriyle bir araya gelerek kamuoyunu teskin edici açıklamalar yap.", "Toplumsal vicdan yatıştırıldı; devlet-vatandaş güveni tazelendi.",
     "Gözaltı merkezlerinin kamera sistemleri ve doktor muayenehaneleri için Hazine bütçesinden özel pay ayır.", "Karakollara kamera ve şeffaf muayene altyapısı kuruldu.",
     "Emniyet teşkilatı içinde disiplin teftiş kurulu görevlendir; meslek etiğini çiğneyen personeli teşkilattan ihraç et.", "Emniyet içinde temizlik yapıldı; kurumsal saygınlık korundu.",
     "'İşkence ve Kötü Muameleye Sıfır Tolerans Yasası' çıkararak gözaltı sürelerini 24 saate indir ve avukatsız ifadeyi yasakla.", "Tarihi bir yasal devrim yapıldı; işkence suçunda zamanaşımı kaldırıldı."),

    ("Metin Göktepe Davası ve Gazeteci Cinayeti Yargılaması", "Adalet Bakanlığı", "char_adalet_bakani", "char_adli_yargi_hakimi",
     "Gözaltında darp edilerek öldürülen gazeteci Metin Göktepe davası, kamuoyu baskısı nedeniyle güvenlik gerekçesiyle ilden ile nakledildi.",
     "Davanın üzerindeki siyasi ve bürokratik baskıları kaldır; cinayetten sorumlu polislerin ağır cezada mahkum edilmesini sağla.", "Hukukun üstünlüğü korundu; gazeteci cinayetinde polisler ilk kez hapis cezası aldı.",
     "Basın meslek örgütleri ve gazetecilerle diyalog kurarak duruşmaların şeffaf izlenmesini temin et.", "Basın camiası ile diyalog sağlandı; adliye önündeki gerginlik dindirildi.",
     "Adliye güvenliğini ve tanık koruma programını Hazine kaynaklarıyla güçlendir.", "Dava güvenliği sağlandı; yargılama kesintisiz tamamlandı.",
     "Duruşma salonları önünde provokasyon yaratmak isteyen gruplara karşı polis barikatlarıyla nizamı koru.", "Adliye çevresinde kamu düzeni tavizsiz sağlandı.",
     "'Basın Özgürlüğü ve Gazetecilerin Güvenliği Kanunu' çıkararak gazetecilerin gözaltında fiziksel dokunulmazlığını anayasal güvenceye al.", "Yasal düzenleme ile haber takibi yapan gazetecilerin korunması kanunlaştı."),

    ("3 Kasım 2002 Erken Genel Seçimleri ve Siyasetin Tasfiyesi", "Yüksek Seçim Kurulu (YSK)", "char_tbmm_baskani", "char_cumhurbaskani",
     "Ekonomik kriz sonrası gidilen erken seçimde merkez sağ ve solun köklü partileri (DYP, ANAP, DSP, MHP) baraj altında kalarak meclis dışı kaldı.",
     "Seçim sonuçlarının itirazsız ve şeffaf tescilini sağla; YSK marifetiyle milli iradenin tecellisini koru.", "Seçim güvenliği ve meşruiyeti tam olarak tescillendi.",
     "Baraj altında kalan parti liderleriyle istişare et; Meclis'te temsil edilemeyen %45'lik seçmen kitlesini teskin et.", "Siyasi geçiş süreci barışçıl ve medeni şekilde tamamlandı.",
     "Seçim masrafları ve siyasi partilere yapılan Hazine yardımlarını Sayıştay denetimiyle kapat.", "Seçim bütçesi denetlendi; kamu zararı oluşması önlendi.",
     "İktidar devir teslimi sırasında bürokraside ve güvenlik teşkilatında herhangi bir zaafiyete izin verme.", "Devlette devamlılık ilkesi korundu; sorunsuz geçiş sağlandı.",
     "'Seçim Kanunu ve Temsilde Adalet Reformu' hazırlayarak %10'luk seçim barajını makul bir seviyeye indirmeyi tartışmaya aç.", "Demokratik temsil için yapısal reform adımı atıldı."),

    ("Recep Tayyip Erdoğan'ın Siirt Seçimi ile Başbakanlığı", "TBMM & YSK", "char_tbmm_baskani", "char_basbakan",
     "Okuduğu şiir nedeniyle siyasi yasaklı olan AK Parti Genel Başkanı, Siirt'teki seçim iptali ve Anayasa değişikliği ile TBMM'ye girip Başbakan oldu.",
     "Anayasa'nın 76. maddesi değişikliğini hukuki çerçevede uygula; seçilme hakkının önündeki engelleri yargı kararıyla kaldır.", "Milli iradenin liderini seçme hakkı hukuken teslim edildi.",
     "Meclisteki ana muhalefet partisi CHP ile uzlaşarak Anayasa değişikliğini geniş mutabakatla kabul et.", "İki partili mecliste tarihi bir uzlaşı sağlandı; siyasi kriz aşıldı.",
     "Siirt yenileme seçiminin getirdiği bütçe masraflarını YSK ödeneğinden karşıla.", "Yenileme seçimi mali disiplin içinde tamamlandı.",
     "Seçim sürecinde meydana gelebilecek olası sokak provokasyonlarına karşı Siirt'te kolluk tedbirlerini artır.", "Seçim günü asayiş kusursuz sağlandı.",
     "'Milletvekili Seçilme Yeterliliği ve Siyasi Haklar Kanunu' çıkararak fikir suçlarından kaynaklı yasakları kalıcı olarak bitir.", "Siyaset yapma özgürlüğü kalıcı kanuni teminata bağlandı."),

    ("1 Mart 2003 Tezkeresi ve TBMM Tarihi Ret Kararı", "TBMM Genel Kurulu", "char_tbmm_baskani", "char_diplomat",
     "ABD birliklerinin Türkiye üzerinden Irak'a girmesine ve TSK'nın Kuzey Irak'a gönderilmesine izin veren tezkere, 264 oya karşı 250 oyla salt çoğunluğu sağlayamadı.",
     "Meclis Başkanının İçtüzük hükümlerine tam uyarak salt çoğunluk kuralını uygulamasını ve ret kararını tescillemesini sağla.", "Meclis iradesine ve hukuka tam bağlı kalındı; Türkiye savaşa girmedi.",
     "ABD ile diplomatik kanalları açık tut; stratejik ortaklığı koruyacak yeni bir işbirliği çerçevesi belirle.", "Diplomatik kriz kontrol altına alındı; müttefiklik dengesi korundu.",
     "Tezkerenin reddiyle ABD'den gelecek milyarlarca dolarlık ekonomik hibe kaybedilse de Hazine'yi yerli kaynaklarla dengele.", "Mali bağımsızlık korundu; yabancı yardım şartlarına boyun eğilmedi.",
     "Kuzey Irak sınırındaki birliklerin tahkimatını artır; sınır hattındaki terör hareketliliğine karşı orduyu teyakkuzda tut.", "Sınır güvenliği en üst seviyeye çıkarıldı; caydırıcılık korundu.",
     "'Yurtdışına Asker Gönderme ve Yabancı Birlikleri Kabul Usulü Kanunu' hazırlayarak tezkere süreçlerini şeffaf kurallara bağla.", "Milli güvenlik tezkereleri kalıcı ve kurumsal bir yasal nizama kavuşturuldu."),

    ("Süleymaniye'de Çuval Olayı (4 Temmuz 2003)", "Milli Savunma Bakanlığı & Dışişleri", "char_savunma_bakani", "char_diplomat",
     "Irak Süleymaniye'de Türk Özel Kuvvetleri karargahına baskın düzenleyen ABD askerleri, 11 Türk subay ve astsubayını başlarına çuval geçirerek Bağdat'a götürdü.",
     "Olayı derhal uluslararası hukuka ve Cenevre Sözleşmesi'ne taşı; ABD askeri yetkilileri hakkında suç duyurusu yap.", "Uluslararası hukuk zemininde haklılığımız dünyaya ilan edildi.",
     "Washington nezdinde en üst düzey diplomatik nota ver; Ankara ve Bağdat'ta ortak kriz masası kurarak askerlerin serbest kalmasını sağla.", "Diplomatik baskı sonuç verdi; 60 saat içinde askerlerimiz sağ salim teslim alındı.",
     "Bölgedeki Türk irtibat bürolarının güvenlik ve lojistik harcamalarını Hazine kaynaklarıyla baştan donat.", "Irak sahasındaki karargahların güvenliği finanse edildi.",
     "İncirlik Üssü ve Türk hava sahasındaki ABD askeri uçuşlarına karşı anında kısmi kısıtlamalar getirerek mütekabiliyet uygula.", "Türkiye'nin askeri onuru ve devlet heybeti hissettirildi.",
     "'Yurtdışı Askeri Misyonların Korunması ve Dokunulmazlık Protokolü' çıkararak sınır ötesi timlerin statüsünü yasal güvenceye al.", "Yurtdışı askeri birliklerimizin statüsü uluslararası protokole bağlandı."),

    ("Kıbrıs Annan Planı Referandumu (2004)", "Dışişleri Bakanlığı & KKTC", "char_diplomat", "char_cumhurbaskani",
     "Birleşmiş Milletler'in Kıbrıs'ta iki toplumlu federasyon öngören Annan Planı, Türk tarafından %65 'Evet', Rum tarafından %75 'Hayır' oyu aldı.",
     "Referandum sonucunu BM ve Lahey Adalet Divanı'na taşı; Rum tarafının uzlaşmazlığını uluslararası hukukta tescille.", "Uluslararası hukukta Türk tarafının çözüm yanlısı olduğu kanıtlandı.",
     "KKTC Cumhurbaşkanı Rauf Denktaş ve muhalefetle Ankara'da milli mutabakat zirvesi düzenle; iç cepheyi tahkim et.", "Kıbrıs davasında iç siyasi çatlaklar onarıldı.",
     "Referandum sonrası KKTC'ye uygulanan ambargoları kırmak için Hazine'den doğrudan ekonomik yardım paketi aç.", "KKTC ekonomisine can suyu sağlandı.",
     "Rum tarafının tek taraflı AB üyesi yapılmasına karşı Doğu Akdeniz ve Ada'daki askeri varlığımızı artır.", "Kıbrıs Türk Barış Kuvvetleri'nin caydırıcılığı pekiştirildi.",
     "'Kuzey Kıbrıs Türk Cumhuriyeti Entegrasyon ve Tanınma Yasası' çıkararak stratejik yatırımları anayasal korumaya al.", "KKTC ile ilişkiler yasal ve kurumsal ortaklık seviyesine yükseltildi."),

    ("AB Uyum Yasaları ve DGM'lerin Kaldırılması (2004)", "Adalet Bakanlığı & TBMM", "char_adalet_bakani", "char_tbmm_baskani",
     "Avrupa Birliği katılım müzakereleri çerçevesinde hazırlanan 8 uyum paketiyle Devlet Güvenlik Mahkemeleri (DGM) tamamen tarihe karıştı.",
     "DGM dosyalarını ihtisaslaşmış Ağır Ceza Mahkemelerine devret; askeri hakim ve savcıların sivil yargıdan çıkışını sağla.", "Yargıda sivilleşme ve şeffaflık sağlandı; çift başlı yargı sona erdi.",
     "Muhalefet partileriyle Meclis Adalet Komisyonu'nda tam mutabakat sağla; yasa paketini firesiz kabul et.", "Geniş siyasi konsensüs ile tarihi reformlar meclisten geçirildi.",
     "Yeni kurulan adliyelerin ve ihtisas mahkemelerinin lojistik altyapısını Hazine bütçesinden karşıla.", "Adli teşkilatın modernizasyonu finanse edildi.",
     "DGM'lerin kalkmasıyla terör suçlularının cezaevlerinden kaçmasını önleyecek yüksek güvenlikli infaz tedbirleri al.", "Güvenlik zafiyeti yaşanması engellendi.",
     "'Yargı Reformu ve Temel Haklar Çerçeve Kanunu' çıkararak AİHM içtihatlarının ulusal kanunların üzerinde olduğunu tescille.", "Anayasa'nın 90. maddesi reformu ile uluslararası insan hakları üstün kılındı."),

    ("İdam Cezasının Tamamen Kaldırılması (2002-2004)", "TBMM Genel Kurulu", "char_tbmm_baskani", "char_adalet_bakani",
     "Avrupa İnsan Hakları Sözleşmesi 6 ve 13 No'lu protokolleri uyarınca barış ve savaş zamanında ölüm cezası Anayasa ve yasalardan çıkarıldı.",
     "İdam cezası alan hükümlülerin cezalarını ağırlaştırılmış müebbet hapis cezasına dönüştürerek infaz dosyalarını güncelle.", "Hukuki kesinlik sağlandı; uluslararası taahhütler yerine getirildi.",
     "Koalisyon ortakları ve muhalefetle meclis zemininde uzlaşarak toplumsal hassasiyetleri dengeleyen formüller üret.", "Siyasi gerginlik yatıştırıldı; Meclis onuru korundu.",
     "Cezaevlerinde ağırlaştırılmış müebbet hükümlülerinin güvenliği için ek tecrit ve kamera ödeneği ayır.", "Cezaevi güvenliği bütçelendirildi.",
     "Şehit yakınlarının tepkilerini dikkate alarak terör elebaşının hiçbir aftan yararlanamayacağını sert bir dille açıkla.", "Devletin terörle mücadeledeki tavizsiz kararlılığı vurgulandı.",
     "'Türk Ceza Kanunu Uyum ve Yaşam Hakkı Güvencesi Yasası' çıkararak idam cezasının geri getirilmesini anayasal olarak imkansız kıl.", "Yaşam hakkı en üst anayasal güvenceye kavuşturuldu."),

    ("Farklı Dil ve Lehçelerde Yayın İzni (TRT 6 ve Özel Radyolar)", "RTÜK & TRT", "char_adalet_bakani", "char_icisleri_bakani",
     "AB uyum yasalarıyla birlikte Türkiye'de ilk kez Türk vatandaşlarının günlük yaşamda geleneksel olarak kullandığı dillerde yayın hakkı tanındı.",
     "Yayın yönetmeliklerini anayasal eşitlik ve düşünce özgürlüğü ilkeleri doğrultusunda yargı denetimine aç.", "Kültürel haklar hukuki güvenceye kavuştu.",
     "Güneydoğu kanaat önderleri ve sivil toplumla görüşerek yayın saatleri ve içerik konusunda mutabakat sağla.", "Toplumsal barış ve aidiyet duygusu güçlendi.",
     "TRT bünyesinde Kürtçe ve diğer dillerde yayın yapacak stüdyolar ve tercüme birimleri için Hazine fonu ayır.", "Kültürel yayıncılık altyapısı bütçelendirildi.",
     "Yayınların bölücü terör propagandasına alet edilmesini önlemek için RTÜK ve emniyet denetimini 24 saat sürdür.", "Kamu nizamı ve milli güvenlik hassasiyeti korundu.",
     "'Kültürel Çeşitlilik ve Yayıncılık Standartları Kanunu' çıkararak anadilde yayın haklarını kurumsal güvenceye bağla.", "Yasal güvence ile kültürel haklar demokratik standarda ulaştırıldı."),

    ("Gayrimüslim Cemaat Vakıfları Mülk İadesi Yasası", "Vakıflar Genel Müdürlüğü", "char_adalet_bakani", "char_diplomat",
     "1936 Beyannamesi sonrası cemaat vakıflarının elinden çıkan taşınmazların hak sahiplerine iadesi veya tazminatı yasalaştı.",
     "Tapu ve kadastro kayıtlarını bağımsız mahkeme heyetleriyle incele; gasp edilmiş mülkleri hak sahiplerine iade et.", "Tarihi mülkiyet adaleti sağlandı; hukuk devleti güven tazeledi.",
     "Azınlık cemaati liderleri ve patrikhanelerle Çankaya'da istişare toplantıları yaparak karşılıklı güven tesis et.", "Azınlık vatandaşların devlete aidiyeti ve toplumsal huzur pekişti.",
     "İadesi mümkün olmayan kamuya geçmiş araziler için Hazine'den hakkaniyete uygun tazminat fonu kur.", "Mülkiyet bedelleri Hazine dengesi gözetilerek ödendi.",
     "Mülk iadelerinin Lozan dengesini bozduğu yönündeki milliyetçi kaygıları giderecek güvenlik şerhleri koy.", "Milli güvenlik hassasiyetleri tavizsiz korundu.",
     "'Vakıflar Kanunu Kapsamlı Reform Paketi' çıkararak tüm tarihi vakıf mallarını uluslararası mülkiyet hukukuna bağla.", "Vakıf hukuku modern standartlara ulaştırıldı; AİHM davaları düştü."),

    ("Yeni Türk Ceza Kanunu (TCK 5237) Reformu (2004-2005)", "Adalet Bakanlığı & TBMM", "char_adalet_bakani", "char_adli_yargi_hakimi",
     "79 yıllık 765 sayılı TCK yerine kişi hak ve hürriyetlerini merkeze alan çağdaş Türk Ceza Kanunu kabul edildi.",
     "Kanundaki işkence, cinsel saldırı ve çocuk istismarı cezalarını en üst sınıra çek; hakimleri yeni kanun için eğit.", "Modern ceza adaleti sistemi yürürlüğe girdi.",
     "Barolar, üniversiteler ve kadın dernekleriyle TBMM Adalet Komisyonu'nda tam uzlaşıyla maddeleri tek tek oyla.", "Geniş toplumsal mutabakatla tarihi ceza reformu tamamlandı.",
     "Yeni TCK'nın uygulanması için adliye binaları ve mahkeme salonlarının teknik altyapısını Hazine bütçesiyle yenile.", "Adli altyapı çağdaş standartlara kavuşturuldu.",
     "Kamu düzenine, devlete ve bayrağa karşı işlenen suçlarda caydırıcılığı artıran güvenlik maddelerini koru.", "Devletin anayasal düzeni çelik hükümlerle tahkim edildi.",
     "'Ceza Hukuku Uygulama ve Uyum Kanunu' çıkararak tüm özel kanunlardaki ceza hükümlerini yeni TCK ile uyumlu kıl.", "Mevzuat karmaşası giderildi; ceza hukukunda tam bütünlük sağlandı."),

    ("Yeni Ceza Muhakemesi Kanunu (CMK 5271) ve Çapraz Sorgu", "Adalet Bakanlığı", "char_adalet_bakani", "char_adli_yargi_hakimi",
     "1929 tarihli CMUK yürürlükten kaldırılarak savunma hakkını güçlendiren, delilden sanığa gitmeyi şart koşan modern CMK kabul edildi.",
     "Duruşmalarda çapraz sorgu ve sesli-görüntülü kayıt (SEGBİS) sistemini zorunlu kılarak yargılamayı şeffaflaştır.", "Savunma makamı güçlendi; adil yargılanma hakkı pekişti.",
     "Türkiye Barolar Birliği ile CMK avukatlık ücretleri ve zorunlu müdafilik sistemi konusunda protokol imzala.", "Avukatlar ve yargı mensupları arasında kurumsal uzlaşı sağlandı.",
     "Zorunlu müdafilik ücretlerinin düzenli ödenmesi için Adalet Bakanlığı bütçesine ek ödenek aktar.", "CMK avukatlarının hak edişleri Hazinece güvenceye alındı.",
     "Tutuklama ve arama kararlarında somut delil şartı getirirken organize suç örgütlerine karşı adli kolluğu güçlendir.", "Hukuk devleti ile suçla mücadele dengesi mükemmel kuruldu.",
     "'Adli Kolluk Teşkilatı Kanun Tasarısı' hazırlayarak adli polislerin savcılara doğrudan bağlı çalışmasını yasalaştır.", "Soruşturmaların bağımsızlığı için devrim niteliğinde adım atıldı."),

    ("Kabahatler Kanunu (5326) ve İdari Para Cezaları", "İçişleri Bakanlığı & Adalet", "char_icisleri_bakani", "char_adalet_bakani",
     "Adliyeleri boğan küçük suç ve kabahatlerin mahkemeler yerine idari yaptırımlara bağlanmasıyla yargının iş yükü hafifletildi.",
     "İdari para cezalarına karşı Sulh Ceza Hakimliklerine başvuru hakkını açık tut; keyfi cezaları yargı denetimine al.", "Vatandaşın hak arama hürriyeti korundu.",
     "Belediyeler ve valiliklerle ortak genelge yayınlayarak sokak nizamı ve gürültü cezalarında standart sağla.", "Yerel yönetimler ile merkezi idare arasında koordinasyon kuruldu.",
     "Toplanan idari para cezalarının doğrudan kamu bütçesine irad kaydedilerek Hazine gelirlerini artırmasını sağla.", "Hazineye düzenli ve kayda değer bir gelir kaynağı oluşturuldu.",
     "Çevreyi kirleten, kamu malına zarar veren ve sarhoşlukla huzur bozanlara karşı kolluk denetimlerini sıklaştır.", "Şehirlerde sokak huzuru ve kamu intizamı sağlandı.",
     "'İdari Ceza Hukuku ve Şehir Nizamı Kanunu' çıkararak kabahatler rejimini modern Avrupa metropolleri standardına getir.", "Şehir hayatında medeni nizam kalıcı kurallara bağlandı."),

    ("Bilgi Edinme Hakkı Kanunu (4982) ile Şeffaflık Çağı", "Başbakanlık", "char_basbakan", "char_adalet_bakani",
     "Vatandaşların kamu kurumlarındaki her türlü idari işlem ve belgeye erişimini sağlayan yasa ile bürokraside gizlilik dönemi kapandı.",
     "Devlet sırrı ve ticari sır kavramlarını dar yorumla; vatandaşın bilgi edinme başvurularını mahkeme korumasına al.", "Bürokraside şeffaflık sağlandı; vatandaşın denetim gücü arttı.",
     "Kamu Denetçiliği ve Bilgi Edinme Değerlendirme Kurulu (BEDK) ile kurumlar arası uzlaşı mekanizması kur.", "Başvurular süratle ve uyuşmazlığa düşmeden çözüldü.",
     "Tüm kamu kurumlarında elektronik bilgi edinme altyapısının kurulması için Hazine ödeneği sağla.", "Dijital şeffaflık altyapısı bütçelendirildi.",
     "Milli güvenliği, dış politikayı ve askeri istihbaratı ilgilendiren kritik belgelerin sızdırılmasını sert cezalarla önle.", "Devlet sırları ve milli güvenlik tavizsiz muhafaza edildi.",
     "'Açık Devlet ve Kamusal Şeffaflık Kanunu' çıkararak bilgi edinme hakkını doğrudan Anayasa'nın temel maddesi yap.", "Vatandaşın bilgi alma hakkı anayasal zirveye çıkarıldı."),

    ("Kamu İhale Kurumu (KİK) ve 4734 Sayılı İhale Devrimi", "Kamu İhale Kurumu & Maliye", "char_hazine_bakani", "char_tusiad_baskani",
     "Devlet ihalelerindeki yolsuzlukları önlemek amacıyla Dünya Bankası ve AB standartlarında özerk Kamu İhale Kurumu kuruldu.",
     "Tüm kamu ihalelerini Elektronik Kamu Alımları Platformu (EKAP) üzerinden şeffaf ve itiraza açık şekilde yürüt.", "İhalelerde kayırmacılık bitti; adil rekabet ortamı doğdu.",
     "İş dünyası, TOBB ve müteahhitler birliği ile istişare ederek yerli üreticiye %15 fiyat avantajı sağlayan uzlaşıyı koru.", "Yerli sanayici korundu; kamu ve özel sektör el sıkıştı.",
     "Açık eksiltme usulüyle kamu alımlarında devlet bütçesine milyarlarca liralık tasarruf sağla.", "Hazine kasasında rekor tasarruf sağlandı.",
     "İhalelere fesat karıştıran, sahte teminat mektubu veren şebekelere karşı mali polis operasyonlarını hızlandır.", "İhale mafyaları ve komisyoncu çeteler çökertildi.",
     "'Kamu Alımları ve Sözleşme Hukuku Temel Kanunu' çıkararak istisna maddelerini daralt ve denetimi Sayıştay'a bağla.", "Kamu harcamaları tavizsiz bir yasal zırha kavuşturuldu.")
]
domains.append(d1)

# Domain 2: Bankacılık Krizleri, Hortumlama ve TMSF Operasyonları (131-160)
d2 = [
    ("Demirbank Fonlama Krizi ve Hazine Müdahalesi", "Merkez Bankası & Hazine", "char_merkez_bankasi_baskani", "char_hazine_bakani",
     "Kasım 2000'de gecelik faizlerin fırlamasıyla Hazine bonosu portföyünü fonlayamayan Demirbank'ın batışı bankacılık sistemini kilitledi.",
     "Banka yönetimi ve portföy manipülasyonu iddiaları hakkında BDDK ve DGM Başsavcılığı soruşturması aç.", "Usulsüz işlemler yargıya taşındı; sorumlulardan hesap soruldu.",
     "Bankalar Birliği ile acil likidite zirvesi topla; kamu bankaları üzerinden gecelik fonlama kanallarını açık tut.", "Sistemik çöküş önlendi; piyasadaki panik havası dağıtıldı.",
     "Merkez Bankası döviz rezervlerini eritmeden bankayı TMSF'ye devret ve yabancı sermayeye satışını hızlandır.", "Hazineye ek maliyet yüklenmeden banka tasfiye edildi.",
     "Spekülatif faiz baskısı yapan piyasa aktörlerine ve dedikodu yayan finansörlere karşı SPK cezaları uygula.", "Piyasa disiplini korundu; kur manipülatörleri püskürtüldü.",
     "'Bankacılıkta Risk Yönetimi ve Likidite Standartları Kanunu' çıkararak bankaların bono taşıma limitlerini kanuna bağla.", "Bankacılık sisteminde yapısal risk sigortası kanunlaştı."),

    ("İmar Bankası Çifte Kayıt Skandalı ve Uzan Grubu Tasfiyesi", "BDDK & TMSF", "char_hazine_bakani", "char_adli_yargi_hakimi",
     "İmar Bankası'na el konulduğunda resmi kayıtların arkasında milyarlarca dolarlık kayıtdışı mevduat tutulduğu ortaya çıktı.",
     "Çifte muhasebe programı yazanlar ve banka yöneticileri hakkında nitelikli zimmetten derhal tutuklama kararı çıkart.", "Tarihin en büyük banka dolandırıcılığına yargı el koydu.",
     "Mağdur olan yüz binlerce küçük tasarruf sahibinin mevduatlarını devlet güvencesi kapsamında takvime bağlayarak öde.", "Toplumsal infial dindirildi; küçük mudi korundu.",
     "Uzan Grubu'na ait 219 şirkete, çimento fabrikalarına ve Telsim'e el koyarak kamu alacağını kuruşu kuruşuna tahsil et.", "Hazineye milyarlarca dolarlık rekor varlık kazandırıldı.",
     "Şirketlerin kaçırılan mallarını ve yurtdışı hesaplarını emniyet mali şube ve MASAK ekipleriyle tespit edip abluka altına al.", "Kaçırılan varlıklar devletin gücüyle geri alındı.",
     "'Finans Kurumlarında Çifte Kayıt ve Zimmet Suçları Kanunu' çıkararak bankacılıkta hileye müebbet hapis cezası getir.", "Bankacılık sistemi tam şeffaf dijital denetime bağlandı."),

    ("Türkbank İhalesi ve Çakıcı Kasetleri Skandalı", "Başbakanlık Teftiş Kurulu", "char_basbakan", "char_adalet_bakani",
     "Türk Ticaret Bankası'nın özelleştirme ihalesine mafya liderinin tehditle müdahale ettiğini gösteren telefon kasetleri hükümeti düşürdü.",
     "İhaleyi derhal iptal et; Başbakan, bakanlar ve organize suç örgütü elebaşı hakkında Yüce Divan soruşturması başlat.", "Hukuk önünde kimseye ayrıcalık tanınmadı; Yüce Divan süreci işletildi.",
     "TBMM Soruşturma Komisyonu kurarak siyasi aktörlerin şeffaf biçimde hesap vermesini sağla; meclis itibarını kurtar.", "Meclis kendi iç denetimini başarıyla çalıştırdı.",
     "Bankanın mevduat sahiplerine zarar gelmeden TMSF gözetiminde tasfiyesini ve Hazine kaynaklarının korunmasını sağla.", "Devlet hazinesine mafya eli uzanması engellendi.",
     "Organize suç örgütü lideri ve ihale aracılarının tüm mal varlıklarına el koy; kaçakları kırmızı bültenle yakalat.", "Devlet otoritesi suç örgütlerine karşı tavizsiz gösterildi.",
     "'Devlet İhalelerinde Şeffaflık ve Suç Örgütleriyle Mücadele Kanunu' çıkararak özelleştirmeleri tam yargı denetimine aç.", "Özelleştirme şaibelerine kalıcı yasal set çekildi."),

    ("Bank Ekspres ve Korkmaz Yiğit Soruşturması", "DGM & BDDK", "char_adli_yargi_hakimi", "char_hazine_bakani",
     "Bank Ekspres'in içini haksız kredi aktarımlarıyla boşalttığı belirlenen iş adamının DGM'de yargılanması finans dünyasında şok yarattı.",
     "Hileli kredilerle banka kaynaklarını kendi şirketlerine aktaran yöneticileri tutukla ve tedbir koy.", "Adalet yerini buldu; banka hortumcuları cezaevine gönderildi.",
     "İş dünyası temsilcileriyle görüşerek bankanın sağlıklı varlıklarının reel sektörü batırmadan devrini temin et.", "Reel sektördeki yüzlerce taşeronun batması önlendi.",
     "Hazine'nin üstlendiği mevduat yükünü iş adamının arsa, medya ve gayrimenkul varlıklarını satarak karşıla.", "Hazine zararı el konulan mülklerle tazmin edildi.",
     "Finansal manipülasyon ve tehdit iddialarına karşı emniyet istihbaratı devreye sokarak suç ağını çökert.", "Yasadışı finans bağlantıları kolluk gücüyle dağıtıldı.",
     "'Bankalar Arası Kredi Sınırları ve Çapraz Ortaklık Denetimi Kanunu' çıkararak patronların kendi bankasından kredi almasını yasakla.", "Patronların kendi bankasını soyması kanunen imkansız kılındı."),

    ("Yurtbank Tasfiyesi ve Ali Balkaner Dosyası", "TMSF & DGM", "char_hazine_bakani", "char_adli_yargi_hakimi",
     "Yurtbank'ın içi boşaltılarak off-shore hesaplar üzerinden paraların buharlaştırılması binlerce yurttaşı sokaklara döktü.",
     "Paravan off-shore şirketleri kurup mevduat kaçıran banka hakim ortağını ağır hapis ve mal varlığı müsaderesiyle yargıla.", "Hukukun kılıcı tavizsiz indi; zimmetçiler mahkum edildi.",
     "Yurtbank mağdurları derneğiyle masaya otur; ödemeleri zamana yayarak sosyal barışı koru.", "Mağdurların öfkesi dindirildi; devlet şefkatini gösterdi.",
     "Balkaner Grubu'na ait gayrimenkul ve lüks plazaları TMSF müzayedelerinde satıp geliri Hazineye aktar.", "El konulan lüks mülkler Hazineye nakit olarak döndü.",
     "Banka şubeleri önünde toplanan öfkeli kalabalıkların provokasyona gelmesini önlemek için kolluk tedbirlerini al.", "Şehir asayişi korundu; taşkınlıklar engellendi.",
     "'Off-Shore Bankacılık ve Kıyı Bankacılığı Yasaklama Kanunu' çıkararak yurt dışı paravan hesaplara devlet güvencesini kaldır.", "Kıyı bankacılığı hilelerine yasal kilit vuruldu."),

    ("Egebank ve 'Kasırga Operasyonu'", "DGM & Mali Şube", "char_adli_yargi_hakimi", "char_icisleri_bakani",
     "Murat Demirel'in sahibi olduğu Egebank'a gece yarısı düzenlenen Kasırga Operasyonu ile banka kasalarının boşaltıldığı belgelendi.",
     "Banka genel müdürlüğündeki gizli evrakları ve bilgisayar sunucularını kaçıran tüm failleri tutukla.", "Deliller kurtarıldı; organize banka soygunu yargıya taşındı.",
     "Bankalar Birliği ile istişare ederek mevduat panik dalgasının diğer özel bankalara sıçramasını engelle.", "Sistemik panik dalgası başarıyla kontrol edildi.",
     "Egebank kaynaklarından finanse edilen şirketlerin ve lüks yatların tamamına el koyup kamuya devret.", "Banka kaynakları geri alındı; kamu zararı azaltıldı.",
     "Kasırga operasyonunu genişlet; emniyet mali şube ve özel harekat timleriyle çetenin tüm hücrelerini bas.", "Devletin heybeti ve kararlılığı mali suçlulara hissettirildi.",
     "'Finansal Bilgi Sistemleri Güvenliği ve Bankacılık Ceza Reformu' çıkararak delil karartmayı en ağır suça bağla.", "Bankacılıkta dijital kayıtların silinmesi müebbet hapse bağlandı."),

    ("Pamukbank'ın Fona Devri ve Çukurova Grubu Borçları", "BDDK & Danıştay", "char_hazine_bakani", "char_anayasa_mahkemesi_baskani",
     "Sermaye yeterlilik rasyosu eksiye düşen Pamukbank'a BDDK tarafından el konulması, Turkcell ve Yapı Kredi hisseleri nedeniyle dev bir krize yol açtı.",
     "Danıştay ve idare mahkemesi kararlarını bekle; BDDK'nın el koyma işleminin hukuki meşruiyetini uluslararası bağımsız denetimle savun.", "BDDK kararının hukuka uygunluğu mahkemede tescillendi.",
     "Çukurova Grubu ile masaya otur; Türkiye'nin milli değeri Turkcell'in yabancıya gitmesini engelleyecek borç protokolü imzala.", "Devlet-özel sektör uzlaşısıyla kritik şirketler korundu.",
     "Grubun medya, telekomünikasyon ve sanayi gelirlerinden 5 milyar dolarlık tarihi kamu tahsilatını tamamla.", "Hazineye tek kalemde milyarlarca dolarlık tarihi nakit aktı.",
     "TMSF yönetimindeki bankaların şubelerinde ve fabrikalarında herhangi bir sabotaj veya varlık kaçırmaya izin verme.", "Kamu güvenliği ve fabrika çarkları korundu.",
     "'Sermaye Yeterliliği ve Finansal Holdingler Kanunu' çıkararak bankaların grup şirketlerine kredi aktarmasını tamamen yasakla.", "Holding bankacılığı kumpası yasal olarak bitirildi."),

    ("Bankacılık Düzenleme ve Denetleme Kurumu'nun (BDDK) Kurulması", "BDDK", "char_hazine_bakani", "char_merkez_bankasi_baskani",
     "Bankaların siyasetçilerin emrinden çıkarılıp bağımsız bir kurulla denetlenmesi amacıyla kurulan BDDK, Türk mali sisteminin miladı oldu.",
     "Kurulun kararlarını her türlü siyasi ve hükümet baskısından arındır; denetim raporlarını yargıya şeffaf ilet.", "Bağımsız mali denetim kurumsallaştı; bankacılığa güven geldi.",
     "TÜSİAD, TOBB ve Bankalar Birliği ile üçlü istişare kurulu kur; piyasa aktörlerinin uyum sürecini kolaylaştır.", "İş dünyası ve finans sektörü ortak akılda buluştu.",
     "BDDK'nın bütçesini bankalardan alınan bağımsız paylarla oluştur; Hazineye yük olmadan denetim gücünü artır.", "Hazine kasasına dokunulmadan dev bir denetim gücü kuruldu.",
     "Riskli ve açığı bulunan bankalara karşı şafak teftişleri düzenle; sermaye açığını kapatmayanlara anında el koy.", "Devletin mali otoritesi ve disiplini tavizsiz uygulandı.",
     "'Bağımsız İdari Otoriteler ve Bankacılık Kanunu' çıkararak BDDK üyelerinin görev güvencesini anayasal seviyeye çıkar.", "Kurul üyelerinin bağımsızlığı kanunla teminat altına alındı."),

    ("Kemal Derviş Reformları: 15 Günde 15 Kanun Paketi", "Ekonomi Bakanlığı & TBMM", "char_hazine_bakani", "char_basbakan",
     "Dünya Bankası'ndan çağrılan Kemal Derviş'in 'Güçlü Ekonomiye Geçiş Programı' kapsamında meclis gece gündüz çalışarak 15 temel reformu kabul etti.",
     "Şeker, tütün ve doğalgaz yasalarını Anayasa ve rekabet hukuku kurallarına tam uyumlu şekilde çıkar.", "Piyasa kuralları hukuki güvenceye kavuşturuldu.",
     "Koalisyon liderleri Ecevit, Bahçeli ve Yılmaz'ı aynı masada tutarak reformların meclisten firesiz geçmesini sağla.", "Koalisyon krizi aşıldı; reformlar mecliste kabul edildi.",
     "IMF ve Dünya Bankası'ndan 16 milyar dolarlık stand-by kredisi çekerek Hazine nakit açığını kapat ve borçları çevir.", "Hazine iflastan kurtuldu; döviz rezervleri takviye edildi.",
     "Sokaklara dökülen esnaf ve memur eylemlerine karşı polis gücüyle kamu düzenini ve Meclis çevresini koru.", "Meclis üzerindeki sokak baskısı kollukla engellendi.",
     "'Güçlü Ekonomi ve Yapısal Dönüşüm Çerçeve Kanunu' çıkararak KİT'lerin ve kamu bankalarının özerkliğini yasal kıl.", "Türk ekonomisinin omurgasını oluşturan tarihi dönüşüm yasalaştı."),

    ("Merkez Bankası Kanunu Reformu ve Fiyat İstikrarı", "TCMB", "char_merkez_bankasi_baskani", "char_hazine_bakani",
     "Nisan 2001'de kabul edilen 4651 sayılı kanunla Merkez Bankası'na Hazine'ye avans verme yasağı getirildi ve birincil amaç fiyat istikrarı oldu.",
     "Banka Başkanı ve Para Politikası Kurulu üyelerinin bağımsızlığını koru; faiz kararlarını hükümet telkiniyle alma.", "Merkez Bankası bağımsızlığı hukuken mühürlendi; enflasyon hedeflemesi başladı.",
     "Hazine ve Maliye Bakanlığı ile Para Politikası Kurulu arasında koordinasyonu sağlayan ortak protokoller imzala.", "Maliye ile para politikası arasında kusursuz ahenk kuruldu.",
     "Hazine'nin TCMB kasasından bedava para basıp bütçe açığı kapatmasını kanunen engelleyerek enflasyonu düşür.", "Karşılıksız para basma dönemi kapandı; Hazine disipline girdi.",
     "Döviz kurlarında spekülasyon yapan yerli-yabancı fonlara karşı piyasaya şok faiz ve likidite silahıyla yanıt ver.", "Merkez Bankası'nın piyasa üzerindeki kudreti gösterildi.",
     "'Merkez Bankası Bağımsızlığı ve Enflasyon Hedeflemesi Kanunu' çıkararak para basma yetkisini salt fiyat istikrarına bağla.", "Enflasyonla mücadelede tarihi kurumsal yasa tamamlandı."),

    ("Kamu İhale Kanunu (4734) ve AB Standartlarına Uyum", "TBMM & KİK", "char_hazine_bakani", "char_tbmm_baskani",
     "Kamudaki ihale yolsuzluklarını bitirmek amacıyla hazırlanan kanun, yabancı şirketlerin ve yerli sanayicinin katılım şartlarıyla tartışıldı.",
     "İhale şartnamelerini Sayıştay ve yargı denetimine aç; eşik değerlerin altındaki kaçamak ihaleleri iptal et.", "Kamuda şeffaflık ve hesap verilebilirlik sağlandı.",
     "İnşaat sektörü ve sanayi odalarıyla uzlaşarak yerli isteklilere %15'e varan fiyat avantajı tanıyan maddeyi koru.", "Yerli müteahhit ve üretici korunarak uzlaşı sağlandı.",
     "Tüm kamu kurumlarının mal ve hizmet alımlarında en düşük teklifi seçmesini sağlayarak Hazine bütçesini rahatlat.", "Hazine harcamalarında milyarlarca liralık tasarruf yapıldı.",
     "İhalelere fesat karıştıran müteahhitleri ve komisyoncuları derhal tüm kamu ihalelerinden men et.", "Kamu ihalelerindeki şaibeli firmalar sistemden temizlendi.",
     "'Kamu Alımları ve Saydamlık Kanunu'nu Avrupa Birliği İhale Direktiflerine tam uyumlu hale getir.", "Türkiye kamu ihale mevzuatında Avrupa standartlarını yakaladı."),

    ("Kamu Mali Yönetimi ve Kontrol Kanunu (5018)", "Maliye Bakanlığı & Sayıştay", "char_hazine_bakani", "char_basbakan",
     "Devlet harcamalarında hesap verilebilirliği, performans esaslı bütçelemeyi ve Sayıştay denetimini getiren 5018 sayılı kanun kabul edildi.",
     "Bakanlıkların örtülü ödenek ve yedek ödenek harcamalarını TBMM Plan ve Bütçe Komisyonu'nun denetimine bağla.", "Devlet harcamalarında tam hukuki şeffaflık sağlandı.",
     "Bütçe hazırlık sürecinde tüm bakanlıklar ve KİT'lerle 3 yıllık harcama tavanlarında uzlaşma sağla.", "Bürokrasi içinde planlı ve uyumlu bütçe dönemi başladı.",
     "Stratejik planı ve performans göstergesi olmayan kurumların harcama taleplerini Hazine adına doğrudan reddet.", "Bütçe açıkları rekor seviyede kontrol altına alındı.",
     "Usulsüz harcama yapan ve kamu zararına yol açan harcama yetkililerine karşı Sayıştay ilamlarını icraya koy.", "Devlet malını israf edenlere karşı mali otorite gösterildi.",
     "'Stratejik Planlama ve Performans Esaslı Bütçe Reformu' ile tüm kamu idarelerini modern mali yönetim sistemine bağla.", "Cumhuriyet tarihinin en kapsamlı mali anayasası yürürlüğe girdi."),

    ("TMSF'ye Devredilen 20 Özel Bankanın Tasfiyesi", "TMSF", "char_hazine_bakani", "char_adli_yargi_hakimi",
     "Batan 20 özel bankanın borçlarını temizlemek ve varlıklarını satmak amacıyla kurulan TMSF, Türkiye'nin en büyük holdingi haline geldi.",
     "Batan bankaların hakim ortakları hakkında açılan zimmet davalarını zaman aşımına uğratmadan sonuçlandır.", "Yargı süreci tavizsiz işletildi; hortumcular mahkum edildi.",
     "Bankaların borçlu müşterileriyle İstanbul Yaklaşımı çerçevesinde borç yapılandırma protokolleri imzala.", "Reel sektördeki yüzlerce fabrika kapanmaktan kurtarıldı.",
     "El konulan gayrimenkulleri, tabloları, yatları ve şirketleri canlı yayında açık artırmayla satıp Hazineye aktar.", "Hazineye milyarlarca liralık nakit tahsilat sağlandı.",
     "Borçlarını ödememek için mal kaçıran patronların villalarına ve gizli kasalarına polis eşliğinde el koy.", "Devletin gücü ve tahsilat iradesi hissettirildi.",
     "'Mali Sektöre Olan Borçların Yeniden Yapılandırılması Kanunu' (İstanbul Yaklaşımı) çıkararak sistemi yasalaştır.", "Finans ve sanayiyi kurtaran tarihi kanuni model oluşturuldu."),

    ("Banka Batıklarının Hazineye Maliyeti ve Özel Tertip Tahviller", "Hazine Müsteşarlığı", "char_hazine_bakani", "char_merkez_bankasi_baskani",
     "Krizde batan bankaların 40 milyar doları aşan maliyetini üstlenen Hazine, kamu bankalarına devasa tutarda Özel Tertip DİBS ihraç etti.",
     "Hazine'ye yüklenen bu dev borcun sorumluları hakkında Meclis Yolsuzlukları Araştırma Komisyonu raporu hazırla.", "Batan bankaların faturası meclis ve yargı önünde belgelendi.",
     "Kamu bankaları yönetimleriyle uzlaşarak görev zararlarını sıfırlayan bir yeniden yapılandırma planı hazırla.", "Halkbank ve Ziraat Bankası operasyonel karlılığa geçirildi.",
     "Hazine borç stoğunu eritmek için kamu arazilerinin satışını ve özelleştirme gelirlerini tahvil itfasına bağla.", "Hazine üzerindeki iç borç faiz yükü kademeli hafifletildi.",
     "Piyasalarda Hazine kağıtlarını speküle eden aracı kurumlara karşı Hazine Müsteşarlığı yetkilerini kullan.", "Borçlanma piyasalarında devlet otoritesi tesis edildi.",
     "'Kamu Borç Yönetiminin Düzenlenmesi Hakkında Kanun' (4749) çıkararak Hazine borçlanmasına yasal limitler getir.", "Hazine'nin keyfi borçlanması kanunla sınırlandırıldı."),

    ("Off-Shore Hesapzedelere Devlet Garantisi Tartışması", "Anayasa Mahkemesi & Hazine", "char_anayasa_mahkemesi_baskani", "char_hazine_bakani",
     "Yurt dışındaki paravan bankalara yüksek faiz tamahıyla para yatıranların devlet güvencesi talep etmesi büyük hukuki kriz yarattı.",
     "Yargıtay ve Anayasa Mahkemesi kararlarına dayanarak off-shore hesapların devlet güvencesi dışında olduğunu ilan et.", "Hukukun temel ilkesi korundu; devlet hileli faize kefil olmadı.",
     "Mağdurların temsilcileriyle görüş; banka hakim ortaklarından tahsil edilecek paradan sıra cetveline göre ödeme vaat et.", "Sokak eylemleri yatıştırıldı; mudilere umut verildi.",
     "Hazine kasasından off-shore hesaplara tek kuruş ödeme yapmayarak kamu bütçesini milyarlarca dolarlık yükten kurtar.", "Hazine bütçesi korunarak milletin parası kurtarıldı.",
     "Hazine müsteşarlığı ve BDDK binalarını basmak isteyen öfkeli hesapzede gruplarını polis kordonuyla durdur.", "Kamu kurumlarının güvenliği tavizsiz sağlandı.",
     "'Tasarruf Mevduatı Sigortası Kapsamı ve Limitleri Kanunu' çıkararak hangi hesapların sigortalı olduğunu kanunla mühürle.", "Mevduat güvencesi sınırları netleştirildi; spekülatif faizcilik bitti."),

    ("Beyaz Enerji Operasyonu: TEAŞ ve TEDAŞ İhaleleri", "DGM & Jandarma", "char_adli_yargi_hakimi", "char_icisleri_bakani",
     "Enerji santralleri ve iletim hatları ihalelerinde bürokratlar ve bakanların rüşvet çarkı kurduğu iddiasıyla DGM operasyonu başlatıldı.",
     "Enerji Bakanlığı bürokratlarını, TEAŞ genel müdürünü ve müteahhitleri DGM'de tutuklu yargıla.", "Enerji sektöründeki dev rüşvet çarkı adaletle dağıtıldı.",
     "Soruşturmanın enerji arzını kesintiye uğratmaması için teknik personelle geçici kriz masası oluştur.", "Şehirlerin elektriksiz kalması önlendi; üretim aksamadı.",
     "Yolsuzlukla şişirilen enerji sözleşmelerini tek taraflı feshederek kamuyu trilyonlarca liralık zarardan kurtar.", "Hazineye yüklenen fahiş enerji taahhütleri iptal edildi.",
     "Jandarma Kaçakçılık Şubesi marifetiyle şüphelilerin ev ve ofislerindeki gizli kasalara ve kasetlere el koy.", "Deliller eksiksiz toplandı; devletin gücü gösterildi.",
     "'Enerji Piyasası Düzenleme Kurumu (EPDK) Kuruluş Kanunu' (4628) çıkararak ihaleleri bakanlıktan alıp özerk kurula devret.", "Enerji piyasası şeffaf ve rekabetçi piyasa kanununa bağlandı."),

    ("Mavi Hat Operasyonu: BOTAŞ Doğalgaz Rüşvet İddiaları", "Ankara Cumhuriyet Başsavcılığı", "char_adli_yargi_hakimi", "char_enerji_bakani" if "char_enerji_bakani" in char_map else "char_sanayi_bakani",
     "BOTAŞ doğalgaz boru hatları ve kompresör istasyonu ihalelerinde rüşvet ve haksız kazanç sağlandığı iddiasıyla dev operasyon düzenlendi.",
     "Rüşvet aldığı teknik takiple belgelenen genel müdür yardımcılarını ve ihale komisyonu üyelerini cezaevine yolla.", "Yargı kamu ihalelerindeki yolsuzluğa neşter vurdu.",
     "Gaz sevkiyatı yapan uluslararası enerji devleriyle görüşerek sevkiyat sözleşmelerinin hukuki devamını sağla.", "Doğalgaz arz güvenliği diplomasiyle korundu.",
     "Rüşvet paralarının aktarıldığı paravan şirket hesaplarına bloke koyarak meblağı Hazineye irad kaydet.", "Kamu zararı sorumlulardan faiziyle tahsil edildi.",
     "Organize rüşvet şebekesinin kaçmaya çalışan kilit isimlerini sınırlarda polis operasyonuyla ele geçir.", "Kaçak bürokratlar yakalandı; devletten kaçılamayacağı gösterildi.",
     "'Doğalgaz Piyasası Kanunu ve İhale Şeffaflığı Reformu' hazırlayarak BOTAŞ'ın tekel alımlarını bağımsız denetime bağla.", "BOTAŞ ihaleleri kalıcı şeffaf yasal denetime kavuşturuldu."),

    ("Balina Operasyonu: İzmir Gümrüklerinde Hayali İhracat", "Maliye Bakanlığı & Emniyet", "char_hazine_bakani", "char_icisleri_bakani",
     "İzmir ve Ege gümrüklerinden taş ve kum yüklü konteynerleri tekstil ürünü gibi gösterip milyarlarca liralık KDV iadesi alan şebeke çökertildi.",
     "Hayali ihracatçıları ve onlara rüşvetle göz yuman gümrük muhafaza müdürlerini Ağır Ceza Mahkemesi'nde yargıla.", "Gümrüklerdeki kaçakçılık çetesine ağır hapis cezaları verildi.",
     "İhracatçı birlikleriyle ortak toplantı yaparak dürüst ihracatçıların KDV iadelerinin gecikmesini önle.", "Dürüst üreticinin mağduriyeti engellendi.",
     "Hayali ihracatla haksız alınan tüm KDV iadelerini faiziyle geri tahsil edip Hazine kasasını takviye et.", "Hazineye yüz milyonlarca liralık vergi geliri geri kazandırıldı.",
     "Gümrük kapılarına dedektif timleri yerleştir; tüm konteynerleri X-Ray ve fiziki kontrolden geçir.", "Gümrük kapılarında devletin çelik disiplini kuruldu.",
     "'Gümrük Kanunu ve Kaçakçılıkla Mücadele Kanunu' (5607) reformu yaparak hayali ihracata en ağır cezaları yasalaştır.", "Hayali ihracat defteri Türk hukukunda kalıcı olarak kapatıldı."),

    ("Paraşüt Operasyonu: Sahte Fatura ve Naylon İhracat", "İçişleri Bakanlığı & MASAK", "char_icisleri_bakani", "char_hazine_bakani",
     "Gaziantep, Şanlıurfa ve İstanbul üçgeninde kurulan yüzlerce tabela şirketi üzerinden trilyonlarca liralık naylon fatura kesildiği ortaya çıkarıldı.",
     "Naylon fatura basan matbaaları ve şebeke liderlerini MASAK mali raporlarıyla mahkemeye sevk et.", "Vergi kaçakçıları yargı önünde hesap verdi.",
     "Güneydoğu Anadolu İhracatçı Birlikleri ile görüşerek bölge ticaretinin bu operasyondan zarar görmesini engelle.", "Bölge ticareti ve istihdam korundu.",
     "Şebekenin banka hesaplarındaki milyonlarca dolarlık kara parayı ve gayrimenkulleri Hazineye aktar.", "Büyük bir kara para hacmi Hazineye irad kaydedildi.",
     "Emniyet Kaçakçılık ve Organize Suçlarla Mücadele (KOM) dairelerini devreye sokup 10 ilde eşzamanlı şafak baskını yap.", "Organize mali suç çetesi tek gecede çökertildi.",
     "'Vergi Usul Kanunu Reformu ve Sahte Belgeyle Mücadele Yasası' çıkararak e-fatura sisteminin temellerini at.", "Elektronik vergi denetiminin temelleri kanunlaştı."),

    ("Örümcek Ağı Operasyonu: Naylon Fatura Baronları", "Ankara DGM & KOM", "char_adli_yargi_hakimi", "char_icisleri_bakani",
     "Devleti hayali ihracat ve sahte faturalarla soyan iş adamı Erol Maks Kohen ve suç ortaklarına yönelik cumhuriyet tarihinin en büyük mali operasyonu yapıldı.",
     "DGM Başsavcılığı koordinesinde delilleri topla; çıkar amaçlı suç örgütü kapsamında tüm sanıkları tutuklat.", "Suç örgütü liderleri adalet karşısında diz çöktü.",
     "Tekstil ve hazır giyim sektöründeki masum tedarikçilerin hesaplarının bloke edilmesini önleyecek ayrımı yap.", "Reel sektördeki zincirleme iflasların önüne geçildi.",
     "Şebekenin off-shore hesaplara kaçırdığı dövizleri İsviçre ve Lüksemburg adli yardımlaşmasıyla Hazineye getirt.", "Uluslararası kara para operasyonuyla kamu zararı karşılandı.",
     "KOM ve jandarma ekipleriyle zanlıların lüks villalarındaki çelik kasaları balyozlarla açıp kayıtları ele geçir.", "Devletin kolluk gücü mali baronların inine girdi.",
     "'Çıkar Amaçlı Suç Örgütleriyle Mücadele Kanunu' (4422) kapsamında mali suçları organize terör suçuyla eşdeğer kıl.", "Mali organize suçlar ilk kez en ağır ceza kapsamına alındı."),

    ("Vurgun Operasyonu: Bayındırlık Bakanlığı İhale Şebekesi", "Ankara DGM & Emniyet", "char_adli_yargi_hakimi", "char_basbakan",
     "Deprem konutları ve kamu binaları ihalelerinde bakanlık müsteşarından müteahhitlere kadar uzanan rüşvet ve komisyon ağı deşifre edildi.",
     "Bayındırlık Bakanlığı Müsteşarını, genel müdürleri ve ihale komisyonu üyelerini DGM kararıyla tutuklat.", "Yolsuzluk yapan üst düzey bürokrasiye yargı tokadı indi.",
     "Hükümet içinde acil inceleme başlat; soruşturmanın selameti için ilgili bakanın istifasını iste.", "Hükümetin siyasi ahlak ve şeffaflık duruşu sergilendi.",
     "Rüşvetle dağıtılan deprem konutları ihalelerini derhal feshet; teminat mektuplarını nakde çevirerek Hazineye al.", "Kamu kaynakları korundu; şaibeli ihaleler iptal edildi.",
     "Deprem bölgesinde eksik veya çürük malzeme kullanan müteahhitlerin şantiyelerine polis eşliğinde el koy.", "Çürük inşaat şebekeleri şantiyeden kovuldu.",
     "'Kamu Görevlileri Mal Bildirimi ve Yolsuzlukla Mücadele Kanunu' (3628) reformu ile haksız mal edinenin malını müsadere et.", "Bürokraside mal bildirimleri tam adli denetime bağlandı."),

    ("Bumerang Operasyonu: Hazine Teşviklerinin Suistimali", "Hazine Müsteşarlığı & DGM", "char_hazine_bakani", "char_adli_yargi_hakimi",
     "Yatırım teşviki alarak fabrikalar kuracağını taahhüt edip teşvik kredilerini faizde ve borsada değerlendiren şirketler ağı çökertildi.",
     "Yatırım teşviklerini amacı dışında kullanan şirket yöneticileri hakkında nitelikli dolandırıcılık davası aç.", "Hazine teşviklerini yağmalayanlar yargı önüne çıkarıldı.",
     "Sanayi Odaları ile görüş; gerçek yatırımcıları koruyacak yeni bir teşvik izleme komisyonu kur.", "Gerçek sanayici desteklendi; istihdam projeleri korundu.",
     "Kullanılan milyarlarca liralık teşvik kredilerini fahiş temerrüt faiziyle geri tahsil ederek Hazine kasasına koy.", "Hazine kaynakları faiziyle geri alındı.",
     "Sahte istihdam ve hayali fabrika gösteren paravan tesisleri polis ve maliye müfettişleriyle mühürle.", "Kağıt üzerindeki hayali fabrikalar mühürlendi.",
     "'Yatırımların Teşviki ve Kamu Desteklerinin İzlenmesi Kanunu' çıkararak her teşviki uydu ve saha teftişine bağla.", "Teşvik sisteminde suiistimalleri bitiren kurumsal reform yapıldı."),

    ("Kentbank ve Sümerbank Tasfiye Süreçleri", "TMSF & BDDK", "char_hazine_bakani", "char_tusiad_baskani",
     "Tarihi Sümerbank ve Süzer Grubu'na ait Kentbank'ın fona devredilmesi ve ardından açılan iptal davaları finans dünyasında uzun soluklu bir hukuk savaşı başlattı.",
     "Danıştay ve AİHM kararlarını hukuki titizlikle incele; mülkiyet haklarını koruyan tarafsız bir tasfiye yürüt.", "Hukuki meşruiyet sağlandı; uluslararası davalar kazanıldı.",
     "Banka sahipleriyle sulh masasına otur; uzun vadeli geri ödeme protokolü imzalayarak banka alacaklarını tahsil et.", "Sulh yoluyla devlet alacakları tahsil edildi.",
     "Bankalara ait tarihi binaları, müzeleri ve sanat eserlerini kamuya kazandırıp Hazine varlıklarını artır.", "Kültürel varlıklar ve binalar Hazine mülkiyetine geçti.",
     "Tasfiye edilen şubelerdeki bankacılık kayıtlarını koruma altına al; herhangi bir evrak imhasına geçit verme.", "Kayıtlar korundu; kamu otoritesi eksiksiz hissettirildi.",
     "'Banka Tasfiyeleri ve Fon Alacaklarının Tahsili Hakkında Kanun' çıkararak TMSF'ye olağanüstü haciz yetkisi ver.", "TMSF'nin tahsilat gücü kanunla tahkim edildi."),

    ("İktisat Bankası ve Erol Aksoy Borç Protokolü", "TMSF", "char_hazine_bakani", "char_adli_yargi_hakimi",
     "Krizde batan İktisat Bankası'nın hakim ortağının medya organları (Cine5, Show TV hisseleri) ve gayrimenkulleri TMSF tarafından haczedildi.",
     "Banka kaynaklarının grup şirketlerine haksız aktarılması dosyasını ceza mahkemesinde karara bağlat.", "Banka patronuna hapis cezası verildi; adalet tecelli etti.",
     "Borçlu iş adamıyla kamu alacağını azami düzeyde tahsil edecek taksitli bir geri ödeme anlaşması yap.", "Finansal uzlaşıyla kamu alacağı güvenceye bağlandı.",
     "El konulan Cine5 televizyonu ve kablo yayın haklarını ihaleyle satarak elde edilen geliri Hazineye aktar.", "Medya varlıkları satılarak Hazineye milyonlarca dolar aktı.",
     "Hacizli şirket merkezlerine polis ve icra memurlarıyla girerek kaçırılmak istenen sanat koleksiyonlarına el koy.", "Paha biçilmez sanat eserleri devlet korumasına alındı.",
     "'Bankacılık Kanununa Ek Fon Alacaklarının Takip Usulü Maddesi' çıkararak borçlu patronların yurtdışı çıkışını yasakla.", "Borçlu patronların yurtdışına kaçması yasal olarak engellendi."),

    ("Yaşarbank ve DYO Grubu Borç Yapılandırması", "TMSF & Sanayi Bakanlığı", "char_hazine_bakani", "char_sanayi_bakani",
     "İzmir merkezli Yaşarbank'ın batışı sonrası gıda ve boya devi Yaşar Holding'in üretimi durma noktasına geldi; işçiler eyleme başladı.",
     "Banka yönetimindeki usulsüz işlemlerle holding üretim tesislerini birbirinden hukuken ayır.", "Üretim tesisleri korunurken suçlular yargıya sevk edildi.",
     "Holding yönetimiyle 10 yıllık borç geri ödeme protokolü imzala; binlerce işçinin çalıştığı fabrikaların çarklarını döndür.", "İzmir sanayisi ve binlerce işçinin ekmeği kurtarıldı.",
     "Banka borçlarını tahsil etmek için holdingin bankacılık dışı gayrimenkullerini Hazineye teminat ipoteği koy.", "Kamu alacağı sağlam ipoteklerle güvenceye alındı.",
     "Fabrikalarda üretimin durmasını ve provokasyonları önlemek için işçi sendikalarıyla koordineli kolluk önlemi al.", "Üretim tesislerinde sükunet ve asayiş sağlandı.",
     "'Reel Sektörün Korunması ve Finansal Yeniden Yapılandırma Kanunu' hazırlayarak fabrika batıran banka krizlerine son ver.", "Sanayi devlerinin banka batığı yüzünden çökmesi kanunla önlendi."),

    ("Toprakbank ve Halis Toprak Gayrimenkul Satışları", "TMSF", "char_hazine_bakani", "char_adli_yargi_hakimi",
     "Halis Toprak'ın sahibi olduğu Toprakbank'ın fona devrinin ardından Boğaz'daki ünlü Aslanlı Köşk ve sanayi tesisleri TMSF tarafından satışa çıkarıldı.",
     "Zimmet ve usulsüz kredi davalarını bağımsız mahkemede hızlandır; yargı kararlarını gecikmeksizin icra et.", "Hukukun kararı şartsız uygulandı.",
     "Sanayici ailenin teklif ettiği geri ödeme planını müzakere et; fabrikaların üretimini aksatmayacak formül üret.", "Bilecik ve Bozüyük'teki seramik fabrikaları üretime devam etti.",
     "Aslanlı Köşk'ü rekor bedelle açık artırmada satıp elde edilen yüz milyonlarca lirayı Hazineye aktar.", "Boğaz'ın lüks köşkü satılarak Hazine kasası dolduruldu.",
     "Haciz sırasında köşk kapılarını kilitleyip polise direnen görevlilere karşı devletin kolluk gücünü kararlılıkla uygula.", "Devletin haciz memuruna direnilmeyeceği gösterildi.",
     "'TMSF Varlıklarının Satışı ve Cebri İcra Kanunu' çıkararak borçluların yargıyı oyalama taktiklerine kanuni set çek.", "Kamu alacaklarının tahsilinde yargısal gecikmeler kanunla bitirildi."),

    ("Gelir İdaresi Başkanlığı'nın (GİB) Yeniden Yapılanması (2005)", "Maliye Bakanlığı", "char_hazine_bakani", "char_esnaf_odasi_baskani",
     "Maliye Bakanlığı bünyesindeki Gelirler Genel Müdürlüğü lağvedilerek yarı-özerk, modern ve dijital Gelir İdaresi Başkanlığı kuruldu.",
     "Mükellef hakları bildirgesi yayınla; vergi denetimlerinde keyfiyeti önleyip adil yargılanma ve itiraz hakkı getir.", "Mükellef hakları güvenceye alındı; vergi adaleti sağlandı.",
     "TOBB, TESK ve esnaf odalarıyla vergi barışı ve beyanname kolaylıkları konusunda ortak protokoller yap.", "Vergi dairesi ile esnaf arasındaki husumet uzlaşıya dönüştü.",
     "Vergi tabanını genişlet; kayıtdışı ekonomiyi dijital takip sistemleriyle yakalayarak Hazine gelirlerini ikiye katla.", "Vergi gelirleri rekor kırdı; bütçe açıkları kapandı.",
     "Sahte fiş kesen, vergi kaçıran lüks işletmelere karşı maliye müfettişleriyle gece denetimlerini aralıksız sürdür.", "Vergi kaçakçılarına karşı devletin kudreti hissettirildi.",
     "'Gelir İdaresi Başkanlığı Teşkilat ve Görevleri Hakkında Kanun' (5345) çıkararak vergi toplamada devrim yap.", "Türk vergi sistemi çağdaş kurumsal bir anayasaya kavuştu."),

    ("Vergi Barışı Kanunları ve Varlık Barışı Uygulamaları", "Maliye Bakanlığı & TBMM", "char_hazine_bakani", "char_tusiad_baskani",
     "Ekonomideki kayıtdışı sermayeyi sisteme çekmek ve yargıdaki milyonlarca vergi ihtilafını temizlemek için tarihi vergi barışları ilan edildi.",
     "Vergi davalarındaki yargı yükünü hafiflet; ihtilaflı vergi cezalarında uzlaşma komisyonlarının tarafsızlığını koru.", "Yargının üzerindeki milyonlarca vergi davası yükü kalktı.",
     "İş dünyası ve esnafa taksitli ödeme kolaylığı sunarak milyonlarca vatandaşın devletle helalleşmesini sağla.", "Geniş bir toplumsal mutabakat ve mali barış sağlandı.",
     "Yurt dışındaki ve yastık altındaki milyarlarca dolarlık döviz ve altını sıfıra yakın vergiyle Hazineye çek.", "Ülkeye on milyarlarca dolarlık taze sermaye girişi sağlandı.",
     "Vergi barışını fırsat bilip kara para aklamaya çalışan suç örgütlerine karşı MASAK filtrelerini tavizsiz işlet.", "Kara para aklayıcılarının barıştan yararlanması engellendi.",
     "'Vergi ve Diğer Bazı Alacakların Yeniden Yapılandırılması Kanunu' çıkararak af yerine düzenli yapılandırma kuralları koy.", "Maliye tarihinde kalıcı bir vergi barışı sistemi kanunlaştı."),

    ("KEY (Konut Edindirme Yardımı) Hak Sahiplerine İadesi", "Emlak Konut & Hazine", "char_hazine_bakani", "char_tuketici_dernekleri_baskani",
     "Yıllarca memur ve işçilerin maaşlarından kesilen fakat unutulan KEY paraları, 8.5 milyon hak sahibine nakit olarak iade edildi.",
     "Hak sahipliği listelerini TC kimlik numaralarıyla eşleştir; hatalı veya eksik kayıtları yargı kararıyla düzelt.", "Hak sahiplerinin alın teri kuruşu kuruşuna tespit edildi.",
     "Sendikalar ve tüketici dernekleriyle Ziraat Bankası şubelerinde izdihamı önleyecek randevu takviminde uzlaş.", "Milyonlarca vatandaş bankalardan parasını huzurla aldı.",
     "8.5 milyon vatandaşa ödenecek milyarlarca liralık nakdi Hazine nakit akışını bozmadan Emlak GYO hisseleriyle finanse et.", "Hazine dengesi bozulmadan dev bir sosyal ödeme tamamlandı.",
     "Bankalarda KEY kuyruklarında fırsatçılık yapmak isteyen dolandırıcılara karşı emniyet tedbirlerini artır.", "Vatandaşın birikimi dolandırıcılara karşı korundu.",
     "'Konut Edindirme Yardımı Hak Sahiplerine Ödeme Yapılması Kanunu' (5664) çıkararak tarihi borcu kanunla kapat.", "Devletin vatandaşına olan 20 yıllık borcu kanunla ödendi."),

    ("Zorunlu Tasarruf Fonu (NEMA) Kesintilerinin Tasfiyesi", "Hazine Müsteşarlığı & TBMM", "char_hazine_bakani", "char_esnaf_odasi_baskani",
     "Çalışanların maaşlarından 1988'den beri kesilen 'Çalışanları Tasarrufa Teşvik Fonu' lağvedilerek biriken nemalar hak sahiplerine ödendi.",
     "Nemaların hesaplanmasında enflasyon farkı ve yasal faizi tam işleterek yargı yoluna giden mağdurların hakkını ver.", "Kul hakkı ve çalışan emeği adaletle korundu.",
     "İşçi ve memur konfederasyonları (Türk-İş, Hak-İş, KESK) ile ödeme takviminde tam uzlaşı sağla.", "Sosyal diyalog ile çalışma barışı zirveye taşındı.",
     "Nemaların ödenmesi için kamu bütçesinden ayrılan trilyonluk kaynağı iç borçlanmayı artırmadan bütçele.", "Mali disiplin sarsılmadan tarihi ödeme gerçekleştirildi.",
     "Ödeme günlerinde kamu bankaları önünde oluşabilecek kargaşayı kolluk kuvvetleriyle intizama bağla.", "Şehirlerde kamu intizamı ve ödeme huzuru sağlandı.",
     "'Çalışanların Tasarruflarının Tasfiyesi ve Nemalarının Ödenmesi Kanunu' (4853) çıkararak zorunlu fonu tarihe göm.", "Maaşlardan zorla fon kesintisi yapma dönemi kanunla bitirildi.")
]
domains.append(d2)

print(f"Part 1 has {len(domains)} domains initialized so far...")
