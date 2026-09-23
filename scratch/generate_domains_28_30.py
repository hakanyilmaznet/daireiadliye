import json
from deck_utils import load_modern_deck, save_modern_deck, apply_options_to_deck

# Domain 28: Çevre Eylemleri ve Sivil Dayanışma (tr_vaka_911 - tr_vaka_940)
# Domain 29: Sokak Güvenliği ve Asayiş (tr_vaka_941 - tr_vaka_970)
# Domain 30: Türkiye Yüzyılı ve Gelecek Vizyonu (tr_vaka_971 - tr_vaka_1000)

def generate_domains_28_to_30():
    deck = load_modern_deck()
    print("Building realistic options for Domains 28, 29, and 30 (tr_vaka_911 to tr_vaka_1000)...")
    options_map = {}

    for i in range(910, 1000):
        ev = deck[i]
        eid = ev['id']
        title = ev['title']
        desc = ev['desc']

        # DOMAIN 28: Çevre Eylemleri ve Sivil Dayanışma (910 to 939: tr_vaka_911 to tr_vaka_940)
        if 910 <= i <= 939:
            if "Gezi Parkı" in title:
                options_map[eid] = [
                    {"label": "Parktaki ağaç kesimini ve Topçu Kışlası projesini İdare Mahkemesi kararı çıkana kadar derhal durdur.",
                     "effects": {"justice": 9, "people": 8, "treasury": -2, "military": 0, "authority": -3},
                     "log": "Yargı kararına saygı duyuldu; Taksim Dayanışması'nın çevre talebi hukuki güvenceye alındı."},
                    {"label": "Taksim Platformu, sanatçılar ve gençlerle Başbakanlıkta müzakere masası topla; Gezi Parkı'nın park olarak kalmasında uzlaş.",
                     "effects": {"justice": -5, "people": 10, "treasury": -2, "military": 0, "authority": 7},
                     "log": "Toplumsal tansiyon düşürüldü; eylemlerin sokak çatışması ve vandallığa dönüşmesi diyalogla önlendi."},
                    {"label": "Eylemler sırasında tahrip edilen kamu binaları, belediye otobüsleri ve esnaf dükkanlarının zararını Hazine fonuyla tazmin et.",
                     "effects": {"justice": -2, "people": -6, "treasury": 8, "military": 0, "authority": 4},
                     "log": "Esnafın zararları karşılandı; kamu bütçesindeki tahribat devletçe telafi edildi."},
                    {"label": "Kamu binalarını yakan, polise molotof atan ve barikat kuran marjinal terör örgütü militanlarına karşı emniyeti göreve çağır.",
                     "effects": {"justice": -3, "people": -8, "treasury": 0, "military": 10, "authority": 9},
                     "log": "Vandallık ve kamu düzeninin bozulması sert müdahaleyle durduruldu; sokak terörüne geçit verilmedi."},
                    {"label": "Şehir merkezlerindeki yeşil alanların imara açılmasını yerel referanduma (plebisit) bağlayan 'Kent Hakkı Kanunu' çıkar.",
                     "effects": {"justice": 8, "people": 5, "treasury": -6, "military": 0, "authority": 8},
                     "log": "Katılımcı şehircilik kanunlaştı; halkın rızası olmadan şehir parklarının dönüştürülmesi yasaklandı."}
                ]
            elif "Kızılay" in title or "Çadır Satışı" in title:
                options_map[eid] = [
                    {"label": "Depremin ilk günlerinde çadır ve gıda satan Kızılay yöneticileri hakkında derhal adli teftiş açtırıp istifalarını sağla.",
                     "effects": {"justice": 10, "people": 8, "treasury": -2, "military": 0, "authority": -2},
                     "log": "Milli kurumun itibarı korundu; 155 yıllık Kızılay'ın ticaret şirketi gibi davranmasına izin verilmedi."},
                    {"label": "Kızılay Genel Kurulu'nu olağanüstü toplayarak cemiyetin başına saygın tıp insanları ve sivil toplum önderlerini getir.",
                     "effects": {"justice": -5, "people": 9, "treasury": -2, "military": 0, "authority": 7},
                     "log": "Milletin kuruma olan güveni tazelendi; bağış ve kan verme seferberliği yeniden şahlandı."},
                    {"label": "Kızılay'ın şirketleşen ticari iştiraklerinin tüm gelirlerini doğrudan afet çadır ve konteyner üretimine tahsis et.",
                     "effects": {"justice": -2, "people": -6, "treasury": 9, "military": 0, "authority": 4},
                     "log": "Afet stokları iki katına çıkarıldı; Hazine denetiminde 500 bin çadır ve aşevi stoku kuruldu."},
                    {"label": "Kızılay depolarındaki yardım malzemelerinin kaçırılmasını veya satılmasını önlemek için depolara kolluk nöbeti koy.",
                     "effects": {"justice": -2, "people": -7, "treasury": 0, "military": 9, "authority": 9},
                     "log": "İnsani yardım lojistiği tam güvenceye alındı; hiçbir yardım malzemesinin piyasaya satılmasına izin verilmedi."},
                    {"label": "Kızılay'ın kamu yararına dernek statüsünü ve ticari satış yasağını tescilleyen 'Kızılay Teşkilat Kanunu Reformu' çıkar.",
                     "effects": {"justice": 8, "people": 4, "treasury": -6, "military": 0, "authority": 8},
                     "log": "Kızılay anayasal zırha kavuştu; afet zamanı çadır ve kan satışı yasal olarak imkansız kılındı."}
                ]
            elif "Akbelen" in title or "Cerattepe" in title or "Kaz Dağları" in title:
                options_map[eid] = [
                    {"label": "Maden ve termik santral şirketlerinin orman kesim izinlerini Danıştay ve İdare Mahkemesi kararlarıyla iptal et.",
                     "effects": {"justice": 9, "people": 8, "treasury": -2, "military": 0, "authority": -2},
                     "log": "Hukuk devleti ormanı savundu; zeytinlik ve su havzalarını tahrip eden maden ruhsatları iptal edildi."},
                    {"label": "Yöre köylüleri, kadınları ve çevreci gençlerle Valilikte buluş; ormanın kesilmesini durduracak alternatif uzlaşı ara.",
                     "effects": {"justice": -5, "people": 9, "treasury": -3, "military": 0, "authority": 7},
                     "log": "Köylülerin asırlık çamları ve zeytinleri korundu; kömür sahası yerine temiz enerjiye geçiş kararı alındı."},
                    {"label": "Termik santrallerin kömür ihtiyacını karşılamak için orman kesmek yerine çevreye duyarlı yer altı madenciliğini finanse et.",
                     "effects": {"justice": -2, "people": -6, "treasury": 8, "military": 0, "authority": 4},
                     "log": "Enerji arzı aksatılmadan korundu; orman tahribatının önüne modern teknolojiyle geçildi."},
                    {"label": "Bölgede provokatif eylemlerle jandarma kalkanına saldıran yasadışı grupları barikat kurarak engelle.",
                     "effects": {"justice": -2, "people": -7, "treasury": 0, "military": 9, "authority": 8},
                     "log": "Kamu düzeni korundu; çevre eylemlerinin silahlı örgüt propagandasına alet edilmesi önlendi."},
                    {"label": "1. derece doğal sit alanları ve ormanlarda maden aramasını anayasal düzeyde yasaklayan 'Orman ve Tabiat Kanunu' çıkar.",
                     "effects": {"justice": 8, "people": 5, "treasury": -6, "military": 0, "authority": 8},
                     "log": "Yeşil Vatan kanunla koruma altına alındı; orman varlığımızın eksilmesine dur dendi."}
                ]
            else:
                options_map[eid] = [
                    {"label": "Çevre ve tabiat varlıklarının korunmasında Anayasa'nın 56. maddesindeki sağlıklı çevrede yaşama hakkını tavizsiz uygula.",
                     "effects": {"justice": 8, "people": 7, "treasury": -2, "military": 0, "authority": -3},
                     "log": "Çevre hakkı korundu; tabiat varlıklarını bozan usulsüzlüklere karşı yargı yolu işletildi."},
                    {"label": "Çevre dernekleri, yerel halk ve bilim insanlarıyla diyalog kurarak kalkınma ile doğa koruma dengesinde uzlaş.",
                     "effects": {"justice": -6, "people": 8, "treasury": -2, "military": 0, "authority": 7},
                     "log": "Toplumsal mutabakat sağlandı; çevre ihtilafları sivil diyalogla çözüldü."},
                    {"label": "Çevre koruma, atık su arıtma ve sıfır atık projeleri için İller Bankası ve Hazine kaynaklarını seferber et.",
                     "effects": {"justice": -2, "people": -6, "treasury": 8, "military": 0, "authority": 4},
                     "log": "Yeşil projeler finanse edildi; çevre altyapısı kamu bütçesiyle güçlendirildi."},
                    {"label": "Doğal sit alanlarında kaçak yapılaşma ve çevre sabotajlarına karşı kolluk devriyelerini artır.",
                     "effects": {"justice": -2, "people": -7, "treasury": 0, "military": 9, "authority": 8},
                     "log": "Çevre asayişi sağlandı; doğa harikalarının rant odaklarınca işgal edilmesi önlendi."},
                    {"label": "Sıfır Atık vizyonunu ve iklim adaleti ilkelerini yasal teminata bağlayan 'Çevre ve Doğa Reform Kanunu' çıkar.",
                     "effects": {"justice": 8, "people": 4, "treasury": -6, "military": 0, "authority": 8},
                     "log": "Çevre mevzuatı çağdaşlaştırıldı; gelecek nesillere temiz bir vatan bırakıldı."}
                ]

        # DOMAIN 29: Sokak Güvenliği ve Asayiş (940 to 969: tr_vaka_941 to tr_vaka_970)
        elif 940 <= i <= 969:
            if "Sahte İçki" in title or "Metil Alkol" in title:
                options_map[eid] = [
                    {"label": "Merdiven altı fabrikalarda metil alkolle vatandaşın canına kıyan zehir tacirlerini 'kasten öldürme'den Ağır Ceza'ya sevk et.",
                     "effects": {"justice": 10, "people": 8, "treasury": -2, "military": 0, "authority": -2},
                     "log": "Zehir şebekeleri çökertildi; yüzlerce vatandaşın ölümüne yol açan sahte içki baronları müebbetle yargılandı."},
                    {"label": "Restoran, büfe ve tekel bayileri federasyonuyla bilgilendirme toplantısı yap; bandrolsüz ürün satanları sektörden dışla.",
                     "effects": {"justice": -5, "people": 9, "treasury": -2, "military": 0, "authority": 7},
                     "log": "Esnafla dayanışma sağlandı; sahte alkolün piyasaya sürülmesi esnafın desteğiyle engellendi."},
                    {"label": "Etil alkol ithalatı ve satışında denatürasyon (acılaştırıcı) maddesi zorunluluğu getirerek Hazine vergi kaçağını önle.",
                     "effects": {"justice": -2, "people": -6, "treasury": 9, "military": 0, "authority": 4},
                     "log": "Endüstriyel alkolün sahte içkide kullanılması kimyasal olarak imkansız kılındı; vergi kaybı sıfırlandı."},
                    {"label": "Kaçakçılık ve Organize Suçlarla Mücadele (KOM) timleriyle 81 ilde eşzamanlı 'Zehir' operasyonları düzenle.",
                     "effects": {"justice": -2, "people": -7, "treasury": 0, "military": 10, "authority": 9},
                     "log": "Binlerce ton sahte alkol ele geçirildi; zehir tacirlerinin üretim merkezleri mühürlendi."},
                    {"label": "Alkol piyasasında bandrol sahteciliğine ve metil alkol ticaretine terör suçları seviyesinde ceza getiren yasa çıkar.",
                     "effects": {"justice": 8, "people": 4, "treasury": -6, "military": 0, "authority": 8},
                     "log": "Yasal kalkan kuruldu; sahte içki ölümlerinin önüne katı kanuni yaptırımlarla geçildi."}
                ]
            elif "Organize Suç" in title or "Ayhan Bora Kaplan" in title or "Sarallar" in title or "Şahinler" in title:
                options_map[eid] = [
                    {"label": "Yeraltı dünyasının suç örgütü liderlerini, tetikçilerini ve bunlara göz yuman rüşvetçi bürokratları bağımsız yargıya ver.",
                     "effects": {"justice": 10, "people": 9, "treasury": -2, "military": 0, "authority": -2},
                     "log": "Mafyaya geçit verilmedi; suç örgütlerinin liderleri havalimanlarında kaçarken ters kelepçeyle paketlendi."},
                    {"label": "Çetelerin haraca bağladığı esnaf ve iş insanlarıyla Valilikte kriz masası topla; can ve mal güvenliğini devletçe sağla.",
                     "effects": {"justice": -5, "people": 9, "treasury": -2, "military": 0, "authority": 7},
                     "log": "Esnafın korku zinciri kırıldı; mafyanın tahsilat ve yağma tehdidine karşı devlet zırhı sağlandı."},
                    {"label": "Suç örgütlerinin el koyduğu gece kulüpleri, lüks araçlar ve kara para aklama şirketlerine MASAK marifetiyle el koy.",
                     "effects": {"justice": -2, "people": -6, "treasury": 10, "military": 0, "authority": 5},
                     "log": "Mafyanın mali damarları kesildi; suçtan elde edilen milyarlarca liralık mal varlığı Hazineye aktarıldı."},
                    {"label": "Özel Harekat polisleri ve Organize Şube timleriyle mafyanın inlerine şafak vakti 'Kafes' operasyonları başlat.",
                     "effects": {"justice": -2, "people": -7, "treasury": 0, "military": 10, "authority": 10},
                     "log": "Sokak çeteleri ve mafya yapılanmaları tek tek kafese sokuldu; devletin sokaktaki mutlak otoritesi kuruldu."},
                    {"label": "Organize suç örgütleri, mafya tipi yapılanmalar ve yasadışı silahlanmaya karşı en katı yaptırımları getiren reform yap.",
                     "effects": {"justice": 9, "people": 4, "treasury": -6, "military": 0, "authority": 9},
                     "log": "Sokaklar temizlendi; mafya düzeni çökerterek şehirlerde tam huzur ve asayiş tesis edildi."}
                ]
            elif "Kokain" in title or "Narkotik" in title or "Limanlar" in title:
                options_map[eid] = [
                    {"label": "Uluslararası uyuşturucu kartellerinin Türkiye rotasındaki baronlarını ve yerli işbirlikçilerini adli takiple çökert.",
                     "effects": {"justice": 10, "people": 9, "treasury": -2, "military": 0, "authority": -2},
                     "log": "Uyuşturucu kartelleri bozguna uğratıldı; tonlarca kokaini sevk eden yabancı suç şebekesi yargı önüne çıkarıldı."},
                    {"label": "Bağımlılıkla mücadele için Yeşilay, AMATEM ve aile dernekleriyle 81 ilde dev rehabilitasyon seferberliği ilan et.",
                     "effects": {"justice": -5, "people": 10, "treasury": -3, "military": 0, "authority": 7},
                     "log": "Gençliğe sahip çıkıldı; sokaklardan kurtarılan binlerce genç tedavi edilerek topluma kazandırıldı."},
                    {"label": "Limanlara son teknoloji x-ray tarama sistemleri ve konteyner tarayıcıları kurarak gümrük denetimini Hazinece finanse et.",
                     "effects": {"justice": -2, "people": -6, "treasury": 9, "military": 0, "authority": 4},
                     "log": "Liman güvenliği tahkim edildi; x-ray tarayıcıları sayesinde muz konteynerlerine gizlenen uyuşturucular yakalandı."},
                    {"label": "Narkotik polisleri, sahil güvenlik botları ve özel eğitimli K-9 köpekleriyle limanlara şafak baskınları yap.",
                     "effects": {"justice": -2, "people": -7, "treasury": 0, "military": 10, "authority": 9},
                     "log": "Cumhuriyet tarihinin en büyük kokain yakalamaları yapıldı; zehir tacirlerinin sevkiyat hatları kesildi."},
                    {"label": "Uyuşturucu ticareti ve sokak torbacılarına karşı hapis cezalarını en üst sınıra çıkaran 'Narkotik Seferberlik Kanunu' çıkar.",
                     "effects": {"justice": 8, "people": 4, "treasury": -6, "military": 0, "authority": 8},
                     "log": "Uyuşturucuyla mücadele kanunlaştı; çocuklarımızı zehirleyen torbacılara karşı tavizsiz rejim kuruldu."}
                ]
            else:
                options_map[eid] = [
                    {"label": "Sokak suçları, gasp ve asayişsizliğe karşı adli tahkikatı ve savcılık işlemlerini hızlandırarak failleri tutuklat.",
                     "effects": {"justice": 8, "people": 7, "treasury": -2, "military": 0, "authority": -3},
                     "log": "Sokak suçluları adliyeye teslim edildi; mahallelerde huzur ve adalet korundu."},
                    {"label": "Mahalle esnafı, muhtarlar ve vatandaşlarla istişare toplantıları yaparak huzur ve sükûnet uzlaşısı sağla.",
                     "effects": {"justice": -6, "people": 8, "treasury": -2, "military": 0, "authority": 7},
                     "log": "Halkla emniyet kaynaştı; ihbar ve dayanışma mekanizmalarıyla mahalleler huzura kavuştu."},
                    {"label": "Emniyet araç filosu, MOBESE kamera sistemleri ve asayiş altyapısı için Hazine bütçesinden özel ödenek ayır.",
                     "effects": {"justice": -2, "people": -6, "treasury": 8, "military": 0, "authority": 4},
                     "log": "Asayiş bütçesi güçlendirildi; sokakların gece gündüz aydınlatılması ve izlenmesi sağlandı."},
                    {"label": "Çarşı ve mahalle bekçilerini, motorize yunus polislerini gece sokaklarında kesintisiz devriyeye çıkar.",
                     "effects": {"justice": -2, "people": -7, "treasury": 0, "military": 10, "authority": 9},
                     "log": "Sokaklarda devletin şefkatli ve caydırıcı düdüğü çaldı; hırsızlık ve gasp olayları bıçak gibi kesildi."},
                    {"label": "Ruhsatsız silah taşımaya ve kuru sıkı tabancalara ağır hapis cezası getiren 'Genel Asayiş ve Silah Reform Kanunu' çıkar.",
                     "effects": {"justice": 8, "people": 4, "treasury": -6, "military": 0, "authority": 8},
                     "log": "Bireysel silahlanmaya geçit verilmedi; sokakların güvenliği kalıcı kanunlarla tahkim edildi."}
                ]

        # DOMAIN 30: Türkiye Yüzyılı ve Gelecek Vizyonu (970 to 999: tr_vaka_971 to tr_vaka_1000)
        elif 970 <= i <= 999:
            if "100. Yıl" in title or "Boğaz'da 100 Savaş Gemisi" in title:
                options_map[eid] = [
                    {"label": "Gazi Mustafa Kemal Atatürk'ün emaneti Cumhuriyetimizin 100. yılını anayasal meşruiyet ve millet iradesiyle taçlandır.",
                     "effects": {"justice": 10, "people": 9, "treasury": -2, "military": 0, "authority": -2},
                     "log": "Cumhuriyetimizin 100. yılı şanla kutlandı; Atatürk'ün 'En büyük eserim' dediği Cumhuriyet ebediyen payidar kılındı."},
                    {"label": "85 milyon vatandaşın ellerinde al bayraklarla meydanları doldurduğu tarihi 29 Ekim gecesini milli bayram coşkusuyla kutla.",
                     "effects": {"justice": -5, "people": 10, "treasury": -2, "military": 0, "authority": 8},
                     "log": "Millet tek yürek oldu; 100. yıl kutlamaları Türkiye'nin birlik ve beraberliğini tüm dünyaya haykırdı."},
                    {"label": "100. yıl hatırası olarak 81 ilde 100 yeni kütüphane, bilim merkezi ve müzeyi Hazine yatırımlarıyla aç.",
                     "effects": {"justice": -2, "people": -6, "treasury": 9, "military": 0, "authority": 4},
                     "log": "Cumhuriyetin mirası abideleşti; 100. yıl kalıcı eserlerle gelecek nesillere armağan edildi."},
                    {"label": "Donanmanın 100 savaş gemisi ve SoloTürk'ün Boğaz semalarındaki geçit töreniyle dosta düşmana Türkiye'nin kudretini göster.",
                     "effects": {"justice": -2, "people": -7, "treasury": 0, "military": 10, "authority": 10},
                     "log": "Boğaz'da tarihi donanma geçişi yapıldı; TCG Anadolu öncülüğündeki leventler şanlı Cumhuriyetimizi selamladı."},
                    {"label": "Cumhuriyetin ikinci yüzyılını kalkınma ve adaletle mühürleyen 'Türkiye Yüzyılı Çerçeve Kanunu'nu Meclis'te kabul et.",
                     "effects": {"justice": 8, "people": 5, "treasury": -6, "military": 0, "authority": 9},
                     "log": "İkinci yüzyılın vizyonu kanunlaştı; Türkiye küresel liderlik rotasına oturdu."}
                ]
            elif "Yeni ve Sivil Anayasa" in title or "Anayasa Uzlaşma" in title:
                options_map[eid] = [
                    {"label": "1982 darbe anayasasını tamamen çöpe atacak, insan onurunu ve kuvvetler ayrılığını esas alan yeni sivil anayasa tasarısını hazırla.",
                     "effects": {"justice": 10, "people": 9, "treasury": -2, "military": 0, "authority": -2},
                     "log": "Tarihi anayasa hamlesi başlatıldı; darbe vesayetinden arındırılmış ilk tamamen sivil anayasa masaya kondu."},
                    {"label": "TBMM'deki tüm siyasi partiler, akademisyenler, barolar ve halk temsilcileriyle geniş tabanlı Anayasa Şurası topla.",
                     "effects": {"justice": -5, "people": 10, "treasury": -2, "military": 0, "authority": 8},
                     "log": "Milli mutabakat arandı; mecliste partiler üstü bir anlayışla temel hak ve hürriyetlerde uzlaşma sağlandı."},
                    {"label": "Anayasa hazırlık ve halkoylaması süreçlerinin finansmanını Hazine bütçesinden şeffaf biçimde karşıla.",
                     "effects": {"justice": -2, "people": -6, "treasury": 8, "military": 0, "authority": 4},
                     "log": "Demokratik süreç Hazinece finanse edildi; bağımsız anayasa çalışmaları güvenceye bağlandı."},
                    {"label": "Anayasa Mahkemesi kararlarının bağlayıcılığını ve anayasal meşruiyet zincirini koruyarak devlet düzenini tahkim et.",
                     "effects": {"justice": -2, "people": -7, "treasury": 0, "military": 9, "authority": 9},
                     "log": "Hukuk güvenliği sağlandı; devlet kurumları arasındaki anayasal yetki karmaşası son buldu."},
                    {"label": "Milletin kendi eliyle yazdığı 'Türkiye Cumhuriyeti Yeni Sivil ve Kuşatıcı Anayasası'nı referandumla yürürlüğe koy.",
                     "effects": {"justice": 9, "people": 5, "treasury": -7, "military": 0, "authority": 10},
                     "log": "Darbe anayasası tarihe gömüldü; milletimiz özgür, demokratik ve sivil anayasasına kavuştu."}
                ]
            elif "Liyakat" in title or "Kamuda Mülakat" in title:
                options_map[eid] = [
                    {"label": "Kamuya personel alımında mülakatı kaldır; KPSS puan üstünlüğünü ve bağımsız kura sistemini tavizsiz işlet.",
                     "effects": {"justice": 10, "people": 9, "treasury": -2, "military": 0, "authority": -2},
                     "log": "Gençlerin adalet inancı perçinlendi; torpil iddiaları tarihe karıştı, hak eden liyakatle göreve başladı."},
                    {"label": "Memur sendikaları ve üniversitelerle 'Kamu Liyakat ve Kariyer Şurası' toplayarak atamalarda ortak kriterler belirle.",
                     "effects": {"justice": -5, "people": 9, "treasury": -2, "military": 0, "authority": 7},
                     "log": "Toplumsal mutabakat sağlandı; bürokraside kayırmacılık yerine performans ve ehliyet esas alındı."},
                    {"label": "Kamuda liyakatli uzman ve mühendis kadrolarının maaşlarını iyileştirerek beyin göçünü Hazine teşvikiyle durdur.",
                     "effects": {"justice": -2, "people": -6, "treasury": 8, "military": 0, "authority": 4},
                     "log": "Nitelikli beyinler devlette kaldı; stratejik kurumlarda mühendis ve uzman kalitesi yükseltildi."},
                    {"label": "Devlet sırlarını sızdıran, liyakat dışı cemaat veya klik yapılanmalarına karşı Devlet Denetleme Kurulu'nu teftişe sür.",
                     "effects": {"justice": -2, "people": -7, "treasury": 0, "military": 9, "authority": 9},
                     "log": "Bürokrasi paralel yapılardan temizlendi; kamu kurumlarında tek hiyerarşi anayasal devlet otoritesi oldu."},
                    {"label": "Kamu görevlerine girişte yazılı sınav harici tüm kayırmacı usulleri yasaklayan 'Kamuda Tam Liyakat Kanunu' çıkar.",
                     "effects": {"justice": 9, "people": 4, "treasury": -6, "military": 0, "authority": 8},
                     "log": "Liyakat anayasal zırha kavuştu; Türkiye ehliyetli ve dürüst kadroların omuzlarında yükseldi."}
                ]
            elif "Kalkınma Yolu" in title or "Zengezur" in title or "Türk Devletleri Teşkilatı" in title:
                options_map[eid] = [
                    {"label": "Basra Körfezi'nden Avrupa'ya uzanan Kalkınma Yolu ve Zengezur Koridoru'nun uluslararası hukuki anlaşmalarını imzala.",
                     "effects": {"justice": 9, "people": 8, "treasury": -2, "military": 0, "authority": -2},
                     "log": "Tarihi ticaret anlaşması tescillendi; Türkiye küresel İpek Yolu'nun vazgeçilmez merkezi haline geldi."},
                    {"label": "Azerbaycan, Kazakistan, Özbekistan ve Kırgızistan ile Türk Devletleri Teşkilatı'nda ortak alfabe ve ticaret anlaşması yap.",
                     "effects": {"justice": -5, "people": 10, "treasury": -3, "military": 0, "authority": 8},
                     "log": "Türk dünyası birleşti; 300 milyonluk Avrasya coğrafyasında kardeş cumhuriyetler tek ekonomik blok oldu."},
                    {"label": "Kalkınma Yolu demiryolu ve otoyol projelerini Hazine ve Körfez fonlarıyla finanse ederek Türkiye'ye yıllık 30 milyar dolar transit gelir sağla.",
                     "effects": {"justice": -2, "people": -6, "treasury": 10, "military": 0, "authority": 5},
                     "log": "Milli ekonomi şahlandı; Süveyş Kanalı'na alternatif en hızlı ticaret koridoru Türkiye'den geçti."},
                    {"label": "Koridor güzergahlarında Mehmetçik ve müttefik kuvvetlerle terör örgütlerinin sabotaj tehditlerini kökünden kazı.",
                     "effects": {"justice": -2, "people": -7, "treasury": 0, "military": 10, "authority": 10},
                     "log": "Stratejik hatlar korundu; Basra'dan Londra'ya kesintisiz yük taşımacılığı güvenlik kalkanına alındı."},
                    {"label": "Türkiye'yi Avrasya'nın lojistik ve finans merkezi yapan 'Milli Kalkınma Yolu ve Transit Ticaret Kanunu' çıkar.",
                     "effects": {"justice": 8, "people": 4, "treasury": -7, "military": 0, "authority": 9},
                     "log": "Küresel ticaret mimarisi kanunlaştı; Türkiye yüzyılın en büyük jeopolitik zaferini kazandı."}
                ]
            elif "Dâire-i Adliyye Felsefesi" in title or "Cumhuriyetin Temeli Adalettir" in title or "Tam Bağımsız Türkiye" in title:
                options_map[eid] = [
                    {"label": "Kınalızâde Ali Efendi'nin Adalet Dairesi felsefesine sarıl: 'Adalet mülkün temelidir; adalet olmadan ne hazine ne ordu ne devlet ayakta kalır!'.",
                     "effects": {"justice": 10, "people": 9, "treasury": -2, "military": 0, "authority": -2},
                     "log": "Devletin ruhu ihya edildi; adaletin tecellisiyle millet devletiyle kucaklaştı, asırlar sürecek beka teminat altına alındı."},
                    {"label": "Halkın refahını, birliğini ve kardeşliğini her şeyin üstünde tut: 'İnsanı yaşat ki devlet yaşasın!'.",
                     "effects": {"justice": -5, "people": 10, "treasury": -2, "military": 0, "authority": 8},
                     "log": "Toplumsal nizam ve maslahat-ı âmme korundu; devlet ile millet arasındaki kopmaz bağ ebediyen mühürlendi."},
                    {"label": "Hazine kasasını bereketli kıl, israfı sıfırla ve milli serveti üretime dönüştürerek ekonomik tam bağımsızlığı sağla.",
                     "effects": {"justice": -2, "people": -6, "treasury": 10, "military": 0, "authority": 5},
                     "log": "Milli ekonomi şahlandı; Hazine bağımsızlığıyla Türkiye hiçbir dış güce el açmayan küresel güç oldu."},
                    {"label": "Kahraman Türk ordusunu ve emniyet teşkilatını yerli teknolojiyle donatarak vatan semalarında ve denizlerinde sarsılmaz otorite kur.",
                     "effects": {"justice": -2, "people": -7, "treasury": 0, "military": 10, "authority": 10},
                     "log": "Devletin heybeti ve caydırıcılığı tescillendi; hiçbir şer odağının vatanımıza kem gözle bakamayacağı kanıtlandı."},
                    {"label": "Gazi Mustafa Kemal Atatürk'ün 'Egemenlik kayıtsız şartsız milletindir' ülküsüyle Türkiye Yüzyılı'nı anayasal zirveye taşı.",
                     "effects": {"justice": 9, "people": 5, "treasury": -6, "military": 0, "authority": 10},
                     "log": "Milli irade ebedileşti; adaletle hükmeden, halkını yaşatan ve tam bağımsız Türkiye Cumhuriyeti kıyamete kadar payidar kılındı!"}
                ]
            else:
                options_map[eid] = [
                    {"label": "Gelecek vizyonunda anayasal meşruiyet, hukukun üstünlüğü ve adaleti en temel sütun olarak koru.",
                     "effects": {"justice": 8, "people": 7, "treasury": -2, "military": 0, "authority": -3},
                     "log": "Hukuk devleti ilkesi gözetildi; Türkiye'nin geleceği adalet zemininde inşa edildi."},
                    {"label": "Milli hedeflerde toplumun tüm kesimleriyle, gençlerle ve bilim insanlarıyla ortak vizyon mutabakatı sağla.",
                     "effects": {"justice": -6, "people": 8, "treasury": -2, "military": 0, "authority": 7},
                     "log": "Toplumsal birlik sağlandı; milletimizin ortak ideali Türkiye Yüzyılı'nda kenetlendi."},
                    {"label": "Gelecek yüzyılın teknolojik ve iktisadi hamleleri için Hazine kaynaklarını stratejik yatırımlara tahsis et.",
                     "effects": {"justice": -2, "people": -6, "treasury": 8, "military": 0, "authority": 4},
                     "log": "Milli servet bereketlendirildi; yüksek teknoloji ve yeşil kalkınma finanse edildi."},
                    {"label": "Milli beka ve sınır güvenliğimizi korumak için caydırıcı savunma gücümüzü sahada tam olarak hissettir.",
                     "effects": {"justice": -2, "people": -7, "treasury": 0, "military": 9, "authority": 9},
                     "log": "Devletin kudreti korundu; Türkiye'nin bağımsızlığı ve güvenliği teminat altına alındı."},
                    {"label": "Cumhuriyetimizin ikinci yüzyılını kalıcı kılan 'Türkiye Yüzyılı Stratejik Reform Kanunu' çıkar.",
                     "effects": {"justice": 8, "people": 4, "treasury": -6, "military": 0, "authority": 8},
                     "log": "Stratejik hedefler kanunlaştı; Türkiye küresel liderlik yolunda kararlılıkla ilerledi."}
                ]

    print(f"Total options generated for Batch 10: {len(options_map)}")
    updated_deck = apply_options_to_deck(deck, options_map)
    save_modern_deck(updated_deck)

if __name__ == '__main__':
    generate_domains_28_to_30()
