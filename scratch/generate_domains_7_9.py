import json
from deck_utils import load_modern_deck, save_modern_deck, apply_options_to_deck

# Domain 7: Terörle Mücadele ve Hendek Olayları (tr_vaka_281 - tr_vaka_310)
# Domain 8: 15 Temmuz Darbe Girişimi ve Yeni Sistem (tr_vaka_311 - tr_vaka_340)
# Domain 9: Dış Politika ve Sınır Ötesi Harekâtlar (tr_vaka_341 - tr_vaka_370)

def generate_domains_7_to_9():
    deck = load_modern_deck()
    print("Building realistic options for Domains 7, 8, and 9 (tr_vaka_281 to tr_vaka_370)...")
    options_map = {}

    for i in range(280, 370):
        ev = deck[i]
        eid = ev['id']
        title = ev['title']
        desc = ev['desc']

        # DOMAIN 7 (indices 280 to 309: tr_vaka_281 to tr_vaka_310)
        if 280 <= i <= 309:
            if "Hendek" in title or "Cizre" in title or "Sur" in title or "Nusaybin" in title:
                options_map[eid] = [
                    {"label": "Operasyon bölgesinde sivillerin zarar görmemesi için tahliye koridorları aç; insan hakları ve tahkikat süreçlerini savcılarla denetle.",
                     "effects": {"justice": 8, "people": 7, "treasury": -2, "military": 0, "authority": -3},
                     "log": "Sivil can kaybını önleyen tahkikatlar yapıldı; hukuki meşruiyet uluslararası arenada korundu."},
                    {"label": "Bölge halkı, kanaat önderleri ve esnafla görüşerek sokağa çıkma yasağının getirdiği mağduriyetleri doğrudan ayni yardımlarla hafiflet.",
                     "effects": {"justice": -6, "people": 8, "treasury": -3, "military": 0, "authority": 7},
                     "log": "Halkın devlete olan bağı korundu; terör örgütünün halkı ayaklandırma çağrıları boşa çıkarıldı."},
                    {"label": "Çatışmalarda yıkılan tarihi Sur içi ve ilçe merkezlerinin yeniden inşası için Hazine'den devasa kentsel dönüşüm fonu ayır.",
                     "effects": {"justice": -2, "people": -6, "treasury": 8, "military": 0, "authority": 4},
                     "log": "Tarihi yapılar ihya edildi; mağdur ailelere modern TOKİ konutları ve kira yardımları bağlandı."},
                    {"label": "Jandarma Özel Asayiş Komutanlığı (JÖAK) ve Polis Özel Harekat (PÖH) müşterek timleriyle hendek ve barikatları patlatarak ilçeleri temizle.",
                     "effects": {"justice": -3, "people": -8, "treasury": 0, "military": 10, "authority": 9},
                     "log": "İlçe merkezleri teröristlerden arındırıldı; çukur siyaseti hendeklere gömülerek devlet hakimiyeti kuruldu."},
                    {"label": "Terörden zarar gören il ve ilçelerin imarı ve yerel yönetimlerin teröre finansman sağlamasını engelleyen 'İl İdaresi Kanunu Reformu' çıkar.",
                     "effects": {"justice": 8, "people": 4, "treasury": -7, "military": 0, "authority": 8},
                     "log": "Yerel yönetimlerin hendek kazmasına karşı kalıcı mülki amir vesayeti ve denetim mekanizması getirildi."}
                ]
            elif "Fethi Sekin" in title:
                options_map[eid] = [
                    {"label": "İzmir Adliyesi'ne saldıran terör hücresinin tüm lojistik ve istihbarat ağını savcılık marifetiyle çözüp işbirlikçileri adalete teslim et.",
                     "effects": {"justice": 9, "people": 8, "treasury": -2, "military": 0, "authority": -2},
                     "log": "Adliye saldırısının arkasındaki şebeke çökertildi; şehit polisin kanı yerde bırakılmadı."},
                    {"label": "Tüm İzmir halkı ve adliye çalışanlarıyla dev bir anma töreni düzenle; şehit polisin kahramanlığını milli hafızaya kazı.",
                     "effects": {"justice": -5, "people": 9, "treasury": -2, "military": 0, "authority": 7},
                     "log": "Millet tek yürek oldu; terörün adliyeyi rehin alma ve yüzlerce insanı katletme planı kahramanca bozuldu."},
                    {"label": "Şehit Trafik Polisi Fethi Sekin ve şehit mübaşir Musa Can'ın ailelerine ömür boyu maaş, konut ve çocuklarına eğitim bursu bağla.",
                     "effects": {"justice": -2, "people": -6, "treasury": 8, "military": 0, "authority": 4},
                     "log": "Şehit ailelerine devletin şefkati uzandı; gelecekleri devlet teminatına alındı."},
                    {"label": "Tek tabancasıyla mermisi bitene kadar kalaşnikoflu teröristlerle çatışan kahramanın izinden giderek adliye önlerinde zırhlı polis noktaları kur.",
                     "effects": {"justice": -3, "people": -7, "treasury": 0, "military": 10, "authority": 9},
                     "log": "Tüm adliyeler çevresinde yüksek güvenlik kalkanı kuruldu; terör hedefleri bertaraf edildi."},
                    {"label": "Görev başında canını siper eden güvenlik görevlilerinin aile haklarını ve kahramanlık taltifini düzenleyen 'Milli Şehitlik Yasası' çıkar.",
                     "effects": {"justice": 8, "people": 4, "treasury": -6, "military": 0, "authority": 8},
                     "log": "Kahraman polis ve askerlerin anayasal hakları güvenceye alındı; anıları adliye caddelerinde yaşatıldı."}
                ]
            elif "Dağlıca" in title or "Aktütün" in title:
                options_map[eid] = [
                    {"label": "Karakol baskınındaki istihbarat zafiyetleri ve lojistik gecikmeler hakkında adli ve askeri teftiş heyeti görevlendir.",
                     "effects": {"justice": 9, "people": 7, "treasury": -2, "military": 0, "authority": -3},
                     "log": "Sınır karakollarındaki açıklar tespit edildi; ihmali olan komuta kademesi adli teftişe tabi tutuldu."},
                    {"label": "Şehit aileleri ve yaralı gazilerle bir araya gelerek milletin infialini vakar ve metanetle kucakla.",
                     "effects": {"justice": -6, "people": 9, "treasury": -2, "military": 0, "authority": 6},
                     "log": "Milletin bağrı yangın yerine döndü; birlik ve beraberlik mesajlarıyla fitne engellendi."},
                    {"label": "Savunma Sanayii İcra Komitesi'ni toplayarak sınır karakollarının yerini alacak 'Yüksek Güvenlikli Kalekol' inşasına acil Hazine fonu aktar.",
                     "effects": {"justice": -2, "people": -6, "treasury": 9, "military": 0, "authority": 4},
                     "log": "Sınır boylarına havan ve roket geçirmez Kalekollar yapıldı; Mehmetçiğin üs güvenliği tahkim edildi."},
                    {"label": "F-16'lar ve Özel Kuvvetler taburlarıyla sınır ötesindeki terör kamplarına (Zap, Avaşin, Kandil) amansız hava harekatı başlat.",
                     "effects": {"justice": -2, "people": -7, "treasury": 0, "military": 10, "authority": 9},
                     "log": "Sınır ötesi terör inleri yerle bir edildi; Mehmetçiğin intikamı misliyle alındı."},
                    {"label": "Milli Savunma Bakanlığı bünyesinde 'Profesyonel Sınır Birlikleri ve Askeri Üs Güvenliği Kanunu' çıkar.",
                     "effects": {"justice": 8, "people": 3, "treasury": -7, "military": 0, "authority": 8},
                     "log": "Zorunlu askerlik yerine profesyonel komando tugayları sınır hattına yerleştirildi."}
                ]
            elif "6-8 Ekim Olayları" in title or "Yasin Börü" in title:
                options_map[eid] = [
                    {"label": "Kobani bahanesiyle sokağa dökülüp kurban eti dağıtan gençleri vahşice katleden failleri ve kışkırtıcıları Ağır Ceza'da yargılat.",
                     "effects": {"justice": 9, "people": 8, "treasury": -2, "military": 0, "authority": -3},
                     "log": "Vahşetin failleri tek tek yakalandı; sokak isyanı çağrısı yapan siyasi sorumlular adalet önüne çıkarıldı."},
                    {"label": "Diyarbakır ve bölge halkıyla temas kurarak sivil toplum kuruluşlarıyla provokasyonun mezhep ve etnik çatışmaya evrilmesini önle.",
                     "effects": {"justice": -6, "people": 8, "treasury": -2, "military": 0, "authority": 7},
                     "log": "Bölge halkı sokak terörüne prim vermedi; iç savaş provokasyonu kardeşlik bağıyla boşa çıkarıldı."},
                    {"label": "Yakılan kamu binaları, okullar, ambulanslar ve yağmalanan esnaf dükkanlarının zararını Hazine fonundan tazmin et.",
                     "effects": {"justice": -2, "people": -6, "treasury": 8, "military": 0, "authority": 4},
                     "log": "Esnafın yaraları sarıldı; kamu binaları hızla tamir edilerek devlet hizmetleri aksatılmadı."},
                    {"label": "35 ilde sokakları ateşe veren ve kamu düzenini tehdit eden kalkışmaya karşı zırhlı polis ve jandarmayla sert müdahale et.",
                     "effects": {"justice": -3, "people": -8, "treasury": 0, "military": 10, "authority": 9},
                     "log": "Kalkışma 48 saatte bastırıldı; sokak teröristlerine devletin demir yumruğu indirildi."},
                    {"label": "Şiddet çağrısı yapan ve kamu düzenini bozan siyasi parti eylemlerine karşı 'İç Güvenlik Reform Kanunu' çıkar.",
                     "effects": {"justice": 8, "people": 4, "treasury": -6, "military": 0, "authority": 8},
                     "log": "Mülki amirlere ve polise molotof ve taşlı saldırılara karşı anında müdahale yetkisi tanındı."}
                ]
            else:
                options_map[eid] = [
                    {"label": f"{title} hadisesinde terör suçlularını hukuk ve anayasa çerçevesinde yargı önüne çıkarıp adli hesabı sor.",
                     "effects": {"justice": 8, "people": 7, "treasury": -2, "military": 0, "authority": -3},
                     "log": f"{title} konusunda hukuki süreç tavizsiz işletildi; terör eylemlerine karşı meşru adli tahkikat yürütüldü."},
                    {"label": f"{title} sürecinde sivil halkı ve mağdur aileleri korumak için toplumsal dayanışma ve uzlaşı kanallarını işlet.",
                     "effects": {"justice": -6, "people": 8, "treasury": -2, "military": 0, "authority": 7},
                     "log": f"{title} hadisesinde halk teskin edildi; fitne ve kargaşa yaratma girişimleri bertaraf edildi."},
                    {"label": f"{title} ile zarar gören kamu altyapısını ve vatandaş mülklerini Hazine fonlarıyla hızla ihya et.",
                     "effects": {"justice": -2, "people": -6, "treasury": 8, "military": 0, "authority": 4},
                     "log": f"{title} mali olarak telafi edildi; kamu kaynaklarıyla bölge güvenliği ve refahı finanse edildi."},
                    {"label": f"{title} karşısında emniyet, jandarma ve TSK unsurlarını tam yetkiyle sahaya sürerek terör tehdidini yok et.",
                     "effects": {"justice": -3, "people": -8, "treasury": 0, "military": 10, "authority": 9},
                     "log": f"{title} karşısında tavizsiz güvenlik tedbirleri uygulandı; devletin kudreti gösterildi."},
                    {"label": f"TBMM'de {title} konusundaki kurumsal zafiyetleri kapatan Terörle Mücadele ve İç Güvenlik Kanunu'nu güncelle.",
                     "effects": {"justice": 8, "people": 4, "treasury": -6, "military": 0, "authority": 8},
                     "log": f"Kabul edilen yasal reform ile güvenlik mimarisi tahkim edildi; benzer tehditler önlendi."}
                ]

        # DOMAIN 8 (indices 310 to 339: tr_vaka_311 to tr_vaka_340)
        elif 310 <= i <= 339:
            if "Boğaziçi Köprüsü" in title or "15 Temmuz" in title or "Ömer Halisdemir" in title:
                options_map[eid] = [
                    {"label": "Darbe teşebbüsünde bulunan cunta mensupları hakkında cumhuriyet başsavcılıklarınca derhal ağırlaştırılmış müebbet davaları aç.",
                     "effects": {"justice": 9, "people": 9, "treasury": -2, "military": 0, "authority": -2},
                     "log": "Hukuk devleti cuntaya teslim olmadı; darbeci generaller ve hainler bağımsız mahkemelerde hesap vermeye başladı."},
                    {"label": "Cumhurbaşkanı'nın çağrısıyla sokaklara, meydanlara ve havalimanlarına akın eden milyonlarca vatansevere öncülük et.",
                     "effects": {"justice": -5, "people": 10, "treasury": -2, "military": 0, "authority": 8},
                     "log": "Milli irade tankları çıplak elleriyle durdurdu; millet devletiyle birleşerek tarihin en büyük destanını yazdı."},
                    {"label": "Darbe girişiminin finansal piyasalarda oluşturduğu şoku önlemek için bankaları açık tut; Merkez Bankası piyasaya sınırsız TL sağla.",
                     "effects": {"justice": -2, "people": -6, "treasury": 9, "military": 0, "authority": 4},
                     "log": "Ekonomik panik püskürtüldü; pazartesi sabahı piyasalar açılarak spekülatif çöküş engellendi."},
                    {"label": "Ömer Halisdemir'in Özel Kuvvetler Karargahı'nda cuntacı Semih Terzi'yi alnından vurarak başlattığı direnişi tüm kışlalarda uygulat.",
                     "effects": {"justice": -2, "people": -7, "treasury": 0, "military": 10, "authority": 10},
                     "log": "Kahraman Mehmetçik ve vatansever polisler cuntayı kışlalarında etkisiz hale getirdi; darbe girişimi ezildi."},
                    {"label": "Milli Güvenlik Kurulu ve Bakanlar Kurulu kararıyla 3 ay süreyle Olağanüstü Hal (OHAL) ilan edip KHK yetkilerini yürürlüğe koy.",
                     "effects": {"justice": 8, "people": 4, "treasury": -6, "military": 0, "authority": 9},
                     "log": "Devletin bekası anayasal OHAL rejimiyle korundu; ordu, emniyet ve yargıdaki cuntacı sızıntılar hızla temizlendi."}
                ]
            elif "KHK İhraçları" in title or "Milli Savunma Üniversitesi" in title:
                options_map[eid] = [
                    {"label": "OHAL İnceleme Komisyonu kurarak ihraç edilen kamu personelinin yargısal denetim ve itiraz yollarını açık tut.",
                     "effects": {"justice": 9, "people": 7, "treasury": -2, "military": 0, "authority": -3},
                     "log": "Hukuki başvuru mekanizması kuruldu; haksız ihraç iddiaları bağımsız komisyonca incelenip hak iadeleri yapıldı."},
                    {"label": "Kapatılan askeri okulların masum öğrencilerini ve kamu personelini sivil üniversitelere yerleştirerek mağduriyeti önle.",
                     "effects": {"justice": -6, "people": 8, "treasury": -3, "military": 0, "authority": 7},
                     "log": "Öğrencilerin eğitim hakları korundu; toplumdaki kutuplaşmanın derinleşmesi engellendi."},
                    {"label": "El konulan terör iltisaklı okul, hastane ve holding varlıklarını Hazine ve Vakıflar Genel Müdürlüğü'ne devret.",
                     "effects": {"justice": -2, "people": -6, "treasury": 10, "military": 0, "authority": 5},
                     "log": "Milyarlarca liralık taşınmaz kamuya kazandırıldı; devlet bütçesi tahkim edildi."},
                    {"label": "Genelkurmay Başkanlığı ve Kuvvet Komutanlıklarını doğrudan Milli Savunma Bakanlığı'na bağlayarak askeri vesayeti bitir.",
                     "effects": {"justice": -3, "people": -7, "treasury": 0, "military": 9, "authority": 10},
                     "log": "Orduda emir-komuta sivil bakanlığa bağlandı; TSK modern demokratik ordu yapısına kavuşturuldu."},
                    {"label": "Harp Akademilerini lağvedip yerine modern ve sivil denetime açık 'Milli Savunma Üniversitesi'ni kuran KHK'yı yasalaştır.",
                     "effects": {"justice": 8, "people": 4, "treasury": -6, "military": 0, "authority": 9},
                     "log": "Askeri eğitim sıfırdan inşa edildi; subay yetiştirme sistemi liyakat ve vatanseverlik esasına bağlandı."}
                ]
            elif "Cumhurbaşkanlığı Hükümet Sistemi" in title or "2017 Referandumu" in title:
                options_map[eid] = [
                    {"label": "16 Nisan referandum sonuçlarını ve YSK kararlarını anayasal meşruiyet ve halk iradesi zemininde tescil ettir.",
                     "effects": {"justice": 8, "people": 8, "treasury": -2, "military": 0, "authority": -2},
                     "log": "Halkoylaması sonucu meşruiyet kazandı; Türkiye parlamenter sistemden başkanlık modeline geçti."},
                    {"label": "Yeni sistemin geçiş sürecinde meclisteki tüm siyasi partiler ve bürokrasiyle uyum komisyonları topla.",
                     "effects": {"justice": -6, "people": 8, "treasury": -2, "military": 0, "authority": 7},
                     "log": "Bakanlıkların birleşme süreci uzlaşıyla yürütüldü; bürokraside kaos yaşanması engellendi."},
                    {"label": "Başbakanlık ve bakanlıkların lağvedilmesiyle ortaya çıkan mükerrer harcamaları keserek Hazine'de tasarruf sağla.",
                     "effects": {"justice": -2, "people": -6, "treasury": 9, "military": 0, "authority": 4},
                     "log": "Bürokratik hantallık azaltıldı; hızlı karar alma süreçleriyle Hazineye tasarruf sağlandı."},
                    {"label": "Yürütmenin tek elde toplanmasıyla krizlere anında müdahale kabiliyetini göster; güvenlik bürokrasisini doğrudan Başkana bağla.",
                     "effects": {"justice": -3, "people": -7, "treasury": 0, "military": 9, "authority": 10},
                     "log": "Yürütmede çift başlılık sona erdi; devletin kriz yönetimi ve operasyon hızı katlandı."},
                    {"label": "1 Numaralı Cumhurbaşkanlığı Kararnamesi ile yeni devlet teşkilatını, ofisleri ve kurulları resmen kur.",
                     "effects": {"justice": 8, "people": 4, "treasury": -7, "military": 0, "authority": 9},
                     "log": "Cumhurbaşkanlığı Hükümet Sistemi yürürlüğe girdi; yeni cumhuriyet dönemi başladı."}
                ]
            elif "İstanbul Seçimleri" in title or "31 Mart 2019" in title:
                options_map[eid] = [
                    {"label": "YSK'nın seçim iptali ve yenileme kararını hukuk çerçevesinde uygulat; 23 Haziran'da şeffaf ve güvenli bir sandık kur.",
                     "effects": {"justice": 9, "people": 8, "treasury": -2, "military": 0, "authority": -3},
                     "log": "Demokratik seçim süreci işletildi; 23 Haziran'da halkın ezici iradesi sandıkta tescillendi."},
                    {"label": "Seçim sonuçlarını vakarla karşılayarak kazanan adayı tebrik et; merkezi hükümet ile yerel yönetim arasında hizmet köprüsü kur.",
                     "effects": {"justice": -5, "people": 9, "treasury": -2, "military": 0, "authority": 7},
                     "log": "Halkın kararına saygı duyuldu; gerilim düşürülerek büyükşehirde hizmetlerin aksamaması sağlandı."},
                    {"label": "Seçimlerin yenilenmesi maliyetini asgari düzeyde tut; belediye bütçesindeki harcamaları Sayıştay denetimine tabi tut.",
                     "effects": {"justice": -2, "people": -6, "treasury": 8, "military": 0, "authority": 4},
                     "log": "Kamu harcamaları denetlendi; seçim harcamalarının kamu bütçesine yükü sınırlandırıldı."},
                    {"label": "Sandık güvenliğini sağlamak için İstanbul genelinde 40 bin polis görevlendir; hiçbir şaibeye ve provokasyona izin verme.",
                     "effects": {"justice": -3, "people": -7, "treasury": 0, "military": 9, "authority": 8},
                     "log": "Sandık güvenliği kusursuz sağlandı; seçim günü tek bir asayiş olayı yaşanmadı."},
                    {"label": "Seçim kurulları ve sandık başkanlarının belirlenmesinde kamu görevlisi şartını katılaştıran 'Seçim Kanunu Reformu' çıkar.",
                     "effects": {"justice": 8, "people": 4, "treasury": -6, "military": 0, "authority": 8},
                     "log": "Seçim şaibeleri kanunla önlendi; sandık başkanlarının atanması net yasal çerçeveye bağlandı."}
                ]
            else:
                options_map[eid] = [
                    {"label": f"{title} hadisesinde Anayasa ve hukuk ilkelerini kararlılıkla savunarak meşruiyeti koru.",
                     "effects": {"justice": 8, "people": 7, "treasury": -2, "military": 0, "authority": -3},
                     "log": f"{title} konusunda anayasal kurallar gözetildi; devletin meşru düzeni korundu."},
                    {"label": f"{title} sürecinde siyasi partiler, meclis ve halkla diyalog kurarak toplumsal mutabakat sağla.",
                     "effects": {"justice": -6, "people": 8, "treasury": -2, "military": 0, "authority": 7},
                     "log": f"{title} geriliminde siyasi uzlaşı işletildi; çatışma ortamı yumuşatıldı."},
                    {"label": f"{title} sürecinin Hazine ve kamu bütçesi üzerindeki yükünü mali disiplinle kontrol altında tut.",
                     "effects": {"justice": -2, "people": -6, "treasury": 8, "military": 0, "authority": 4},
                     "log": f"{title} sebebiyle oluşabilecek kamu zararı engellendi; mali disiplin korundu."},
                    {"label": f"{title} karşısında emniyet ve kolluk bürokrasisini teyakkuza geçirerek kamu nizamını ve devlet otoritesini koru.",
                     "effects": {"justice": -3, "people": -8, "treasury": 0, "military": 9, "authority": 9},
                     "log": f"{title} karşısında devletin otoritesi gösterildi; kamu düzeni tavizsiz korundu."},
                    {"label": f"TBMM'de {title} konusunu yapısal olarak düzenleyen reform mevzuatını yürürlüğe koy.",
                     "effects": {"justice": 8, "people": 4, "treasury": -6, "military": 0, "authority": 8},
                     "log": f"Yürürlüğe giren yasa ile kurumsal intizam sağlandı; benzer krizlerin tekerrürü önlendi."}
                ]

        # DOMAIN 9 (indices 340 to 369: tr_vaka_341 to tr_vaka_370)
        elif 340 <= i <= 369:
            if "Mavi Marmara" in title or "İsrail" in title:
                options_map[eid] = [
                    {"label": "Uluslararası Ceza Mahkemesi ve BM İnsan Hakları Konseyi'nde İsrail aleyhine korsanlık ve kasten adam öldürme davaları açtır.",
                     "effects": {"justice": 9, "people": 8, "treasury": -2, "military": 0, "authority": -2},
                     "log": "Hukuk mücadelesi uluslararası alana taşındı; İsrailli komutanlar hakkında kırmızı bülten kararları çıkarıldı."},
                    {"label": "Şehit aileleri ve İHH heyetiyle koordinasyon kur; İsrail'den resmi özür ve tazminat şartı gelene kadar ilişkileri dondur.",
                     "effects": {"justice": -6, "people": 9, "treasury": -2, "military": 0, "authority": 7},
                     "log": "Milli onur tavizsiz savunuldu; Netanyahu'nun resmi özür dilemesi ve tazminat ödemesi sağlandı."},
                    {"label": "İsrail ile askeri ve savunma sanayii ihalelerini derhal iptal ederek yerli savunma sanayiine ek bütçe aktar.",
                     "effects": {"justice": -2, "people": -6, "treasury": 8, "military": 0, "authority": 4},
                     "log": "Milli savunma projeleri hızlandırıldı; Heron ve tank modernizasyonu bağımlılığı yerli firmalara devredildi."},
                    {"label": "Türk donanmasını Doğu Akdeniz'de teyakkuza geçir; Gazze ambargosuna karşı deniz sahasında fırkateyn devriyelerini artır.",
                     "effects": {"justice": -2, "people": -7, "treasury": 0, "military": 10, "authority": 9},
                     "log": "Doğu Akdeniz'de donanmanın caydırıcılığı hissettirildi; Türk bayraklı gemilere yönelik yeni tacizler önlendi."},
                    {"label": "Uluslararası sularda sivil yardım konvoylarının korunmasını güvenceye alan 'Deniz Güvenliği ve İnsani Diplomasi Kanunu' çıkar.",
                     "effects": {"justice": 8, "people": 4, "treasury": -6, "military": 0, "authority": 8},
                     "log": "İnsani diplomasinin hukuki altyapısı kuruldu; Türkiye mazlum milletlerin küresel hamisi oldu."}
                ]
            elif "Rus Su-24" in title or "Uçak Krizi" in title or "Putin" in title:
                options_map[eid] = [
                    {"label": "Suriye sınırında 17 saniyelik hava sahası ihlalini ve yapılan 10 acil telsiz uyarısını radar kayıtlarıyla BM'ye sun.",
                     "effects": {"justice": 8, "people": 8, "treasury": -3, "military": 0, "authority": -2},
                     "log": "Hukuki haklılık dünyaya belgelendi; sınır egemenliğini ihlal eden jete angajman kurallarının işletildiği kanıtlandı."},
                    {"label": "Moskova ile temas kanallarını açık tut; Cumhurbaşkanı mektubu ve diplomatik temaslarla iki ülke arasındaki krizi tatlıya bağla.",
                     "effects": {"justice": -6, "people": 8, "treasury": -3, "military": 0, "authority": 8},
                     "log": "Diplomatik kriz aşıldı; Rusya ile turizm, charter uçuşları ve ticari ilişkiler yeniden canlandırıldı."},
                    {"label": "Rusya'nın uyguladığı domates ve turizm ambargosunun Antalya ve Ege çiftçisine zararını Hazine sübvansiyonlarıyla karşıla.",
                     "effects": {"justice": -2, "people": -6, "treasury": 8, "military": 0, "authority": 4},
                     "log": "Çiftçiler iflastan kurtarıldı; alternatif ihracat pazarları bulunarak Hazine destekleri sağlandı."},
                    {"label": "Hatay ve Gaziantep sınır boylarına uçaksavar ve Hawk hava savunma bataryalarını yerleştirerek hava sahasını kapat.",
                     "effects": {"justice": -2, "people": -7, "treasury": 0, "military": 10, "authority": 9},
                     "log": "Hava sahası çelik kalkanla korundu; sınır boyunda caydırıcı hava üstünlüğü kuruldu."},
                    {"label": "TSK Hava Angajman Kuralları'nı modernize ederek ihlal anında otomatik mukabele yetkilerini kanunlaştıran reform yap.",
                     "effects": {"justice": 8, "people": 3, "treasury": -6, "military": 0, "authority": 8},
                     "log": "Sınır ihlallerine karşı Türk Hava Kuvvetleri'nin operasyonel yetkisi kanunla tescillendi."}
                ]
            elif "Fırat Kalkanı" in title or "Zeytin Dalı" in title or "Barış Pınarı" in title:
                options_map[eid] = [
                    {"label": "BM Şartı'nın 51. maddesindeki meşru müdafaa hakkına dayanarak sınır ötesi harekatın uluslararası hukuki zeminini tescille.",
                     "effects": {"justice": 9, "people": 8, "treasury": -3, "military": 0, "authority": -2},
                     "log": "Uluslararası meşruiyet sağlandı; terör koridoruna karşı askeri harekatın BM Sözleşmesi'ne uygunluğu kayıtlara geçti."},
                    {"label": "Suriye Milli Ordusu ve yerel aşiretlerle ortak harekat masası kur; kurtarılan bölgelerde sivil idare ve meclisleri canlandır.",
                     "effects": {"justice": -6, "people": 8, "treasury": -3, "military": 0, "authority": 7},
                     "log": "Yerel halkın desteği alındı; Cerablus, El-Bab ve Afrin'de yüz binlerce Suriyelinin güvenle evine dönmesi sağlandı."},
                    {"label": "Kurtarılan 4 bin kilometrekarelik güvenli bölgede hastane, okul, elektrik ve su altyapısı için AFAD bütçesinden fon ayır.",
                     "effects": {"justice": -2, "people": -6, "treasury": 8, "military": 0, "authority": 4},
                     "log": "Bölgede hayat normale döndü; Türkiye sınır ötesinde kalkınma ve huzur adası inşa etti."},
                    {"label": "Komandolar, zırhlı tugaylar ve Bayraktar TB2 SİHA'larla terör örgütü mevzilerini imha ederek güvenli derinlik oluştur.",
                     "effects": {"justice": -2, "people": -7, "treasury": 0, "military": 10, "authority": 10},
                     "log": "Terör koridoru parçalandı; Mehmetçik Afrin ve Fırat'ın doğusuna şanlı bayrağımızı dikti."},
                    {"label": "Kurtarılan bölgelerde mülki koordinatör valilikler ve yerel kolluk teşkilatını kuran 'Sınır Ötesi İnsani İdare Kanunu' çıkar.",
                     "effects": {"justice": 8, "people": 4, "treasury": -7, "military": 0, "authority": 9},
                     "log": "Güvenli bölgelerde kalıcı nizam tesis edildi; Türkiye'nin güney sınırında terör devleti kurulması önlendi."}
                ]
            elif "S-400" in title or "F-35" in title or "CAATSA" in title:
                options_map[eid] = [
                    {"label": "ABD'nin F-35 program ortaklığı sözleşmesini tek taraflı feshetmesini uluslararası tahkime taşı ve ödenen 1.4 milyar doları talep et.",
                     "effects": {"justice": 9, "people": 8, "treasury": -2, "military": 0, "authority": -2},
                     "log": "Uluslararası hukuk işletildi; parasını ödediğimiz jetlerin gasp edilmesine karşı dava açıldı."},
                    {"label": "Washington ile F-16 Blok 70 ve modernizasyon kitleri tedariki için Kongre nezdinde mekik diplomasisi yürüt.",
                     "effects": {"justice": -6, "people": 8, "treasury": -3, "military": 0, "authority": 7},
                     "log": "Kongre vetosu aşıldı; Türk Hava Kuvvetleri'nin vurucu gücünü koruyacak 40 yeni F-16 tedariki onaylandı."},
                    {"label": "CAATSA yaptırımlarına inat; Savunma Sanayii Destekleme Fonu'nu iki katına çıkararak KAAN ve Kızılelma projelerini hızlandır.",
                     "effects": {"justice": -2, "people": -6, "treasury": 9, "military": 0, "authority": 5},
                     "log": "Milli savunma sanayii şahlandı; ambargo Türkiye'yi kendi 5. nesil savaş uçağını (KAAN) üretmeye sevk etti."},
                    {"label": "Rusya'dan teslim alınan S-400 bataryalarını Mürted Hava Meydanı'na konuşlandırarak hava savunma teyakkuzuna al.",
                     "effects": {"justice": -2, "people": -7, "treasury": 0, "military": 10, "authority": 9},
                     "log": "Stratejik hava savunma kalkanı kuruldu; Türkiye ilk kez uzun menzilli balistik hava savunma füzesine sahip oldu."},
                    {"label": "Yerli hava savunma füzelerimizi (HİSAR, SİPER, KORKUT) kurumsallaştıran 'Çelik Kubbe Hava Savunma Kanunu' çıkar.",
                     "effects": {"justice": 8, "people": 4, "treasury": -7, "military": 0, "authority": 9},
                     "log": "Türkiye'nin katmanlı hava savunma mimarisi kanunlaştı; yabancı hava savunma bağımlılığı kırıldı."}
                ]
            elif "Mavi Vatan" in title or "Libya" in title or "Karabağ" in title:
                options_map[eid] = [
                    {"label": "Libya Ulusal Mutabakat Hükümeti ile imzalanan Deniz Yetki Alanları Anlaşması'nı Birleşmiş Milletler nezdinde resmen tescil ettir.",
                     "effects": {"justice": 10, "people": 8, "treasury": -2, "military": 0, "authority": -2},
                     "log": "Akdeniz'de tarihi hukuk zaferi kazanıldı; Sevilla haritası çöpe atılarak Türkiye'nin kıta sahanlığı tescillendi."},
                    {"label": "Kardeş Azerbaycan ile 'Tek Millet, İki Devlet' prensibiyle Şuşa Beyannamesi'ni imzalayarak askeri ittifakı taçlandır.",
                     "effects": {"justice": -5, "people": 10, "treasury": -3, "military": 0, "authority": 8},
                     "log": "Türk dünyası kenetlendi; Karabağ'ın 30 yıllık işgali 44 günlük şanlı harekatla sonlandırıldı."},
                    {"label": "Doğu Akdeniz ve Karadeniz'deki sismik arama ve petrol sondaj gemilerimiz (Oruç Reis, Fatih, Abdülhamid Han) için Hazine fonu tahsis et.",
                     "effects": {"justice": -2, "people": -6, "treasury": 9, "military": 0, "authority": 4},
                     "log": "Enerjide bağımsızlık rotası çizildi; Türkiye kendi gemileriyle derin denizlerde hidrokarbon aramaya başladı."},
                    {"label": "Mavi Vatan'da bayrak dalgalandıran Oruç Reis'i fırkateyn, denizaltı ve İHA'larımızla donanma kalkanına alarak Yunan tacizlerini defet.",
                     "effects": {"justice": -2, "people": -7, "treasury": 0, "military": 10, "authority": 10},
                     "log": "Donanmanın heybeti Doğu Akdeniz'i titretti; Türk gemilerine müdahale etmek isteyenler geri çekilmek zorunda kaldı."},
                    {"label": "Deniz yetki alanları, kıta sahanlığı ve münhasır ekonomik bölgeleri güvenceye alan 'Mavi Vatan Deniz Egemenliği Kanunu' çıkar.",
                     "effects": {"justice": 8, "people": 4, "treasury": -7, "military": 0, "authority": 9},
                     "log": "Denizlerimizdeki egemenlik haklarımız kanunlaştı; Türkiye Akdeniz'in vazgeçilmez lider gücü oldu."}
                ]
            else:
                options_map[eid] = [
                    {"label": f"{title} krizinde uluslararası hukuk, ikili anlaşmalar ve egemenlik haklarımızı tavizsiz savun.",
                     "effects": {"justice": 8, "people": 7, "treasury": -2, "military": 0, "authority": -3},
                     "log": f"{title} konusunda diplomatik ve hukuki meşruiyet korundu; Türkiye'nin haklılığı dünyaya anlatıldı."},
                    {"label": f"{title} sürecinde ilgili ülkeler ve müttefiklerle müzakere masası kurarak barışçıl ve uzlaşmacı diplomasi yürüt.",
                     "effects": {"justice": -6, "people": 8, "treasury": -2, "military": 0, "authority": 7},
                     "log": f"{title} geriliminde diplomatik diyalog işletildi; krizin tırmanması önlendi."},
                    {"label": f"{title} ile bağlantılı dış ticaret, turizm ve enerji çıkarlarımızı korumak için Hazine dengelerini tahkim et.",
                     "effects": {"justice": -2, "people": -6, "treasury": 8, "military": 0, "authority": 4},
                     "log": f"{title} kaynaklı ekonomik riskler önlendi; milli ekonomi dış baskılara karşı korundu."},
                    {"label": f"{title} karşısında Türk Silahlı Kuvvetleri ve MİT unsurlarını teyakkuza geçirerek sahada caydırıcı güç göster.",
                     "effects": {"justice": -2, "people": -7, "treasury": 0, "military": 10, "authority": 9},
                     "log": f"{title} karşısında milli güvenlik tedbirleri uygulandı; Türkiye'nin sahadaki ağırlığı hissettirildi."},
                    {"label": f"TBMM'de {title} konusunu milli doktrine bağlayan Stratejik Dış Politika ve Güvenlik Kanunu'nu yürürlüğe koy.",
                     "effects": {"justice": 8, "people": 4, "treasury": -6, "military": 0, "authority": 8},
                     "log": f"Kabul edilen yasal reform ile milli güvenlik kırmızı çizgileri kanunlaştı; egemenliğimiz korundu."}
                ]

    print(f"Total options generated for Batch 3: {len(options_map)}")
    updated_deck = apply_options_to_deck(deck, options_map)
    save_modern_deck(updated_deck)

if __name__ == '__main__':
    generate_domains_7_to_9()
