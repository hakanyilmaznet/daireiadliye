import json
from deck_utils import load_modern_deck, save_modern_deck, apply_options_to_deck

# Domain 19: Sağlıkta Dönüşüm ve Salgınlar (tr_vaka_641 - tr_vaka_670)
# Domain 20: Spor Zaferleri ve Stadyum Krizleri (tr_vaka_671 - tr_vaka_700)
# Domain 21: Kültür, Sanat ve Ayasofya (tr_vaka_701 - tr_vaka_730)

def generate_domains_19_to_21():
    deck = load_modern_deck()
    print("Building realistic options for Domains 19, 20, and 21 (tr_vaka_641 to tr_vaka_730)...")
    options_map = {}

    for i in range(640, 730):
        ev = deck[i]
        eid = ev['id']
        title = ev['title']
        desc = ev['desc']

        # DOMAIN 19: Sağlıkta Dönüşüm ve Salgınlar (640 to 669: tr_vaka_641 to tr_vaka_670)
        if 640 <= i <= 669:
            if "SSK Hastaneleri" in title or "Sağlıkta Dönüşüm" in title:
                options_map[eid] = [
                    {"label": "Tüm vatandaşların dilediği hastanede ve eczanede eşit sağlık hizmeti alma hakkını anayasal sosyal devlet ilkesiyle sağla.",
                     "effects": {"justice": 9, "people": 9, "treasury": -3, "military": 0, "authority": -2},
                     "log": "Hastanelerde rehin kalma ayıbı bitti; SSK, Bağ-Kur ve Emekli Sandığı mensupları aynı çatı altında eşit hizmete kavuştu."},
                    {"label": "Türk Tabipleri Birliği, eczacı odaları ve sendikalarla görüşerek hastanelerin Sağlık Bakanlığı'na devrini uzlaşıyla yürüt.",
                     "effects": {"justice": -6, "people": 9, "treasury": -3, "military": 0, "authority": 7},
                     "log": "Doktor ve hemşirelerin özlük hakları korundu; hastanelerin devir sürecinde hiçbir sağlık aksaması yaşanmadı."},
                    {"label": "İlaç Takip Sistemi (İTS) kurarak sahte kupür ve ilaç yolsuzluğunu sıfırla; Hazineye yıllık 10 milyar TL tasarruf sağla.",
                     "effects": {"justice": -2, "people": -6, "treasury": 10, "military": 0, "authority": 4},
                     "log": "İlaçta karekod devrimi yapıldı; sahte reçete çeteleri çökertilerek kamu bütçesi korunmuş oldu."},
                    {"label": "Korsan ilaç fabrikaları ve sahte medikal malzeme depolarına karşı polis ve sağlık müfettişleriyle baskınlar yap.",
                     "effects": {"justice": -2, "people": -7, "treasury": 0, "military": 9, "authority": 9},
                     "log": "Halk sağlığıyla oynayan fırsatçılar yakalandı; sahte tıbbi malzemeler imha edildi."},
                    {"label": "5283 Sayılı Bazı Kamu Kurum ve Kuruluşlarına Ait Sağlık Birimlerinin Sağlık Bakanlığı'na Devredilmesi Kanunu'nu kabul et.",
                     "effects": {"justice": 8, "people": 5, "treasury": -7, "military": 0, "authority": 8},
                     "log": "Sağlıkta devrim tamamlandı; sabah 4'te SSK kuyruklarında bekleme devri ebediyen kapandı."},
                ]
            elif "COVID-19" in title or "Bilim Kurulu" in title or "Sokağa Çıkma" in title:
                options_map[eid] = [
                    {"label": "Salgın döneminde temel hak ve hürriyetlerin sınırlandırılmasını Anayasa ve Umumi Hıfzıssıhha Kanunu zemininde yürüt.",
                     "effects": {"justice": 8, "people": 8, "treasury": -3, "military": 0, "authority": -2},
                     "log": "Hukuki meşruiyet korundu; pandemi kararları keyfilikten uzak bilimsel kurul tavsiyelerine dayandırıldı."},
                    {"label": "Koronavirüs Bilim Kurulu'nun tavsiyeleriyle 14 günlük tam kapanma ilan et; esnafa ve dar gelirliye doğrudan gelir desteği ver.",
                     "effects": {"justice": -6, "people": 9, "treasury": -4, "military": 0, "authority": 7},
                     "log": "Vaka sayıları hızla düşürüldü; esnaf ve çalışanlar nakdi ücret desteğiyle korundu."},
                    {"label": "Yerli aşı TURKOVAC ve şehir hastanelerinin pandemi yoğun bakımları için Hazine bütçesinden sınırsız acil kaynak sağla.",
                     "effects": {"justice": -2, "people": -6, "treasury": 9, "military": 0, "authority": 5},
                     "log": "Milli aşı geliştirildi; yabancı aşı kartellerine milyarlarca dolar akıtılmasının önüne yerli üretimle geçildi."},
                    {"label": "Filyasyon ekiplerini, polis ve jandarma devriyeleriyle destekleyerek karantina ihlallerini ve stokçuluğu sertçe cezalandır.",
                     "effects": {"justice": -2, "people": -7, "treasury": 0, "military": 9, "authority": 9},
                     "log": "Salgın disiplini sağlandı; maske ve dezenfektan karaborsacılarına göz açtırılmadı."},
                    {"label": "Sağlık çalışanlarına şiddet uygulayanların tutuklu yargılanmasını zorunlu kılan 'Sağlıkta Şiddetle Mücadele Kanunu' çıkar.",
                     "effects": {"justice": 9, "people": 4, "treasury": -6, "military": 0, "authority": 8},
                     "log": "Beyaz Kod ve sağlık personeli koruma altına alındı; hekimlerin can güvenliği kanunla teminat altına alındı."}
                ]
            elif "Şehir Hastaneleri" in title:
                options_map[eid] = [
                    {"label": "Şehir hastanelerinin Kamu-Özel İşbirliği (KÖİ) kira ve hizmet sözleşmelerini Sayıştay ve bağımsız denetime aç.",
                     "effects": {"justice": 9, "people": 7, "treasury": -2, "military": 0, "authority": -3},
                     "log": "Sözleşmeler şeffaflıkla denetlendi; kamu kaynaklarının kullanımında hesap verilebilirlik sağlandı."},
                    {"label": "Günde 50 bin hastaya bakan dev kampüslerde hasta ve yaşlıların transferini kolaylaştıracak ücretsiz ring seferleri kur.",
                     "effects": {"justice": -5, "people": 9, "treasury": -3, "military": 0, "authority": 7},
                     "log": "Vatandaş memnuniyeti zirve yaptı; 5 yıldızlı otel konforundaki hastaneler halkın hizmetine sunuldu."},
                    {"label": "Hastanelerin medikal ve laboratuvar işletme bedellerini yerli firmalara açarak Hazine kira yükümlülüklerini azalt.",
                     "effects": {"justice": -2, "people": -6, "treasury": 9, "military": 0, "authority": 4},
                     "log": "Hazine borç yükü hafifletildi; kamu hastaneleri yüksek teknolojik donanıma kavuştu."},
                    {"label": "Hastanelerin nükleer tıp, radyasyon ve yoğun bakım binalarında siber ve fiziki güvenliği en üst düzeye çıkar.",
                     "effects": {"justice": -2, "people": -7, "treasury": 0, "military": 9, "authority": 8},
                     "log": "Stratejik sağlık merkezleri korundu; hasta veri tabanlarının siber saldırıya uğraması engellendi."},
                    {"label": "Türkiye'yi sağlık turizminin küresel başkenti yapan 'Uluslararası Sağlık Hizmetleri Kanunu' çıkar.",
                     "effects": {"justice": 8, "people": 4, "treasury": -7, "military": 0, "authority": 8},
                     "log": "Türkiye yılda 2 milyon yabancı hastaya bakan küresel sağlık üssü oldu; milyarlarca dolar döviz girdisi sağlandı."}
                ]
            else:
                options_map[eid] = [
                    {"label": "Sağlık hizmetlerinde hasta hakları, tıbbi etik ve malpraktis soruşturmalarını adli bağımsızlıkla yürüt.",
                     "effects": {"justice": 8, "people": 7, "treasury": -2, "military": 0, "authority": -3},
                     "log": "Tıbbi etik korundu; hasta hakları ve hekim güvencesi adil bir dengede tutuldu."},
                    {"label": "Tabip odaları, sağlık sendikaları ve hasta dernekleriyle diyalog kurarak sağlıkta reform mutabakatı sağla.",
                     "effects": {"justice": -6, "people": 8, "treasury": -2, "military": 0, "authority": 7},
                     "log": "Sağlık çalışanlarının talepleri dinlendi; grev ve aksamaların önüne uzlaşıyla geçildi."},
                    {"label": "İlaç ve tıbbi cihaz yerlileştirme projelerine Hazine bütçesinden doğrudan Ar-Ge teşviki ver.",
                     "effects": {"justice": -2, "people": -6, "treasury": 8, "military": 0, "authority": 4},
                     "log": "İlaçta yerlilik oranı arttı; ithal tıbbi cihaz harcamalarında Hazineye tasarruf sağlandı."},
                    {"label": "Hastanelerde acil servis baskınları ve sağlık personeline saldırılara karşı polis güvenlik noktaları kur.",
                     "effects": {"justice": -2, "people": -7, "treasury": 0, "military": 9, "authority": 8},
                     "log": "Acil servislerde asayiş sağlandı; sağlık görevlilerinin huzurla çalışması temin edildi."},
                    {"label": "Kamu sağlığı ve koruyucu hekimlik altyapısını güçlendiren 'Milli Sağlık Reform Kanunu' çıkar.",
                     "effects": {"justice": 8, "people": 4, "treasury": -6, "military": 0, "authority": 8},
                     "log": "Aile hekimliği ve koruyucu sağlık modeli yaygınlaştırıldı; hastalıklara erken teşhis sağlandı."}
                ]

        # DOMAIN 20: Spor Zaferleri ve Stadyum Krizleri (670 to 699: tr_vaka_671 to tr_vaka_700)
        elif 670 <= i <= 699:
            if "Galatasaray" in title or "UEFA Kupası" in title or "Süper Kupa" in title:
                options_map[eid] = [
                    {"label": "Kopenhag ve Monako zaferlerini Türk futbolunun uluslararası marka değeri ve adil oyun (Fair-Play) ilkesiyle taçlandır.",
                     "effects": {"justice": 8, "people": 9, "treasury": -2, "military": 0, "authority": -2},
                     "log": "Tarihi kupa zaferi dünyaya ilan edildi; Türk futbolunun Avrupa'daki saygınlığı zirveye çıktı."},
                    {"label": "Taksim Meydanı'nda toplanan milyonlarca taraftarla milli bayram coşkusunu kutla; tüm kulüpleri tek yürek yap.",
                     "effects": {"justice": -5, "people": 10, "treasury": -2, "military": 0, "authority": 8},
                     "log": "Türkiye sokaklara döküldü; 17 Mayıs gecesi Türk spor tarihinin altın sayfası olarak milletçe kutlandı."},
                    {"label": "Avrupa şampiyonu kulübe ve futbolculara devlet üstün hizmet madalyası ve Hazine prim desteği ver.",
                     "effects": {"justice": -2, "people": -6, "treasury": 8, "military": 0, "authority": 4},
                     "log": "Başarı devletçe ödüllendirildi; Türk futbolunun UEFA katsayısı ve yayın geliri tavan yaptı."},
                    {"label": "Şampiyonluk kutlamalarında taşkınlık, havaya ateş açma ve holiganizm eylemlerine karşı polis devriyelerini artır.",
                     "effects": {"justice": -2, "people": -7, "treasury": 0, "military": 9, "authority": 8},
                     "log": "Kutlamalar güven içinde tamamlandı; provokasyon ve yaralanmaların önüne geçildi."},
                    {"label": "Spor kulüplerinin borç batağına düşmesini engelleyen ve mali şeffaflık getiren 'Spor Kulüpleri ve Federasyonları Kanunu' çıkar.",
                     "effects": {"justice": 8, "people": 4, "treasury": -6, "military": 0, "authority": 8},
                     "log": "Dernekler Kanunu'ndan çıkarılan kulüpler anonim şirket yapısına kavuşturuldu; batık borçlara fren vuruldu."}
                ]
            elif "Filenin Sultanları" in title or "Yusuf Dikeç" in title or "Mete Gazoz" in title:
                options_map[eid] = [
                    {"label": "Olimpiyat ve Avrupa şampiyonu sporcularımızın dünya rekorlarını ve başarılarını uluslararası tescile bağla.",
                     "effects": {"justice": 9, "people": 9, "treasury": -2, "military": 0, "authority": -2},
                     "log": "Milli sporcuların zaferi tüm dünyada alkışlandı; Türk kadınının ve Türk gençliğinin gücü dünyaya kanıtlandı."},
                    {"label": "Brüksel'deki final maçını 81 ilin meydanlarına kurulan dev ekranlarda yüz binlerce vatandaşla birlikte izlet.",
                     "effects": {"justice": -5, "people": 10, "treasury": -2, "military": 0, "authority": 8},
                     "log": "Millet ekran başına kilitlendi; Vargas, Eda Erdem ve kızlarımızın zaferi 85 milyonun ortak sevinci oldu."},
                    {"label": "Milli sporculara ömür boyu sporcu şeref aylığı bağla; Anadolu'daki 10 bin köy okuluna voleybol ve okçuluk sahaları aç.",
                     "effects": {"justice": -2, "people": -6, "treasury": 9, "military": 0, "authority": 4},
                     "log": "Geleceğin şampiyonları için altyapı fonu ayrıldı; Hazine kaynakları gençliğin sporla buluşmasına tahsis edildi."},
                    {"label": "Uluslararası turnuvalarda sporcularımıza yönelik siber linç ve provokasyonlara karşı siber polis kalkanı kur.",
                     "effects": {"justice": -2, "people": -7, "treasury": 0, "military": 8, "authority": 8},
                     "log": "Milli sporcuların itibarı korundu; sosyal medyadaki organize saldırılar savcılıkça soruşturuldu."},
                    {"label": "Olimpik branşlarda madalya alan sporculara kalıcı kariyer ve üniversite öğretim üyeliği hakkı tanıyan 'Milli Sporcu Kanunu' çıkar.",
                     "effects": {"justice": 8, "people": 5, "treasury": -6, "military": 0, "authority": 8},
                     "log": "Olimpiyat şampiyonlarına devlet güvencesi getirildi; Türkiye spor ülkesine dönüştü."}
                ]
            elif "3 Temmuz" in title or "Şike Davası" in title:
                options_map[eid] = [
                    {"label": "Fenerbahçe ve kulüplere yönelik kumpas iddialarını, sahte tapeleri ve usulsüz dinlemeleri bağımsız yargıda incelet.",
                     "effects": {"justice": 9, "people": 8, "treasury": -2, "military": 0, "authority": -3},
                     "log": "Kumpas davası çöktü; Yargıtay tüm sanıklar hakkında beraat kararı vererek kulüplerin itibarını iade etti."},
                    {"label": "Milyonlarca taraftarın adalet yürüyüşlerini sükûnetle karşıla; futbol camiasındaki kutuplaşmayı giderecek barış masası kur.",
                     "effects": {"justice": -5, "people": 9, "treasury": -2, "military": 0, "authority": 7},
                     "log": "Taraftarların haklı isyanı dinlendi; kulüpler arasındaki düşmanlık havası sağduyuyla yatıştırıldı."},
                    {"label": "Kulüplerin UEFA gelirlerinden mahrum kalması ve borsada uğradığı yüz milyonlarca Euro'luk zararı telafi edecek yapılandırma yap.",
                     "effects": {"justice": -2, "people": -6, "treasury": 8, "military": 0, "authority": 4},
                     "log": "Kulüplerin mali iflası önlendi; Hazine ve kamu bankalarıyla borç tasfiye protokolleri imzalandı."},
                    {"label": "Kumpas soruşturan savcı ve emniyet amirleri hakkında 'örgütlü yargı kumpası' suçlamasıyla tutuklama kararı çıkart.",
                     "effects": {"justice": -2, "people": -7, "treasury": 0, "military": 9, "authority": 9},
                     "log": "Futbolu ele geçirmeye çalışan paralel çete yargıya teslim edildi; emniyet içindeki kumpasçılar temizlendi."},
                    {"label": "Sporda şiddet, düzensizlik ve şike suçlarını yeniden tanzim eden 6222 Sayılı Kanun'da demokratik reform yap.",
                     "effects": {"justice": 8, "people": 4, "treasury": -6, "military": 0, "authority": 8},
                     "log": "Sporda adalet sağlandı; keyfi ceza ve tutuklama yetkileri törpülenerek adil yargılanma getirildi."}
                ]
            elif "Riyad Krizi" in title or "Süper Kupa" in title or "Faruk Koca" in title:
                options_map[eid] = [
                    {"label": "Hakeme yumruk atan kulüp başkanı ve saldırganlar hakkında 6222 sayılı kanun kapsamında derhal tutuklama kararı çıkar.",
                     "effects": {"justice": 10, "people": 8, "treasury": -2, "military": 0, "authority": -2},
                     "log": "Hukuk devleti taviz vermedi; hakem Halil Umut Meler'e saldıran başkan hapse atıldı ve futboldan ömür boyu men edildi."},
                    {"label": "Riyad'da Atatürk pankartına izin verilmeyince maça çıkmayıp dönen Fenerbahçe ve Galatasaray kafilelerini havalimanında bayraklarla karşıla.",
                     "effects": {"justice": -5, "people": 10, "treasury": -2, "military": 0, "authority": 8},
                     "log": "Milli haysiyet tavizsiz korundu; iki ezeli rakip Cumhuriyetin kurucusuna sahip çıkarak tek yumruk oldu."},
                    {"label": "Süper Kupa organizatörlerine sözleşmeye aykırılık gerekçesiyle dava açıp tazminatı ve maç gelirlerini Türkiye'ye aktar.",
                     "effects": {"justice": -2, "people": -6, "treasury": 8, "military": 0, "authority": 4},
                     "log": "Hukuki tazminat süreci başlatıldı; milli kulüplerimizin maddi hakları uluslararası sözleşmelerle korundu."},
                    {"label": "Stadyumlarda sahaya giren holiganlara ve hakem soyunma odasını basmaya kalkan yöneticilere karşı çevik kuvveti göreve çağır.",
                     "effects": {"justice": -2, "people": -7, "treasury": 0, "military": 9, "authority": 9},
                     "log": "Stadyumlarda tam asayiş sağlandı; spor sahalarının terörize edilmesine geçit verilmedi."},
                    {"label": "Hakemlere karşı saldırıyı kamu görevlisine yapılmış sayan ve stadyum yasaklarını artıran 'Sporda Güvenlik Kanunu' çıkar.",
                     "effects": {"justice": 8, "people": 4, "treasury": -6, "military": 0, "authority": 8},
                     "log": "Hakemlerin can güvenliği kanunla korundu; holiganizme karşı en ağır cezalar yasalaştı."}
                ]
            else:
                options_map[eid] = [
                    {"label": "Spor müsabakalarında Fair-Play, spor ahlakı ve federasyon kurallarını tavizsiz uygula.",
                     "effects": {"justice": 8, "people": 7, "treasury": -2, "military": 0, "authority": -3},
                     "log": "Sporda dürüstlük ve kurallar korundu; haksız rekabet ve kural ihlalleri cezalandırıldı."},
                    {"label": "Kulüpler Birliği, sporcular ve taraftar dernekleriyle diyalog kurarak tribünlerde dostluk iklimi sağla.",
                     "effects": {"justice": -6, "people": 8, "treasury": -2, "military": 0, "authority": 7},
                     "log": "Tribün gerilimi düşürüldü; sporun birleştirici ve kardeşlik ruhu öne çıkarıldı."},
                    {"label": "Amatör spor kulüpleri ve olimpiyat hazırlık merkezleri için Hazine destekli sporcu bursu tahsis et.",
                     "effects": {"justice": -2, "people": -6, "treasury": 8, "military": 0, "authority": 4},
                     "log": "Altyapıya kaynak sağlandı; binlerce genç yetenek Türk sporuna kazandırıldı."},
                    {"label": "Derbi maçları ve deplasman yasaklarında stadyum çevrelerinde polis asayiş çemberini sıkı tut.",
                     "effects": {"justice": -2, "people": -7, "treasury": 0, "military": 9, "authority": 8},
                     "log": "Maç günleri asayiş sağlandı; holigan grupların sokak çatışması çıkarması önlendi."},
                    {"label": "Milli spor teşkilatını profesyonel standartlara kavuşturan 'Beden Eğitimi ve Spor Federasyonları Kanunu' çıkar.",
                     "effects": {"justice": 8, "people": 4, "treasury": -6, "military": 0, "authority": 8},
                     "log": "Spor yönetimi modernleştirildi; federasyonların özerkliği ve denetimi kanunla sağlandı."}
                ]

        # DOMAIN 21: Kültür, Sanat ve Ayasofya (700 to 729: tr_vaka_701 to tr_vaka_730)
        elif 700 <= i <= 729:
            if "Ayasofya" in title:
                options_map[eid] = [
                    {"label": "Danıştay 10. Dairesi'nin 1934 tarihli Bakanlar Kurulu kararını iptal eden tarihi hükmünü derhal Resmi Gazete'de yayımla.",
                     "effects": {"justice": 10, "people": 9, "treasury": -2, "military": 0, "authority": -2},
                     "log": "Hukuk zaferi ilan edildi; Fatih Sultan Mehmet Han'ın vakfiyesi gereğince Ayasofya 86 yıl sonra cami statüsüne kavuştu."},
                    {"label": "Sultanahmet Meydanı'nı dolduran 350 bin vatandaşla ilk Cuma namazını eda et; UNESCO heyetiyle mozaiklerin korunmasında uzlaş.",
                     "effects": {"justice": -5, "people": 10, "treasury": -2, "military": 0, "authority": 8},
                     "log": "Tarihi gün milletçe kutlandı; kılıçla hutbe okunurken paha biçilmez Hristiyan mozaikleri perde sistemiyle korundu."},
                    {"label": "Ayasofya'nın restorasyonu, minarelerin güçlendirilmesi ve kubbe onarımı için Vakıflar Genel Müdürlüğü'ne rekor bütçe ayır.",
                     "effects": {"justice": -2, "people": -6, "treasury": 9, "military": 0, "authority": 4},
                     "log": "Tarihi mabet depreme karşı çelik gergilerle korundu; Hazine kaynaklarıyla kubbe restorasyonu başlatıldı."},
                    {"label": "Ayasofya ve çevresinde özel güvenlik, turist güzergahı ve polis noktalarıyla 24 saat kesintisiz koruma sağla.",
                     "effects": {"justice": -2, "people": -7, "treasury": 0, "military": 9, "authority": 9},
                     "log": "Tarihi mabedin güvenliği kusursuz sağlandı; provokatif eylemler ve tarihi kapılara zarar verilmesi engellendi."},
                    {"label": "Fatih Sultan Mehmet Vakfı ve vakıf taşınmazlarının korunmasını anayasal güvenceye alan 'Tarihi Vakıflar ve Mabetler Kanunu' çıkar.",
                     "effects": {"justice": 8, "people": 4, "treasury": -6, "military": 0, "authority": 8},
                     "log": "Vakıf hukuku tahkim edildi; ecdat yadigarı eserlerin vakfiye şartlarına aykırı kullanımı ebediyen yasaklandı."}
                ]
            elif "Göbeklitepe" in title or "Zeugma" in title or "Tarihi Eser" in title:
                options_map[eid] = [
                    {"label": "Kaçırılan Çingene Kızı mozaikleri, lahitler ve heykelleri uluslararası mahkemelerde diplomatik baskıyla Türkiye'ye iade ettir.",
                     "effects": {"justice": 10, "people": 8, "treasury": -2, "military": 0, "authority": -2},
                     "log": "Kültür diplomasisi zaferle sonuçlandı; ABD ve Avrupa müzelerindeki kaçak eserlerimiz şanlı bayrağımızın altına getirildi."},
                    {"label": "Göbeklitepe'yi UNESCO Dünya Mirası Listesi'ne kaydettir; Şanlıurfa'da 'Tarihin Sıfır Noktası' turizm seferberliği başlat.",
                     "effects": {"justice": -5, "people": 9, "treasury": -2, "military": 0, "authority": 7},
                     "log": "Dünya arkeolojisi Türkiye'ye aktı; 12 bin yıllık tapınaklar milyonlarca turisti bölgeye çekerek esnafı ihya etti."},
                    {"label": "Karahantepe ve Taş Tepeler neolitik kazı alanları için Kültür ve Turizm Bakanlığı'na dev kazı ve koruma bütçesi tahsis et.",
                     "effects": {"justice": -2, "people": -6, "treasury": 9, "military": 0, "authority": 4},
                     "log": "Arkeolojik kazılar hızlandırıldı; Türkiye dünyanın 1 numaralı açık hava müzesi haline geldi."},
                    {"label": "Tarihi ören yerlerinde defineci kaçak kazılarını önlemek için jandarma ve dron devriyeleriyle 24 saat nöbet tut.",
                     "effects": {"justice": -2, "people": -7, "treasury": 0, "military": 9, "authority": 8},
                     "log": "Milli miras kaçakçılardan korundu; tarihi höyükleri talan eden define çeteleri suçüstü yakalandı."},
                    {"label": "Kültür ve tabiat varlıkları kaçakçılığına en ağır hapis cezaları getiren 'Kültür Varlıklarını Koruma Reform Kanunu' çıkar.",
                     "effects": {"justice": 8, "people": 4, "treasury": -6, "military": 0, "authority": 8},
                     "log": "Tarihi eser kaçakçılığı terör suçu derecesinde cezalandırıldı; Anadolu mirası yasal zırha kavuştu."}
                ]
            elif "Aziz Sancar" in title or "Orhan Pamuk" in title or "Daron Acemoğlu" in title or "Nobel" in title:
                options_map[eid] = [
                    {"label": "Nobel ödüllü bilim insanlarımızın ve yazarlarımızın düşünce ve bilimsel hürriyetini anayasal güvenceye bağla.",
                     "effects": {"justice": 9, "people": 8, "treasury": -2, "military": 0, "authority": -2},
                     "log": "Bilim ve edebiyat onurlandırıldı; Prof. Dr. Aziz Sancar Nobel madalyasını Anıtkabir'e armağan ederek milli hafızaya kazıdı."},
                    {"label": "Genç bilim insanlarını ve araştırmacıları desteklemek için TÜBİTAK bünyesinde 'Aziz Sancar Bilim Köyü ve Bursu' kur.",
                     "effects": {"justice": -5, "people": 9, "treasury": -2, "military": 0, "authority": 7},
                     "log": "Gençliğe ilham verildi; Anadolu'nun dört bir yanındaki öğrenciler moleküler biyoloji ve temel bilimlere yöneldi."},
                    {"label": "Temel bilimler ve araştırma üniversitelerine Hazine bütçesinden özel Ar-Ge ve laboratuvar fonu sağla.",
                     "effects": {"justice": -2, "people": -6, "treasury": 8, "military": 0, "authority": 4},
                     "log": "Üniversitelerin araştırma bütçeleri artırıldı; beyin göçünün tersine dönmesi için kaynak sağlandı."},
                    {"label": "Stratejik biyoteknoloji ve genetik araştırma laboratuvarlarını yabancı veri hırsızlığına karşı koruma kalkanına al.",
                     "effects": {"justice": -2, "people": -7, "treasury": 0, "military": 8, "authority": 8},
                     "log": "Milli DNA ve biyolojik veriler korundu; Türkiye'nin gen haritası güvenliğe alındı."},
                    {"label": "Bilim insanlarına tam bağımsız araştırma ve patent tescili imkanı sağlayan 'Milli Bilim ve Araştırma Kanunu' çıkar.",
                     "effects": {"justice": 8, "people": 4, "treasury": -6, "military": 0, "authority": 8},
                     "log": "Bilim insanları bürokratik engellerden kurtarıldı; Türkiye'nin küresel bilimsel yayın sayısı rekor kırdı."}
                ]
            elif "Türk Dizi" in title or "AKM" in title or "TRT Kurdî" in title:
                options_map[eid] = [
                    {"label": "Devlet televizyonunda TRT Kurdî ile farklı dillerde yayın hakkını anayasal kültürel haklar çerçevesinde güvenceye al.",
                     "effects": {"justice": 9, "people": 9, "treasury": -2, "military": 0, "authority": -2},
                     "log": "Tarihi kültürel tabu yıkıldı; TRT Kurdî ile kardeşlik hukuku tahkim edilerek terörün istismar kapısı kapatıldı."},
                    {"label": "Taksim Meydanı'ndaki Atatürk Kültür Merkezi'ni (AKM) opera, bale ve tiyatronun kalbi olarak halka aç.",
                     "effects": {"justice": -5, "people": 9, "treasury": -3, "military": 0, "authority": 7},
                     "log": "Kültür hayatı canlandı; modern opera salonu ve kültür kompleksi İstanbulluların buluşma noktası oldu."},
                    {"label": "150 ülkeye ihraç edilen ve 1 milyar seyirciye ulaşan Türk dizi sektörüne Ticaret Bakanlığı eliyle hizmet ihracatı desteği ver.",
                     "effects": {"justice": -2, "people": -6, "treasury": 10, "military": 0, "authority": 4},
                     "log": "Dizi sektörü Türkiye'ye milyarlarca dolar kazandırdı; Latin Amerika'dan Orta Doğu'ya kadar Türk kültürü hayranlığı oluştu."},
                    {"label": "Kültürel etkinliklerde ve film festivallerinde terör propagandası ve milli değerlere hakaret girişimlerini engelle.",
                     "effects": {"justice": -2, "people": -7, "treasury": 0, "military": 8, "authority": 9},
                     "log": "Kültürel alan provokasyonlardan korundu; sanatın terör propagandasına alet edilmesine izin verilmedi."},
                    {"label": "Sinema, dizi ve müzik sektörlerinde telif haklarını ve yapımcı paylarını güvenceye alan 'Yeni Sinema ve Telif Kanunu' çıkar.",
                     "effects": {"justice": 8, "people": 4, "treasury": -6, "military": 0, "authority": 8},
                     "log": "Sanatçıların ve yapımcıların telif gelirleri korundu; Türk sinema endüstrisi küresel rekabete hazırlandı."}
                ]
            else:
                options_map[eid] = [
                    {"label": "Tarihi ve kültürel varlıkların korunmasında vakfiye şartları, Anayasa ve evrensel koruma ilkelerini gözet.",
                     "effects": {"justice": 8, "people": 7, "treasury": -2, "military": 0, "authority": -3},
                     "log": "Kültürel miras korundu; ecdat yadigarı eserlerin restorasyonunda tarihi aslına sadık kalındı."},
                    {"label": "Sanatçılar, kültür insanları ve sivil toplumla istişare kurulları toplayarak milli kültür politikasını güçlendir.",
                     "effects": {"justice": -6, "people": 8, "treasury": -2, "military": 0, "authority": 7},
                     "log": "Kültür hayatında toplumsal mutabakat sağlandı; sanatçıların eser üretmesi desteklendi."},
                    {"label": "Müze, kütüphane ve tarihi restorasyon projeleri için Hazine bütçesinden özel ödenekler ayır.",
                     "effects": {"justice": -2, "people": -6, "treasury": 8, "military": 0, "authority": 4},
                     "log": "Kültür yatırımları finanse edildi; Türkiye'nin tarihi mirası ihya edilerek turizme kazandırıldı."},
                    {"label": "Tarihi eser kaçakçılarına ve sit alanlarını tahrip eden rant odaklarına karşı kolluk devriyelerini artır.",
                     "effects": {"justice": -2, "people": -7, "treasury": 0, "military": 9, "authority": 8},
                     "log": "Sit alanları korundu; tarihi dokuyu bozan kaçak yapılaşmalar dozerlerle yıkıldı."},
                    {"label": "Türkiye'nin kültürel diplomasisini ve tarihi mirasını koruyan 'Milli Kültür ve Sanat Reform Kanunu' çıkar.",
                     "effects": {"justice": 8, "people": 4, "treasury": -6, "military": 0, "authority": 8},
                     "log": "Kültür politikası kanunlaştı; Türkiye'nin tarihi derinliği dünyaya gururla tanıtıldı."}
                ]

    print(f"Total options generated for Batch 7: {len(options_map)}")
    updated_deck = apply_options_to_deck(deck, options_map)
    save_modern_deck(updated_deck)

if __name__ == '__main__':
    generate_domains_19_to_21()
