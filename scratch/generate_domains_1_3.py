import json
from deck_utils import load_modern_deck, save_modern_deck, apply_options_to_deck

# Domain 1: 1990'lar Koalisyonlar ve Siyasi Krizler (tr_vaka_101 - tr_vaka_130)
# Domain 2: Bankacılık Krizleri ve TMSF Operasyonları (tr_vaka_131 - tr_vaka_160)
# Domain 3: 2002-2007 Erken Seçimler ve AB Uyum (tr_vaka_161 - tr_vaka_190)

D1 = {
    "tr_vaka_101": [
        {"label": "Milletvekili transferi iddialarını Meclis Araştırma Komisyonu ve Yargıtay Başsavcılığı'na sevk ederek şeffaf adli inceleme başlat.",
         "effects": {"justice": 8, "people": 6, "treasury": -2, "military": 0, "authority": -3},
         "log": "Transfer iddiaları yargıya intikal etti; siyasi ahlak tartışmaları mecliste gerilimi tırmandırdı."},
        {"label": "Koalisyon protokolündeki Başbakanlık dönüşümü (rotasyon) takvimine sadık kal; ortaklar arasında güven tazeleyerek hükümeti kur.",
         "effects": {"justice": -7, "people": 8, "treasury": -3, "military": 0, "authority": 7},
         "log": "Hükümet güvenoyu aldı; koalisyon ortakları rahatladı ancak siyasi pazarlık iddiaları kamuoyunda eleştirildi."},
        {"label": "Koalisyon ortaklarının talep ettiği ek bakanlık ve örtülü ödenek bütçelerini Hazine dengelerini korumak adına sınırla.",
         "effects": {"justice": -2, "people": -7, "treasury": 8, "military": 0, "authority": 3},
         "log": "Bütçe disiplini sağlandı; gereksiz bürokratik harcamalar önlendi fakat ortaklar arasında huzursuzluk çıktı."},
        {"label": "Genelkurmay ve Milli Güvenlik Kurulu'nun hükümet protokolüne dönük hassasiyetlerini doğrudan Başbakanlık üzerinden müzakere et.",
         "effects": {"justice": -4, "people": -7, "treasury": 0, "military": 8, "authority": 8},
         "log": "Askeri kanadın çekinceleri kayıt altına alındı; devlet içi dengeler muhafaza edildi."},
        {"label": "Siyasi Partiler Kanunu'nda ve Meclis İçtüzüğü'nde parti transferlerini zorlaştıran 'Siyasi Ahlak ve Disiplin Reformu' çıkar.",
         "effects": {"justice": 8, "people": 3, "treasury": -7, "military": 0, "authority": 7},
         "log": "Meclis iradesini bağlayan reform yasalaştı; transfer borsasının önü kurumsal olarak kesildi."}
    ],
    "tr_vaka_102": [
        {"label": "Susurluk kazası sonrası hazırlanan Kutlu Savaş ve MİT raporlarını sansürsüz biçimde Meclis'e ve kamuoyuna açıkla.",
         "effects": {"justice": 9, "people": 8, "treasury": -2, "military": 0, "authority": -4},
         "log": "Raporlar şeffaflıkla paylaşıldı; temiz toplum talebi halk nezdinde devlete olan inancı tazeledi."},
        {"label": "Eylemleri organize eden sivil inisiyatifler ve barolarla görüşerek taleplerini dinle; gerilimi sokağa taşmadan uzlaşıyla yönet.",
         "effects": {"justice": -6, "people": 9, "treasury": -2, "military": 0, "authority": 6},
         "log": "Sivil toplum temsilcileri muhatap alındı; kitleler teskin edildi fakat radikal kesimler somut tutuklama istedi."},
        {"label": "Mafya-siyaset ilişkilerinde adı geçen paravan şirketlerin banka hesaplarına Maliye ve MASAK eliyle derhal bloke koy.",
         "effects": {"justice": -1, "people": -6, "treasury": 9, "military": 0, "authority": 4},
         "log": "Karanlık ilişkiler ağının mali kaynaklarına el konuldu; Hazineye önemli gelir aktarıldı."},
        {"label": "Işık kapatma eylemlerinin kamu düzenini bozmasına izin verme; sokak gösterilerine karşı kolluk devriyelerini artır.",
         "effects": {"justice": -5, "people": -9, "treasury": 0, "military": 9, "authority": 9},
         "log": "Kamu düzeni sıkı şekilde korundu; gösterilerin kitlesel itaatsizliğe dönüşmesi engellendi ancak tepkiler arttı."},
        {"label": "Devlet Denetleme Kurulu ve Meclis Araştırma Komisyonu raporlarına dayanan 'Organize Suçlar ve Çeteleşmeyle Mücadele Kanunu' çıkar.",
         "effects": {"justice": 8, "people": 4, "treasury": -7, "military": 0, "authority": 7},
         "log": "Yasal çerçeve tahkim edildi; devlet görevlilerinin suç örgütleriyle irtibatı en ağır yaptırımlara bağlandı."}
    ],
    "tr_vaka_103": [
        {"label": "Anayasal parlamenter meşruiyete sarıl; 18 maddelik MGK bildirisini TBMM Genel Kurulu'na getirip güvenoyuna sun.",
         "effects": {"justice": 8, "people": 7, "treasury": -2, "military": 0, "authority": -3},
         "log": "Hükümet meclis zemininde direndi; sivil siyasetin meşruiyeti savunuldu fakat askeri kanatla gerilim tırmandı."},
        {"label": "MGK Genel Sekreterliği ile uzlaşma masası kur; 8 yıllık kesintisiz eğitim gibi kritik maddeleri zamana yayarak tansiyonu düşür.",
         "effects": {"justice": -7, "people": 8, "treasury": -3, "military": 0, "authority": 7},
         "log": "Tansiyon geçici olarak düşürüldü; hükümet erken seçime kadar zaman kazandı ancak tabanda kırılma yaşandı."},
        {"label": "Siyasi krizin tetiklediği sermaye kaçışını ve repo faizlerindeki tırmanışı önlemek için kamu bankalarına acil likidite sağla.",
         "effects": {"justice": -2, "people": -7, "treasury": 8, "military": 0, "authority": 3},
         "log": "Finansal panik durduruldu; döviz rezervleri korundu ancak faiz yükü bütçeyi zorladı."},
        {"label": "Batı Çalışma Grubu'nun (BÇG) fişlemelerine karşı Emniyet İstihbarat Dairesi marifetiyle gizli karşı-istihbarat tedbiri al.",
         "effects": {"justice": -4, "people": -8, "treasury": 0, "military": 8, "authority": 8},
         "log": "Emniyet kanadı harekete geçirildi; fişleme kasetleri ele geçirilerek bürokratik baskı hafifletildi."},
        {"label": "Siyasi Partiler Kanunu ve TCK'da kapsamlı demokratikleşme reformu hazırlayarak sivil-asker ilişkilerini AB normlarına yaklaştır.",
         "effects": {"justice": 8, "people": 3, "treasury": -7, "military": 0, "authority": 8},
         "log": "Demokratik standartları yükselten taslak sunuldu; uluslararası destek sağlandı fakat iç siyasetin ateşi sönmedi."}
    ],
    "tr_vaka_104": [
        {"label": "Askeri savcılık ve DGM'ye resmi başvuru yaparak yetki aşımıyla yapılan fişlemelerin sorumluları hakkında soruşturma açtır.",
         "effects": {"justice": 9, "people": 6, "treasury": -2, "military": 0, "authority": -4},
         "log": "Fişleme iddiaları adliyeye taşındı; yargı yolu işletildi ancak askeri hiyerarşiyle derin çatışma doğdu."},
        {"label": "Bülent Orakoğlu ve İçişleri bürokrasisi ile komutanlar arasında Başbakanlıkta gizli arabuluculuk yürüt.",
         "effects": {"justice": -7, "people": 7, "treasury": -2, "military": 0, "authority": 7},
         "log": "Kriz kapalı kapılar ardında yumuşatıldı; açık darbe ihtimali ötelendi fakat belgeler sızmaya devam etti."},
        {"label": "Fişleme belgelerinde adı geçen bürokrat ve şirketlerin kamu ihalelerinden men edilmesini önleyerek ekonomik istikrarı koru.",
         "effects": {"justice": -2, "people": -6, "treasury": 8, "military": 0, "authority": 4},
         "log": "Piyasada sermayenin yeşil-beyaz diye bölünmesi frenlendi; Anadolu sermayesinin vergi üretimi korundu."},
        {"label": "Deniz Kuvvetleri bünyesindeki BÇG birimine köstebek yerleştiren emniyet görevlilerini korumaya al; istihbarat arşivini güvenliğe çek.",
         "effects": {"justice": -3, "people": -8, "treasury": 0, "military": 9, "authority": 8},
         "log": "Emniyet istihbarat arşivi emniyete alındı; sivil irade karşı bilgi gücünü korudu."},
        {"label": "Devlet Memurları Kanunu'nda değişiklik yaparak çalışanların inanç, mezhep ve siyasi görüş nedeniyle fişlenmesini ağır cezalara bağla.",
         "effects": {"justice": 8, "people": 4, "treasury": -6, "military": 0, "authority": 7},
         "log": "Kamu personelinin anayasal hakları güvenceye alındı; fişleme bürokrasisine yasal barikat kuruldu."}
    ],
    "tr_vaka_105": [
        {"label": "Kudüs Gecesi'nde anayasal düzene aykırı pankart ve konuşmalar yapan belediye başkanı hakkında derhal adli soruşturma açtır.",
         "effects": {"justice": 8, "people": 6, "treasury": -1, "military": 0, "authority": -2},
         "log": "Hukuk devleti kuralları işletildi; provoke edici söylemlere karşı savcılık fezlekesi hazırlandı."},
        {"label": "Sincan Kaymakamı ve sivil toplum temsilcileriyle görüşerek ilçe halkını teskin et; sokak çatışmasını önleyecek itidal çağrısı yap.",
         "effects": {"justice": -6, "people": 8, "treasury": -2, "military": 0, "authority": 7},
         "log": "Halk sağduyuyla hareket etti; tankların geçişi provokasyona dönüşmeden ilçe sükûnete kavuştu."},
        {"label": "Tankların asfalt ve yol altyapısında yarattığı maddi hasarı tespit ettirerek Milli Savunma bütçesinden tazmin edilmesini sağla.",
         "effects": {"justice": -2, "people": -6, "treasury": 8, "military": 0, "authority": 3},
         "log": "Belediye bütçesindeki tahribat Hazinece karşılandı; kamu zararı tanzim edildi."},
        {"label": "Zırhlı Birlikler Tümen Komutanlığı'na resmi yazı yazarak güzergah dışına çıkan askeri araçların kışlalara çekilmesini emret.",
         "effects": {"justice": -4, "people": -8, "treasury": 0, "military": 8, "authority": 9},
         "log": "Hükümet otoritesi kağıt üzerinde gösterildi; kışladan plansız çıkışlar durduruldu."},
        {"label": "Belediyelerin kültürel ve sosyal etkinliklerinin milli mevzuata uygunluğunu denetleyen 'Belediye Etkinlikleri Çerçeve Yönetmeliği' çıkar.",
         "effects": {"justice": 7, "people": 3, "treasury": -6, "military": 0, "authority": 7},
         "log": "Yerel yönetimlerin dış politika ve ideolojik istismara alet olmasını engelleyen kurumsal standart getirildi."}
    ]
}

def generate_domain_1_to_3():
    deck = load_modern_deck()
    print("Building realistic options for Domains 1, 2, and 3 (tr_vaka_101 to tr_vaka_190)...")
    
    # Let's inspect events and build rich mappings
    options_map = {}
    options_map.update(D1)
    
    # Generate remaining events with tailored logic
    for i in range(100, 190):
        ev = deck[i]
        eid = ev['id']
        if eid in options_map:
            continue
        
        title = ev['title']
        desc = ev['desc']
        
        # Domain 1 events (105-129: tr_vaka_106 to tr_vaka_130)
        if 105 <= i <= 129:
            if "Fazilet Partisi" in title:
                options_map[eid] = [
                    {"label": "Anayasa Mahkemesi'ndeki kapatma davasında savunmayı evrensel örgütlenme özgürlüğü ve AİHM içtihatlarına dayandır.",
                     "effects": {"justice": 8, "people": 7, "treasury": -2, "military": 0, "authority": -3},
                     "log": "Hukuki savunma titizlikle sunuldu; odak olma iddiasının delilsizliği uluslararası hukuka dayandırıldı."},
                    {"label": "Meclisteki diğer parti liderleriyle temas kurarak parti kapatmayı zorlaştıran bir anayasa değişikliği için uzlaşma ara.",
                     "effects": {"justice": -6, "people": 8, "treasury": -2, "military": 0, "authority": 7},
                     "log": "Partiler arası diyalog kapısı aralandı; mecliste kapatmaya karşı geniş bir mutabakat zemini yoklandı."},
                    {"label": "Partinin kapatılması halinde hazine yardımının kesilmesini hesaba katarak teşkilat bütçesini tedbiren koru.",
                     "effects": {"justice": -2, "people": -6, "treasury": 8, "military": 0, "authority": 3},
                     "log": "Mali tedbirler alındı; teşkilatların borç yükü ve hazine yardımı riskleri minimize edildi."},
                    {"label": "Kapatma davası sürecinde sokak gösterilerini ve provokatif yürüyüşleri emniyet tedbirleriyle sıkı kontrol altında tut.",
                     "effects": {"justice": -3, "people": -8, "treasury": 0, "military": 8, "authority": 8},
                     "log": "Kamu düzeni korundu; kitlesel taşkınlıklar önlendi ve gerilimin sokağa taşması engellendi."},
                    {"label": "Venedik Komisyonu ilkeleri doğrultusunda 'Siyasi Partiler Kanunu ve Kapatma Usulleri Reformu'nu meclise sun.",
                     "effects": {"justice": 8, "people": 4, "treasury": -7, "military": 0, "authority": 7},
                     "log": "Parti kapatmanın Meclis iznine bağlanması taslağı hazırlandı; kurumsal demokrasi çıtası yükseltildi."}
                ]
            elif "18 Nisan 1999" in title:
                options_map[eid] = [
                    {"label": "Seçim sonuçlarını ve YSK tutanaklarını titizlikle denetle; tüm itirazları hukukun üstünlüğü çerçevesinde sonuçlandır.",
                     "effects": {"justice": 8, "people": 7, "treasury": -1, "military": 0, "authority": -2},
                     "log": "YSK kararları şeffaflıkla açıklandı; sandık iradesine tam güven sağlandı."},
                    {"label": "DSP, MHP ve ANAP genel başkanlarıyla üçlü koalisyon protokolü imzala; bakanlıkları liyakat ve dengelerle dağıt.",
                     "effects": {"justice": -7, "people": 8, "treasury": -3, "military": 0, "authority": 8},
                     "log": "57. Hükümet kuruldu; siyasi belirsizlik giderildi fakat koalisyon içi sürtüşmeler hissedildi."},
                    {"label": "Üç partinin seçim vaatleri arasında yer alan popülist harcamaları bütçe disiplini adına sınırlı tut.",
                     "effects": {"justice": -2, "people": -7, "treasury": 9, "military": 0, "authority": 4},
                     "log": "Hazine kasası korundu; bütçe açığı kontrol altına alındı fakat seçmen tabanında homurdanmalar başladı."},
                    {"label": "Hükümet güvenoyu alır almaz terörle mücadele ve sınır güvenliği için Milli Güvenlik Kurulu ile acil zirve topla.",
                     "effects": {"justice": -3, "people": -7, "treasury": 0, "military": 9, "authority": 8},
                     "log": "Güvenlik bürokrasisi teyakkuza geçirildi; devletin kararlılığı dosta düşmana hissettirildi."},
                    {"label": "Koalisyon protokolünü 'Ekonomik ve Sosyal Konsey ile Kamu Reformu Kanunu' ile yasal çerçeveye bağla.",
                     "effects": {"justice": 8, "people": 4, "treasury": -7, "military": 0, "authority": 7},
                     "log": "Sosyal tarafların hükümete katılımı kurumsallaştı; reform takvimi yasal güvenceye bağlandı."}
                ]
            elif "Merve Kavakçı" in title:
                options_map[eid] = [
                    {"label": "Milletvekilinin seçilme yeterliliği ve çifte vatandaşlık durumunu Danıştay ve YSK nezdinde hukuki karara bağlat.",
                     "effects": {"justice": 8, "people": 6, "treasury": -2, "military": 0, "authority": -3},
                     "log": "Hukuki süreç işletildi; meclis içi kavga yerine resmi mevzuat ve vatandaşlık kaydı incelendi."},
                    {"label": "TBMM Başkanlık Divanı ve parti grup başkanvekilleriyle kapalı meşveret toplayıp yemin törenini uzlaşıyla ertele.",
                     "effects": {"justice": -6, "people": 8, "treasury": -2, "military": 0, "authority": 7},
                     "log": "Genel kuruldaki fiziki gerilim yatıştırıldı; meclis krizinin erken patlaması önlendi."},
                    {"label": "Meclis çalışmalarının tıkanması sebebiyle Hazine'nin gecikme faizi ve ekonomik kayba uğramasını önleyecek tedbir al.",
                     "effects": {"justice": -2, "people": -6, "treasury": 8, "military": 0, "authority": 3},
                     "log": "Piyasalar krizden asgari düzeyde etkilendi; bütçe görüşmeleri gecikmeden sürdürüldü."},
                    {"label": "Genel kurul salonunda nizamı bozan ve fiziki müdahalede bulunanlara karşı TBMM İdare Amirliği'ni göreve çağır.",
                     "effects": {"justice": -4, "people": -8, "treasury": 0, "military": 8, "authority": 9},
                     "log": "Meclis iç güvenliği sağlandı; kürsü işgali önlendi fakat siyasi cepheleşme derinleşti."},
                    {"label": "TBMM İçtüzüğü'nde milletvekili kıyafet serbestisini ve yemin usullerini netleştiren kalıcı bir düzenleme yap.",
                     "effects": {"justice": 8, "people": 4, "treasury": -6, "military": 0, "authority": 7},
                     "log": "Kıyafet yönetmeliğindeki muğlaklıklar giderildi; gelecekteki yemin krizlerinin önüne geçildi."}
                ]
            elif "Anayasa Kitapçığı" in title:
                options_map[eid] = [
                    {"label": "Devlet Denetleme Kurulu'nun kamu bankaları teftiş raporlarını gecikmeksizin DGM Başsavcılığı'na ilet ve yargıyı işlet.",
                     "effects": {"justice": 9, "people": 6, "treasury": -3, "military": 0, "authority": -4},
                     "log": "Yargı süreci tavizsiz işletildi; kamu bankalarındaki yolsuzlukların üzerine gidildi."},
                    {"label": "Cumhurbaşkanı Sezer ile Başbakan Ecevit arasında Çankaya'da acil bir barışma ve ortak basın toplantısı organize et.",
                     "effects": {"justice": -7, "people": 8, "treasury": -4, "military": 0, "authority": 7},
                     "log": "Devletin zirvesindeki kavga yumuşatılmaya çalışıldı; ancak piyasa şoku çoktan tetiklenmişti."},
                    {"label": "Gecelik repo faizlerinin %7500'e fırlamasını durdurmak için Merkez Bankası'na döviz satış yetkisi ver ve dalgalı kura geç.",
                     "effects": {"justice": -2, "people": -8, "treasury": 9, "military": 0, "authority": 4},
                     "log": "Sabit kur rejiminden çıkıldı; Hazine döviz rezervleri kurtarıldı fakat devalüasyon halkı vurdu."},
                    {"label": "Bankalar ve döviz büroları önündeki panik havasına karşı mali şube ve güvenlik güçlerini teyakkuza geçir.",
                     "effects": {"justice": -3, "people": -8, "treasury": 0, "military": 9, "authority": 8},
                     "log": "Finans merkezlerinde asayiş sağlandı; banka yağması veya fiziki panik önlendi."},
                    {"label": "Dünya Bankası ve IMF ile müzakere ederek 'Güçlü Ekonomiye Geçiş Programı ve Bağımsız Kurullar Reformu'nu ilan et.",
                     "effects": {"justice": 8, "people": 3, "treasury": -8, "military": 0, "authority": 8},
                     "log": "Kemal Derviş reformları devreye alındı; bankacılık sistemi kurumsal zırha kavuşturuldu."}
                ]
            elif "Abdullah Öcalan" in title or "İmralı Duruşmaları" in title:
                options_map[eid] = [
                    {"label": "İmralı DGM duruşmalarını şehit aileleri, yerli ve yabancı basın önünde hukukun evrensel ilkeleriyle yürüt.",
                     "effects": {"justice": 9, "people": 7, "treasury": -2, "military": 0, "authority": -3},
                     "log": "Hukuk devleti ciddiyeti tüm dünyaya gösterildi; yargılamanın meşruiyetine gölge düşürülmedi."},
                    {"label": "AİHM'in ihtiyati tedbir çağrısını ve Avrupa Konseyi taahhütlerini meclisteki tüm siyasi partilerle müzakere et.",
                     "effects": {"justice": -6, "people": 8, "treasury": -2, "military": 0, "authority": 7},
                     "log": "Dış politika krizine dönüşmesi engellendi; siyasi uzlaşıyla infaz ertelendi."},
                    {"label": "İmralı Adası'nın yüksek güvenlikli cezaevi dönüşümü ve yargılama lojistiği için Adalet bütçesine ek ödenek aktar.",
                     "effects": {"justice": -2, "people": -6, "treasury": 8, "military": 0, "authority": 3},
                     "log": "Lojistik altyapı eksiksiz kuruldu; adadaki duruşma güvenliği Hazine kaynaklarıyla sağlandı."},
                    {"label": "İmralı ve çevresinde denizaltı, savaş gemisi ve hava sahası teyakkuzu kurarak olası tüm sızma girişimlerini engelle.",
                     "effects": {"justice": -2, "people": -7, "treasury": 0, "military": 10, "authority": 9},
                     "log": "Ada çevresinde aşılmaz bir güvenlik kalkanı tesis edildi; askeri otorite tam olarak kuruldu."},
                    {"label": "AB uyum süreci kapsamında 'Ölüm Cezasının Kaldırılması ve Ağırlaştırılmış Müebbet İnfaz Kanunu'nu kabul et.",
                     "effects": {"justice": 8, "people": 3, "treasury": -7, "military": 0, "authority": 8},
                     "log": "İdam cezası kaldırıldı; ağırlaştırılmış müebbet hapis sistemi Türk ceza infaz hukukuna girdi."}
                ]
            elif "Rahşan Affı" in title or "Şartlı Salıverme" in title:
                options_map[eid] = [
                    {"label": "Yasa kapsamındaki devlete karşı suçlar ile şahsa karşı suçlar ayrımını anayasa ve hakkaniyet ilkelerine göre uygula.",
                     "effects": {"justice": 8, "people": 6, "treasury": -2, "military": 0, "authority": -3},
                     "log": "Hukuki sınırlar titizlikle korundu; affın kapsamı mahkemelerde hukuka uygun yorumlandı."},
                    {"label": "Cezaevlerindeki doluluğu ve açlık grevlerini bitirmek için mahkum aileleri ve barolarla tahliye takvimini koordine et.",
                     "effects": {"justice": -7, "people": 8, "treasury": -2, "military": 0, "authority": 7},
                     "log": "Cezaevlerindeki isyan havası yatıştı; binlerce aile sevindi fakat sokakta güvenlik endişesi başladı."},
                    {"label": "Cezaevlerinin iaşe ve bakım giderlerindeki yükün hafiflemesiyle oluşan tasarrufu adliye yatırımlarına aktar.",
                     "effects": {"justice": -2, "people": -6, "treasury": 8, "military": 0, "authority": 3},
                     "log": "Cezaevi bütçesinde rahatlama sağlandı; tasarruf adli altyapıya kanalize edildi."},
                    {"label": "Tahliye olan mükerrir suçluların takibi için emniyet asayiş şubelerine özel gözetim ve devriye görevi ver.",
                     "effects": {"justice": -3, "people": -8, "treasury": 0, "military": 8, "authority": 8},
                     "log": "Tahliyelerin ardından sokakta sıkı asayiş kontrolü kuruldu; suç oranlarının patlaması önlendi."},
                    {"label": "Ceza İnfaz Kanunu'nu baştan yazarak şartlı salıverme oranlarını ve denetimli serbestlik müessesesini kurumsallaştır.",
                     "effects": {"justice": 8, "people": 4, "treasury": -6, "military": 0, "authority": 7},
                     "log": "Modern infaz hukuku inşa edildi; affa gerek bırakmayan kademeli infaz nizamı kuruldu."}
                ]
            elif "Hayata Dönüş Operasyonu" in title:
                options_map[eid] = [
                    {"label": "Operasyon sırasında meydana gelen ölümler ve aşırı güç kullanımı iddiaları hakkında adli ve idari soruşturma açtır.",
                     "effects": {"justice": 8, "people": 6, "treasury": -2, "military": 0, "authority": -4},
                     "log": "Cumhuriyet savcıları cezaevlerinde delil tespiti yaptı; aşırı güç iddiaları soruşturuldu."},
                    {"label": "Yaşar Kemal, Zülfü Livaneli ve aydınlar heyetinin ölüm orucundaki mahkumlarla yürüttüğü arabuluculuk müzakerelerini uzat.",
                     "effects": {"justice": -6, "people": 8, "treasury": -3, "military": 0, "authority": 6},
                     "log": "Müzakere masası son ana kadar açık tutuldu; aydınların çabası kamuoyunda saygı gördü."},
                    {"label": "F Tipi cezaevlerinin modern güvenlik teknolojileri ve oda sistemleri için Hazine'den acil inşaat ödeneği çıkar.",
                     "effects": {"justice": -2, "people": -6, "treasury": 8, "military": 0, "authority": 4},
                     "log": "Koğuş sisteminden oda sistemine geçişin finansmanı tamamlandı; cezaevi mimarisi yenilendi."},
                    {"label": "Jandarma komando birlikleri marifetiyle 20 cezaevine eşzamanlı müdahale ederek örgütlerin cezaevi hakimiyetini kır.",
                     "effects": {"justice": -4, "people": -9, "treasury": 0, "military": 10, "authority": 9},
                     "log": "Cezaevlerindeki örgüt hakimiyeti zor kullanılarak kırıldı; devlet otoritesi tesis edildi ancak can kayıpları oldu."},
                    {"label": "Ceza ve Tevkifevleri Genel Müdürlüğü teşkilatını yenileyen 'İnfaz Kurumları Güvenliği ve İyileştirme Kanunu' çıkar.",
                     "effects": {"justice": 7, "people": 3, "treasury": -7, "military": 0, "authority": 8},
                     "log": "İnfaz koruma memurlarının yetkileri ve tutuklu hakları yasal çerçevede yeniden tanzim edildi."}
                ]
            elif "1 Mart 2003 Tezkeresi" in title:
                options_map[eid] = [
                    {"label": "TBMM Genel Kurulu'nun verdiği ret kararına kayıtsız şartsız saygı göster; milletvekillerine baskı yapılmasını engelle.",
                     "effects": {"justice": 9, "people": 8, "treasury": -3, "military": 0, "authority": -3},
                     "log": "Milli iradenin üstünlüğü korundu; Türkiye'nin savaşa girmesini engelleyen karar tüm dünyada yankı buldu."},
                    {"label": "Washington ve bölge ülkeleriyle diplomatik temas kurarak tezkerenin reddi sonrası doğan tansiyonu yatıştır.",
                     "effects": {"justice": -6, "people": 8, "treasury": -2, "military": 0, "authority": 7},
                     "log": "Diplomatik diyalog kanalları işletildi; ABD ile ilişkilerin kopma noktasına gelmesi önlendi."},
                    {"label": "Tezkere karşılığı vadedilen 26 milyar dolarlık ABD yardım paketinden vazgeçerek milli bütçe tasarrufuna odaklan.",
                     "effects": {"justice": -2, "people": -6, "treasury": 8, "military": 0, "authority": 4},
                     "log": "Yabancı yardıma bağımlı olunmadığı kanıtlandı; Hazine kendi özkaynaklarıyla mali disiplini sürdürdü."},
                    {"label": "Kuzey Irak sınır boylarında doğabilecek otorite boşluğuna karşı 2. Ordu birliklerini sınır hattına yığ.",
                     "effects": {"justice": -2, "people": -7, "treasury": 0, "military": 9, "authority": 8},
                     "log": "Sınır güvenliği tahkim edildi; terör koridoru açılmasına karşı caydırıcı askeri yığınak yapıldı."},
                    {"label": "Anayasa'nın 92. maddesi kapsamında 'Yurtdışına Asker Gönderme ve Yabancı Birlikleri Kabul Kanunu'nu netleştir.",
                     "effects": {"justice": 8, "people": 4, "treasury": -6, "military": 0, "authority": 8},
                     "log": "Askeri tezkerelerin meclis oylama usulleri kanunen berraklaştırıldı; geleceğe yasal emsal bırakıldı."}
                ]
            elif "Süleymaniye'de Çuval" in title:
                options_map[eid] = [
                    {"label": "ABD hükümetine derhal en sert diplomatik notayı ver ve uluslararası hukuk nezdinde subaylarımızın dokunulmazlığını savun.",
                     "effects": {"justice": 8, "people": 8, "treasury": -2, "military": 0, "authority": -2},
                     "log": "Hukuki ve diplomatik nota verildi; müttefiklik hukukunun çiğnendiği kayıtlara geçirildi."},
                    {"label": "Genelkurmay Başkanı ve Başbakanlık nezdinde ortak kriz masası topla; personelin derhal ve koşulsuz serbest kalmasını sağla.",
                     "effects": {"justice": -6, "people": 8, "treasury": -2, "military": 0, "authority": 8},
                     "log": "60 saatlik yoğun müzakereler sonucunda Özel Kuvvetler timimiz salıverildi; çatışma çıkmadan kriz aşıldı."},
                    {"label": "İncirlik Üssü ve Türk hava sahasının ABD askeri nakliyelerine kullanım ücret ve kısıtlamalarını Hazine lehine revize et.",
                     "effects": {"justice": -2, "people": -6, "treasury": 8, "military": 0, "authority": 3},
                     "log": "Lojistik izinler üzerinden Hazineye gelir sağlandı; askeri geçişler kontrol altına alındı."},
                    {"label": "Kuzey Irak'taki tüm Özel Kuvvetler ve MİT unsurlarını teyakkuza geçir; yeni bir tacize anında silahla mukabele emri ver.",
                     "effects": {"justice": -3, "people": -7, "treasury": 0, "military": 10, "authority": 9},
                     "log": "Angajman kuralları sertleştirildi; Türk askerinin sahadaki caydırıcılığı yeniden tahkim edildi."},
                    {"label": "Yurtdışı askeri irtibat timlerinin statüsünü ve müttefik kuvvetlerle ilişkilerini düzenleyen 'Özel Görev Gücü Kanunu' çıkar.",
                     "effects": {"justice": 7, "people": 3, "treasury": -6, "military": 0, "authority": 8},
                     "log": "Yurtdışı operasyon timlerine kalıcı hukuki zırh ve harekat protokolü kazandırıldı."}
                ]
            elif "Kıbrıs Annan Planı" in title:
                options_map[eid] = [
                    {"label": "BM ve uluslararası toplum nezdinde Rum tarafının 'Hayır'ına rağmen Türk tarafının barış iradesini tescil ettir.",
                     "effects": {"justice": 9, "people": 8, "treasury": -2, "military": 0, "authority": -2},
                     "log": "Kıbrıs Türkü'nün haklılığı uluslararası arenada tescillendi; izolasyonların kalkması talep edildi."},
                    {"label": "Rauf Denktaş ve KKTC meclisiyle istişare yürüt; anavatan ile yavruvatan arasındaki güven bağlarını tazele.",
                     "effects": {"justice": -6, "people": 8, "treasury": -3, "military": 0, "authority": 7},
                     "log": "KKTC içi siyasi dengeler gözetildi; halkın referandum kararı ortak kabul gördü."},
                    {"label": "KKTC'ye uygulanan ambargoları kırmak için Hazine'den doğrudan ekonomik yardım ve altyapı fonu aktar.",
                     "effects": {"justice": -2, "people": -6, "treasury": 8, "military": 0, "authority": 3},
                     "log": "Kıbrıs Türk ekonomisi sübvanse edildi; turizm ve eğitim yatırımları canlandırıldı."},
                    {"label": "Kıbrıs Türk Barış Kuvvetleri'nin adadaki askeri varlığını ve garantörlük haklarımızı tavizsiz muhafaza et.",
                     "effects": {"justice": -2, "people": -7, "treasury": 0, "military": 9, "authority": 9},
                     "log": "Garantörlük hakları korundu; Türk askerinin adadaki caydırıcı varlığı sürdürüldü."},
                    {"label": "Türkiye ile KKTC arasında 'Stratejik Ortaklık ve Serbest Ticaret Bölgesi Çerçeve Kanunu'nu yürürlüğe koy.",
                     "effects": {"justice": 8, "people": 4, "treasury": -7, "military": 0, "authority": 8},
                     "log": "İki devlet arasındaki iktisadi ve hukuki entegrasyon kanunla mühürlendi."}
                ]
            elif "AB Uyum Yasaları ve DGM" in title:
                options_map[eid] = [
                    {"label": "Devlet Güvenlik Mahkemeleri'ni anayasadan tamamen çıkar; askeri üyeli yargılamalara son verip adil yargılanmayı sağla.",
                     "effects": {"justice": 9, "people": 7, "treasury": -2, "military": 0, "authority": -3},
                     "log": "DGM'ler tarihe karıştı; sivil yargının bağımsızlığı ve tabi hakim ilkesi güvenceye kavuştu."},
                    {"label": "Barolar Birliği, yüksek yargı organları ve akademisyenlerle ortak hukuk şurası toplayarak uyum paketini tartış.",
                     "effects": {"justice": -6, "people": 8, "treasury": -2, "military": 0, "authority": 7},
                     "log": "Yargı camiasının mutabakatı sağlandı; kanunların uygulanmasında direnç kırıldı."},
                    {"label": "AB hibe fonlarını adalet saraylarının inşasına ve adli tıp bilişim altyapısının kurulmasına tahsis et.",
                     "effects": {"justice": -2, "people": -6, "treasury": 8, "military": 0, "authority": 4},
                     "log": "Adliye binalarının fiziki modernizasyonu Hazineye yük olmadan AB fonlarıyla finanse edildi."},
                    {"label": "Terör suçlarında uzmanlaşmış Ağır Ceza Mahkemeleri kurarak güvenlik bürokrasisinin yargı zafiyetine düşmesini önle.",
                     "effects": {"justice": -3, "people": -7, "treasury": 0, "military": 8, "authority": 8},
                     "log": "Terörle mücadele ihtisas mahkemelerine devredildi; kamu düzeni boşluğa düşürülmedi."},
                    {"label": "8 temel uyum paketini birleştiren 'Temel Haklar ve Adil Yargılanma Çerçeve Kanunu'nu meclisten geçir.",
                     "effects": {"justice": 9, "people": 4, "treasury": -7, "military": 0, "authority": 7},
                     "log": "Hukuk devrimi gerçekleştirildi; Türkiye'nin Kopenhag kriterlerine uyumu tescillendi."}
                ]
            elif "Yeni Türk Ceza Kanunu" in title:
                options_map[eid] = [
                    {"label": "İşkence, kadına karşı şiddet ve çocuk istismarına sıfır tolerans tanıyan en ağır cezai maddeleri tavizsiz yasalaştır.",
                     "effects": {"justice": 9, "people": 8, "treasury": -2, "military": 0, "authority": -3},
                     "log": "Evrensel ceza hukuku ilkeleri kanunlaştı; işkencede zamanaşımı kaldırılarak insan onuru korundu."},
                    {"label": "Kadın dernekleri ve sivil toplumla istişare ederek töre ve namus cinayetlerindeki haksız tahrik indirimlerini kaldır.",
                     "effects": {"justice": -6, "people": 9, "treasury": -2, "military": 0, "authority": 6},
                     "log": "Toplumsal vicdanın sesi dinlendi; töre cinayetlerinde caydırıcılık en üst seviyeye çıkarıldı."},
                    {"label": "Adli para cezalarını güncel ekonomik verilere bağla; suçtan elde edilen gelirlere Hazine adına el koymayı kolaylaştır.",
                     "effects": {"justice": -2, "people": -6, "treasury": 9, "military": 0, "authority": 4},
                     "log": "Müsadere rejimi sıkılaştırıldı; suç gelirleri devlete gelir olarak kaydedildi."},
                    {"label": "Devletin güvenliğine ve anayasal düzene karşı suçlar faslını milli menfaatleri koruyacak şekilde güçlendir.",
                     "effects": {"justice": -3, "people": -7, "treasury": 0, "military": 9, "authority": 8},
                     "log": "Devlet güvenliği hukuki koruma altına alındı; terör ve anarşiyle mücadelede ceza zırhı sağlandı."},
                    {"label": "5237 Sayılı Türk Ceza Kanunu'nu tüm maddeleriyle yürürlüğe koyarak 1926 tarihli eski ceza kanununu lağvet.",
                     "effects": {"justice": 8, "people": 4, "treasury": -7, "military": 0, "authority": 8},
                     "log": "Çağdaş ceza hukuku çağı başladı; kişi güvenliği ve hürriyeti kanunun merkezine oturtuldu."}
                ]
            elif "Kamu İhale Kurumu" in title:
                options_map[eid] = [
                    {"label": "Devlet ihalelerindeki yolsuzlukları ve kayırmacılığı önlemek için Kamu İhale Kurumu'nu tam bağımsız özerk yapıya kavuştur.",
                     "effects": {"justice": 9, "people": 7, "treasury": -2, "military": 0, "authority": -3},
                     "log": "İhalelerde şeffaflık sağlandı; kamu kaynaklarının peşkeş çekilmesinin önüne bağımsız denetimle geçildi."},
                    {"label": "TOBB ve Türkiye Müteahhitler Birliği ile görüşerek ihale itiraz süreçlerinin yatırımları kilitlemesini engelleyecek formül bul.",
                     "effects": {"justice": -6, "people": 8, "treasury": -3, "military": 0, "authority": 7},
                     "log": "İş dünyasıyla istişare edildi; projelerin bürokratik itirazlarla aksaması kısmen önlendi."},
                    {"label": "Elektronik Kamu Alımları Platformu (EKAP) kurarak ihaleleri dijitalleştir; Hazine alımlarında %20 tasarruf sağla.",
                     "effects": {"justice": -2, "people": -6, "treasury": 9, "military": 0, "authority": 4},
                     "log": "Devlet alımlarında rekor tasarruf sağlandı; yolsuzluk komisyonları dijital kayıtla sıfırlandı."},
                    {"label": "Savunma ve istihbarat harcamalarını gizlilik prensibiyle Kamu İhale Kanunu'nun katı prosedürlerinden muaf tut.",
                     "effects": {"justice": -3, "people": -7, "treasury": 0, "military": 9, "authority": 8},
                     "log": "Milli güvenlik ihalelerinde gizlilik korundu; stratejik savunma alımları aksatılmadan yapıldı."},
                    {"label": "4734 Sayılı Kamu İhale Kanunu ve 4735 Sayılı Sözleşmeler Kanunu'nu çıkararak kamu harcamalarında devrim yap.",
                     "effects": {"justice": 8, "people": 4, "treasury": -7, "military": 0, "authority": 8},
                     "log": "Kamu maliyesinde kurumsal intizam sağlandı; devlet harcamaları uluslararası standartlara oturtuldu."}
                ]
            else:
                # Default high-quality generator for domain 1
                options_map[eid] = [
                    {"label": f"{title} hadisesinde mevzuatı ve yargı denetimini tavizsiz işleterek hukukun üstünlüğünü ve adaleti sağla.",
                     "effects": {"justice": 8, "people": 7, "treasury": -2, "military": 0, "authority": -3},
                     "log": f"{title} kapsamında hukukun üstünlüğü gözetildi; idari işlemler yargı denetimine tabi tutuldu."},
                    {"label": f"{title} sürecinde ilgili taraflar, sivil toplum ve siyasi aktörlerle ortak masa kurarak toplumsal mutabakat sağla.",
                     "effects": {"justice": -6, "people": 8, "treasury": -3, "military": 0, "authority": 7},
                     "log": f"{title} meselesinde meşveret ve uzlaşı sağlandı; tarafların gerilimi düşürüldü."},
                    {"label": f"{title} ile bağlantılı kamu kaynaklarını ve Hazine fonlarını sıkı tasarruf tedbirleriyle koruma altına al.",
                     "effects": {"justice": -2, "people": -6, "treasury": 8, "military": 0, "authority": 3},
                     "log": f"{title} hadisesinde mali disiplin korundu; kamu bütçesi olası zararlardan korundu."},
                    {"label": f"{title} karşısında kolluk ve idari bürokrasiyi kararlılıkla görevlendirerek kamu düzenini ve devlet otoritesini göster.",
                     "effects": {"justice": -3, "people": -8, "treasury": 0, "military": 8, "authority": 8},
                     "log": f"{title} karşısında kamu nizamı korundu; devletin otoritesi ve güvenliği hissettirildi."},
                    {"label": f"TBMM'de {title} konusunu yapısal olarak çözecek kapsamlı bir reform ve ihtisas kanununu yürürlüğe koy.",
                     "effects": {"justice": 8, "people": 4, "treasury": -7, "military": 0, "authority": 7},
                     "log": f"Yürürlüğe giren reform kanunu ile kurumsal güvence sağlandı; benzer krizlerin tekerrürü önlendi."}
                ]

        # Domain 2: Bankacılık Krizleri ve TMSF Operasyonları (130 <= i <= 159: tr_vaka_131 to tr_vaka_160)
        elif 130 <= i <= 159:
            if "Demirbank" in title:
                options_map[eid] = [
                    {"label": "Demirbank'ın hazine bonosu portföyündeki zararı bağımsız murakıplarla tespit et; usulsüz fon aktarımları hakkında DGM'ye başvur.",
                     "effects": {"justice": 8, "people": 6, "treasury": -2, "military": 0, "authority": -3},
                     "log": "Hukuki süreç işletildi; banka yönetimi ve fon aktarımları adli incelemeye alındı."},
                    {"label": "Türkiye Bankalar Birliği ve özel banka genel müdürleriyle likidite konsorsiyumu kur; bankayı piyasa içinde yüzdür.",
                     "effects": {"justice": -6, "people": 8, "treasury": -4, "military": 0, "authority": 7},
                     "log": "Özel bankalarla uzlaşıldı; piyasa paniği frenlendi fakat batık yükü dağıtıldı."},
                    {"label": "Demirbank'ın bono portföyünü kamu bankaları üzerinden fonlayarak piyasadaki gecelik repo faizlerini aşağı çek.",
                     "effects": {"justice": -2, "people": -7, "treasury": 8, "military": 0, "authority": 4},
                     "log": "Mali panik önlendi; gecelik faiz dalgası durduruldu fakat Hazine kamu kaynaklarını seferber etti."},
                    {"label": "Demirbank yönetimine BDDK ve TMSF marifetiyle el koy; bankanın tüm işlem terminallerini kapatıp varlıklarını devral.",
                     "effects": {"justice": -3, "people": -8, "treasury": 0, "military": 8, "authority": 9},
                     "log": "Devlet bankaya el koydu; piyasa spekülasyonu sert bir idari kararla durduruldu."},
                    {"label": "Bankaların kamu borçlanma kağıdı taşıma oranlarını ve likidite rasyolarını bağlayan 'Bankacılık Risk Yönetmeliği' çıkar.",
                     "effects": {"justice": 8, "people": 3, "treasury": -7, "military": 0, "authority": 8},
                     "log": "Bankacılık sistemine kalıcı risk sınırları getirildi; tek bir bankanın piyasayı kilitlemesi önlendi."}
                ]
            elif "İmar Bankası" in title:
                options_map[eid] = [
                    {"label": "İmar Bankası'ndaki çifte kayıt sistemini ve off-shore hortumlamayı ortaya çıkaran teftiş raporuyla hakim ortaklar hakkında tutuklama kararı çıkart.",
                     "effects": {"justice": 9, "people": 7, "treasury": -2, "military": 0, "authority": -3},
                     "log": "Adalet çarkları işletildi; cumhuriyet tarihinin en büyük banka dolandırıcılığı yargıya taşındı."},
                    {"label": "Yüz binlerce mağdur mudiyle görüşerek hakiki mevduatları sahte kayıtlardan ayıracak şeffaf bir uzlaşma komisyonu kur.",
                     "effects": {"justice": -6, "people": 9, "treasury": -4, "military": 0, "authority": 6},
                     "log": "Mudilerin feryadı dindirildi; sahte olmayan mevduatlar devlet güvencesiyle taksitlendirildi."},
                    {"label": "Uzan Grubu'nun tüm çimento fabrikaları, barajları ve şirketlerine TMSF eliyle el koyup satışa çıkararak kamu zararını tahsil et.",
                     "effects": {"justice": -2, "people": -6, "treasury": 10, "military": 0, "authority": 5},
                     "log": "TMSF milyarlarca dolarlık varlığı paraya çevirdi; Hazine kasasına devasa gelir aktarıldı."},
                    {"label": "Banka yöneticilerinin yurt dışına kaçmasını önlemek için hudut kapılarına ve havalimanlarına emniyet kırmızı alarmı ver.",
                     "effects": {"justice": -3, "people": -7, "treasury": 0, "military": 9, "authority": 8},
                     "log": "Sınır kapılarında sıkı önlem alındı; şüphelilerin mal kaçırması ve kaçışı sınırlandırıldı."},
                    {"label": "Bankalarda çift kayıt ve bilişim sahteciliğine ağırlaştırılmış hapis cezası getiren 'Bankacılık Ceza Reformu' çıkar.",
                     "effects": {"justice": 8, "people": 4, "treasury": -7, "military": 0, "authority": 8},
                     "log": "Bankacılık bilişim sistemlerine bağımsız denetim zorunluluğu getirildi; çifte kayıt devri kapandı."}
                ]
            elif "Beyaz Enerji" in title or "Mavi Hat" in title:
                options_map[eid] = [
                    {"label": "TEAŞ ve BOTAŞ ihalelerindeki rüşvet kasetlerini DGM savcılığına ilet; rüşvet alan bürokrat ve şirket sahiplerini derhal tutuklat.",
                     "effects": {"justice": 9, "people": 7, "treasury": -2, "military": 0, "authority": -3},
                     "log": "Yolsuzluk şebekesi çökertildi; enerji ihalelerindeki karanlık ilişkiler kamuoyu önünde yargılandı."},
                    {"label": "Elektrik ve doğalgaz dağıtımındaki aksamayı önlemek için sektör temsilcileriyle görüşüp temiz enerji şirketleriyle sözleşmeleri yenile.",
                     "effects": {"justice": -6, "people": 8, "treasury": -3, "military": 0, "authority": 7},
                     "log": "Enerji arz güvenliği korundu; elektrik kesintisi riski uzlaşıyla bertaraf edildi."},
                    {"label": "Hileli sözleşmelerle devlete pahalıya satılan doğalgaz ve elektrik alım garantilerini feshederek Hazineyi milyarlarca dolar zarardan kurtar.",
                     "effects": {"justice": -2, "people": -6, "treasury": 9, "military": 0, "authority": 4},
                     "log": "Hazine kasası kurtarıldı; 'Al ya da Öde' sözleşmelerindeki fahiş rant iptal edildi."},
                    {"label": "Jandarma Kaçakçılık ve Organize Suçlar timleriyle şüphelilerin ev ve holding binalarına şafak baskınları düzenle.",
                     "effects": {"justice": -3, "people": -7, "treasury": 0, "military": 9, "authority": 8},
                     "log": "Operasyonel güç kararlılıkla kullanıldı; deliller karartılmadan kasalara ve belgelere el konuldu."},
                    {"label": "Enerji Piyasası Düzenleme Kurumu (EPDK) yetkilerini tahkim eden 'Elektrik ve Doğalgaz Piyasası Reform Kanunu' çıkar.",
                     "effects": {"justice": 8, "people": 3, "treasury": -7, "military": 0, "authority": 8},
                     "log": "Enerji sektörü siyasetin keyfi vesayetinden çıkarıldı; şeffaf borsa ve lisanslama kuruldu."}
                ]
            elif "BDDK" in title or "Kemal Derviş" in title:
                options_map[eid] = [
                    {"label": "Bankaların siyasetçilerin arka bahçesi olmasını bitirmek için BDDK Murakıplar Kurulu'na tam bağımsız teftiş ve yetki ver.",
                     "effects": {"justice": 9, "people": 7, "treasury": -2, "military": 0, "authority": -3},
                     "log": "Bankacılıkta liyakat ve kural hakim kılındı; usulsüz kredi dağıtan patronlara geçit verilmedi."},
                    {"label": "TOBB, TÜSİAD ve işçi sendikalarıyla 'Ekonomik İstikrar Protokolü' imzalayarak reformlara toplumsal meşruiyet sağla.",
                     "effects": {"justice": -6, "people": 8, "treasury": -3, "military": 0, "authority": 7},
                     "log": "Toplumsal taraflar ikna edildi; '15 Günde 15 Kanun' reformları sokak çatışması olmadan yürürlüğe girdi."},
                    {"label": "Kamu bankalarını görev zararlarından arındırmak için Hazine kaynaklarından özel tertip tahvil ihraç et.",
                     "effects": {"justice": -2, "people": -7, "treasury": 8, "military": 0, "authority": 4},
                     "log": "Kamu bankalarının bilançoları temizlendi; Ziraat ve Halkbank batmaktan kurtarıldı."},
                    {"label": "Batık bankaların içini boşaltmaya yeltenen yöneticilere karşı Mali Şube polislerini görevlendirerek kaçak para transferlerini durdur.",
                     "effects": {"justice": -3, "people": -8, "treasury": 0, "military": 8, "authority": 8},
                     "log": "Kolluk gücüyle para kaçırma girişimleri engellendi; mali otorite sağlandı."},
                    {"label": "TBMM'den 'Bankalar Kanunu ve Bağımsız İdari Otoriteler Reform Paketi'ni kabul ederek finansal sisteme zırh geçir.",
                     "effects": {"justice": 8, "people": 4, "treasury": -7, "military": 0, "authority": 8},
                     "log": "Türk finans tarihinin en kapsamlı reformu tamamlandı; Türkiye 2008 küresel krizine dayanıklı hale geldi."}
                ]
            else:
                options_map[eid] = [
                    {"label": f"{title} olayında mali usulsüzlükleri bağımsız murakıplarca belgele ve sorumluları Ağır Ceza Mahkemesi'ne sevk et.",
                     "effects": {"justice": 8, "people": 7, "treasury": -2, "military": 0, "authority": -3},
                     "log": f"{title} hakkında yargı süreci işletildi; zimmet ve usulsüzlük iddiaları mahkemede hesap verdi."},
                    {"label": f"{title} mağdurları ve sektör temsilcileriyle uzlaşma masası kurarak alacakların tasfiyesini adil bir takvime bağla.",
                     "effects": {"justice": -6, "people": 8, "treasury": -3, "military": 0, "authority": 7},
                     "log": f"{title} kapsamında taraflar uzlaştırıldı; piyasa çalkantısı yatıştırılarak sulh sağlandı."},
                    {"label": f"{title} ile buharlaştırılan varlıkları TMSF marifetiyle haczedip kamu ihalesiyle satarak Hazine'ye gelir kaydet.",
                     "effects": {"justice": -2, "people": -6, "treasury": 9, "military": 0, "authority": 4},
                     "log": f"{title} varlıkları paraya çevrildi; Hazine kasasına gelir sağlanarak kamu zararı tazmin edildi."},
                    {"label": f"{title} sorumlularının mal varlıklarını kaçırmasını önlemek için kolluk ve MASAK marifetiyle sınır ötesi tedbir koy.",
                     "effects": {"justice": -3, "people": -7, "treasury": 0, "military": 8, "authority": 8},
                     "log": f"{title} şüphelilerine karşı sert mali kolluk tedbiri uygulandı; mal kaçırma teşebbüsü engellendi."},
                    {"label": f"Mali piyasaları regüle eden 'Finansal İstikrar ve Denetim Kanunu' çıkararak {title} gibi krizlerin tekrarını önle.",
                     "effects": {"justice": 8, "people": 3, "treasury": -7, "military": 0, "authority": 8},
                     "log": f"Kabul edilen yasal reform ile sistemik riskler önlendi; piyasaya kurumsal güven geldi."}
                ]

        # Domain 3: 2002-2007 Erken Seçimler ve AB Uyum (160 <= i <= 189: tr_vaka_161 to tr_vaka_190)
        elif 160 <= i <= 189:
            if "Katılım Müzakereleri" in title or "Çerçeve Belgesi" in title:
                options_map[eid] = [
                    {"label": "Lüksemburg müzakerelerinde tam üyelik hedefinden zerre taviz verme; 'imtiyazlı ortaklık' dayatmasını derhal reddet.",
                     "effects": {"justice": 8, "people": 8, "treasury": -2, "military": 0, "authority": -2},
                     "log": "Milli onur tavizsiz korundu; AB Türkiye'nin tam üyelik müzakere statüsünü resmen kabul etti."},
                    {"label": "Avrupa Birliği liderleriyle diplomatik mekik diplomasisi yürüt; Kıbrıs vetolarını aşacak esnek fasıl başlıklarında uzlaş.",
                     "effects": {"justice": -6, "people": 8, "treasury": -3, "military": 0, "authority": 7},
                     "log": "Diplomasi zaferle sonuçlandı; 3 Ekim 2005'te tarihi müzakere turları resmen başladı."},
                    {"label": "Katılım müzakereleriyle birlikte Türkiye'ye akacak doğrudan yabancı sermaye ve AB hibe fonlarını sanayiye kanalize et.",
                     "effects": {"justice": -2, "people": -6, "treasury": 9, "military": 0, "authority": 4},
                     "log": "Ülkeye rekor döviz girişi oldu; AB çıpası sayesinde Hazine borçlanma faizleri tarihi dipleri gördü."},
                    {"label": "Müzakere sürecinde milli güvenlik ve savunma sanayii projelerinin AB denetimine açılmasına kesinlikle izin verme.",
                     "effects": {"justice": -3, "people": -7, "treasury": 0, "military": 9, "authority": 9},
                     "log": "Savunma ve istihbarat alanında egemenlik korundu; milli güvenlikten taviz verilmedi."},
                    {"label": "AB müktesebatını 35 fasılda uyumlaştıran 'Avrupa Birliği Entegrasyon Çerçeve Kanunu'nu meclisten geçir.",
                     "effects": {"justice": 8, "people": 4, "treasury": -7, "military": 0, "authority": 8},
                     "log": "Bakanlıkların tüm mevzuatı AB standartlarıyla güncellendi; kurumsal dönüşüm ivme kazandı."}
                ]
            elif "TCK 301" in title or "Orhan Pamuk" in title or "Hrant Dink" in title:
                options_map[eid] = [
                    {"label": "AİHM içtihatları ve ifade özgürlüğü gereğince TCK 301 davalarında soruşturma iznini Adalet Bakanlığı iznine bağlayıp düşür.",
                     "effects": {"justice": 9, "people": 7, "treasury": -2, "military": 0, "authority": -3},
                     "log": "Düşünce özgürlüğü korundu; yazarların ve aydınların haksız mahkumiyetlerinin önüne geçildi."},
                    {"label": "Yazarlar ve aydınlarla Çankaya'da istişare toplantısı yap; linç atmosferini dağıtacak sivil bir diyalog bildirisi yayınla.",
                     "effects": {"justice": -6, "people": 8, "treasury": -2, "military": 0, "authority": 7},
                     "log": "Kutuplaşma teskin edildi; aydınlar ile devlet arasında karşılıklı anlayış zemini arandı."},
                    {"label": "Uluslararası boykot ve diplomatik yaptırım tehditlerinin Türkiye'nin turizm ve ticaret gelirlerine zarar vermesini önle.",
                     "effects": {"justice": -2, "people": -6, "treasury": 8, "military": 0, "authority": 3},
                     "log": "Ekonomik itibar korundu; uluslararası piyasalarda Türkiye algısının zedelenmesi önlendi."},
                    {"label": "Mahkeme önlerinde avukat ve aydınlara yönelik fiziki saldırı girişimlerine karşı adliye çevresinde polis kordonu kur.",
                     "effects": {"justice": -3, "people": -8, "treasury": 0, "military": 8, "authority": 8},
                     "log": "Adliye çevresinde asayiş sağlandı; provokasyonların sokak çatışmasına dönüşmesi engellendi."},
                    {"label": "TCK 301. maddede 'Türklük' ibaresini 'Türk Milleti' olarak değiştirip ceza alt sınırını düşüren reform kanununu kabul et.",
                     "effects": {"justice": 8, "people": 4, "treasury": -6, "military": 0, "authority": 7},
                     "log": "Maddenin istismar edilmesinin önü kesildi; yargıya somut ve dar yorum zorunluluğu getirildi."}
                ]
            elif "Genel Sağlık Sigortası" in title or "Sosyal Güvenlik" in title:
                options_map[eid] = [
                    {"label": "Her vatandaşın hastanelerde eşit ve ücretsiz tedavi hakkını anayasal sosyal devlet ilkesi gereği tavizsiz güvenceye al.",
                     "effects": {"justice": 9, "people": 8, "treasury": -3, "military": 0, "authority": -3},
                     "log": "Sosyal adalet tesis edildi; hastane kapılarında rehin kalma ve senet imzalama ayıbı tarihe karıştı."},
                    {"label": "TÜRK-İŞ, DİSK ve HAK-İŞ sendikalarıyla emeklilik yaşı ve prim gün sayısında ortak bir geçiş takviminde uzlaş.",
                     "effects": {"justice": -6, "people": 9, "treasury": -4, "military": 0, "authority": 6},
                     "log": "Sendikaların itirazları dinlendi; kademeli geçiş formülüyle sokak eylemleri durduruldu."},
                    {"label": "SSK, Bağ-Kur ve Emekli Sandığı açıklarını kapatacak aktüeryal dengeyi sağlamak için Hazine bütçesinden uzun vadeli fon ayır.",
                     "effects": {"justice": -2, "people": -7, "treasury": 8, "military": 0, "authority": 4},
                     "log": "Sosyal güvenlik açıkları kontrol altına alındı; bütçe disiplini geleceğe dönük kurtarıldı."},
                    {"label": "Sahte sigortalılık, kayıtdışı istihdam ve sahte engelli raporu çetelerine karşı SGK müfettişlerini ve polisi seferber et.",
                     "effects": {"justice": -3, "people": -7, "treasury": 0, "military": 8, "authority": 8},
                     "log": "Hileli emeklilik şebekeleri çökertildi; kamunun milyarlarca liralık kaynağı güvenceye alındı."},
                    {"label": "5510 Sayılı Sosyal Sigortalar ve Genel Sağlık Sigortası Kanunu'nu yürürlüğe koyarak üç kurumu SGK çatısında birleştir.",
                     "effects": {"justice": 8, "people": 4, "treasury": -8, "military": 0, "authority": 8},
                     "log": "Cumhuriyet tarihinin en büyük sosyal reformu tamamlandı; tek çatı altında modern SGK kuruldu."}
                ]
            elif "Doğrudan Yabancı Yatırımlar" in title:
                options_map[eid] = [
                    {"label": "Yabancı yatırımcıların mülkiyet ve tahkim haklarını uluslararası hukuk standartlarıyla teminat altına al.",
                     "effects": {"justice": 8, "people": 7, "treasury": -2, "military": 0, "authority": -3},
                     "log": "Hukuki öngörülebilirlik sağlandı; küresel sermayenin Türk yargısına olan güveni perçinlendi."},
                    {"label": "Yatırım Ajansı üzerinden yerli sanayiciler ile çok uluslu devleri ortak üretim ve teknoloji transferi masasında buluştur.",
                     "effects": {"justice": -6, "people": 8, "treasury": -2, "military": 0, "authority": 7},
                     "log": "Yerli sanayi güçlendirildi; teknoloji transferi anlaşmalarıyla katma değerli üretim başladı."},
                    {"label": "Ülkeye giren doğrudan yabancı yatırımlarla cari açığı finanse et ve Merkez Bankası rezervlerini rekor seviyelere taşı.",
                     "effects": {"justice": -2, "people": -6, "treasury": 10, "military": 0, "authority": 4},
                     "log": "Hazine kasasına 20 milyar doları aşan rekor döviz girdi; enflasyon ve faizler hızla geriledi."},
                    {"label": "Stratejik savunma, liman ve kritik altyapı tesislerinin yabancı kontrolüne geçmesini engelleyen güvenlik filtreleri koy.",
                     "effects": {"justice": -2, "people": -7, "treasury": 0, "military": 9, "authority": 8},
                     "log": "Milli güvenlik filtreleri uygulandı; kritik altyapının yabancı tekellere teslim edilmesi önlendi."},
                    {"label": "4875 Sayılı Doğrudan Yabancı Yatırımlar Kanunu'nu yürürlüğe koyarak bürokratik izinleri tek kapıdan çözüme kavuştur.",
                     "effects": {"justice": 8, "people": 4, "treasury": -7, "military": 0, "authority": 8},
                     "log": "Şirket kuruluş süreleri 3 güne indi; Türkiye küresel yatırımcıların cazibe merkezi oldu."}
                ]
            else:
                options_map[eid] = [
                    {"label": f"{title} düzenlemesinde AB standartları ve Anayasa ilkelerini gözeterek hukuki güvenceyi ve şeffaflığı tesis et.",
                     "effects": {"justice": 8, "people": 7, "treasury": -2, "military": 0, "authority": -3},
                     "log": f"{title} ile adli ve idari süreçler evrensel normlara kavuşturuldu; birey hakları korundu."},
                    {"label": f"{title} hususunda ilgili meslek örgütleri, sivil toplum ve halk temsilcileriyle diyalog kurarak toplumsal mutabakat sağla.",
                     "effects": {"justice": -6, "people": 8, "treasury": -3, "military": 0, "authority": 7},
                     "log": f"{title} uygulamasında toplumsal uzlaşı sağlandı; çatışma ve protesto riskleri bertaraf edildi."},
                    {"label": f"{title} için kamu bütçesinden gereken finansmanı sağlarken Hazine dengelerini ve mali disiplini tavizsiz koru.",
                     "effects": {"justice": -2, "people": -6, "treasury": 8, "military": 0, "authority": 3},
                     "log": f"{title} mali olarak disipline edildi; kamu kaynaklarının israf edilmesi önlendi."},
                    {"label": f"{title} kapsamında devletin kamu nizamını ve kolluk otoritesini kararlılıkla koruyacak güvenlik tedbirlerini al.",
                     "effects": {"justice": -3, "people": -8, "treasury": 0, "military": 8, "authority": 8},
                     "log": f"{title} sürecinde asayiş ve devlet otoritesi sağlandı; kamu düzeni muhafaza edildi."},
                    {"label": f"TBMM'den {title} konusunda kalıcı ve yapısal dönüşüm getiren reform kanununu kabul ettir.",
                     "effects": {"justice": 8, "people": 4, "treasury": -7, "military": 0, "authority": 7},
                     "log": f"Kabul edilen reform kanunu ile kurumsal nizam sağlandı; modern mevzuat yürürlüğe girdi."}
                ]

    print(f"Total options generated for Batch 1: {len(options_map)}")
    updated_deck = apply_options_to_deck(deck, options_map)
    save_modern_deck(updated_deck)

if __name__ == '__main__':
    generate_domain_1_to_3()
