import json
from deck_utils import load_modern_deck, save_modern_deck, apply_options_to_deck

# Domain 10: Doğal Afetler ve Çevre Krizleri (tr_vaka_371 - tr_vaka_400)
# Domain 11: 6 Şubat 2023 Kahramanmaraş Depremleri (tr_vaka_401 - tr_vaka_430)
# Domain 12: Mega Ulaşım ve Altyapı Projeleri (tr_vaka_431 - tr_vaka_460)

def generate_domains_10_to_12():
    deck = load_modern_deck()
    print("Building realistic options for Domains 10, 11, and 12 (tr_vaka_371 to tr_vaka_460)...")
    options_map = {}

    for i in range(370, 460):
        ev = deck[i]
        eid = ev['id']
        title = ev['title']
        desc = ev['desc']

        # DOMAIN 10 (370 to 399: tr_vaka_371 to tr_vaka_400)
        if 370 <= i <= 399:
            if "17 Ağustos" in title or "Gölcük Depremi" in title or "Düzce" in title:
                options_map[eid] = [
                    {"label": "Yıkılan binaların müteahhitleri, fenni mesulleri ve kaçak yapılara ruhsat veren belediye yetkilileri hakkında derhal adli tutuklama kararı çıkart.",
                     "effects": {"justice": 9, "people": 8, "treasury": -2, "military": 0, "authority": -3},
                     "log": "Adli soruşturmalar hızla başlatıldı; Veli Göçer ve sorumsuz müteahhitler hakkında davalar açıldı."},
                    {"label": "Bölgeye uluslararası yardım çağrısı yap; AKUT, sivil toplum örgütleri ve Kızılay ile ortaklaşa çadır kent kriz masaları kur.",
                     "effects": {"justice": -6, "people": 9, "treasury": -3, "military": 0, "authority": 7},
                     "log": "Toplumsal dayanışma şahlandı; yüz binlerce depremzedenin acil barınma ve sıcak yemek ihtiyacı karşılandı."},
                    {"label": "Depremin yaralarını sarmak için geçici 'Özel İletişim Vergisi' çıkar ve Dünya Bankası afet kredisini kalıcı konutlara tahsis et.",
                     "effects": {"justice": -2, "people": -6, "treasury": 9, "military": 0, "authority": 4},
                     "log": "Afet bütçesi oluşturuldu; Marmara Bölgesi'nde kalıcı deprem konutlarının inşası finanse edildi."},
                    {"label": "1. Ordu birliklerini ve askeri istihkam taburlarını derhal enkaz sahasına sevk ederek arama-kurtarma ve sahra hastaneleri kur.",
                     "effects": {"justice": -3, "people": -7, "treasury": 0, "military": 10, "authority": 9},
                     "log": "Mehmetçik enkaz başlarına ulaştı; yağma ve asayişsizliğe karşı sıkı askeri güvenlik çemberi kuruldu."},
                    {"label": "Zorunlu Deprem Sigortası'nı (DASK) kuran ve Yapı Denetim firmalarını yetkilendiren 587 Sayılı KHK'yı yürürlüğe koy.",
                     "effects": {"justice": 8, "people": 4, "treasury": -7, "military": 0, "authority": 8},
                     "log": "DASK ve modern yapı denetim sistemi kuruldu; Türkiye'nin deprem mevzuatında yeni bir çağ başladı."}
                ]
            elif "Orman Yangınları" in title or "Manavgat" in title:
                options_map[eid] = [
                    {"label": "Yangınların kundaklama veya sabotaj sonucu çıkıp çıkmadığını MİT ve Jandarma Kriminal laboratuvarlarıyla çok yönlü soruştur.",
                     "effects": {"justice": 8, "people": 8, "treasury": -2, "military": 0, "authority": -2},
                     "log": "Sabotaj iddiaları titizlikle incelendi; ihmali ve kastı bulunan şüpheliler adliyeye sevk edildi."},
                    {"label": "Köyleri ve ahırları yanan afetzedelere Cumhurbaşkanlığı Acil Destek Fonu'ndan nakit hibe verip canlı hayvan desteği sağla.",
                     "effects": {"justice": -6, "people": 9, "treasury": -3, "military": 0, "authority": 7},
                     "log": "Köylülerin feryadı dindirildi; yerinde köy evleri ve ahırlar inşa edilerek üreticiler ayağa kaldırıldı."},
                    {"label": "Gelecek yılların yangın riskini önlemek için Savunma Sanayii Başkanlığı koordinasyonunda dev amfibik yangın söndürme uçağı filosu satın al.",
                     "effects": {"justice": -2, "people": -6, "treasury": 9, "military": 0, "authority": 4},
                     "log": "Milli yangın söndürme filosu kuruldu; THK uçakları ve modern amfibik uçaklar envantere alındı."},
                    {"label": "Alevlerin Kemerköy Termik Santrali'ne sıçramasını önlemek için santral çevresine iş makineleriyle hendek kazıp jandarma kordonu kur.",
                     "effects": {"justice": -2, "people": -7, "treasury": 0, "military": 10, "authority": 9},
                     "log": "Termik santral faciası son anda önlendi; stratejik enerji tesisleri yangından korundu."},
                    {"label": "Yanan orman arazilerinin imara açılmasını kesin olarak yasaklayan ve fidan dikimini anayasal güvenceye bağlayan reformu yasalaştır.",
                     "effects": {"justice": 8, "people": 5, "treasury": -6, "military": 0, "authority": 8},
                     "log": "Kül olan alanlara tek bir beton dahi sokulmadı; milyonlarca yeni fidanla yeşil vatan yeniden canlandırıldı."}
                ]
            elif "Müsilaj" in title:
                options_map[eid] = [
                    {"label": "Marmara Denizi'ne arıtmasız zehirli atık ve kimyasal deşarj eden fabrikaları Çevre Müfettişleri marifetiyle kapatıp savcılığa sevk et.",
                     "effects": {"justice": 9, "people": 7, "treasury": -2, "military": 0, "authority": -3},
                     "log": "Korsan deşarj yapan organize sanayi tesislerine kapatma ve en üst baremden rekor çevre cezaları kesildi."},
                    {"label": "Marmara Belediyeler Birliği, balıkçı kooperatifleri ve bilim insanlarıyla 'Marmara Denizi Eylem Planı' seferberliği ilan et.",
                     "effects": {"justice": -6, "people": 8, "treasury": -3, "military": 0, "authority": 7},
                     "log": "Toplumsal dayanışma sağlandı; deniz süpürgeleriyle yüzeyden binlerce metreküp salya temizlendi."},
                    {"label": "Havzadaki tüm belediyelerin biyolojik ve ileri arıtma tesislerine geçişi için İller Bankası üzerinden düşük faizli kredi fonu aç.",
                     "effects": {"justice": -2, "people": -6, "treasury": 8, "military": 0, "authority": 4},
                     "log": "Arıtma altyapısı hızla finanse edildi; Marmara'ya tek damla arıtmasız su akmaması için tesis yatırımları başladı."},
                    {"label": "Sahil Güvenlik Komutanlığı botlarına gece deniz kirliliği teftişi ve sintine boşaltan gemilere anında el koyma yetkisi ver.",
                     "effects": {"justice": -2, "people": -7, "treasury": 0, "military": 9, "authority": 8},
                     "log": "Boğaz ve körfezde 7/24 deniz gözetimi kuruldu; gemilerin kaçak atık basması engellendi."},
                    {"label": "Marmara Denizi'nin tamamını 'Özel Çevre Koruma Bölgesi' ilan eden tarihi koruma kanununu kabul et.",
                     "effects": {"justice": 8, "people": 4, "treasury": -7, "military": 0, "authority": 8},
                     "log": "Marmara Denizi kanunen koruma kalkanına alındı; oksijen seviyeleri yeniden yükselmeye başladı."}
                ]
            elif "İliç" in title or "Maden" in title:
                options_map[eid] = [
                    {"label": "Maden sahasındaki liç kayması ve siyanürlü toprak kayması faciasında şirketin yabancı ve yerli yöneticilerini derhal tutuklat.",
                     "effects": {"justice": 9, "people": 8, "treasury": -2, "military": 0, "authority": -3},
                     "log": "Adli tahkikat başlatıldı; altın madeni şirketi yetkilileri ve fenni denetimciler cezaevine gönderildi."},
                    {"label": "Toprak altında kalan 9 madencinin aileleriyle kriz merkezinde buluş; Fırat Nehri'ne siyanür sızmasını önleyecek tedbirleri açıkla.",
                     "effects": {"justice": -6, "people": 8, "treasury": -3, "military": 0, "authority": 7},
                     "log": "Bölge halkı bilgilendirildi; menfez kapakları kapatılarak Fırat Nehri'ne kimyasal sızıntı sıfırlandı."},
                    {"label": "Şirketin tüm maden işletme ruhsatlarını iptal et; çevre rehabilitasyonu ve işçi tazminatları için şirket hesaplarına el koy.",
                     "effects": {"justice": -2, "people": -6, "treasury": 9, "military": 0, "authority": 4},
                     "log": "Şirketin teminat mektupları nakde çevrildi; çevre temizliği masrafları kirleten şirketten tahsil edildi."},
                    {"label": "Bölgeye AFAD, JAK ve TSK KBRN (Kimyasal, Biyolojik, Radyasyon, Nükleer) timlerini sevk ederek güvenlik kordonu kur.",
                     "effects": {"justice": -2, "people": -7, "treasury": 0, "military": 9, "authority": 9},
                     "log": "Liç yığını çevresi izole edildi; gaz ölçümleri ve toprak analizleri kesintisiz takip edildi."},
                    {"label": "Açık liç yöntemiyle siyanürlü madenciliği katı çevre sınırlarına ve ağır teminatlara bağlayan 'Maden Güvenliği Reform Kanunu' çıkar.",
                     "effects": {"justice": 8, "people": 4, "treasury": -7, "military": 0, "authority": 8},
                     "log": "Vahşi madencilik devri kapandı; çevre ve işçi can güvenliğini önceleyen yasal rejim kuruldu."}
                ]
            else:
                options_map[eid] = [
                    {"label": "Afet bölgesindeki usulsüzlükler, ihmaller ve mevzuata aykırı yapılaşmalar hakkında adli soruşturma açtır.",
                     "effects": {"justice": 8, "people": 7, "treasury": -2, "military": 0, "authority": -3},
                     "log": "Hukuki tahkikat başlatıldı; afet sorumluları hakkında yargı süreci işletildi."},
                    {"label": "Afetzede vatandaşlar, mahalle muhtarları ve sivil toplumla koordinasyon kurarak acil insani yardım ulaştır.",
                     "effects": {"justice": -6, "people": 8, "treasury": -3, "military": 0, "authority": 7},
                     "log": "Halkın acil ihtiyaçları karşılandı; toplumsal dayanışma ile yaralar hızla sarıldı."},
                    {"label": "Hasar gören yerleşim yerlerinin yeniden inşası ve esnafa faizsiz can suyu kredisi için Hazine fonlarını devreye sok.",
                     "effects": {"justice": -2, "people": -6, "treasury": 8, "military": 0, "authority": 4},
                     "log": "Mali kaynaklar seferber edildi; afetin bölge ekonomisinde yol açtığı hasar sübvanse edildi."},
                    {"label": "Arama-kurtarma ve enkaz kaldırma sahalarında yağma ve kargaşayı önlemek için jandarma ve polis devriyelerini artır.",
                     "effects": {"justice": -2, "people": -7, "treasury": 0, "military": 9, "authority": 9},
                     "log": "Sahada tam kamu düzeni ve asayiş sağlandı; devletin koruyucu otoritesi hissettirildi."},
                    {"label": "Afet risklerini önceden azaltan ve yerel yönetimlerin imar denetimini sıkılaştıran 'Kentsel Dayanıklılık Kanunu' çıkar.",
                     "effects": {"justice": 8, "people": 4, "treasury": -6, "military": 0, "authority": 8},
                     "log": "Afet yönetimi modern yasal standartlara kavuşturuldu; benzer felaketlerin önlenmesi için zemin hazırlandı."}
                ]

        # DOMAIN 11: 6 Şubat 2023 Kahramanmaraş Depremleri (400 to 429: tr_vaka_401 to tr_vaka_430)
        elif 400 <= i <= 429:
            if "İsias Otel" in title or "Rönesans Rezidans" in title or "Müteahhit" in title:
                options_map[eid] = [
                    {"label": "Kolon kesen dükkan sahipleri, statik projeyi değiştiren müteahhitler ve imar affı verenler hakkında 'olası kastla öldürme'den tutuklama çıkar.",
                     "effects": {"justice": 10, "people": 8, "treasury": -2, "military": 0, "authority": -2},
                     "log": "Adalet arayışı tavizsiz işletildi; yüzlerce masumun canına mal olan müteahhit ve fenni mesuller adliyeye sevk edildi."},
                    {"label": "KKTC sporcu kafilesi ve deprem şehitlerinin aileleriyle Adalet Bakanlığı'nda düzenli duruşma koordinasyon masası kur.",
                     "effects": {"justice": -5, "people": 9, "treasury": -2, "military": 0, "authority": 7},
                     "log": "Mağdur ailelere devlet sahip çıktı; davanın unutturulması ve delillerin karartılması engellendi."},
                    {"label": "Kaçmaya çalışan şüphelilerin havalimanlarında yakalanması ve banka hesapları ile şirket varlıklarına MASAK aracılığıyla tedbir koy.",
                     "effects": {"justice": -2, "people": -6, "treasury": 9, "military": 0, "authority": 4},
                     "log": "Şüphelilerin mal kaçırması önlendi; mağdur aileler için haciz ve tazminat fonu oluşturuldu."},
                    {"label": "Enkaz kaldırma sürecinde bilirkişiler karot numunesi almadan hiçbir molozun taşınmaması için savcılık nöbeti kurdur.",
                     "effects": {"justice": -3, "people": -7, "treasury": 0, "military": 9, "authority": 9},
                     "log": "Deliller enkaz başında güvenliğe alındı; hukuki hesap sorma sürecinin delilsiz kalması önlendi."},
                    {"label": "İmar affı ve barışı uygulamalarını anayasal suç kapsamına alan ve yapı denetimini devlet tekeline veren 'Fay Yasası' çıkar.",
                     "effects": {"justice": 9, "people": 4, "treasury": -7, "military": 0, "authority": 8},
                     "log": "Türkiye'de kaçak yapı affı defteri ebediyen kapatıldı; fenni mesuliyet en katı cezalara bağlandı."}
                ]
            elif "4. Seviye Alarm" in title or "Pazarcık" in title or "Elbistan" in title:
                options_map[eid] = [
                    {"label": "Asrın Felaketi karşısında anayasal yetkileri kullanarak 11 ilde 3 ay süreyle 'Olağanüstü Hal (OHAL)' ilan et.",
                     "effects": {"justice": 8, "people": 8, "treasury": -3, "military": 0, "authority": -2},
                     "log": "OHAL rejimi devreye alındı; yağma, stokçuluk ve fahiş fiyat artışlarına karşı olağanüstü adli tedbirler yürürlüğe girdi."},
                    {"label": "Uluslararası topluma 4. Seviye Acil Çağrı yap; 90 ülkeden gelen arama-kurtarma ekiplerini havalimanlarında AFAD ile koordine et.",
                     "effects": {"justice": -6, "people": 10, "treasury": -3, "military": 0, "authority": 7},
                     "log": "Dünya Türkiye için seferber oldu; on binlerce yabancı ve yerli kurtarma görevlisi enkazlardan can kurtardı."},
                    {"label": "Milli Dayanışma Kampanyası ('Türkiye Tek Yürek') ile toplanan 115 milyar TL'yi doğrudan AFAD barınma ve konteyner bütçesine bağla.",
                     "effects": {"justice": -2, "people": -6, "treasury": 10, "military": 0, "authority": 5},
                     "log": "Tarihi kaynak toplandı; yüz binlerce konteyner kentin altyapısı Hazineye yük olmadan kuruldu."},
                    {"label": "2. Ordu komando tugaylarını, jandarma asayiş birliklerini ve polis özel harekatı 11 ilin cadde ve sokaklarında devriyeye çıkar.",
                     "effects": {"justice": -2, "people": -7, "treasury": 0, "military": 10, "authority": 10},
                     "log": "Mehmetçik sokaklara indi; yağma ve asayişsizlik dedikoduları bıçak gibi kesilerek tam kamu düzeni kuruldu."},
                    {"label": "Deprem bölgesinde yıkılan şehirlerin yerinde ve rezerv alanlarda inşasını hızlandıran 'Afet Yeniden İmar Fonu Kanunu' çıkar.",
                     "effects": {"justice": 8, "people": 4, "treasury": -8, "military": 0, "authority": 9},
                     "log": "Afet fonu kuruldu; 11 ilin şehir merkezlerinin yeniden imarı için yasal bürokrasi sıfırlandı."}
                ]
            elif "Kalıcı Konut" in title or "Kura Çekilişleri" in title or "Rezerv Alan" in title:
                options_map[eid] = [
                    {"label": "Kalıcı konut kura çekilişlerini noter huzurunda ve canlı yayında şeffafça yaparak hak sahipliği itirazlarını adilce sonuçlandır.",
                     "effects": {"justice": 9, "people": 8, "treasury": -2, "military": 0, "authority": -2},
                     "log": "Kura çekimi şeffaflıkla yapıldı; hiçbir şaibeye yer bırakılmadan evler hak sahiplerine teslim edildi."},
                    {"label": "Konteyner kentlerde yaşayan yüz binlerce aileye kalıcı evleri teslim edilene kadar kira ve taşınma yardımlarını kesintisiz sürdür.",
                     "effects": {"justice": -5, "people": 9, "treasury": -3, "military": 0, "authority": 7},
                     "log": "Halkın barınma güvencesi korundu; depremzedelerin yalnız bırakılmadığı devlet şefkatiyle gösterildi."},
                    {"label": "46 bin konutun inşa edildiği tünel kalıp şantiyelerine Hazine bütçesinden hak ediş ödemelerini aksatmadan aktar.",
                     "effects": {"justice": -2, "people": -6, "treasury": 9, "military": 0, "authority": 4},
                     "log": "İnşaatlar gece gündüz sürdürüldü; 1 yılda yüz bin konutun tamamlanması için nakit akışı korundu."},
                    {"label": "Fay hatları üzerinde yapılaşmaya kesinlikle izin verme; şehir merkezlerini sağlam zeminli dağ eteklerine kaydır.",
                     "effects": {"justice": -2, "people": -7, "treasury": 0, "military": 9, "authority": 9},
                     "log": "Bilimsel zemin etütlerine uyuldu; yeni şehirler radye temel ve tünel kalıp ile kaya zeminlere kuruldu."},
                    {"label": "Şehir merkezlerinin tarihi ve kültürel dokusunu koruyarak ayağa kaldıran 'Kentsel Dönüşüm ve Rezerv Alan Kanunu'nu çıkar.",
                     "effects": {"justice": 8, "people": 4, "treasury": -7, "military": 0, "authority": 8},
                     "log": "Yasal engeller kaldırıldı; Antakya, Maraş ve Malatya meydanları devlet eliyle baştan inşa edilmeye başlandı."}
                ]
            else:
                options_map[eid] = [
                    {"label": "Deprem bölgesindeki kamu hizmetlerini, adli teftişi ve zarar tespit davalarını şeffafça yürüt.",
                     "effects": {"justice": 8, "people": 7, "treasury": -2, "military": 0, "authority": -3},
                     "log": "Adli ve idari süreçler işletildi; depremzedelerin hak kayıpları önlendi."},
                    {"label": "Afet bölgesindeki sivil toplum, yerel esnaf ve vatandaşlarla kriz masasında buluşarak dayanışmayı güçlendir.",
                     "effects": {"justice": -6, "people": 8, "treasury": -2, "military": 0, "authority": 7},
                     "log": "Halkla el ele verildi; bölgede hayatın normale dönmesi için toplumsal mutabakat sağlandı."},
                    {"label": "Deprem illerindeki esnaf ve çiftçiye vergi terki, SGK muafiyeti ve hibe kredileri Hazinece tahsis et.",
                     "effects": {"justice": -2, "people": -6, "treasury": 8, "military": 0, "authority": 4},
                     "log": "Bölge ekonomisi canlandırıldı; vergi muafiyetleriyle üreticilerin iflas etmesi önlendi."},
                    {"label": "Konteyner kentler ve lojistik depolarda emniyet ve jandarma nöbetlerini 24 saat kesintisiz sürdür.",
                     "effects": {"justice": -2, "people": -7, "treasury": 0, "military": 9, "authority": 9},
                     "log": "Huzur ve asayiş temin edildi; geçici barınma alanlarında vatandaşın can ve mal güvenliği korundu."},
                    {"label": "TBMM'de deprem bölgesinin kalkınmasını 10 yıl süresince güvenceye alan 'Deprem İlleri İmar ve Teşvik Kanunu' çıkar.",
                     "effects": {"justice": 8, "people": 4, "treasury": -7, "military": 0, "authority": 8},
                     "log": "Bölgeye kalıcı ekonomik ve hukuki teşvik sağlandı; tersine göç için zemin hazırlandı."}
                ]

        # DOMAIN 12: Mega Ulaşım ve Altyapı Projeleri (430 to 459: tr_vaka_431 to tr_vaka_460)
        elif 430 <= i <= 459:
            if "Marmaray" in title or "Avrasya Tüneli" in title:
                options_map[eid] = [
                    {"label": "Yenikapı kazılarında ortaya çıkan Theodosius Limanı ve 37 antik batığı arkeolojik kurallarla koruma altına al.",
                     "effects": {"justice": 9, "people": 8, "treasury": -2, "military": 0, "authority": -2},
                     "log": "Tarihi miras korundu; İstanbul'un 8500 yıllık tarihi tüm dünyanın hayranlıkla izlediği müzeye dönüştürüldü."},
                    {"label": "Günde 1 milyon yolcu taşıyan hatta tren seferlerini sıklaştır; iki yaka arasındaki toplu taşıma biletlerini sübvanse et.",
                     "effects": {"justice": -5, "people": 9, "treasury": -3, "military": 0, "authority": 7},
                     "log": "Vatandaşın ulaşım çilesi bitti; Boğaz geçişi 4 dakikaya inerek İstanbulluların hayatı kolaylaştı."},
                    {"label": "Tünel geçiş ücretleri ve banliyö hattı gelirleriyle Hazine garantilerini ve dış kredi geri ödemelerini dengeli yürüt.",
                     "effects": {"justice": -2, "people": -6, "treasury": 9, "military": 0, "authority": 4},
                     "log": "Proje kendi kendini finanse eder hale geldi; kamu bütçesine döviz katkısı sağlandı."},
                    {"label": "Boğaz'ın 60 metre altındaki tüp tünellerde sismik erken uyarı ve su geçirmez tsunami kapaklarıyla askeri düzeyde güvenlik sağla.",
                     "effects": {"justice": -2, "people": -7, "treasury": 0, "military": 9, "authority": 9},
                     "log": "Dünyanın en güvenli tüneli işletildi; 9 büyüklüğündeki depreme dayanıklı mühendislik güvenceye alındı."},
                    {"label": "Türkiye'nin demiryolu ve metro hatlarını entegre eden 'Milli Raylı Sistemler ve Tünel Altyapı Kanunu' çıkar.",
                     "effects": {"justice": 8, "people": 4, "treasury": -6, "military": 0, "authority": 8},
                     "log": "Demiryolu ulaşımı stratejik öncelik oldu; Londra'dan Pekin'e demir ipekyolu kesintisiz bağlandı."}
                ]
            elif "Köprüsü" in title or "Osmangazi" in title or "Çanakkale" in title:
                options_map[eid] = [
                    {"label": "Köprü ve otoyol yapım sözleşmelerindeki Hazine geçiş garantilerini bağımsız Sayıştay denetimine tabi tutarak şeffaflığı sağla.",
                     "effects": {"justice": 9, "people": 7, "treasury": -2, "military": 0, "authority": -3},
                     "log": "Sayıştay raporlarıyla sözleşmeler incelendi; geçiş garantisi ve maliyet dengesi kamuoyuyla paylaşıldı."},
                    {"label": "Bayramlarda ve tatillerde köprü ve otoyolları ücretsiz yaparak vatandaşın memleketine güvenle ulaşmasını temin et.",
                     "effects": {"justice": -6, "people": 9, "treasury": -3, "military": 0, "authority": 7},
                     "log": "Milyonlarca vatandaş bayram sevinci yaşadı; feribot kuyrukları tarihe karıştı."},
                    {"label": "Geçiş garantilerinin Hazineye oluşturduğu kur farkı yükünü frenlemek için sözleşmelerdeki araç başı tarifeyi TL bazında revize et.",
                     "effects": {"justice": -2, "people": -6, "treasury": 9, "military": 0, "authority": 4},
                     "log": "Hazine borç yükü hafifletildi; kamu-özel işbirliği projelerinde bütçe dengesi korundu."},
                    {"label": "Stratejik asma köprülerin kulelerinde radar, kamera ve hava savunma sensörleriyle 24 saat kesintisiz koruma çemberi kur.",
                     "effects": {"justice": -2, "people": -7, "treasury": 0, "military": 9, "authority": 9},
                     "log": "Boğaz ve körfez köprüleri terör ve sabotaj tehdidine karşı yüksek teknolojiyle korundu."},
                    {"label": "Yap-İşlet-Devret (YİD) projelerinde kamu menfaatini maksimize eden 'Kamu-Özel İşbirliği Çerçeve Reform Kanunu' çıkar.",
                     "effects": {"justice": 8, "people": 4, "treasury": -7, "military": 0, "authority": 8},
                     "log": "Gelecek mega projelerin ihale ve garanti şartları kanuni şeffaflık standartlarına bağlandı."}
                ]
            elif "İstanbul Havalimanı" in title or "İGA" in title or "Atatürk Havalimanı" in title:
                options_map[eid] = [
                    {"label": "Atatürk Havalimanı'ndan İstanbul Havalimanı'na yapılan 45 saatlik 'Büyük Göç' lojistiğini sıfır kaza ve hatayla adli güvenceye al.",
                     "effects": {"justice": 8, "people": 8, "treasury": -2, "military": 0, "authority": -2},
                     "log": "Dünya havacılık tarihinin en büyük lojistik taşınması kusursuz tamamlandı; uçuşlar aksatılmadan yeni meydana geçti."},
                    {"label": "Atatürk Havalimanı arazisini ranta açmayıp halkın kullanımına 2 milyon metrekarelik dev Millet Bahçesi ve acil durum hastanesi yap.",
                     "effects": {"justice": -5, "people": 10, "treasury": -3, "military": 0, "authority": 7},
                     "log": "Şehre devasa bir nefes alanı kazandırıldı; pandemi döneminde 1008 yataklı acil hastane hızla açıldı."},
                    {"label": "Yılda 90 milyon yolcu ağırlayan İGA'nın devlete ödediği yıllık 1 milyar Euro'luk kira gelirini Hazine kasasına aktar.",
                     "effects": {"justice": -2, "people": -6, "treasury": 10, "military": 0, "authority": 5},
                     "log": "Havalimanı devlete para basan bir kuruluşa dönüştü; Hazineye rekor döviz geliri girdi."},
                    {"label": "Havalimanı çevresinde siber radar, İHA savar ve uçaksavar bataryalarıyla dünyanın en korunaklı hava sahasını tesis et.",
                     "effects": {"justice": -2, "people": -7, "treasury": 0, "military": 9, "authority": 9},
                     "log": "Havacılık güvenliği küresel çapta tescillendi; havalimanı uluslararası transit trafiğin 1 numaralı merkezi oldu."},
                    {"label": "Türkiye'yi küresel havacılık ve lojistik üssü yapan 'Sivil Havacılık ve Uluslararası Transit Merkezleri Kanunu' çıkar.",
                     "effects": {"justice": 8, "people": 4, "treasury": -7, "military": 0, "authority": 8},
                     "log": "THY ve Türk sivil havacılığı dünya liderliğine taşındı; transit uçuş gelirleri yasal güvenceye alındı."}
                ]
            elif "Yüksek Hızlı Tren" in title or "YHT" in title:
                options_map[eid] = [
                    {"label": "Hızlı tren hatlarındaki sinyalizasyon, hat bakım ve makinist kontrollerini en katı uluslararası güvenlik denetimine bağla.",
                     "effects": {"justice": 9, "people": 8, "treasury": -2, "military": 0, "authority": -2},
                     "log": "Demiryolu güvenliği tescillendi; sinyalizasyon açıkları ve kaza riskleri sıfırlandı."},
                    {"label": "Ankara, Eskişehir, Konya, Sivas ve İstanbul hatlarında bilet fiyatlarını öğrenci ve emekliler için indirimli tut.",
                     "effects": {"justice": -5, "people": 9, "treasury": -3, "military": 0, "authority": 7},
                     "log": "Hızlı tren halkın gözbebeği oldu; milyonlarca vatandaş otobüs ve uçak yerine konforlu treni seçti."},
                    {"label": "YHT bilet gelirleri ve yük taşımacılığı karıyla TCDD'nin yeni hızlı tren seti alımlarını özkaynaklarla finanse et.",
                     "effects": {"justice": -2, "people": -6, "treasury": 8, "military": 0, "authority": 4},
                     "log": "Demiryolları mali bağımsızlığa kavuştu; Hazineye yük olmadan yeni hızlı tren setleri satın alındı."},
                    {"label": "400 kilometreyi aşan viyadük ve dağ tünellerinde sabotaj ve hırsızlığa karşı jandarma ray devriyelerini görevlendir.",
                     "effects": {"justice": -2, "people": -7, "treasury": 0, "military": 9, "authority": 8},
                     "log": "Ray boylarında kesintisiz güvenlik kuruldu; hızlı tren seferlerinin aksamasına izin verilmedi."},
                    {"label": "Türkiye'nin 81 ilini yüksek hızlı demiryolu ağıyla buluşturmayı hedefleyen 'Milli Demiryolu Seferberlik Kanunu' çıkar.",
                     "effects": {"justice": 8, "people": 4, "treasury": -7, "military": 0, "authority": 8},
                     "log": "Cumhuriyetin demiryolu ideali yeniden şahlandı; Anadolu hızlı raylarla baştan başa örüldü."}
                ]
            else:
                options_map[eid] = [
                    {"label": "Ulaşım ve altyapı projelerinin ihale, kamulaştırma ve sözleşme süreçlerini şeffaf adli denetime tabi tut.",
                     "effects": {"justice": 8, "people": 7, "treasury": -2, "military": 0, "authority": -3},
                     "log": "Altyapı yatırımlarında hukuki şeffaflık sağlandı; kamulaştırma bedelleri hak sahiplerine ödendi."},
                    {"label": "Mega projelerin hizmete girmesiyle birlikte vatandaşın erişimini kolaylaştıracak uygun tarife ve indirimleri uygula.",
                     "effects": {"justice": -6, "people": 8, "treasury": -3, "military": 0, "authority": 7},
                     "log": "Vatandaş memnuniyeti sağlandı; modern ulaşım imkanları halkın refahına sunuldu."},
                    {"label": "Proje finansmanında Hazine dengelerini koru; gelir getirici ticari alanlarla kamu bütçesine katkı sağla.",
                     "effects": {"justice": -2, "people": -6, "treasury": 8, "military": 0, "authority": 4},
                     "log": "Altyapı yatırımları bütçeyi sarsmadan finanse edildi; kamu maliyesi korundu."},
                    {"label": "Stratejik liman, tünel ve köprü altyapısını terör ve siber sabotajlara karşı kolluk teyakkuzuna al.",
                     "effects": {"justice": -2, "people": -7, "treasury": 0, "military": 9, "authority": 9},
                     "log": "Kritik ulaşım koridorları korundu; devletin lojistik güvenliği sağlandı."},
                    {"label": "Türkiye'nin ulaştırma ve lojistik master planını yasal güvenceye bağlayan 'Milli Altyapı ve Ulaştırma Kanunu' çıkar.",
                     "effects": {"justice": 8, "people": 4, "treasury": -6, "military": 0, "authority": 8},
                     "log": "Ulaştırma politikası kanunlaştı; Türkiye küresel ticaretin vazgeçilmez köprüsü haline geldi."}
                ]

    print(f"Total options generated for Batch 4: {len(options_map)}")
    updated_deck = apply_options_to_deck(deck, options_map)
    save_modern_deck(updated_deck)

if __name__ == '__main__':
    generate_domains_10_to_12()
