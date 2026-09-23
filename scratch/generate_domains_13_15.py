import json
from deck_utils import load_modern_deck, save_modern_deck, apply_options_to_deck

# Domain 13: Savunma Sanayii, Havacılık ve Uzay (tr_vaka_461 - tr_vaka_490)
# Domain 14: Enerji Keşifleri ve Nükleer Hamle (tr_vaka_491 - tr_vaka_520)
# Domain 15: Ekonomi, Enflasyon ve Rasyonel Dönüş (tr_vaka_521 - tr_vaka_550)

def generate_domains_13_to_15():
    deck = load_modern_deck()
    print("Building realistic options for Domains 13, 14, and 15 (tr_vaka_461 to tr_vaka_550)...")
    options_map = {}

    for i in range(460, 550):
        ev = deck[i]
        eid = ev['id']
        title = ev['title']
        desc = ev['desc']

        # DOMAIN 13: Savunma Sanayii, Havacılık ve Uzay (460 to 489: tr_vaka_461 to tr_vaka_490)
        if 460 <= i <= 489:
            if "KAAN" in title or "Milli Muharip Uçak" in title:
                options_map[eid] = [
                    {"label": "5. nesil stealth aviyonik ve yerli motor patentlerini Savunma Sanayii Başkanlığı adına uluslararası fikri mülkiyette tescil ettir.",
                     "effects": {"justice": 9, "people": 8, "treasury": -2, "military": 0, "authority": -2},
                     "log": "KAAN'ın tüm milli hakları tescillendi; yabancı ambargo ve patent kısıtlamaları bertaraf edildi."},
                    {"label": "Mühendis ordusunu ve TUSAŞ çalışanlarını Cumhurbaşkanlığı Külliyesi'nde ödüllendir; ilk uçuşu milletle bayram havasında kutla.",
                     "effects": {"justice": -5, "people": 10, "treasury": -3, "military": 0, "authority": 8},
                     "log": "Milli gurur şahlandı; Türk mühendislerinin gökyüzüne yazdığı zafer gençliğe ilham kaynağı oldu."},
                    {"label": "Seri üretim takvimini finanse etmek için Savunma Sanayii Destekleme Fonu'na doğrudan Hazine bütçesinden 5 milyar dolar kaynak aktar.",
                     "effects": {"justice": -2, "people": -6, "treasury": 10, "military": 0, "authority": 5},
                     "log": "Hava Kuvvetleri'nin modernizasyonu Hazinece garantiye alındı; seri üretim hatları kuruldu."},
                    {"label": "Mürted ve Eskişehir hava üslerinde KAAN için özel stealth hangar ve radar test tesislerini 24 saat teyakkuzla koru.",
                     "effects": {"justice": -2, "people": -7, "treasury": 0, "military": 10, "authority": 10},
                     "log": "Havacılık casusluğuna karşı çelik kalkan kuruldu; Türk semaları KAAN ile zırha büründü."},
                    {"label": "Dost ve müttefik ülkelere (Azerbaycan, Pakistan, Körfez) ortak üretim ve ihracat imkanı tanıyan 'Milli Muharip Havacılık Kanunu' çıkar.",
                     "effects": {"justice": 8, "people": 4, "treasury": -7, "military": 0, "authority": 9},
                     "log": "Milli savaş uçağı programı küresel ortaklıklarla kanunlaştı; Türkiye 5. nesil uçak üreten 4 ülkeden biri oldu."}
                ]
            elif "Bayraktar" in title or "Kızılelma" in title or "Akıncı" in title or "SİHA" in title:
                options_map[eid] = [
                    {"label": "İHA ve SİHA ihraç sözleşmelerine 'Türkiye aleyhine ve gayriahlaki kullanılamaz' şartını bağlayan bağlayıcı adli maddeler koy.",
                     "effects": {"justice": 9, "people": 8, "treasury": -2, "military": 0, "authority": -2},
                     "log": "Milli savunma ihracatına ahlaki ve hukuki çerçeve getirildi; küresel pazarda Türkiye'nin itibarı yükseldi."},
                    {"label": "35 ülkeye ihraç edilen SİHA zaferini TEKNOFEST meydanlarında gençlerle buluştur; yerli yazılım seferberliği başlat.",
                     "effects": {"justice": -5, "people": 10, "treasury": -2, "military": 0, "authority": 8},
                     "log": "Teknoloji hamlesi halk hareketi haline geldi; milyonlarca genç havacılık ve yazılıma yöneldi."},
                    {"label": "SİHA ihracatından elde edilen milyarlarca dolarlık döviz gelirini doğrudan yerli mikroçip ve motor projelerine kanalize et.",
                     "effects": {"justice": -2, "people": -6, "treasury": 10, "military": 0, "authority": 5},
                     "log": "Savunma sanayiinde ihracat rekoru kırıldı; Hazineye net döviz girdisi sağlanarak cari açık azaltıldı."},
                    {"label": "Kızılelma İnsansız Savaş Uçağı'nı TCG Anadolu amfibi gemisine entegre ederek dünya harp tarihinin ilk SİHA filosunu kur.",
                     "effects": {"justice": -2, "people": -7, "treasury": 0, "military": 10, "authority": 10},
                     "log": "Harp doktrini baştan yazıldı; deniz aşırı görevlerde Türk SİHA'ları küresel dengeleri değiştirdi."},
                    {"label": "İnsansız hava araçlarının sivil ve askeri hava sahasındaki uçuş kurallarını tanzim eden 'İnsansız Havacılık Reform Kanunu' çıkar.",
                     "effects": {"justice": 8, "people": 4, "treasury": -6, "military": 0, "authority": 8},
                     "log": "İHA teknolojisinin hukuki altyapısı tamamlandı; Türkiye dünyanın 1 numaralı SİHA gücü olarak tescillendi."}
                ]
            elif "TCG Anadolu" in title or "MİLGEM" in title or "Denizaltı" in title:
                options_map[eid] = [
                    {"label": "Donanmanın amiral gemisinin yapımında emeği geçen tüm tersane mühendisleri ve işçilerinin haklarını yasal tescile bağla.",
                     "effects": {"justice": 9, "people": 8, "treasury": -2, "military": 0, "authority": -2},
                     "log": "Milli gemi inşası hukuki ve teknik olarak tescillendi; Türk denizcilik endüstrisinin gururu oldu."},
                    {"label": "TCG Anadolu'yu Sarayburnu ve İzmir limanlarında halkın ziyaretine aç; yüz binlerce vatandaşın gemiyi gezmesini sağla.",
                     "effects": {"justice": -5, "people": 10, "treasury": -2, "military": 0, "authority": 8},
                     "log": "Millet kendi ordusuyla kucaklaştı; kilometrelerce kuyruk oluşturan vatandaşlar Mavi Vatan'a sahip çıktı."},
                    {"label": "MİLGEM korvetleri ve havadan bağımsız Reis sınıfı denizaltı projeleri için Savunma Fonu'ndan Hazine garantisi ver.",
                     "effects": {"justice": -2, "people": -6, "treasury": 9, "military": 0, "authority": 4},
                     "log": "Tersane yatırımları aralıksız sürdürüldü; Hazine kaynaklarıyla fırkateyn ve denizaltı filosu büyütüldü."},
                    {"label": "TCG Anadolu'yu Ege, Doğu Akdeniz ve Karadeniz'de sancak göstererek Mavi Vatan'ın en güçlü caydırıcı gücü haline getir.",
                     "effects": {"justice": -2, "people": -7, "treasury": 0, "military": 10, "authority": 10},
                     "log": "Denizlerdeki caydırıcılık zirveye çıktı; Türkiye açık denizlerde çıkarma ve hava harekatı gücünü ispatladı."},
                    {"label": "Milli tersaneler ve askeri gemi sanayiini stratejik koruma altına alan 'Milli Askeri Denizcilik Kanunu' çıkar.",
                     "effects": {"justice": 8, "people": 4, "treasury": -7, "military": 0, "authority": 9},
                     "log": "Donanmanın milli üretim oranı %80'in üzerine çıkarıldı; dışa bağımlılık tarihe gömüldü."}
                ]
            elif "Alper Gezeravcı" in title or "Uzay" in title or "Türksat" in title:
                options_map[eid] = [
                    {"label": "ISS'de gerçekleştirilen 13 bilimsel deneyin tüm veri ve patent haklarını Türkiye Uzay Ajansı (TUA) adına uluslararası hukukta tescille.",
                     "effects": {"justice": 9, "people": 8, "treasury": -2, "military": 0, "authority": -2},
                     "log": "Bilimsel veriler korundu; mikro yerçekimi ve genetik araştırmaların tüm mülkiyeti Türkiye'ye kazandırıldı."},
                    {"label": "İlk Türk astronotun uzay misyonunu 81 ildeki üniversite ve liselerde konferanslarla gençliğe aşıla; bilim şurası topla.",
                     "effects": {"justice": -5, "people": 10, "treasury": -3, "military": 0, "authority": 8},
                     "log": "Milli heyecan şahlandı; 'İstikbal Göklerdedir' ideali uzay çağıyla buluşturularak genç bilim insanları yetiştirildi."},
                    {"label": "Milli Uzay Programı'nın Ay Misyonu ve yerli roket fırlatma üssü için Hazine bütçesinden özel ödenek ayır.",
                     "effects": {"justice": -2, "people": -6, "treasury": 9, "military": 0, "authority": 4},
                     "log": "Yerli uzay motoru ve fırlatma rampası yatırımları finanse edildi; Türksat 6A ile haberleşmede yerlilik sağlandı."},
                    {"label": "Askeri istihbarat ve gözetleme uydularının (Göktürk, İMECE) veri güvenliğini korumak üzere Siber ve Uzay Komutanlığı'nı kur.",
                     "effects": {"justice": -2, "people": -7, "treasury": 0, "military": 9, "authority": 9},
                     "log": "Uzay savunma mimarisi kuruldu; Türk uydularına yönelik elektronik harp tehditleri engellendi."},
                    {"label": "Uzay ve havacılık sektöründe yerli şirketlere 20 yıllık vergi muafiyeti getiren 'Milli Uzay ve Uydu Sanayii Kanunu' çıkar.",
                     "effects": {"justice": 8, "people": 4, "treasury": -7, "military": 0, "authority": 9},
                     "log": "Uzay endüstrisi kanunlaştı; Türkiye kendi uydusunu üreten ve uzaya astronot gönderen ülkeler ligine girdi."}
                ]
            else:
                options_map[eid] = [
                    {"label": "Savunma sanayii projelerinin fikri mülkiyet ve patent haklarını devlet adına güvenceye alan yasal tescilleri yap.",
                     "effects": {"justice": 8, "people": 7, "treasury": -2, "military": 0, "authority": -3},
                     "log": "Teknolojik mülkiyet korundu; milli projelerin yabancı şirketler tarafından taklit edilmesi önlendi."},
                    {"label": "Yerli mühendis ordusu, üniversiteler ve KOBİ'lerle teknoloji şurası toplayarak savunma ekosistemini tabana yay.",
                     "effects": {"justice": -6, "people": 8, "treasury": -2, "military": 0, "authority": 7},
                     "log": "Toplumsal ve sektörel uzlaşı sağlandı; binlerce yan sanayi firması milli savunma üretimine dahil oldu."},
                    {"label": "Stratejik savunma sanayii Ar-Ge projeleri için Savunma Destekleme Fonu'ndan Hazine destekli teşvik sağla.",
                     "effects": {"justice": -2, "people": -6, "treasury": 8, "military": 0, "authority": 4},
                     "log": "Milli savunma yatırımları finanse edildi; dışa bağımlılık azaltılarak ihracat potansiyeli artırıldı."},
                    {"label": "Kritik savunma tesisleri ve Ar-Ge merkezlerinde casusluk ve sabotaja karşı askeri güvenlik kordonunu tahkim et.",
                     "effects": {"justice": -2, "people": -7, "treasury": 0, "military": 10, "authority": 9},
                     "log": "Stratejik sırlar korundu; milli teknolojilere yönelik yabancı istihbarat operasyonları engellendi."},
                    {"label": "Savunma sanayiinde yerlilik oranını %85'e çıkaran 'Stratejik Savunma Sanayii ve İleri Teknoloji Kanunu' çıkar.",
                     "effects": {"justice": 8, "people": 4, "treasury": -6, "military": 0, "authority": 8},
                     "log": "Savunma bağımsızlığı kanunlaştı; Türkiye kendi silahını üreten küresel aktör oldu."}
                ]

        # DOMAIN 14: Enerji Keşifleri ve Nükleer Hamle (490 to 519: tr_vaka_491 to tr_vaka_520)
        elif 490 <= i <= 519:
            if "Sakarya Gaz" in title or "Filyos" in title or "Fatih Sondaj" in title:
                options_map[eid] = [
                    {"label": "Karadeniz'deki 710 milyar metreküplük doğalgaz sahasının kıta sahanlığı ve münhasır ekonomik bölge haklarını BM'ye tescille.",
                     "effects": {"justice": 9, "people": 8, "treasury": -2, "military": 0, "authority": -2},
                     "log": "Karadeniz hidrokarbon egemenliğimiz tescillendi; yabancı iddiaların önü uluslararası hukukla kesildi."},
                    {"label": "Karadeniz gazının karaya ulaştığı gün tüm konutlarda 1 ay ücretsiz doğalgaz ve 1 yıl mutfak gazı desteği sağla.",
                     "effects": {"justice": -5, "people": 10, "treasury": -3, "military": 0, "authority": 7},
                     "log": "Vatandaşın hanesine bayram havası girdi; yerli gazın bereketi doğrudan halkın cebine yansıtıldı."},
                    {"label": "Karadeniz gazı ile yıllık 15 milyar dolarlık enerji ithalat faturasını düşürerek Hazine cari dengesini artıya geçir.",
                     "effects": {"justice": -2, "people": -6, "treasury": 10, "military": 0, "authority": 5},
                     "log": "Milli ekonomi nefes aldı; enerjide dışa bağımlılık kırılarak Merkez Bankası rezervleri korundu."},
                    {"label": "Filyos Doğalgaz İşleme Tesisi ve Fatih, Yavuz, Kanuni filolarını denizaltı ve hava savunma radarlarıyla 24 saat koru.",
                     "effects": {"justice": -2, "people": -7, "treasury": 0, "military": 9, "authority": 9},
                     "log": "Mavi Vatan'ın enerji üsleri korundu; sondaj gemilerimize yönelik olası sabotajlar engellendi."},
                    {"label": "Türkiye'yi Doğu Avrupa ve Akdeniz'in gaz dağıtım merkezi yapan 'Milli Doğalgaz Piyasası ve Transit Ticaret Kanunu' çıkar.",
                     "effects": {"justice": 8, "people": 4, "treasury": -7, "military": 0, "authority": 9},
                     "log": "Enerji borsası ve hub merkezi kuruldu; Türkiye küresel doğalgaz ticaretinin karar vericisi oldu."}
                ]
            elif "Gabar" in title or "Petrol" in title:
                options_map[eid] = [
                    {"label": "Gabar ve Cudi dağlarında şehit düşen öğretmen Aybüke Yalçın ve jandarma Esma Çevik'in adını kuyulara vererek milli hafızaya kazı.",
                     "effects": {"justice": 9, "people": 9, "treasury": -2, "military": 0, "authority": -2},
                     "log": "Şehitlerimizin adı petrol kuyularında ölümsüzleşti; terör yuvaları milli zenginlik pınarına dönüştü."},
                    {"label": "Günde 100 bin varil kaliteli petrol üreten sahalarda Şırnak ve bölge gençlerine istihdam ve meslek okulu aç.",
                     "effects": {"justice": -5, "people": 9, "treasury": -2, "military": 0, "authority": 7},
                     "log": "Bölge kalkınması hızlandı; terörden arındırılan dağlarda petrol refahı kardeşliği perçinledi."},
                    {"label": "Gabar petrolünün rafinerilere taşınmasıyla TPAO gelirlerini iki katına çıkar; Hazineye yıllık milyarlarca dolar tasarruf sağla.",
                     "effects": {"justice": -2, "people": -6, "treasury": 10, "military": 0, "authority": 5},
                     "log": "Türkiye'nin petrol ihtiyacının %20'si yerli kuyulardan karşılanmaya başladı; Hazine rahatladı."},
                    {"label": "Cudi ve Gabar'daki petrol kulelerini jandarma üs bölgeleri ve SİHA devriyeleriyle terör saldırılarına karşı koru.",
                     "effects": {"justice": -2, "people": -7, "treasury": 0, "military": 10, "authority": 9},
                     "log": "Eski çatışma alanlarında kesintisiz huzur kuruldu; petrol konvoyları güvenle sevkiyat yaptı."},
                    {"label": "Milli petrol arama ve maden imtiyazlarını genişleten 'Milli Petrol ve Hidrokarbon Seferberlik Kanunu' çıkar.",
                     "effects": {"justice": 8, "people": 4, "treasury": -7, "military": 0, "authority": 8},
                     "log": "TPAO dünyanın en güçlü milli petrol şirketlerinden biri oldu; arama ve sondaj filosu genişletildi."}
                ]
            elif "Akkuyu" in title or "Nükleer" in title:
                options_map[eid] = [
                    {"label": "Uluslararası Atom Enerjisi Ajansı (UAEA) ve Nükleer Düzenleme Kurumu (NDK) ile en katı sismik ve güvenlik teftişlerini uygula.",
                     "effects": {"justice": 9, "people": 7, "treasury": -2, "military": 0, "authority": -2},
                     "log": "Nükleer güvenlik tescillendi; Akkuyu NGS uluslararası en üst seviye 3+ nesil VVER-1200 güvenlik zırhına kavuştu."},
                    {"label": "Mersin halkı, ziraat odaları ve çevrecilerle düzenli bilgilendirme masası topla; deniz suyu sıcaklığı ve tarım endişelerini gider.",
                     "effects": {"justice": -6, "people": 8, "treasury": -3, "military": 0, "authority": 7},
                     "log": "Toplumsal endişeler giderildi; radyasyon ölçüm istasyonları canlı olarak halkın erişimine açıldı."},
                    {"label": "İlk taze nükleer yakıtın santrale gelmesiyle Türkiye'yi resmen nükleer kulübe sok; yıllık 35 milyar kWh baz yük elektriği finanse et.",
                     "effects": {"justice": -2, "people": -6, "treasury": 9, "military": 0, "authority": 5},
                     "log": "Türkiye nükleer güç statüsü kazandı; 4 reaktörün devreye girmesiyle elektriğin %10'u sıfır karbonla üretilmeye başlandı."},
                    {"label": "Santral çevresinde hava savunma füzeleri, radar sistemleri ve denizaltısavar kalkanıyla askeri düzeyde koruma çemberi kur.",
                     "effects": {"justice": -2, "people": -7, "treasury": 0, "military": 10, "authority": 10},
                     "log": "Stratejik nükleer tesis koruma kalkanına alındı; hava ve deniz sahası tam kontrole bağlandı."},
                    {"label": "Türkiye'nin nükleer yakıt, atık yönetimi ve reaktör işletimini tanzim eden 'Nükleer Enerji ve Radyasyon Güvenliği Kanunu' çıkar.",
                     "effects": {"justice": 8, "people": 4, "treasury": -7, "military": 0, "authority": 8},
                     "log": "Nükleer enerji hukuku inşa edildi; Sinop ve Trakya'daki yeni santral projelerine yasal zemin açıldı."}
                ]
            else:
                options_map[eid] = [
                    {"label": "Enerji projelerinde çevre mevzuatı, kamulaştırma ve lisanslama süreçlerini şeffaf adli denetime tabi tut.",
                     "effects": {"justice": 8, "people": 7, "treasury": -2, "military": 0, "authority": -3},
                     "log": "Enerji yatırımlarında hukuki intizam sağlandı; kamu menfaati ve çevre dengesi korundu."},
                    {"label": "Yenilenebilir ve yerli enerji yatırımlarında yerel halk ve sanayicilerle istişare ederek enerji verimliliği seferberliği başlat.",
                     "effects": {"justice": -6, "people": 8, "treasury": -2, "military": 0, "authority": 7},
                     "log": "Halkın desteği sağlandı; enerji tasarrufu ve verimliliği tabana yayıldı."},
                    {"label": "Yerli ve yenilenebilir enerji kaynaklarını sübvanse ederek Hazine'nin döviz bazlı enerji faturasını hafiflet.",
                     "effects": {"justice": -2, "people": -6, "treasury": 8, "military": 0, "authority": 4},
                     "log": "Milli bütçe korundu; yerli kömür, hidroelektrik ve güneşle ithal gaz bağımlılığı azaltıldı."},
                    {"label": "Stratejik barajlar, boru hatları ve trafo merkezlerinde sabotajlara karşı kolluk devriyelerini artır.",
                     "effects": {"justice": -2, "people": -7, "treasury": 0, "military": 9, "authority": 8},
                     "log": "Enerji iletim hatları korundu; şebekenin kesintisiz elektrik vermesi güvenceye alındı."},
                    {"label": "Türkiye'nin 2053 net sıfır emisyon hedefini destekleyen 'Yenilenebilir Enerji ve Tabii Kaynaklar Reform Kanunu' çıkar.",
                     "effects": {"justice": 8, "people": 4, "treasury": -6, "military": 0, "authority": 8},
                     "log": "Temiz enerji mevzuatı kabul edildi; rüzgar ve güneş kurulu gücünde Türkiye Avrupa liderliğine yükseldi."}
                ]

        # DOMAIN 15: Ekonomi, Enflasyon ve Rasyonel Dönüş (520 to 549: tr_vaka_521 to tr_vaka_550)
        elif 520 <= i <= 549:
            if "Kur Korumalı Mevduat" in title or "KKM" in title:
                options_map[eid] = [
                    {"label": "KKM sisteminin getirdiği kur farkı yükümlülüklerini anayasal bütçe hakkı çerçevesinde Sayıştay ve Meclis denetimine aç.",
                     "effects": {"justice": 9, "people": 7, "treasury": -2, "military": 0, "authority": -3},
                     "log": "Hazine yükümlülükleri şeffafça denetlendi; kamu kaynaklarının kullanımında hesap verilebilirlik sağlandı."},
                    {"label": "TÜSİAD, MÜSİAD ve bankalarla görüşerek mudilerin döviz talebini kesen KKM mekanizmasının avantajlarını piyasaya anlat.",
                     "effects": {"justice": -6, "people": 8, "treasury": -4, "military": 0, "authority": 7},
                     "log": "Piyasa paniği yatıştırıldı; döviz kurundaki çılgın tırmanış 20 Aralık gecesi sert şekilde kırıldı."},
                    {"label": "KKM stokunu kademeli ve piyasayı sarsmadan eritmek için TL mevduat faizlerini cazip kıl; Hazine desteğini sonlandır.",
                     "effects": {"justice": -2, "people": -7, "treasury": 9, "military": 0, "authority": 4},
                     "log": "Hazine sırtındaki devasa kur farkı kamburundan kurtuldu; KKM hacmi 140 milyar dolardan hızla eridi."},
                    {"label": "Döviz spekülasyonu yapan ve kara para aklayan kayıt dışı finans çevrelerine karşı MASAK ve Mali Şube'yi sahaya sür.",
                     "effects": {"justice": -3, "people": -8, "treasury": 0, "military": 8, "authority": 8},
                     "log": "Döviz büroları ve tezgah altı piyasalarda sıkı denetim kuruldu; manipülatif ataklar önlendi."},
                    {"label": "Mevduat sisteminde TL'yi önceleyen ve bütçeden kur farkı aktarımını sonlandıran 'Finansal Normalleşme Kanunu' çıkar.",
                     "effects": {"justice": 8, "people": 4, "treasury": -7, "military": 0, "authority": 8},
                     "log": "Ortodoks para politikasına geçiş kanunlaştı; makroekonomik istikrar teminat altına alındı."}
                ]
            elif "Mehmet Şimşek" in title or "Rasyonel" in title or "Politika Faizi" in title:
                options_map[eid] = [
                    {"label": "Merkez Bankası'nın araç bağımsızlığına ve fiyat istikrarı hedefine saygı göstererek faiz kararlarına siyasi müdahaleyi durdur.",
                     "effects": {"justice": 9, "people": 7, "treasury": -2, "military": 0, "authority": -3},
                     "log": "Merkez Bankası bağımsızlığı korundu; küresel piyasalarda Türkiye'nin ekonomi yönetimine güven tavan yaptı."},
                    {"label": "İş dünyası, ihracatçılar ve sendikalarla 'Orta Vadeli Program' (OVP) üzerinde mutabakat sağlayarak enflasyon hedeflerini açıkla.",
                     "effects": {"justice": -6, "people": 8, "treasury": -3, "military": 0, "authority": 7},
                     "log": "Piyasalarla şeffaf iletişim kuruldu; OVP hedefleri reel sektör tarafından çıpa kabul edildi."},
                    {"label": "Politika faizini kademeli olarak %50'ye yükselt ve kamuda tasarruf genelgesiyle Hazine harcamalarını sıkı kontrol altına al.",
                     "effects": {"justice": -2, "people": -7, "treasury": 10, "military": 0, "authority": 5},
                     "log": "Swap hariç net rezervler artıya geçti; yabancı sermaye girişiyle döviz rezervleri tarihi rekor kırdı."},
                    {"label": "Kayıtdışı ekonomi, sahte fatura ve vergi kaçakçılarına karşı Maliye denetmenlerini ve vergi müfettişlerini sahaya dök.",
                     "effects": {"justice": -3, "people": -8, "treasury": 0, "military": 8, "authority": 8},
                     "log": "Vergi tabanı genişletildi; lüks tüketim ve beyan edilmeyen gelirler sıkı denetimle vergilendirildi."},
                    {"label": "Türkiye'yi FATF Gri Listesi'nden çıkaran ve kripto varlıkları regüle eden 'Mali Eylem ve Tasarruf Reform Kanunu' çıkar.",
                     "effects": {"justice": 8, "people": 4, "treasury": -6, "military": 0, "authority": 9},
                     "log": "Türkiye gri listeden başarıyla çıktı; kredi derecelendirme kuruluşları Türkiye'nin notunu peş peşe artırdı."}
                ]
            elif "Kira" in title or "Arabuluculuk" in title or "Sulh Hukuk" in title:
                options_map[eid] = [
                    {"label": "Ev sahibi ve kiracı arasındaki davalarda Borçlar Kanunu ve hakkaniyet ilkelerini gözeterek tahliye davalarında yığılmayı önle.",
                     "effects": {"justice": 9, "people": 8, "treasury": -2, "military": 0, "authority": -3},
                     "log": "Sulh Hukuk Mahkemeleri'nde adli süreçler hızlandırıldı; haksız tahliye ve fırsatçı zamlara sınır getirildi."},
                    {"label": "Kira uyuşmazlıklarında 'Zorunlu Arabuluculuk' mekanizmasını devreye sokarak tarafların %60'ının mahkemesiz sulh olmasını sağla.",
                     "effects": {"justice": -5, "people": 9, "treasury": -2, "military": 0, "authority": 7},
                     "log": "Yüz binlerce dosya mahkemeye gitmeden arabulucuda çözüldü; komşuluk ve kira barışı korundu."},
                    {"label": "Dar gelirli kiracılar için Hazine destekli 'Sosyal Konut Seferberliği' başlatarak piyasadaki fahiş kira balonunu patlat.",
                     "effects": {"justice": -2, "people": -6, "treasury": 9, "military": 0, "authority": 4},
                     "log": "Arz tarafı güçlendirildi; TOKİ eliyle 250 bin sosyal konut inşa edilerek kira enflasyonu dizginlendi."},
                    {"label": "Kayıt dışı kiralama yapan, elden nakit para alan ve yabancılara yasadışı kiralık ev tutanlara karşı maliye zabıtasını denetime çıkar.",
                     "effects": {"justice": -3, "people": -7, "treasury": 0, "military": 8, "authority": 8},
                     "log": "Kiralık konut piyasasında mali denetim sağlandı; vergi kaçıran ev sahiplerine ağır cezalar kesildi."},
                    {"label": "%25 tavanını TÜFE 12 aylık ortalamasına bağlayan ve kira sözleşmelerini e-Devlet'e taşıyan 'Konut Kiraları Reform Kanunu' çıkar.",
                     "effects": {"justice": 8, "people": 4, "treasury": -6, "military": 0, "authority": 8},
                     "log": "Kira sözleşmeleri e-Devlet güvencesine alındı; sahte tahliye taahhütnameleri tarihe karıştı."}
                ]
            elif "Asgari Ücret" in title or "EYT" in title:
                options_map[eid] = [
                    {"label": "Çalışanların refahını korumak için asgari ücretten gelir ve damga vergisini tamamen kaldıran anayasal sosyal adalet adımını at.",
                     "effects": {"justice": 9, "people": 9, "treasury": -3, "military": 0, "authority": -2},
                     "log": "Tarihi vergi devrimi yapıldı; tüm çalışanların maaşındaki vergi yükü devlet tarafından üstlenildi."},
                    {"label": "TÜRK-İŞ, TİSK ve hükümet heyetiyle Asgari Ücret Tespit Komisyonu'nda enflasyonu ezen dengeli bir mutabakat imzala.",
                     "effects": {"justice": -6, "people": 9, "treasury": -3, "military": 0, "authority": 7},
                     "log": "Milyonlarca işçinin yüzü güldü; ara zamlarla çalışanlar yüksek enflasyona karşı korundu."},
                    {"label": "EYT düzenlemesiyle emekli olan 2 milyon vatandaşın kıdem tazminatı için işverenlere KGF kefaletli Hazine kredisi aç.",
                     "effects": {"justice": -2, "people": -7, "treasury": 9, "military": 0, "authority": 4},
                     "log": "İş dünyasının nakit krizi önlendi; EYT'lilerin tazminatları ve ilk emekli maaşları tıkır tıkır ödendi."},
                    {"label": "Sahte işyeri açıp kendisini sigortalı göstererek haksız emekli olan şebekelere karşı SGK denetmenlerini seferber et.",
                     "effects": {"justice": -3, "people": -7, "treasury": 0, "military": 8, "authority": 8},
                     "log": "Sahte sigortalılık çeteleri çökertildi; kamunun milyarlarca liralık emeklilik kaynağı korundu."},
                    {"label": "Emekli taban aylıklarını ve sosyal güvenlik dengesini sürdürülebilir kılan 'Sosyal Güvenlik ve Emeklilik Reform Kanunu' çıkar.",
                     "effects": {"justice": 8, "people": 4, "treasury": -8, "military": 0, "authority": 8},
                     "log": "Emeklilerin kök maaş mağduriyetleri giderildi; sosyal güvenlik sistemi kalıcı bütçe zırhına kavuşturuldu."}
                ]
            else:
                options_map[eid] = [
                    {"label": "Ekonomik kararlarda hukuki öngörülebilirlik, rekabet kuralları ve mülkiyet hakkını tavizsiz gözet.",
                     "effects": {"justice": 8, "people": 7, "treasury": -2, "military": 0, "authority": -3},
                     "log": "Hukuki güvence piyasaya hakim kılındı; yatırımcı güveni ve tüketici hakları korundu."},
                    {"label": "İş dünyası, esnaf ve tüketici dernekleriyle istişare kurulları toplayarak piyasada fiyat istikrarı uzlaşısı sağla.",
                     "effects": {"justice": -6, "people": 8, "treasury": -2, "military": 0, "authority": 7},
                     "log": "Sosyal diyalog işletildi; piyasadaki panik ve fiyatlama davranışlarındaki bozulma yatıştırıldı."},
                    {"label": "Hazine kasasını korumak ve enflasyonu düşürmek için kamu harcamalarında sıkı tasarruf tedbirlerini tavizsiz uygula.",
                     "effects": {"justice": -2, "people": -6, "treasury": 9, "military": 0, "authority": 4},
                     "log": "Mali disiplin tesis edildi; kamu bütçesi açık vermeden dengelendi."},
                    {"label": "Stokçuluk, fahiş fiyat ve karaborsa fırsatçılarına karşı ticaret müfettişlerini ve zabıtayı sahaya dök.",
                     "effects": {"justice": -3, "people": -7, "treasury": 0, "military": 8, "authority": 8},
                     "log": "Piyasada fırsatçılara göz açtırılmadı; fahiş fiyat koyan zincirlere caydırıcı cezalar kesildi."},
                    {"label": "Türkiye ekonomisinin yapısal reformlarını hayata geçiren 'Mali İstikrar ve Fiyat İstikrarı Reform Kanunu' çıkar.",
                     "effects": {"justice": 8, "people": 4, "treasury": -7, "military": 0, "authority": 8},
                     "log": "Yapısal reformlar yasalaştı; Türkiye sürdürülebilir büyüme ve dezenflasyon rotasına oturdu."}
                ]

    print(f"Total options generated for Batch 5: {len(options_map)}")
    updated_deck = apply_options_to_deck(deck, options_map)
    save_modern_deck(updated_deck)

if __name__ == '__main__':
    generate_domains_13_to_15()
