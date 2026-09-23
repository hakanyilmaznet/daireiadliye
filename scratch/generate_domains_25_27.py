import json
from deck_utils import load_modern_deck, save_modern_deck, apply_options_to_deck

# Domain 25: Sosyal Güvenlik ve Çalışma Hayatı (tr_vaka_821 - tr_vaka_850)
# Domain 26: Kamu Hukuku ve Yargı Reformları (tr_vaka_851 - tr_vaka_880)
# Domain 27: Tarım, Hayvancılık ve Gıda Güvenliği (tr_vaka_881 - tr_vaka_910)

def generate_domains_25_to_27():
    deck = load_modern_deck()
    print("Building realistic options for Domains 25, 26, and 27 (tr_vaka_821 to tr_vaka_910)...")
    options_map = {}

    for i in range(820, 910):
        ev = deck[i]
        eid = ev['id']
        title = ev['title']
        desc = ev['desc']

        # DOMAIN 25: Sosyal Güvenlik ve Çalışma Hayatı (820 to 849: tr_vaka_821 to tr_vaka_850)
        if 820 <= i <= 849:
            if "Taşeron" in title or "Kadro" in title:
                options_map[eid] = [
                    {"label": "Kamuda çalışan taşeron işçilerin daimi işçi kadrosuna geçişini şeffaf güvenlik soruşturması ve liyakatle tamamla.",
                     "effects": {"justice": 9, "people": 9, "treasury": -3, "military": 0, "authority": -2},
                     "log": "Taşeron ayıbına son verildi; 900 bin kamu işçisi devlet güvencesine ve sendikal haklarına kavuştu."},
                    {"label": "İşçi sendikalarıyla Toplu İş Sözleşmesi (TİS) masasına oturarak ücret artışlarını enflasyon oranında dengele.",
                     "effects": {"justice": -6, "people": 9, "treasury": -3, "military": 0, "authority": 7},
                     "log": "İş barışı sağlandı; kamu işçilerinin ücret ve ikramiye hakları uzlaşıyla bağıtlandı."},
                    {"label": "Kadroya geçen işçilerin kıdem tazminatı ve özlük giderlerini Hazine merkezi bütçesinde planlı tasarrufla karşıla.",
                     "effects": {"justice": -2, "people": -6, "treasury": 8, "military": 0, "authority": 4},
                     "log": "Kamu maliyesinde denge korundu; taşeron firmaların aracı komisyonları kaldırılarak tasarruf sağlandı."},
                    {"label": "Kadro sürecini istismar eden sahte taşeron şirket yöneticileri ve rüşvet çarkına karşı mali polisi görevlendir.",
                     "effects": {"justice": -2, "people": -7, "treasury": 0, "military": 9, "authority": 8},
                     "log": "İstihdam yolsuzluğu engellendi; sadece hak eden gerçek işçilerin kadroya girmesi sağlandı."},
                    {"label": "Kamuda güvencesiz ve kiralık işçiliği kesin olarak yasaklayan 696 Sayılı KHK Reformu'nu yasalaştır.",
                     "effects": {"justice": 8, "people": 4, "treasury": -6, "military": 0, "authority": 8},
                     "log": "İş güvencesi kanunlaştı; Türkiye'nin en büyük istihdam devrimi yasal teminata alındı."}
                ]
            elif "3600 Ek Gösterge" in title or "Memur" in title or "Bayram İkramiyesi" in title:
                options_map[eid] = [
                    {"label": "Öğretmen, polis, hemşire ve din görevlilerinin 3600 ek gösterge haklarını eşitlik ve kariyer liyakatine göre tescille.",
                     "effects": {"justice": 9, "people": 9, "treasury": -3, "military": 0, "authority": -2},
                     "log": "Yılların beklentisi karşılandı; 5.3 milyon kamu personeli ve emeklisinin maaşı ve ikramiyesi yükseltildi."},
                    {"label": "Memur-Sen ve Kamu-Sen heyetleriyle Kamu Görevlileri Hakem Kurulu'nda zam oranlarında sosyal uzlaşı sağla.",
                     "effects": {"justice": -5, "people": 9, "treasury": -3, "military": 0, "authority": 7},
                     "log": "Memur grevi önlendi; kamu çalışanlarının refah payı ve taban aylıkları uzlaşıyla artırıldı."},
                    {"label": "16 milyon emekliye yılda iki kez ödenen bayram ikramiyelerinin finansmanını Hazine vergi gelirlerinden karşıla.",
                     "effects": {"justice": -2, "people": -6, "treasury": 8, "military": 0, "authority": 4},
                     "log": "Emeklilerin bayram sevinci korundu; Hazine bütçesinde emekli ikramiyeleri planlı ödendi."},
                    {"label": "Memurların çalışma saatlerini ve mesai disiplinini denetleyerek kamuda verimlilik kaybını önle.",
                     "effects": {"justice": -2, "people": -7, "treasury": 0, "military": 8, "authority": 9},
                     "log": "Kamu hizmetlerinde disiplin korundu; vatandaşın devlet dairelerindeki işleri aksatılmadı."},
                    {"label": "Devlet Memurları Kanunu'nda kariyer baremlerini yenileyen 'Kamu Personel Rejimi Reform Kanunu' çıkar.",
                     "effects": {"justice": 8, "people": 4, "treasury": -7, "military": 0, "authority": 8},
                     "log": "Memur maaş hiyerarşisi adil hale getirildi; emekli maaşları arasındaki uçurumlar kapatıldı."}
                ]
            elif "Moto-Kurye" in title or "Tekel İşçileri" in title:
                options_map[eid] = [
                    {"label": "Dijital platformlarda çalışan moto-kuryeleri ve esnaf-kuryeleri 'işçi' statüsünde koruyup sendikal hak tanı.",
                     "effects": {"justice": 9, "people": 9, "treasury": -2, "military": 0, "authority": -2},
                     "log": "Kuryelerin kölelik düzenine son verildi; hız baskısı ve kaza riskine karşı yasal koruma sağlandı."},
                    {"label": "Platform patronları ve kurye dernekleriyle asgari paket başı ücret ve dinlenme haklarında uzlaşma sağla.",
                     "effects": {"justice": -5, "people": 9, "treasury": -2, "military": 0, "authority": 7},
                     "log": "Sokak grevleri yatıştırıldı; kuryelerin insani çalışma şartları şirketlerle müzakere edildi."},
                    {"label": "Kuryelerin kaza ve meslek hastalığı tazminatları için şirketlerden zorunlu iş kazası prim fonu tahsil et.",
                     "effects": {"justice": -2, "people": -6, "treasury": 8, "military": 0, "authority": 4},
                     "log": "Kamuya yük olmadan özel güvence fonu kuruldu; kazada yaralanan kuryelere maaş bağlandı."},
                    {"label": "Trafikte kurallara uymayan, yayaları ezen ve kaldırımlardan giden kuryelere karşı trafik polisini denetime çıkar.",
                     "effects": {"justice": -2, "people": -7, "treasury": 0, "military": 9, "authority": 8},
                     "log": "Trafik düzeni korundu; kurye kazaları ve yaya yaralanmalarının önüne geçildi."},
                    {"label": "Dijital platform işçilerinin haklarını Avrupa normlarında koruyan 'Platform ve Kurye Çalışma Kanunu' çıkar.",
                     "effects": {"justice": 8, "people": 4, "treasury": -6, "military": 0, "authority": 8},
                     "log": "Yeni nesil çalışma hayatı mevzuata kavuştu; platform işçileri anayasal güvenceye alındı."}
                ]
            else:
                options_map[eid] = [
                    {"label": "Çalışma hayatında emeğin hakkı, anayasal sendika özgürlüğü ve iş sağlığı ilkelerini tavizsiz gözet.",
                     "effects": {"justice": 8, "people": 7, "treasury": -2, "military": 0, "authority": -3},
                     "log": "İşçi hakları korundu; çalışma hayatında adil ücret ve güvenli çalışma ortamı sağlandı."},
                    {"label": "İşçi sendikaları, işveren örgütleri ve hükümetle Üçlü Danışma Kurulu'nda sosyal mutabakat sağla.",
                     "effects": {"justice": -6, "people": 8, "treasury": -2, "military": 0, "authority": 7},
                     "log": "Sosyal diyalog korundu; çalışma barışını bozan gerilimler uzlaşıyla aşıldı."},
                    {"label": "Sosyal güvenlik prim gelirlerini artırarak SGK aktüeryal dengesini ve Hazine disiplinini koru.",
                     "effects": {"justice": -2, "people": -6, "treasury": 8, "military": 0, "authority": 4},
                     "log": "Kamu maliyesi korundu; sosyal güvenlik açıkları kontrol altında tutuldu."},
                    {"label": "Kayıtdışı kaçak işçi çalıştıran ve çocuk emeğini istismar eden işletmelere polis ve müfettişle baskın yap.",
                     "effects": {"justice": -2, "people": -7, "treasury": 0, "military": 9, "authority": 8},
                     "log": "Kayıtdışı istihdamla mücadele edildi; kaçak işçi çalıştıranlara ağır cezalar kesildi."},
                    {"label": "Çalışma hayatını ve kıdem tazminatı güvencesini tanzim eden 'Milli İstihdam ve İş Kanunu Reformu' çıkar.",
                     "effects": {"justice": 8, "people": 4, "treasury": -6, "military": 0, "authority": 8},
                     "log": "İş kanunu çağdaşlaştırıldı; çalışanların özlük hakları yasal teminata bağlandı."}
                ]

        # DOMAIN 26: Kamu Hukuku ve Yargı Reformları (850 to 879: tr_vaka_851 to tr_vaka_880)
        elif 850 <= i <= 879:
            if "Ombudsman" in title or "Kamu Denetçiliği" in title:
                options_map[eid] = [
                    {"label": "Kamu Denetçiliği Kurumu'nun (Ombudsman) idare aleyhine verdiği 'hukuka aykırılık' kararlarını bakanlıklara zorunlu uygulat.",
                     "effects": {"justice": 10, "people": 8, "treasury": -2, "military": 0, "authority": -2},
                     "log": "Vatandaşın hakkı idareye karşı korundu; kamu kurumlarının mahkemesiz hatasından dönmesi sağlandı."},
                    {"label": "Ombudsmanlık kararlarıyla idare ile mağdur vatandaşlar arasında arabuluculuk masaları kurarak ihtilafları çöz.",
                     "effects": {"justice": -5, "people": 9, "treasury": -2, "military": 0, "authority": 7},
                     "log": "İdare ile vatandaş barıştırıldı; yüz binlerce dava mahkemeye gitmeden sulh ile sonuçlandı."},
                    {"label": "İdare mahkemelerinin dava yükünü hafifleterek devletin yıllık 2 milyar liralık avukatlık ve harç masrafını tasarruf et.",
                     "effects": {"justice": -2, "people": -6, "treasury": 8, "military": 0, "authority": 4},
                     "log": "Hazine kasasına tasarruf sağlandı; gereksiz idari davaların masrafları önlendi."},
                    {"label": "Ombudsman teftişine direnen ve vatandaşın evrakını gizleyen liyakatsiz bürokratlar hakkında idari ceza ver.",
                     "effects": {"justice": -2, "people": -7, "treasury": 0, "military": 8, "authority": 9},
                     "log": "Bürokraside hesap verilebilirlik sağlandı; devlet kapısında vatandaşa eziyet eden memurlar uyarıldı."},
                    {"label": "Kamu Denetçiliği tavsiye kararlarını idare için bağlayıcı kılan 'Ombudsmanlık Reform Kanunu' çıkar.",
                     "effects": {"justice": 8, "people": 4, "treasury": -6, "military": 0, "authority": 8},
                     "log": "İyi yönetim ilkeleri kanunlaştı; Türkiye'de idarenin hukuka bağlılığı tescillendi."}
                ]
            elif "İstinaf Mahkemeleri" in title or "Yargı Reformu" in title or "e-Duruşma" in title:
                options_map[eid] = [
                    {"label": "Bölge Adliye Mahkemeleri (İstinaf) ve Yargıtay arasındaki yetki çatışmasını adil yargılanma ve tabi hakim ilkesiyle çöz.",
                     "effects": {"justice": 9, "people": 8, "treasury": -2, "military": 0, "authority": -2},
                     "log": "Yargıtay'daki 2 milyon dosya yükü eritildi; 5 yıl süren ceza ve hukuk davaları 1 yılda sonuçlanmaya başladı."},
                    {"label": "Barolar, hakimler ve savcılarla Yargı Şurası düzenleyerek e-Duruşma ve UYAP üzerinden savunma hakkını güçlendir.",
                     "effects": {"justice": -5, "people": 9, "treasury": -2, "military": 0, "authority": 7},
                     "log": "Avukatlar bürolarından duruşmalara katıldı; yargılama süreleri kısalarak adalet hızlandı."},
                    {"label": "Tüm adliyelere ses ve görüntü bilişim sistemi (SEGBİS) kurarak sanık nakil harcamalarında Hazineye rekor tasarruf sağla.",
                     "effects": {"justice": -2, "people": -6, "treasury": 9, "military": 0, "authority": 4},
                     "log": "Milyonlarca liralık jandarma nakil ve lojistik masrafı önlendi; adli harcamalar Hazinece dengelendi."},
                    {"label": "Sahte bilirkişilik yapan ve mahkemeleri rüşvetle manipüle eden çetelere karşı adli zabıtayı görevlendir.",
                     "effects": {"justice": -2, "people": -7, "treasury": 0, "military": 9, "authority": 8},
                     "log": "Adliyeler temizlendi; sahte rapor düzenleyen bilirkişiler tutuklanarak sicilden silindi."},
                    {"label": "Yargılama sürelerini kesin hedef sürelere bağlayan 'Yargı Reformu Strateji Belgesi Kanun Paketi'ni çıkar.",
                     "effects": {"justice": 8, "people": 4, "treasury": -6, "military": 0, "authority": 8},
                     "log": "Hedef süre uygulaması kanunlaştı; 'Geciken adalet, adalet değildir' ilkesi hayata geçirildi."}
                ]
            elif "Çoklu Baro" in title or "Avukatlık Kanunu" in title:
                options_map[eid] = [
                    {"label": "Savunma makamının bağımsızlığı ve Barolar Birliği'nin anayasal kamu kurumu niteliğindeki meslek örgütü yapısını koru.",
                     "effects": {"justice": 9, "people": 8, "treasury": -2, "military": 0, "authority": -3},
                     "log": "Savunmanın gücü korundu; avukatların mesleki bağımsızlığı anayasal zeminde savunuldu."},
                    {"label": "Türkiye Barolar Birliği ve il baro başkanlarıyla Çankaya'da meşveret toplayıp avukatların özlük haklarında uzlaş.",
                     "effects": {"justice": -5, "people": 8, "treasury": -2, "military": 0, "authority": 7},
                     "log": "Baro yürüyüşleri diyalogla sonlandırıldı; avukatlık mesleğinin itibarını koruyacak formül bulundu."},
                    {"label": "Genç avukatlara ilk 3 yıl büro ve vergi muafiyeti tanıyarak Hazine destekli faizsiz kuruluş kredisi aç.",
                     "effects": {"justice": -2, "people": -6, "treasury": 8, "military": 0, "authority": 4},
                     "log": "Genç hukukçular desteklendi; mezun avukatların büro açma çilesi devletçe hafifletildi."},
                    {"label": "Adliye koridorlarında terör propagandası ve cübbeyle yasadışı slogan atan marjinal grupları polisçe engelle.",
                     "effects": {"justice": -2, "people": -7, "treasury": 0, "military": 8, "authority": 8},
                     "log": "Adliyelerde vakar korundu; meslek cübbesinin ideolojik eylemlere alet edilmesi önlendi."},
                    {"label": "Büyükşehirlerde 5 bin avukatı aşan illerde 2. baronun kurulabilmesini sağlayan 7249 Sayılı Kanun'u kabul et.",
                     "effects": {"justice": 8, "people": 4, "treasury": -6, "military": 0, "authority": 8},
                     "log": "Avukatlık Kanunu güncellendi; çoklu baro sistemi yasal çerçevede yürürlüğe girdi."}
                ]
            else:
                options_map[eid] = [
                    {"label": "Yargısal denetim, anayasal kurallar ve tabi hakim güvencesini tüm kamu işlemlerinde tavizsiz işlet.",
                     "effects": {"justice": 8, "people": 7, "treasury": -2, "military": 0, "authority": -3},
                     "log": "Hukuk devleti korundu; idari tasarruflar bağımsız yargı denetimine tabi tutuldu."},
                    {"label": "Yargı mensupları, akademisyenler ve sivil toplumla hukuk şuraları toplayarak kanunlaştırma uzlaşısı sağla.",
                     "effects": {"justice": -6, "people": 8, "treasury": -2, "military": 0, "authority": 7},
                     "log": "Hukuk camiasında uzlaşı sağlandı; mevzuat hazırlıklarında katılımcılık sağlandı."},
                    {"label": "Adalet sarayları ve adli tıp altyapısı yatırımları için Hazine bütçesinden planlı finansman sağla.",
                     "effects": {"justice": -2, "people": -6, "treasury": 8, "military": 0, "authority": 4},
                     "log": "Adli bütçe korundu; mahkemelerin fiziki ve dijital altyapısı tamamlandı."},
                    {"label": "Adliyelerde provokasyon, rüşvet ve sahte evrak şebekelerine karşı adli kolluğu teyakkuzda tut.",
                     "effects": {"justice": -2, "people": -7, "treasury": 0, "military": 9, "authority": 8},
                     "log": "Adliyelerde güvenlik sağlandı; yargı mekanizmasına sızmaya çalışan çeteler engellendi."},
                    {"label": "Yargı bağımsızlığı ve şeffaflığı tahkim eden 'Kamu Hukuku ve Adli Teşkilat Reform Kanunu' çıkar.",
                     "effects": {"justice": 8, "people": 4, "treasury": -6, "military": 0, "authority": 8},
                     "log": "Hukuk mevzuatı modernleştirildi; adalet hizmetleri çağdaş standartlara kavuşturuldu."}
                ]

        # DOMAIN 27: Tarım, Hayvancılık ve Gıda Güvenliği (880 to 909: tr_vaka_881 to tr_vaka_910)
        elif 880 <= i <= 909:
            if "Çiftçi Kayıt Sistemi" in title or "TARSİM" in title or "Kuraklık" in title:
                options_map[eid] = [
                    {"label": "Kuraklık ve don felaketinde çiftçinin zararını TARSİM eksperlerince yerinde tespit ettirip hak sahiplerine eksiksiz ödet.",
                     "effects": {"justice": 9, "people": 8, "treasury": -2, "military": 0, "authority": -2},
                     "log": "Çiftçinin hakkı korundu; afet mağduru üreticilerin zararları devlet güvenceli sigortayla ödendi."},
                    {"label": "Ziraat Odaları ve Türkiye Damızlık Yetiştiricileri Birliği ile kuraklık eylem planı ve acil tohum yardımı uzlaşısı yap.",
                     "effects": {"justice": -5, "people": 9, "treasury": -3, "military": 0, "authority": 7},
                     "log": "Üreticinin morali yükseldi; tohum ve gübre destekleriyle tarlaların boş kalması önlendi."},
                    {"label": "Çiftçilere mazot ve gübre desteğini doğrudan Başak Kart'a yükleyerek Hazine tarımsal destek bütçesini 63 milyar TL'ye çıkar.",
                     "effects": {"justice": -2, "people": -6, "treasury": 9, "military": 0, "authority": 4},
                     "log": "Tarım sübvanse edildi; Hazine kaynaklarıyla çiftçinin girdi maliyetleri hafifletildi."},
                    {"label": "Mera arazilerini kaçak sürerek işgal eden ve kaçak su kuyusu açan fırsatçılara karşı tarım jandarmasını sahaya sür.",
                     "effects": {"justice": -2, "people": -7, "treasury": 0, "military": 8, "authority": 8},
                     "log": "Mera ve yeraltı suları korundu; kanunsuz kuyu açan şebekelere ağır cezalar kesildi."},
                    {"label": "Havza bazlı üretimi zorunlu kılan ve su kısıtı olan alanlarda çok su tüketen bitkileri yasaklayan 'Milli Tarım Kanunu' çıkar.",
                     "effects": {"justice": 8, "people": 4, "treasury": -6, "military": 0, "authority": 8},
                     "log": "Tarımsal planlama kanunlaştı; Türkiye'nin gıda güvenliği ve su kaynakları teminat altına alındı."}
                ]
            elif "Ata Tohumu" in title or "Milli Tohum Gen Bankası" in title:
                options_map[eid] = [
                    {"label": "Anadolu'nun bin yıllık yerli tohumlarını ve gen kaynaklarını devlet korumasına alarak yabancı patent tekellerine kapat.",
                     "effects": {"justice": 10, "people": 8, "treasury": -2, "military": 0, "authority": -2},
                     "log": "Milli tohum bağımsızlığı korundu; Siyez buğdayı ve yerli tohumların mülkiyeti millete tescillendi."},
                    {"label": "Cumhurbaşkanlığı öncülüğünde 'Ata Tohumu Seferberliği' başlat; köylülerin elindeki yerli tohumları toplayıp takas bayramları yap.",
                     "effects": {"justice": -5, "people": 10, "treasury": -2, "military": 0, "authority": 7},
                     "log": "Halk seferber oldu; sandıklarda saklanan asırlık domates, karpuz ve buğday tohumları tarlalarla buluşturuldu."},
                    {"label": "Ankara'da dünyanın en büyük 3. Milli Tohum Gen Bankası'nı kurarak 120 bin tohum numunesini -196 derecede Hazine fonuyla koru.",
                     "effects": {"justice": -2, "people": -6, "treasury": 9, "military": 0, "authority": 4},
                     "log": "Geleceğin gıda bankası kuruldu; nükleer savaş ve kuraklık tehdidine karşı Türkiye'nin tohumları güvenceye alındı."},
                    {"label": "Biyokaçakçılık yaparak Türkiye'nin endemik bitki soğanlarını ve tohumlarını yurtdışına kaçıran yabancılara havalimanında dur de.",
                     "effects": {"justice": -2, "people": -7, "treasury": 0, "military": 9, "authority": 9},
                     "log": "Biyolojik miras korundu; gümrük kapılarında kaçakçılık şebekeleri yakalandı."},
                    {"label": "Geleneksel yerli tohumların köylüler arasında serbestçe alınıp satılabilmesini sağlayan 'Yerli Tohumculuk Reform Kanunu' çıkar.",
                     "effects": {"justice": 8, "people": 5, "treasury": -6, "military": 0, "authority": 8},
                     "log": "Yerli tohum serbestisi kanunlaştı; Anadolu'nun kadim lezzetleri sofralara geri döndü."}
                ]
            elif "Mavi Tünel" in title or "Obruk" in title or "Konya Ovası" in title:
                options_map[eid] = [
                    {"label": "Yeraltı sularını kaçak çeken 100 bin kaçak kuyuya sayaç taktır; kaçak sulamayı adli cezalarla durdur.",
                     "effects": {"justice": 9, "people": 7, "treasury": -2, "military": 0, "authority": -2},
                     "log": "Yeraltı su havzası korundu; mısır tarlalarında yeni obrukların açılmasının önüne geçildi."},
                    {"label": "Konya ve Karaman çiftçilerine damla sulama ve az su tüketen arpa-buğday tohumları dağıtarak çiftçileri teşvik et.",
                     "effects": {"justice": -5, "people": 9, "treasury": -3, "military": 0, "authority": 7},
                     "log": "Çiftçiler tasarruflu sulamaya geçti; vahşi sulamanın ovayı kurutması diyalogla önlendi."},
                    {"label": "Toros Dağları'nı delen 17 kilometrelik Mavi Tünel ile Göksu Nehri'nin sularını Konya Ovası'na akıtan dev yatırımı finanse et.",
                     "effects": {"justice": -2, "people": -6, "treasury": 10, "military": 0, "authority": 5},
                     "log": "Mavi Tünel tamamlandı; Akdeniz'e boşa akan sular Anadolu'nun tahıl ambarını canlandırdı."},
                    {"label": "Obruk riski taşıyan fay çatlakları ve yer altı boşluklarını AFAD ve MTA jeoradarlarıyla 24 saat izlemeye al.",
                     "effects": {"justice": -2, "people": -7, "treasury": 0, "military": 8, "authority": 9},
                     "log": "Erken uyarı sistemi kuruldu; köylerin ve yerleşim alanlarının obruk tehlikesine karşı güvenliği sağlandı."},
                    {"label": "Tarımsal sulamada kapalı basınçlı boru sistemini ve modern sulamayı zorunlu kılan 'Su ve Sulama Kanunu' çıkar.",
                     "effects": {"justice": 8, "people": 4, "treasury": -7, "military": 0, "authority": 8},
                     "log": "Su kanunu yürürlüğe girdi; Türkiye'nin tarımsal su kaynaklarında %40 su tasarrufu sağlandı."}
                ]
            else:
                options_map[eid] = [
                    {"label": "Tarımsal üretimde kalite standartları, gıda güvenliği ve çiftçi haklarını yasal güvencede tut.",
                     "effects": {"justice": 8, "people": 7, "treasury": -2, "military": 0, "authority": -3},
                     "log": "Gıda güvenliği gözetildi; halkın sağlıklı ve güvenilir gıdaya erişimi sağlandı."},
                    {"label": "Ziraat odaları, besiciler ve köylülerle istişare kurulları toplayarak tarımsal kalkınma uzlaşısı sağla.",
                     "effects": {"justice": -6, "people": 8, "treasury": -2, "military": 0, "authority": 7},
                     "log": "Köylünün sesi dinlendi; tarım ve hayvancılıkta üretici memnuniyeti sağlandı."},
                    {"label": "Tarımsal destekleme primleri ve faizsiz sübvansiyonlu krediler için Hazine bütçesinden kaynak aktar.",
                     "effects": {"justice": -2, "people": -6, "treasury": 8, "military": 0, "authority": 4},
                     "log": "Tarımsal ekonomi desteklendi; girdi maliyetlerine karşı çiftçi sübvanse edildi."},
                    {"label": "Kaçak hayvan nakilleri ve gıdada tağşiş yapan sahtekarlara karşı gıda zabıtası ve kolluğu görevlendir.",
                     "effects": {"justice": -2, "people": -7, "treasury": 0, "military": 9, "authority": 8},
                     "log": "Sahte gıda depoları basıldı; halkın sağlığıyla oynayan fırsatçılar cezalandırıldı."},
                    {"label": "Sözleşmeli besicilik ve lisanslı depoculuğu teşvik eden 'Tarımsal Üretim Planlama Kanunu' çıkar.",
                     "effects": {"justice": 8, "people": 4, "treasury": -6, "military": 0, "authority": 8},
                     "log": "Tarım planlaması kanunlaştı; arz fazlası ve ürün ziyanının önüne geçildi."}
                ]

    print(f"Total options generated for Batch 9: {len(options_map)}")
    updated_deck = apply_options_to_deck(deck, options_map)
    save_modern_deck(updated_deck)

if __name__ == '__main__':
    generate_domains_25_to_27()
