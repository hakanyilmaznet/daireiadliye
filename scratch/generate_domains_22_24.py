import json
from deck_utils import load_modern_deck, save_modern_deck, apply_options_to_deck

# Domain 22: Ticaret, Tüketici Hakları ve Pazar (tr_vaka_731 - tr_vaka_760)
# Domain 23: Enerji Piyasası ve Madencilik (tr_vaka_761 - tr_vaka_790)
# Domain 24: Şehir Hayatı ve Yerel Dinamikler (tr_vaka_791 - tr_vaka_820)

def generate_domains_22_to_24():
    deck = load_modern_deck()
    print("Building realistic options for Domains 22, 23, and 24 (tr_vaka_731 to tr_vaka_820)...")
    options_map = {}

    for i in range(730, 820):
        ev = deck[i]
        eid = ev['id']
        title = ev['title']
        desc = ev['desc']

        # DOMAIN 22: Ticaret, Tüketici Hakları ve Pazar (730 to 759: tr_vaka_731 to tr_vaka_760)
        if 730 <= i <= 759:
            if "Zincir Market" in title or "Kartel" in title or "Haksız Fiyat" in title:
                options_map[eid] = [
                    {"label": "Rekabet Kurumu marifetiyle zincir marketlerin 'hub-and-spoke' kartel anlaşmalarını belgele ve milyarlarca liralık ceza kes.",
                     "effects": {"justice": 10, "people": 8, "treasury": -2, "military": 0, "authority": -2},
                     "log": "Kartel çetesi çökertildi; 5 büyük zincir markete rekabet kanununu ihlalden 2.7 milyar TL rekor ceza kesildi."},
                    {"label": "Türkiye Perakendeciler Federasyonu ve yerel marketlerle görüşerek 1000 temel gıda ürününde 1 yıl fiyat sabitleme mutabakatı yap.",
                     "effects": {"justice": -5, "people": 9, "treasury": -3, "military": 0, "authority": 7},
                     "log": "Piyasada fiyat istikrarı sağlandı; yerel marketler un, yağ ve şekerde zam yapmayarak vatandaşı korudu."},
                    {"label": "Haksız Fiyat Değerlendirme Kurulu'nun kestiği idari para cezalarını doğrudan Hazine gelirlerine irad kaydet.",
                     "effects": {"justice": -2, "people": -6, "treasury": 10, "military": 0, "authority": 5},
                     "log": "Hazine kasasına gelir sağlandı; fahiş fiyat artışıyla haksız kazanç sağlayanların paraları devlete geçti."},
                    {"label": "Ticaret Bakanlığı müfettişleri ve zabıta ekiplerini 81 ilde eşzamanlı etiket ve stok denetimine çıkar.",
                     "effects": {"justice": -2, "people": -7, "treasury": 0, "military": 9, "authority": 9},
                     "log": "Market depolarında stokçular yakalandı; raf ile kasa arasındaki fiyat hilelerine anında ceza yağdı."},
                    {"label": "Marketlerde tarladan sofraya fiyat takibini zorunlu kılan 'Hal Kanunu ve Perakende Ticaret Reformu' çıkar.",
                     "effects": {"justice": 8, "people": 4, "treasury": -6, "military": 0, "authority": 8},
                     "log": "Aracı ve komisyoncu rantı kırıldı; üretici ile tüketici arasındaki fahiş makas kanunla daraltıldı."}
                ]
            elif "Tanzim Satış" in title or "Tarım Kredi" in title or "Kırmızı Et" in title:
                options_map[eid] = [
                    {"label": "Et ve Süt Kurumu (ESK) ile spekülatif et stokçuluğu yapan büyük tüccarlar hakkında adli ve mali soruşturma açtır.",
                     "effects": {"justice": 9, "people": 8, "treasury": -2, "military": 0, "authority": -2},
                     "log": "Et piyasasındaki fırsatçılar yargıya sevk edildi; spekülatörlerin kesimhanelerde et saklaması önlendi."},
                    {"label": "Büyükşehir meydanlarında belediyeler ve Tarım Kredi eliyle tanzim satış çadırları kurarak sebzeyi maliyetine sat.",
                     "effects": {"justice": -5, "people": 10, "treasury": -3, "military": 0, "authority": 7},
                     "log": "Dar gelirli rahat nefes aldı; domates, biber ve patateste aracı vurgunu kırıldı, fiyatlar yarı yarıya indi."},
                    {"label": "Tarım Kredi Kooperatif Marketlerinin 3 bin şubeye ulaşması için Hazine destekli ucuz kredi hattı aç.",
                     "effects": {"justice": -2, "people": -6, "treasury": 9, "military": 0, "authority": 4},
                     "log": "Market ağı 81 ile yayıldı; Hazine kaynaklarıyla doğrudan üreticiden alınıp tüketiciye ulaştırılan model büyütüldü."},
                    {"label": "Besihanelerde et kesimini durdurup piyasayı kilitlemeye çalışan lobilere karşı tarım zabıtasıyla baskın yap.",
                     "effects": {"justice": -2, "people": -7, "treasury": 0, "military": 9, "authority": 8},
                     "log": "Piyasada suni et kıtlığı yaratılması engellendi; kombinalarda kesimler hızla başlatıldı."},
                    {"label": "Gıda arz güvenliğini sağlayan ve temel gıda maddelerine tavan fiyat getiren 'Milli Gıda Güvenliği Kanunu' çıkar.",
                     "effects": {"justice": 8, "people": 4, "treasury": -7, "military": 0, "authority": 8},
                     "log": "Gıda fiyatları devlet güvencesine alındı; spekülatif fiyat hareketlerine karşı yasal kalkan kuruldu."}
                ]
            elif "6 Ay ve 6 Bin Kilometre" in title or "İkinci El" in title:
                options_map[eid] = [
                    {"label": "Sıfır araçları stoklayıp liste fiyatının üzerinde listeleyen yetkili bayilerin ticaret lisanslarını iptal et.",
                     "effects": {"justice": 10, "people": 8, "treasury": -2, "military": 0, "authority": -2},
                     "log": "Otomotiv fırsatçılarına tokat vuruldu; haksız kazanç sağlayan yüzlerce galeri ve bayiye kapatma cezası kesildi."},
                    {"label": "Otomotiv Yetkili Satıcıları Derneği (OYDER) ile görüşerek liste fiyatından satış ve şeffaf teslimat taahhüdü al.",
                     "effects": {"justice": -5, "people": 9, "treasury": -2, "military": 0, "authority": 7},
                     "log": "Piyasa rayına oturdu; vatandaşların sıfır araca liste fiyatından erişmesi güvenceye bağlandı."},
                    {"label": "Yılda 3'ten fazla araç alıp satan ve vergi kaçıran al-satçılardan geçmişe dönük vergi ve cezaları Hazineye tahsil et.",
                     "effects": {"justice": -2, "people": -6, "treasury": 10, "military": 0, "authority": 5},
                     "log": "Kayıtdışı oto ticaretine vergi darbesi vuruldu; Hazineye yüz milyonlarca liralık vergi geliri girdi."},
                    {"label": "Oto galericiler siteleri ve otoparklarda saklanan sıfır kilometre plakalı araçları polis drone'larıyla tespit et.",
                     "effects": {"justice": -2, "people": -7, "treasury": 0, "military": 9, "authority": 9},
                     "log": "Stokçuluk yuvaları basıldı; gizli otoparklarda saklanan yüzlerce lüks araç piyasaya sürüldü."},
                    {"label": "İkinci el araç satışlarında '6 Ay ve 6 Bin Km' şartını getiren 'Motorlu Kara Taşıtları Ticareti Kanunu' çıkar.",
                     "effects": {"justice": 8, "people": 5, "treasury": -6, "military": 0, "authority": 8},
                     "log": "Otomobil yatırım aracı olmaktan çıkarıldı; ikinci el araç fiyatlarındaki fahiş balon patlatıldı."}
                ]
            else:
                options_map[eid] = [
                    {"label": "Ticari ilişkilerde tüketici hakları, sözleşme serbestisi ve dürüstlük kuralını mahkemelerde tavizsiz koru.",
                     "effects": {"justice": 8, "people": 7, "treasury": -2, "military": 0, "authority": -3},
                     "log": "Tüketicinin hakkı korundu; hileli satış ve fahiş fiyat uygulamalarına karşı yargı devreye girdi."},
                    {"label": "Esnaf odaları, ticaret odaları ve tüketici dernekleriyle istişare kurulları toplayarak pazar uzlaşısı sağla.",
                     "effects": {"justice": -6, "people": 8, "treasury": -2, "military": 0, "authority": 7},
                     "log": "Piyasada sosyal uzlaşı sağlandı; esnaf ile müşteri arasındaki anlaşmazlıklar diyalogla giderildi."},
                    {"label": "Ticaret hacmini artırırken kayıtdışı işlemleri önleyerek Hazine vergi gelirlerini koruma altına al.",
                     "effects": {"justice": -2, "people": -6, "treasury": 8, "military": 0, "authority": 4},
                     "log": "Vergi kayıpları engellendi; perakende ticaret Hazine denetimine alındı."},
                    {"label": "Karaborsa, sahte ürün ve kaçak ticaret yapan şebekelere karşı maliye ve polis zabıtasını göreve çağır.",
                     "effects": {"justice": -2, "people": -7, "treasury": 0, "military": 9, "authority": 8},
                     "log": "Pazar yerlerinde asayiş sağlandı; kaçak ve sahte ürünlerin piyasaya girmesi engellendi."},
                    {"label": "Piyasa gözetimi ve tüketici hakem heyetlerini güçlendiren 'Tüketicinin Korunması Reform Kanunu' çıkar.",
                     "effects": {"justice": 8, "people": 4, "treasury": -6, "military": 0, "authority": 8},
                     "log": "Tüketici hakları kanunla tahkim edildi; ayıplı mal ve haksız şartlara karşı yaptırımlar ağırlaştırıldı."}
                ]

        # DOMAIN 23: Enerji Piyasası ve Madencilik (760 to 789: tr_vaka_761 to tr_vaka_790)
        elif 760 <= i <= 789:
            if "Eşel Mobil" in title or "Akaryakıt" in title:
                options_map[eid] = [
                    {"label": "Akaryakıt kaçakçılığı, 10 numara yağ ve faturasız yakıt satan istasyonları EPDK denetimiyle kapatıp savcılığa sevk et.",
                     "effects": {"justice": 9, "people": 8, "treasury": -2, "military": 0, "authority": -2},
                     "log": "Akaryakıtta vergi kaçakçılığı önlendi; ulusal marker denetimiyle kaçak petrol şebekeleri çökertildi."},
                    {"label": "Petrol fiyatları tırmanırken Eşel Mobil Sistemi ile ÖTV'den feragat ederek pompa fiyatlarını sabit tut.",
                     "effects": {"justice": -5, "people": 10, "treasury": -4, "military": 0, "authority": 7},
                     "log": "Vatandaş ve nakliyeci korundu; akaryakıt zamlarının enflasyonu ve nakliye maliyetlerini vurması engellendi."},
                    {"label": "Ulusal Taşıt Tanıma Sistemi (UTTS) zorunluluğu getirerek akaryakıt fişlerindeki yıllık 15 milyar liralık KDV kaybını Hazineye kazandır.",
                     "effects": {"justice": -2, "people": -6, "treasury": 10, "military": 0, "authority": 5},
                     "log": "Hazine kasasına dev gelir girdi; şirketlerin sahte akaryakıt fişiyle gider göstermesi çipli sistemle sıfırlandı."},
                    {"label": "Kaçak akaryakıt boru hatları ve tanker kaçakçılığına karşı jandarma ve gümrük muhafaza timlerini sınıra yığ.",
                     "effects": {"justice": -2, "people": -7, "treasury": 0, "military": 9, "authority": 8},
                     "log": "Sınır kapılarında kaçak yakıt geçişleri durduruldu; organize petrol kaçakçıları yakalandı."},
                    {"label": "Enerji Piyasası Düzenleme Kurumu (EPDK) denetim yetkilerini artıran 'Petrol Piyasası Reform Kanunu' çıkar.",
                     "effects": {"justice": 8, "people": 4, "treasury": -6, "military": 0, "authority": 8},
                     "log": "Akaryakıt sektörü tam şeffaflığa kavuştu; dağıtıcı ve bayiler arasındaki kar payı kanunla düzenlendi."}
                ]
            elif "Bor Karbür" in title or "Nadir Toprak" in title:
                options_map[eid] = [
                    {"label": "Beylikova'daki 694 milyon tonluk nadir toprak elementleri ve Eti Maden rezervlerini milli egemenlik tesciline al.",
                     "effects": {"justice": 9, "people": 8, "treasury": -2, "military": 0, "authority": -2},
                     "log": "Milli maden hakları korundu; dünyanın 2. büyük nadir element rezervi devletin kontrolünde tescillendi."},
                    {"label": "Bandırma ve Eskişehir tesislerinde yerli üniversite ve kimya mühendisleriyle ortak Ar-Ge şurası topla.",
                     "effects": {"justice": -5, "people": 9, "treasury": -2, "military": 0, "authority": 7},
                     "log": "Yerli teknoloji ekosistemi kuruldu; lityum, bor ve çip üretiminde milli kabiliyet geliştirildi."},
                    {"label": "Ham bor satmak yerine tonu 40 bin dolar olan Bor Karbür ve zırh malzemesi üreterek Hazineye devasa ihracat geliri sağla.",
                     "effects": {"justice": -2, "people": -6, "treasury": 10, "military": 0, "authority": 5},
                     "log": "Katma değerli madencilik başladı; Türkiye ham cevher satıcılığından ileri teknoloji ihracatçılığına geçti."},
                    {"label": "Milli maden tesisleri ve zenginleştirme fabrikalarını yabancı siber casusluk ve sabotajlara karşı askeri korumaya al.",
                     "effects": {"justice": -2, "people": -7, "treasury": 0, "military": 9, "authority": 9},
                     "log": "Stratejik maden üsleri korundu; Türkiye'nin nadir element formüllerinin dışarı sızması engellendi."},
                    {"label": "Stratejik madenlerin yabancılara imtiyaz olarak devredilmesini yasaklayan 'Milli Maden ve Tabii Kaynaklar Kanunu' çıkar.",
                     "effects": {"justice": 8, "people": 4, "treasury": -6, "military": 0, "authority": 9},
                     "log": "Bor ve nadir elementler anayasal korumaya alındı; Türkiye'nin yer altı zenginliği geleceğe mühürlendi."}
                ]
            elif "Kademeli Tarife" in title or "Tuz Gölü" in title:
                options_map[eid] = [
                    {"label": "Elektrik ve doğalgaz dağıtım şirketlerinin haksız fatura ve sayaç okuma hatalarını EPDK marifetiyle adli teftişe aç.",
                     "effects": {"justice": 9, "people": 8, "treasury": -2, "military": 0, "authority": -2},
                     "log": "Tüketici hakkı korundu; haksız yere yüksek fatura kesen dağıtım şirketlerine ağır cezalar uygulandı."},
                    {"label": "Dar gelirli hanelerin düşük elektrik ve gaz tüketimini Hazine sübvansiyonuyla %50 indirimli faturalandır.",
                     "effects": {"justice": -5, "people": 10, "treasury": -4, "military": 0, "authority": 7},
                     "log": "Sosyal devlet desteği verildi; milyonlarca haneye kış aylarında ısınma ve elektrik desteği doğrudan yansıtıldı."},
                    {"label": "Tuz Gölü Yeraltı Doğalgaz Depolama Tesisinin kapasitesini 5.4 milyar metreküpe çıkararak kış gaz krizlerini bertaraf et.",
                     "effects": {"justice": -2, "people": -6, "treasury": 9, "military": 0, "authority": 5},
                     "log": "Stratejik rezerv kuruldu; kış aylarında spot piyasadan pahalı gaz alımının önüne geçilerek milyarlarca dolar tasarruf edildi."},
                    {"label": "Doğalgaz kompresör istasyonları ve yer altı depolarını olası terör sabotajlarına karşı jandarma üsleriyle koru.",
                     "effects": {"justice": -2, "people": -7, "treasury": 0, "military": 9, "authority": 8},
                     "log": "Enerji arz güvenliği korundu; ulusal gaz iletim şebekesinin kesintisiz çalışması temin edildi."},
                    {"label": "Enerji verimliliği ve akıllı şebeke dönüşümünü zorunlu kılan 'Milli Enerji Verimliliği ve Depolama Kanunu' çıkar.",
                     "effects": {"justice": 8, "people": 4, "treasury": -6, "military": 0, "authority": 8},
                     "log": "Enerji israfı önlendi; Türkiye'nin enerji yoğunluğu azaltılarak küresel standartlara ulaşıldı."}
                ]
            else:
                options_map[eid] = [
                    {"label": "Madencilik ve enerji faaliyetlerinde iş güvenliği, çevre kanunları ve ruhsat şartlarını bağımsız denetle.",
                     "effects": {"justice": 8, "people": 7, "treasury": -2, "military": 0, "authority": -3},
                     "log": "Madenlerde iş güvenliği korundu; çevreye zarar veren kuralsız işletmeler durduruldu."},
                    {"label": "Maden işçileri, sendikalar ve sektör temsilcileriyle ortak istişare meclisi kurarak madencilik barışını sağla.",
                     "effects": {"justice": -6, "people": 8, "treasury": -2, "military": 0, "authority": 7},
                     "log": "Sosyal diyalog sağlandı; maden işçilerinin çalışma koşulları ve ücretleri iyileştirildi."},
                    {"label": "Yerli maden üretimi ve cevher zenginleştirme yatırımlarına Hazine bütçesinden teşvik ve vergi indirimi sağla.",
                     "effects": {"justice": -2, "people": -6, "treasury": 8, "military": 0, "authority": 4},
                     "log": "Milli madencilik desteklendi; yerli kaynaklarla sanayinin hammadde ihtiyacı karşılandı."},
                    {"label": "Ruhsatsız kaçak maden ocaklarına ve kömür hırsızlığına karşı jandarma komandolarıyla baskınlar yap.",
                     "effects": {"justice": -2, "people": -7, "treasury": 0, "military": 9, "authority": 8},
                     "log": "Kaçak madenler kapatıldı; can güvenliğini hiçe sayan merdiven altı işletmeler mühürlendi."},
                    {"label": "Maden çalışanlarına yıpranma payı ve erken emeklilik getiren 'Maden İşçileri ve Sektörel Reform Kanunu' çıkar.",
                     "effects": {"justice": 8, "people": 4, "treasury": -6, "military": 0, "authority": 8},
                     "log": "Madencilerin özlük hakları kanunlaştı; işçi sağlığı en yüksek yasal korumaya alındı."}
                ]

        # DOMAIN 24: Şehir Hayatı ve Yerel Dinamikler (790 to 819: tr_vaka_791 to tr_vaka_820)
        elif 790 <= i <= 819:
            if "Taksi" in title or "UKOME" in title or "Uber" in title:
                options_map[eid] = [
                    {"label": "Taksici esnafının plaka tekeli ve fahiş hava parası düzenini Rekabet Kurumu ve adli makamlarca denetime tabi tut.",
                     "effects": {"justice": 9, "people": 8, "treasury": -2, "military": 0, "authority": -2},
                     "log": "Plaka karaborsasına neşter vuruldu; taksici odasının vatandaşı mağdur eden tekelci baskısı kırıldı."},
                    {"label": "İBB ve Taksiciler Odası'nı UKOME masasında uzlaştırarak 2.500 yeni uygulama tabanlı taksinin hizmete girmesini sağla.",
                     "effects": {"justice": -5, "people": 9, "treasury": -2, "military": 0, "authority": 7},
                     "log": "Ulaşım krizi çözüldü; İstanbul halkı dijital uygulama üzerinden temiz ve güvenli taksilere kavuştu."},
                    {"label": "Yeni taksi plakası ihalelerinden elde edilen milyarlarca liralık geliri belediye ve Hazine raylı sistem bütçesine aktar.",
                     "effects": {"justice": -2, "people": -6, "treasury": 9, "military": 0, "authority": 4},
                     "log": "Kamu bütçesine kaynak sağlandı; plaka ihale gelirleri metro hatlarının inşasına aktarıldı."},
                    {"label": "Yolcu seçen, turist dolandıran ve taksimetre açmayan korsan ve fırsatçı taksicilere karşı sivil trafik zabıtası görevlendir.",
                     "effects": {"justice": -2, "people": -7, "treasury": 0, "military": 8, "authority": 9},
                     "log": "Taksi denetimleri sıkılaştırıldı; vatandaşa kaba davranan şoförlerin ruhsatları anında askıya alındı."},
                    {"label": "Tüm taksilerde kamera, panik butonu ve kredi kartı pos cihazını zorunlu kılan 'Şehir İçi Yolcu Taşımacılığı Kanunu' çıkar.",
                     "effects": {"justice": 8, "people": 4, "treasury": -6, "military": 0, "authority": 8},
                     "log": "Taksi taşımacılığı kurumsallaştı; taksici cinayetleri ve müşteri mağduriyetleri önlendi."}
                ]
            elif "Mansur Yavaş" in title or "Ekrem İmamoğlu" in title or "Şeffaf İhale" in title:
                options_map[eid] = [
                    {"label": "Belediye ihalelerinin canlı yayında, açık eksiltmeyle yapılmasını ve tüm harcamaların Sayıştay denetimine açılmasını sağla.",
                     "effects": {"justice": 10, "people": 9, "treasury": -2, "military": 0, "authority": -2},
                     "log": "Şeffaf belediyecilik çağı başladı; kapalı kapılar ardındaki rant ihaleleri milletin gözü önünde canlı yayınlandı."},
                    {"label": "Merkezi idare ile büyükşehir belediyeleri arasında metro ve altyapı projelerinde siyasi çatışmayı bırakıp protokol imzala.",
                     "effects": {"justice": -5, "people": 9, "treasury": -3, "military": 0, "authority": 7},
                     "log": "Hizmet öncelendi; başkent ve metropollerde ulaşım projeleri hükümet-belediye işbirliğiyle hızlandırıldı."},
                    {"label": "Canlı yayınlanan ihalelerde sağlanan %30'luk kırım oranlarıyla belediye bütçelerinde milyarlarca lira tasarruf et.",
                     "effects": {"justice": -2, "people": -6, "treasury": 9, "military": 0, "authority": 4},
                     "log": "Kamuda israf önlendi; tasarruf edilen kaynaklar dar gelirli ailelere et ve doğalgaz desteği olarak dağıtıldı."},
                    {"label": "Belediyelerde terör iltisaklı kişilerin istihdam edilmesini önlemek için emniyet güvenlik soruşturmalarını tavizsiz uygula.",
                     "effects": {"justice": -2, "people": -7, "treasury": 0, "military": 9, "authority": 9},
                     "log": "Kamu kurumlarının güvenliği korundu; belediye kaynaklarının terör örgütlerine aktarılması engellendi."},
                    {"label": "Tüm yerel yönetim ihalelerinin canlı yayınlanmasını ve EKAP üzerinden yapılmasını zorunlu kılan 'Şeffaf Yerel Yönetim Kanunu' çıkar.",
                     "effects": {"justice": 9, "people": 5, "treasury": -6, "military": 0, "authority": 8},
                     "log": "İhalelerde yolsuzluk imkansız hale getirildi; vatandaşın vergileri tam denetim altına alındı."}
                ]
            elif "Sokak Hayvanları" in title or "5199" in title:
                options_map[eid] = [
                    {"label": "Sahipsiz ve saldırgan köpeklerin çocukları ve yaşlıları parçalamasını önlemek için anayasal yaşam hakkını en üstte tut.",
                     "effects": {"justice": 9, "people": 8, "treasury": -2, "military": 0, "authority": -2},
                     "log": "Vatandaşın can güvenliği korundu; kuduz ve köpek saldırısı sonucu çocuk kayıplarının önüne geçildi."},
                    {"label": "Hayvansever dernekleri, veteriner hekim odaları ve belediyelerle ortak aşılama, kısırlaştırma ve sahiplendirme seferberliği yap.",
                     "effects": {"justice": -5, "people": 9, "treasury": -3, "military": 0, "authority": 7},
                     "log": "Vicdani denge sağlandı; modern hayvan bakımevlerinde kısırlaştırma ve sahiplendirme kampanyaları hızlandırıldı."},
                    {"label": "81 ilde doğal yaşam alanlı modern hayvan barınakları ve rehabilitasyon merkezleri için belediyelere Hazine fonu aktar.",
                     "effects": {"justice": -2, "people": -6, "treasury": 8, "military": 0, "authority": 4},
                     "log": "Barınak kapasiteleri artırıldı; sokaklardan toplanan hayvanların aç ve bakımsız kalması önlendi."},
                    {"label": "Okul çevreleri, parklar ve hastane bahçelerindeki saldırgan başıboş köpek sürülerini zabıta ve belediye ekiplerince topla.",
                     "effects": {"justice": -2, "people": -7, "treasury": 0, "military": 8, "authority": 9},
                     "log": "Sokaklar yeniden güvenli hale geldi; sabah erken saatte okula giden çocuklar ve cami cemaati güvenceye alındı."},
                    {"label": "Sahipli hayvanları terk etmeyi ağır cezalara bağlayan ve sahipsiz hayvanları rehabilite eden 5199 Sayılı Kanun Reformu'nu çıkar.",
                     "effects": {"justice": 8, "people": 4, "treasury": -6, "military": 0, "authority": 8},
                     "log": "Avrupa standartlarında yasa kabul edildi; hem insan canı korundu hem de hayvanlar korunaklı bakımevlerine alındı."}
                ]
            elif "Kentsel Dönüşüm" in title or "Yarısı Bizden" in title or "Fikirtepe" in title:
                options_map[eid] = [
                    {"label": "Deprem riski altındaki binaların dönüşümünde hak sahipliği anlaşmazlıklarını hızla çözecek ihtisas mahkemelerini görevlendir.",
                     "effects": {"justice": 9, "people": 8, "treasury": -2, "military": 0, "authority": -2},
                     "log": "Kentsel dönüşümde hukuki tıkanıklıklar aşıldı; tek bir mülk sahibinin yüzlerce aileyi rehin alması engellendi."},
                    {"label": "İstanbul'da 'Yarısı Bizden' kampanyasıyla evini yenilemek isteyen vatandaşlara 700 bin TL hibe ve uygun vadeli kredi ver.",
                     "effects": {"justice": -5, "people": 10, "treasury": -4, "military": 0, "authority": 7},
                     "log": "Vatandaşın tabut binalardan kurtulması sağlandı; yüz binlerce konut güvenli binalara dönüştürüldü."},
                    {"label": "Fikirtepe'de müteahhitlerin yarım bıraktığı 60 bin konutluk alanı TOKİ ve Emlak Konut ile devralarak şantiyeleri tamamla.",
                     "effects": {"justice": -2, "people": -6, "treasury": 9, "military": 0, "authority": 5},
                     "log": "Yıllardır çadırlarda bekleyen Fikirtepe mağdurları evlerine kavuştu; devlet güvencesiyle inşaatlar bitirildi."},
                    {"label": "Kaçak inşaat yapan, çürük malzeme kullanan ve kaçak kat çıkan sorumsuz müteahhitlerin inşaatlarını derhal mühürle.",
                     "effects": {"justice": -2, "people": -7, "treasury": 0, "military": 9, "authority": 9},
                     "log": "İmar denetimi tavizsiz işletildi; afet riski taşıyan kaçak yapıların yükselmesine izin verilmedi."},
                    {"label": "Riskli binalarda kentsel dönüşüm kararını salt çoğunluğa (yarıdan bir fazla) bağlayan 'Kentsel Dönüşüm Başkanlığı Kanunu' çıkar.",
                     "effects": {"justice": 8, "people": 5, "treasury": -7, "military": 0, "authority": 9},
                     "log": "Dönüşümün önündeki bürokratik engeller yıkıldı; Türkiye genelinde 6.5 milyon riskli konutun yenilenme süreci hızlandı."}
                ]
            else:
                options_map[eid] = [
                    {"label": "Şehirleşme, imar ve yerel yönetim hizmetlerinde hukukun üstünlüğü ve imar planı ilkelerini tavizsiz koru.",
                     "effects": {"justice": 8, "people": 7, "treasury": -2, "military": 0, "authority": -3},
                     "log": "İmar disiplini sağlandı; şehir planlarına aykırı keyfi yapılaşmalar engellendi."},
                    {"label": "Mahalle muhtarları, sivil toplum ve ilçe sakinleriyle diyalog kurarak yerel hizmetlerde halkın rızasını al.",
                     "effects": {"justice": -6, "people": 8, "treasury": -2, "military": 0, "authority": 7},
                     "log": "Vatandaşın talepleri karşılandı; mahalle ölçeğinde katılımcı belediyecilik uygulandı."},
                    {"label": "Yerel altyapı, çevre ve park yatırımları için İller Bankası ve Hazine bütçesinden planlı finansman sağla.",
                     "effects": {"justice": -2, "people": -6, "treasury": 8, "military": 0, "authority": 4},
                     "log": "Belediye yatırımları bütçeden karşılandı; şehirlerin altyapı eksikleri tamamlandı."},
                    {"label": "Kaçak otopark mafyası ve kaldırımları işgal eden kanunsuz unsurlara karşı zabıta ve polis denetimini artır.",
                     "effects": {"justice": -2, "people": -7, "treasury": 0, "military": 9, "authority": 8},
                     "log": "Şehirlerde kamu nizamı korundu; sokak eşkıyalığına ve korsan otoparkçılara son verildi."},
                    {"label": "Büyükşehir ve ilçe belediyelerinin imar yetkilerini şeffaf kurallara bağlayan 'Belediyeler ve İmar Kanunu Reformu' çıkar.",
                     "effects": {"justice": 8, "people": 4, "treasury": -6, "military": 0, "authority": 8},
                     "log": "Yerel yönetim mevzuatı güncellendi; çarpık kentleşmenin önüne kalıcı kanuni set çekildi."}
                ]

    print(f"Total options generated for Batch 8: {len(options_map)}")
    updated_deck = apply_options_to_deck(deck, options_map)
    save_modern_deck(updated_deck)

if __name__ == '__main__':
    generate_domains_22_to_24()
