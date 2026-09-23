# -*- coding: utf-8 -*-
"""
Generates Part 1 Events (tr_vaka_101 to tr_vaka_400 = 300 Events)
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

def make_event(id_num, title, source, char1, char2, desc,
               opt1_lbl, opt1_log,
               opt2_lbl, opt2_log,
               opt3_lbl, opt3_log,
               opt4_lbl, opt4_log,
               opt5_lbl, opt5_log,
               e1=(8, 7, -2, 0, -2), e2=(-7, 8, -2, 0, 7), e3=(-2, -7, 8, 0, 3), e4=(-3, -8, 0, 8, 7), e5=(8, 3, -7, 0, 7)):
    
    eff1 = {'justice': e1[0], 'people': e1[1], 'treasury': e1[2], 'military': e1[3], 'authority': e1[4]}
    eff2 = {'justice': e2[0], 'people': e2[1], 'treasury': e2[2], 'military': e2[3], 'authority': e2[4]}
    eff3 = {'justice': e3[0], 'people': e3[1], 'treasury': e3[2], 'military': e3[3], 'authority': e3[4]}
    eff4 = {'justice': e4[0], 'people': e4[1], 'treasury': e4[2], 'military': e4[3], 'authority': e4[4]}
    eff5 = {'justice': e5[0], 'people': e5[1], 'treasury': e5[2], 'military': e5[3], 'authority': e5[4]}

    c1_name = char_map.get(char1, "Devlet Temsilcisi")
    c2_name = char_map.get(char2, "Bürokrasi Temsilcisi")

    options = [
        {'label': opt1_lbl, 'preview': format_preview(eff1), 'effects': eff1, 'log': opt1_log},
        {'label': opt2_lbl, 'preview': format_preview(eff2), 'effects': eff2, 'log': opt2_log},
        {'label': opt3_lbl, 'preview': format_preview(eff3), 'effects': eff3, 'log': opt3_log},
        {'label': opt4_lbl, 'preview': format_preview(eff4), 'effects': eff4, 'log': opt4_log},
        {'label': opt5_lbl, 'preview': format_preview(eff5), 'effects': eff5, 'log': opt5_log}
    ]

    return {
        'id': f'tr_vaka_{id_num:03d}' if id_num < 1000 else f'tr_vaka_{id_num}',
        'characters': [
            {'id': char1, 'name': c1_name},
            {'id': char2, 'name': c2_name}
        ],
        'source': source,
        'title': title,
        'desc': desc,
        'options': options
    }

raw_data = []

# Block 1: 1990'lar Koalisyonlar ve Siyasi Krizler (101-130)
b1 = [
    ("Refahyol Hükümeti Protokolü ve Güvenoyu Çalkantısı", "TBMM & Başbakanlık", "char_basbakan", "char_milletvekili",
     "54. Hükümetin kurulması sürecinde partiler arası protokol pazarlıkları ve güvenoyu oylaması meclis kulislerinde büyük gerilim yarattı.",
     "Milletvekili transferi iddialarına karşı Meclis Araştırması aç ve süreci yargıya sevk et.", "Hukuki süreç işletildi, siyaset üzerindeki şaibeler dağıtıldı.",
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
     "'Yurtdışı Askeri Misyonların Korunması ve Dokunulmazlık Protokolü' çıkararak sınır ötesi timlerin statüsünü yasal güvenceye al.", "Yurtdışı askeri birliklerimizin statüsü uluslararası protokole bağlandı.")
]

for item in b1:
    raw_data.append(item)

print(f"Block 1 appended. Total raw: {len(raw_data)}")
