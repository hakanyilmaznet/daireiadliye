import json
from deck_utils import load_modern_deck, save_modern_deck, apply_options_to_deck

# Domain 16: Dijitalleşme, Siber Olaylar ve Kripto (tr_vaka_551 - tr_vaka_580)
# Domain 17: Vicdan Davaları ve Toplumsal Adalet (tr_vaka_581 - tr_vaka_610)
# Domain 18: Eğitim, Sınavlar ve Gençlik (tr_vaka_611 - tr_vaka_640)

def generate_domains_16_to_18():
    deck = load_modern_deck()
    print("Building realistic options for Domains 16, 17, and 18 (tr_vaka_551 to tr_vaka_640)...")
    options_map = {}

    for i in range(550, 640):
        ev = deck[i]
        eid = ev['id']
        title = ev['title']
        desc = ev['desc']

        # DOMAIN 16: Dijitalleşme, Siber Olaylar ve Kripto (550 to 579: tr_vaka_551 to tr_vaka_580)
        if 550 <= i <= 579:
            if "THODEX" in title or "Kripto" in title:
                options_map[eid] = [
                    {"label": "Interpol Kırmızı Bülteni çıkar ve firari Faruk Fatih Özer'in Arnavutluk'tan iadesini diplomatik ve adli kanallarla sağla.",
                     "effects": {"justice": 9, "people": 8, "treasury": -2, "military": 0, "authority": -2},
                     "log": "Firari şüpheli Türkiye'ye getirildi; 40 bin yılı aşan rekor ceza istemiyle hakim karşısına çıkarıldı."},
                    {"label": "Kripto varlık mağdurlarıyla kriz masasında buluş; tasfiye masasındaki paraların hak sahiplerine dağıtımını koordine et.",
                     "effects": {"justice": -6, "people": 9, "treasury": -3, "military": 0, "authority": 7},
                     "log": "Mağdurların sesi dinlendi; şirket hesaplarındaki blokeli varlıklar tasfiye masasına aktarıldı."},
                    {"label": "Şirketin tüm banka hesapları, kripto soğuk cüzdanları ve menkul varlıklarına MASAK marifetiyle derhal bloke koy.",
                     "effects": {"justice": -2, "people": -6, "treasury": 10, "military": 0, "authority": 4},
                     "log": "Milyonlarca dolarlık kripto varlık donduruldu; paraların yurtdışına kaçırılması önlendi."},
                    {"label": "Siber Suçlarla Mücadele Daire Başkanlığı bünyesinde zincir üstü (on-chain) cüzdan takip timi kurup transferleri izle.",
                     "effects": {"justice": -2, "people": -7, "treasury": 0, "military": 9, "authority": 9},
                     "log": "Sanal takip ağı kuruldu; kripto paraların aklanmaya çalışıldığı borsalar tek tek tespit edildi."},
                    {"label": "SPK lisansı ve asgari 100 milyon TL sermaye teminatı getiren 'Kripto Varlık Hizmet Sağlayıcıları Kanunu' çıkar.",
                     "effects": {"justice": 8, "people": 4, "treasury": -7, "military": 0, "authority": 9},
                     "log": "Kripto piyasası devlet güvencesine alındı; merdiven altı kripto borsalarının dolandırıcılığı yasayla önlendi."}
                ]
            elif "Dilan Polat" in title or "Kara Para" in title or "Çiftlik Bank" in title:
                options_map[eid] = [
                    {"label": "Lüks hayat paylaşımları arkasındaki yasadışı bahis, naylon fatura ve kara para aklama çarkını MASAK raporuyla savcılığa ver.",
                     "effects": {"justice": 10, "people": 8, "treasury": -2, "military": 0, "authority": -2},
                     "log": "Sosyal medya fenomenlerinin lüks saltanatı adliyede bitti; örgüt liderleri ve yöneticileri tutuklandı."},
                    {"label": "Mağdur olan franchise sahipleri ve güzellik merkezi çalışanlarının haklarını korumak için kayyum heyeti oluştur.",
                     "effects": {"justice": -6, "people": 8, "treasury": -3, "military": 0, "authority": 7},
                     "log": "İşletmelerde çalışan masum personelin işsiz kalması önlendi; merkezlerin faaliyetleri denetim altına alındı."},
                    {"label": "Şüphelilerin yüzlerce lüks aracına, villalarına ve şirketlerine TMSF marifetiyle el koyup Hazineye devret.",
                     "effects": {"justice": -2, "people": -6, "treasury": 10, "military": 0, "authority": 5},
                     "log": "Lüks spor arabalar polis aracı yapıldı; kara para şebekesinin serveti kamuya irad kaydedildi."},
                    {"label": "Mali Şube ve Organize Suçlar timleriyle şüphelilerin şirket merkezlerine ve villalarına şafak baskını yap.",
                     "effects": {"justice": -2, "people": -7, "treasury": 0, "military": 9, "authority": 9},
                     "log": "Deliller karartılmadan kasalara ve belgelere el konuldu; kayıt dışı para trafiği çökertildi."},
                    {"label": "Sosyal medya üzerinden yürütülen kayıt dışı ticaret ve bahis reklamlarını yasaklayan 'Mali Şeffaflık Kanunu' çıkar.",
                     "effects": {"justice": 8, "people": 4, "treasury": -6, "military": 0, "authority": 8},
                     "log": "Fenomenler vergi ve adli denetime tabi kılındı; kara paranın aklanma yolları kapatıldı."}
                ]
            elif "Instagram" in title or "Sosyal Medya" in title or "Discord" in title:
                options_map[eid] = [
                    {"label": "Katalog suçlar (çocuk istismarı, terör, intihara yönlendirme) sebebiyle platformun Türkiye temsilcilik açmasını şart koş.",
                     "effects": {"justice": 9, "people": 7, "treasury": -2, "military": 0, "authority": -3},
                     "log": "Egemenlik hakları korundu; küresel platformlar Türk kanunlarına uymayı ve temsilci atamayı kabul etti."},
                    {"label": "Dijital içerik üreticileri ve e-ticaret esnafıyla görüşerek platform engellerinin ekonomik zararlarını asgaride tut.",
                     "effects": {"justice": -6, "people": 8, "treasury": -3, "military": 0, "authority": 7},
                     "log": "Esnafın mağduriyeti dinlendi; şirketle yapılan müzakerelerin ardından platformlar kurallara uyarak açıldı."},
                    {"label": "Türkiye'de milyarlarca dolar reklam geliri elde edip vergi kaçıran küresel teknoloji devlerine %7.5 Dijital Hizmet Vergisi koy.",
                     "effects": {"justice": -2, "people": -6, "treasury": 9, "military": 0, "authority": 4},
                     "log": "Dijital devler vergi mükellefi yapıldı; Hazineye yıllık milyarlarca liralık vergi geliri girdi."},
                    {"label": "BTK ve Siber Suçlarla Mücadele Dairesi'ne siber zorbalık ve pedofili ağlarına karşı anında IP erişim engeli yetkisi ver.",
                     "effects": {"justice": -3, "people": -8, "treasury": 0, "military": 9, "authority": 9},
                     "log": "Çocuklar ve gençler dijital bataklıktan korundu; sapkın şantaj çetelerinin sunucuları çökertildi."},
                    {"label": "Sosyal medya platformlarının Türkçe içerik denetimi ve mahkeme kararlarına uymasını zorunlu kılan 'Sosyal Medya Kanunu' çıkar.",
                     "effects": {"justice": 8, "people": 4, "treasury": -6, "military": 0, "authority": 8},
                     "log": "Siber vatanda egemenlik tescillendi; platformların keyfi sansür ve kural tanımazlığı kanunla durduruldu."}
                ]
            elif "e-Devlet" in title or "UYAP" in title or "KVKK" in title:
                options_map[eid] = [
                    {"label": "Kişisel Verileri Koruma Kurumu (KVKK) marifetiyle vatandaş verilerini sızdıran şirketlere rekor idari para cezaları kes.",
                     "effects": {"justice": 9, "people": 8, "treasury": -2, "military": 0, "authority": -2},
                     "log": "Vatandaşların mahremiyeti korundu; veri güvenliğini sağlamayan şirketlere ağır yaptırımlar uygulandı."},
                    {"label": "65 milyon vatandaşın kullandığı e-Devlet kapısında bürokratik belge talebini sıfırlayarak tek tıkla hizmet sun.",
                     "effects": {"justice": -5, "people": 10, "treasury": -2, "military": 0, "authority": 7},
                     "log": "Bürokrasi tarihe karıştı; adli sicilden ikametgaha kadar tüm devlet kapıları vatandaşın cebine girdi."},
                    {"label": "UYAP ve e-Devlet entegrasyonuyla devlet kurumlarında yıllık 5 milyar liralık kağıt, posta ve kırtasiye tasarrufu sağla.",
                     "effects": {"justice": -2, "people": -6, "treasury": 9, "military": 0, "authority": 4},
                     "log": "Kamu maliyesinde rekor tasarruf sağlandı; dijital devlet modeli kamu bütçesini ferahlattı."},
                    {"label": "Ulusal Siber Olaylara Müdahale Merkezi'ni (USOM) 24 saat teyakkuza geçirerek kamu veri tabanlarına siber saldırıları püskürt.",
                     "effects": {"justice": -2, "people": -7, "treasury": 0, "military": 9, "authority": 9},
                     "log": "Siber vatan savunması başarıyla yapıldı; devlet arşivlerine yönelik dış kaynaklı siber sızmalar engellendi."},
                    {"label": "Türkiye'nin siber savunma doktrinini ve dijital egemenliğini yasal teminata bağlayan 'Ulusal Siber Güvenlik Kanunu' çıkar.",
                     "effects": {"justice": 8, "people": 4, "treasury": -6, "military": 0, "authority": 8},
                     "log": "Siber güvenlik başkanlığı kuruldu; Türkiye'nin dijital altyapısı yabancı bağımlılıktan kurtarıldı."}
                ]
            else:
                options_map[eid] = [
                    {"label": "Dijital suçlar, internet dolandırıcılığı ve yasadışı bahis faaliyetlerine karşı adli soruşturmaları tavizsiz yürüt.",
                     "effects": {"justice": 8, "people": 7, "treasury": -2, "military": 0, "authority": -3},
                     "log": "Siber suçlular adalet önüne çıkarıldı; vatandaşların dijital ortamdaki hak ve güvenliği korundu."},
                    {"label": "Bilişim sektörü, yazılımcılar ve sivil toplumla istişare ederek milli yazılım ve yapay zeka ekosistemini destekle.",
                     "effects": {"justice": -6, "people": 8, "treasury": -2, "military": 0, "authority": 7},
                     "log": "Sektörel uzlaşı sağlandı; yerli teknoloji girişimlerinin önü açıldı."},
                    {"label": "Siber güvenlik ve dijitalleşme altyapısı yatırımları için Hazine fonlarından teknolojik Ar-Ge desteği tahsis et.",
                     "effects": {"justice": -2, "people": -6, "treasury": 8, "military": 0, "authority": 4},
                     "log": "Dijital dönüşüm Hazine kaynaklarıyla hızlandırıldı; kamu veri güvenliği tahkim edildi."},
                    {"label": "Siber suç şebekelerine ve korsan çağrı merkezlerine karşı emniyet siber timlerini eşzamanlı operasyona sür.",
                     "effects": {"justice": -2, "people": -7, "treasury": 0, "military": 9, "authority": 8},
                     "log": "Siber çeteler çökertildi; vatandaşları dolandıran sahte çağrı merkezleri mühürlendi."},
                    {"label": "Dijital veri güvenliği ve yapay zeka etiğini düzenleyen 'Milli Dijitalleşme ve Bilişim Kanunu' çıkar.",
                     "effects": {"justice": 8, "people": 4, "treasury": -6, "military": 0, "authority": 8},
                     "log": "Bilişim mevzuatı çağın gereksinimlerine göre yenilendi; kurumsal siber güvenlik sağlandı."}
                ]

        # DOMAIN 17: Vicdan Davaları ve Toplumsal Adalet (580 to 609: tr_vaka_581 to tr_vaka_610)
        elif 580 <= i <= 609:
            if "Narin Güran" in title or "Çocuk Cinayeti" in title:
                options_map[eid] = [
                    {"label": "Tavşantepe köyündeki cinayeti örten organize suskunluk çemberini özel jandarma istihbaratı ve kriminal DNA ile kır; tüm failleri tutuklat.",
                     "effects": {"justice": 10, "people": 9, "treasury": -2, "military": 0, "authority": -2},
                     "log": "Adalet yerini buldu; küçük meleğin katilleri ve delilleri karartan tüm akraba ağı ağırlaştırılmış müebbet istemiyle hakim karşısına çıkarıldı."},
                    {"label": "Bölgedeki kadın dernekleri, barolar ve sivil toplumla ortaklaşa çocuk koruma seferberliği ilan et; köydeki çocukları devlet korumasına al.",
                     "effects": {"justice": -5, "people": 9, "treasury": -2, "military": 0, "authority": 7},
                     "log": "Milletin vicdanı teskin edildi; çocukların feodal baskı ve aile içi istismardan korunması için devlet zırhı sağlandı."},
                    {"label": "Davanın aydınlatılması için Adli Tıp, kriminal laboratuvarlar ve arama operasyonlarına sınırsız Hazine ödeneği sağla.",
                     "effects": {"justice": -2, "people": -6, "treasury": 8, "military": 0, "authority": 4},
                     "log": "Devletin tüm imkanları seferber edildi; tek bir karanlık nokta bırakılmaması için teknik analizler tamamlandı."},
                    {"label": "Köy çevresinde komando ve jandarma kordonu kurarak delil karartma, telefon sıfırlama ve tanıkları tehdit etme girişimlerini engelle.",
                     "effects": {"justice": -2, "people": -7, "treasury": 0, "military": 10, "authority": 9},
                     "log": "Köyde tam adli kontrol sağlandı; organize suç örgütü gibi hareket eden şebeke çökertildi."},
                    {"label": "Çocuk cinayetlerinde ve cinsel istismarda af ve infaz indirimini kesin olarak yasaklayan 'Narin Çocuk Koruma Kanunu' çıkar.",
                     "effects": {"justice": 9, "people": 5, "treasury": -6, "military": 0, "authority": 9},
                     "log": "Çocuklara kalkan olan tarihi kanun kabul edildi; çocuk katillerine af kapısı ebediyen kapatıldı."}
                ]
            elif "Yenidoğan Çetesi" in title or "Bebek Skandalı" in title:
                options_map[eid] = [
                    {"label": "SGK'dan para almak için bebekleri yoğun bakımda ölüme terk eden çetenin doktor ve yöneticilerini 'kasten öldürme'den tutuklat.",
                     "effects": {"justice": 10, "people": 9, "treasury": -2, "military": 0, "authority": -2},
                     "log": "Cumhuriyet tarihinin en vahşi sağlık çetesi çökertildi; savcıyı tehdit eden tetikçiler dahil tüm failler cezaevine tıkıldı."},
                    {"label": "Evlatlarını kaybeden acılı ailelerle Sağlık Bakanlığı'nda kriz masası topla; bebeklerin naklini devlet hastanelerine güvenle sağla.",
                     "effects": {"justice": -5, "people": 10, "treasury": -2, "military": 0, "authority": 7},
                     "log": "Ailelerin feryadına sahip çıkıldı; bebek yoğun bakımları tamamen kamunun güvenli ellerine devredildi."},
                    {"label": "Çeteye karışan 10 özel hastanenin ruhsatlarını derhal iptal et ve SGK'dan haksız aldıkları yüz milyonlarca lirayı Hazineye tahsil et.",
                     "effects": {"justice": -2, "people": -6, "treasury": 10, "military": 0, "authority": 5},
                     "log": "Hastaneler kapatıldı ve mühürlendi; kamunun hortumlanan kaynakları faiziyle kasaya geri aktarıldı."},
                    {"label": "Soruşturmayı yürüten Cumhuriyet Savcısı Engin Göknar'ı makamında tehdit eden mafya artıklarına adliyede ters kelepçe taktır.",
                     "effects": {"justice": -2, "people": -7, "treasury": 0, "military": 10, "authority": 10},
                     "log": "Devletin savcısına pusu kurmaya kalkanlar saatler içinde yakalandı; devletin heybeti gösterildi."},
                    {"label": "Özel hastanelerin yoğun bakım işletmelerini taşeronlaştırmasını yasaklayan 'Özel Hastaneler Teftiş ve Bebek Güvenliği Kanunu' çıkar.",
                     "effects": {"justice": 9, "people": 4, "treasury": -7, "military": 0, "authority": 9},
                     "log": "Sağlıkta taşeronluk vahşeti yasaklandı; tüm yoğun bakımlar bakanlığın anlık yapay zeka denetimine bağlandı."}
                ]
            elif "Özgecan Aslan" in title or "Münevver Karabulut" in title or "Emine Bulut" in title:
                options_map[eid] = [
                    {"label": "Kadın cinayetlerinde faillere 'iyi hal indirimi', 'kravat indirimi' ve 'haksız tahrik indirimi' uygulanmasını yargıda kesin olarak yasakla.",
                     "effects": {"justice": 10, "people": 9, "treasury": -2, "military": 0, "authority": -2},
                     "log": "Kadın katillerine hukuk zırhı delindi; hiçbir indirim uygulanmadan ağırlaştırılmış müebbet cezaları onandı."},
                    {"label": "Milyonlarca kadının meydanlara çıktığı gün adalet yürüyüşlerine destek ver; kadına şiddete karşı topyekun seferberlik ilan et.",
                     "effects": {"justice": -5, "people": 10, "treasury": -2, "military": 0, "authority": 7},
                     "log": "Millet kadınların çığlığına sahip çıktı; 'Ölmek İstemiyorum' feryadı devlet politikasına dönüştürüldü."},
                    {"label": "81 ilde Şiddet Önleme ve İzleme Merkezleri (ŞÖNİM) ve kadın sığınma evleri için Hazine bütçesinden özel ödenek ayır.",
                     "effects": {"justice": -2, "people": -6, "treasury": 9, "military": 0, "authority": 4},
                     "log": "Şiddet mağduru kadınlara güvenli sığınak ve nakdi destek sağlandı; devlet himayesi tahkim edildi."},
                    {"label": "Emniyet bünyesinde KADES uygulamasını ve Elektronik Kelepçe İzleme Merkezi'ni kurarak saldırganları 7/24 uydudan izle.",
                     "effects": {"justice": -2, "people": -7, "treasury": 0, "military": 10, "authority": 9},
                     "log": "KADES butonuyla binlerce kadının hayatı kurtarıldı; uzaklaştırma alan saldırganlar yakınına dahi yaklaşamadı."},
                    {"label": "Kadına ve çocuğa karşı şiddette cezaları artıran ve koruma tedbirlerini genişleten 'Kadına Karşı Şiddetle Mücadele Kanunu' çıkar.",
                     "effects": {"justice": 9, "people": 5, "treasury": -6, "military": 0, "authority": 8},
                     "log": "Tarihi kadın koruma zırhı kanunlaştı; kadın cinayetlerinde cezalar en ağır seviyeye çıkarıldı."}
                ]
            elif "Soma" in title or "Çorlu Tren" in title:
                options_map[eid] = [
                    {"label": "Faciada ihmali ve kusuru bulunan maden patronları, bürokratlar ve denetimciler hakkında 'olası kastla öldürme'den ceza ver.",
                     "effects": {"justice": 10, "people": 8, "treasury": -2, "military": 0, "authority": -2},
                     "log": "İş kazası değil katliam tescillendi; patronlar ve sorumlular Ağır Ceza Mahkemesi'nde onlarca yıl hapse mahkum edildi."},
                    {"label": "Şehit madenci ve tren yolcusu aileleriyle bir araya gelerek her aileye bir devlet memuriyeti ve konut desteği sağla.",
                     "effects": {"justice": -5, "people": 9, "treasury": -3, "military": 0, "authority": 7},
                     "log": "Yetim kalan evlatlara devlet sahip çıktı; madenci ailelerinin gelecekleri devlet teminatına alındı."},
                    {"label": "Faciaya yol açan maden ocaklarını ve demiryolu hatlarını baştan sona yenilemek için Hazine afet bütçesini tahsis et.",
                     "effects": {"justice": -2, "people": -6, "treasury": 9, "military": 0, "authority": 4},
                     "log": "Madenlerde ve demiryollarında altyapı yenilendi; Hazine kaynaklarıyla modern sinyalizasyon ve yaşam odaları kuruldu."},
                    {"label": "İş güvenliği kurallarına uymayan tüm maden ocaklarını Çalışma Bakanlığı ve polis zoruyla derhal mühürle.",
                     "effects": {"justice": -2, "people": -7, "treasury": 0, "military": 9, "authority": 9},
                     "log": "İş güvenliği tavizsiz uygulandı; kurallara uymayan vahşi işletmelerin çalışmasına izin verilmedi."},
                    {"label": "Madenlerde zorunlu 'Sığınma Odaları' (Yaşam Odası) ve demiryollarında meteorolojik erken uyarı şartı getiren reform kanunu çıkar.",
                     "effects": {"justice": 8, "people": 4, "treasury": -7, "military": 0, "authority": 8},
                     "log": "İşçi sağlığı ve can güvenliği kanunla korundu; madenlerde yaşam odası zorunlu hale getirildi."}
                ]
            else:
                options_map[eid] = [
                    {"label": "Vicdanları yaralayan adli vakada hukukun üstünlüğü, şeffaflık ve adil yargılanma ilkelerini tavizsiz işlet.",
                     "effects": {"justice": 9, "people": 7, "treasury": -2, "military": 0, "authority": -3},
                     "log": "Hukuk devleti işletildi; failler mahkemede adil ve ağır cezalarla yargılandı."},
                    {"label": "Mağdur aileler, barolar ve sivil toplumla istişare ederek toplumsal adalet ve vicdan beklentisini karşıla.",
                     "effects": {"justice": -6, "people": 8, "treasury": -2, "military": 0, "authority": 7},
                     "log": "Toplumsal infial dindirildi; devletin adalet dağıtıcı şefkati halka hissettirildi."},
                    {"label": "Mağdurların rehabilitasyonu ve adli yardım masrafları için Adalet bütçesinden özel fon tahsis et.",
                     "effects": {"justice": -2, "people": -6, "treasury": 8, "military": 0, "authority": 4},
                     "log": "Mağdur hakları finanse edildi; adli süreçlerde ailelerin yalnız kalması önlendi."},
                    {"label": "Toplumsal infial yaratan olaylarda provokasyonlara ve linç girişimlerine karşı kolluk tedbirlerini sıkı tut.",
                     "effects": {"justice": -3, "people": -8, "treasury": 0, "military": 9, "authority": 8},
                     "log": "Sokak asayişi korundu; adaletin sokakta değil mahkeme salonlarında tecelli etmesi sağlandı."},
                    {"label": "Mağdur haklarını ve adil yargılanma standartlarını yükselten 'Toplumsal Adalet Reform Kanunu' çıkar.",
                     "effects": {"justice": 8, "people": 4, "treasury": -6, "military": 0, "authority": 8},
                     "log": "Ceza mevzuatı güncellendi; benzer vicdani faciaların önü kurumsal kanunlarla kesildi."}
                ]

        # DOMAIN 18: Eğitim, Sınavlar ve Gençlik (610 to 639: tr_vaka_611 to tr_vaka_640)
        elif 610 <= i <= 639:
            if "KPSS" in title or "Soru Sızıntısı" in title:
                options_map[eid] = [
                    {"label": "Soru sızıntısı ve şaibe iddiaları üzerine sınavı derhal iptal et; ÖSYM yöneticilerini görevden alıp DDK teftişi başlat.",
                     "effects": {"justice": 10, "people": 8, "treasury": -3, "military": 0, "authority": -2},
                     "log": "Milyonlarca gencin hakkı korundu; şaibeli sınav iptal edilerek soru hırsızları hakkında adli soruşturma açıldı."},
                    {"label": "Sınava giren gençlerle ve sendikalarla görüş; yeni sınavı tamamen ücretsiz ve güvenli koşullarda yapma taahhüdü ver.",
                     "effects": {"justice": -5, "people": 9, "treasury": -3, "military": 0, "authority": 7},
                     "log": "Gençlerin devlete olan güveni tazelendi; ücretsiz tekrar sınavıyla mağduriyetler giderildi."},
                    {"label": "İptal edilen sınavın yeniden basımı, nakli ve güvenliği için Hazine bütçesinden ek sınav ödeneği çıkar.",
                     "effects": {"justice": -2, "people": -6, "treasury": 8, "military": 0, "authority": 4},
                     "log": "Yeni sınav maliyeti Hazinece üstlenildi; adaylardan tek kuruş sınav ücreti alınmadı."},
                    {"label": "ÖSYM Soru Hazırlama Merkezi'ne sinyal kesici jammer, faraday kafesi ve kriptolu çelik kapılarla askeri güvenlik kur.",
                     "effects": {"justice": -2, "people": -7, "treasury": 0, "military": 9, "authority": 9},
                     "log": "Soru basım merkezi kozmik odaya dönüştürüldü; soruların dışarı sızması imkansız kılındı."},
                    {"label": "Tüm merkezi sınavlarda liyakati güvenceye alan 'ÖSYM Teşkilat ve Sınav Güvenliği Reform Kanunu' çıkar.",
                     "effects": {"justice": 8, "people": 4, "treasury": -6, "military": 0, "authority": 8},
                     "log": "Sınav hırsızlığına en ağır hapis cezaları getirildi; kamuya personel alımında adalet tesis edildi."}
                ]
            elif "Başörtüsü" in title or "Katsayı" in title:
                options_map[eid] = [
                    {"label": "Üniversitelerde ve kamuda kılık-kıyafet yasağı ve katsayı adaletsizliğini anayasal eşitlik ilkesiyle tamamen bitir.",
                     "effects": {"justice": 10, "people": 9, "treasury": -2, "military": 0, "authority": -2},
                     "log": "Tarihi zulüm son buldu; başörtülü kızlar ikna odalarından kurtularak tıp, hukuk ve mühendislik fakültelerini birincilikle bitirdi."},
                    {"label": "Öğrenci kulüpleri, akademisyenler ve sivil toplumla görüşerek kampüslerde barış ve özgürlük iklimini kurumsallaştır.",
                     "effects": {"justice": -5, "people": 10, "treasury": -2, "military": 0, "authority": 7},
                     "log": "Üniversitelerde kucaklaşma sağlandı; ideolojik kutuplaşmanın yerini bilimsel çalışma aldı."},
                    {"label": "Meslek liseleri ve İmam Hatiplerin laboratuvar ve atölye altyapısını güçlendirmek için Hazine destekli teşvikler sağla.",
                     "effects": {"justice": -2, "people": -6, "treasury": 8, "military": 0, "authority": 4},
                     "log": "Mesleki eğitim ihya edildi; sanayinin nitelikli eleman ihtiyacı giderildi."},
                    {"label": "Yasağın kaldırılmasına karşı kampüslerde provokasyon ve baskı yapmaya kalkan kliklere karşı üniversite güvenliğini koru.",
                     "effects": {"justice": -2, "people": -7, "treasury": 0, "military": 8, "authority": 9},
                     "log": "Öğrencilerin eğitim hakkı korundu; hiç kimsenin kılık-kıyafetinden dolayı engellenmesine izin verilmedi."},
                    {"label": "Kamuda ve üniversitelerde temel hak ve hürriyetleri teminat altına alan 'Eğitimde Fırsat Eşitliği Kanunu' çıkar.",
                     "effects": {"justice": 8, "people": 5, "treasury": -6, "military": 0, "authority": 8},
                     "log": "Katsayı ve başörtüsü engelleri tarihe gömüldü; tüm evlatlarımız anayasal eşitliğe kavuştu."}
                ]
            elif "KYK" in title or "Yurt" in title or "Barınamıyoruz" in title:
                options_map[eid] = [
                    {"label": "Öğrenim kredisi alan gençlerin sırtındaki TÜFE ve gecikme faizi borçlarını kanunla tamamen sil; sadece ana parayı al.",
                     "effects": {"justice": 9, "people": 9, "treasury": -3, "military": 0, "authority": -2},
                     "log": "Gençliğe tarihi müjde verildi; 3.3 milyon mezunun 30 milyar liralık faiz borcu devlet tarafından affedildi."},
                    {"label": "Öğrenci temsilcileriyle Bakanlıkta buluş; barınma sorunu yaşayan tüm üniversitelilere acil geçici otel ve misafirhane aç.",
                     "effects": {"justice": -5, "people": 10, "treasury": -3, "military": 0, "authority": 7},
                     "log": "Öğrenciler sokakta bırakılmadı; devletin tüm tesisleri üniversite gençliğine tahsis edildi."},
                    {"label": "Devlet yurt kapasitesini 950 bin yatağa çıkarmak için Hazine bütçesinden 100 yeni modern yurt binası inşa et.",
                     "effects": {"justice": -2, "people": -6, "treasury": 9, "military": 0, "authority": 4},
                     "log": "Dünyanın en büyük yurt kapasitesi kuruldu; başvuran öğrencilerin %98'i devlet yurtlarına yerleştirildi."},
                    {"label": "Yurtları ve öğrenci eylemlerini bahane ederek kampüslerde kaos çıkarmak isteyen marjinal örgütleri engelle.",
                     "effects": {"justice": -3, "people": -8, "treasury": 0, "military": 8, "authority": 8},
                     "log": "Gençlerin güvenliği sağlandı; provokatörlerin öğrencileri sokak çatışmasına sürüklemesi önlendi."},
                    {"label": "Tüm üniversite öğrencilerine ücretsiz internet, ulaşım indirimi ve beslenme yardımı sağlayan 'Gençlik Destek Kanunu' çıkar.",
                     "effects": {"justice": 8, "people": 4, "treasury": -7, "military": 0, "authority": 8},
                     "log": "Gençlik hakları kanunlaştı; burs ve beslenme yardımları kalıcı devlet güvencesine alındı."}
                ]
            else:
                options_map[eid] = [
                    {"label": "Eğitimde liyakat, fırsat eşitliği ve öğretmenlik meslek standartlarını anayasal kurallarla koru.",
                     "effects": {"justice": 8, "people": 7, "treasury": -2, "military": 0, "authority": -3},
                     "log": "Eğitimde fırsat eşitliği gözetildi; tüm öğrencilerin eğitime erişim hakkı korundu."},
                    {"label": "Öğretmen sendikaları, veliler ve eğitim bilimcilerle ortak milli eğitim şurası toplayarak müfredat uzlaşısı sağla.",
                     "effects": {"justice": -6, "people": 8, "treasury": -2, "military": 0, "authority": 7},
                     "log": "Eğitim camiası ile diyalog kuruldu; okullarda huzur ve motivasyon sağlandı."},
                    {"label": "Okulların teknolojik altyapısı, akıllı tahta ve ücretsiz yemek dağıtımı için Hazine bütçesinden kaynak ayır.",
                     "effects": {"justice": -2, "people": -6, "treasury": 8, "military": 0, "authority": 4},
                     "log": "Okulların fiziki imkanları güçlendirildi; eğitim yatırımları bütçeden karşılandı."},
                    {"label": "Okul çevrelerinde uyuşturucu tacirleri ve çetelere karşı 'Güvenli Okul' polis devriyelerini görevlendir.",
                     "effects": {"justice": -2, "people": -7, "treasury": 0, "military": 9, "authority": 8},
                     "log": "Okul kapılarında tam güvenlik sağlandı; çocuklarımız zararlı alışkanlıklardan korundu."},
                    {"label": "Türkiye Yüzyılı maarif vizyonunu hayata geçiren 'Milli Eğitim ve Öğretmenlik Reform Kanunu' çıkar.",
                     "effects": {"justice": 8, "people": 4, "treasury": -6, "military": 0, "authority": 8},
                     "log": "Eğitim sistemi çağdaş standartlarla yenilendi; nesillerin geleceği teminat altına alındı."}
                ]

    print(f"Total options generated for Batch 6: {len(options_map)}")
    updated_deck = apply_options_to_deck(deck, options_map)
    save_modern_deck(updated_deck)

if __name__ == '__main__':
    generate_domains_16_to_18()
