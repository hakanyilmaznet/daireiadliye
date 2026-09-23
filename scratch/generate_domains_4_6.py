import json
from deck_utils import load_modern_deck, save_modern_deck, apply_options_to_deck

# Domain 4: 367 Krizi, E-Muhtıra ve Kapatma Davası (tr_vaka_191 - tr_vaka_220)
# Domain 5: Ergenekon, Balyoz ve Kozmik Oda (tr_vaka_221 - tr_vaka_250)
# Domain 6: 2010 Referandumu, MİT Krizi ve 17-25 Aralık (tr_vaka_251 - tr_vaka_280)

def generate_domains_4_to_6():
    deck = load_modern_deck()
    print("Building realistic options for Domains 4, 5, and 6 (tr_vaka_191 to tr_vaka_280)...")
    options_map = {}

    for i in range(190, 280):
        ev = deck[i]
        eid = ev['id']
        title = ev['title']
        desc = ev['desc']

        # DOMAIN 4 (indices 190 to 219)
        if 190 <= i <= 219:
            if "367" in title:
                options_map[eid] = [
                    {"label": "Anayasa Mahkemesi'nin 367 toplantı yeter sayısı kararını meşruiyet dairesinde kabul et ve derhal erken seçim kararı al.",
                     "effects": {"justice": 9, "people": 8, "treasury": -3, "military": 0, "authority": -2},
                     "log": "Hukuk sınırlarına sadık kalındı; vesayet dayatmasına karşı en meşru cevap olan 'Millet Sandığı'na gidildi."},
                    {"label": "Meclisteki muhalefet liderleriyle Çankaya adaylığı üzerinde uzlaşı turları yap; kriz çıkarmayacak tarafsız bir isimde anlaş.",
                     "effects": {"justice": -6, "people": 8, "treasury": -2, "military": 0, "authority": 7},
                     "log": "Muhalefetle müzakere edildi; meclis içi uzlaşı arandı fakat iktidar kendi adayından taviz vermek durumunda kaldı."},
                    {"label": "Erken seçim kararının döviz ve borsa üzerindeki dalgalanmasını önlemek için Hazine ve Merkez Bankası likidite hattını aç.",
                     "effects": {"justice": -2, "people": -6, "treasury": 8, "military": 0, "authority": 4},
                     "log": "Ekonomik istikrar korundu; 367 krizinin piyasalarda yıkıcı bir finansal krize dönüşmesi engellendi."},
                    {"label": "Meclis oylamasına katılmayan ve Meclis'i kilitlemeye çalışan siyasi bloklara karşı hükümetin demokratik otoritesini ilan et.",
                     "effects": {"justice": -3, "people": -7, "treasury": 0, "military": 8, "authority": 9},
                     "log": "Hükümet geri adım atmayacağını gösterdi; siyasi kararlılık halk tabanında büyük destek buldu."},
                    {"label": "Anayasa'yı değiştirerek 'Cumhurbaşkanının doğrudan halkoyu ile seçilmesi' reformunu meclisten geçirip referanduma sun.",
                     "effects": {"justice": 8, "people": 5, "treasury": -7, "military": 0, "authority": 9},
                     "log": "Sistem krizi kökten çözüldü; cumhurbaşkanını seçme yetkisi vesayet odaklarından alınıp doğrudan millete verildi."}
                ]
            elif "27 Nisan E-Muhtırası" in title or "Muhtıra" in title:
                options_map[eid] = [
                    {"label": "Anayasa'nın amir hükümleri uyarınca Genelkurmay Başkanı'nın Başbakan'a bağlı olduğunu hatırlatarak hukukun üstünlüğünü savun.",
                     "effects": {"justice": 9, "people": 9, "treasury": -2, "military": 0, "authority": -2},
                     "log": "Cumhuriyet tarihinde ilk kez bir hükümet gece yarısı muhtırasına sabahın ilk ışıklarında sert bir anayasal karşı bildiriyle cevap verdi."},
                    {"label": "Genelkurmay Karargahı ile temas kurup bildiriyi yumuşatacak ortak bir basın açıklaması üzerinde uzlaşma ara.",
                     "effects": {"justice": -7, "people": 7, "treasury": -2, "military": 0, "authority": 7},
                     "log": "Sivil-asker gerilimi yatıştırılmaya çalışıldı; darbe ihtimali ötelendi ancak hükümetin dirayeti sorgulandı."},
                    {"label": "Muhtıranın yarattığı siyasi şokun Hazine borçlanma faizlerini zıplatmaması için yabancı yatırımcılara güven mektubu gönder.",
                     "effects": {"justice": -2, "people": -6, "treasury": 8, "military": 0, "authority": 4},
                     "log": "Mali panik önlendi; Londra ve New York piyasalarında Türkiye tahvillerine satış gelmesi engellendi."},
                    {"label": "Kolluk kuvvetlerine ve emniyet teşkilatına teyakkuz emri vererek muhtırayı fırsat bilip sokağa inmek isteyen odakları engelle.",
                     "effects": {"justice": -3, "people": -8, "treasury": 0, "military": 9, "authority": 9},
                     "log": "Devlet otoritesi korundu; cuntacıların sokakta kaos çıkararak fiili müdahaleye zemin hazırlaması önlendi."},
                    {"label": "TSK İç Hizmet Kanunu'nun 35. maddesini darbe gerekçesi olmaktan çıkaracak yasal reform taslağını meclise getir.",
                     "effects": {"justice": 8, "people": 4, "treasury": -6, "military": 0, "authority": 8},
                     "log": "Askeri vesayetin yasal dayanaklarına neşter vuruldu; sivil demokratik denetim güçlendirildi."}
                ]
            elif "Kapatma Davası" in title:
                options_map[eid] = [
                    {"label": "Yargıtay Cumhuriyet Başsavcılığı'nın iddianamesine karşı Anayasa Mahkemesi'nde evrensel demokrasi ve savunma hakkını kullan.",
                     "effects": {"justice": 9, "people": 8, "treasury": -3, "military": 0, "authority": -3},
                     "log": "AYM'de tarihi savunma yapıldı; %47 oy almış iktidar partisinin kapatılmasının rejimi çökerteceği hukuken kanıtlandı."},
                    {"label": "Meclisteki tüm siyasi partilerle geniş tabanlı diyalog kurarak siyasi partilerin kapatılmasını imkansız kılan mutabakat ara.",
                     "effects": {"justice": -6, "people": 8, "treasury": -3, "military": 0, "authority": 7},
                     "log": "Siyasi uzlaşı arandı; meclis zemininde parti kapatmaya karşı ortak bir tavır geliştirilmeye çalışıldı."},
                    {"label": "Davanın açılmasıyla borsa ve dövizde yaşanan çalkantıyı durdurmak için Merkez Bankası ve Hazine rezervlerini devreye sok.",
                     "effects": {"justice": -2, "people": -7, "treasury": 8, "military": 0, "authority": 4},
                     "log": "Piyasalar sakinleştirildi; 'kapatma davası şoku' yabancı sermaye kaçışına dönüşmeden Hazinece dengelendi."},
                    {"label": "Kapatma davasını sokakta çatışmaya dönüştürmek isteyen marjinal gruplara karşı güvenlik tedbirlerini en üst düzeye çıkar.",
                     "effects": {"justice": -3, "people": -8, "treasury": 0, "military": 8, "authority": 8},
                     "log": "Sokak sükûneti sağlandı; kitlesel provokasyonların mahkeme sürecini baskı altına almasına izin verilmedi."},
                    {"label": "Anayasa'nın 68 ve 69. maddelerini değiştirerek parti kapatmayı Venedik Kriterleri uyarınca yalnızca şiddet şartına bağla.",
                     "effects": {"justice": 8, "people": 4, "treasury": -7, "military": 0, "authority": 8},
                     "log": "Parti kapatma tehdidi Türk siyasetinin üzerinden kaldırıldı; demokratik temsil teminat altına alındı."}
                ]
            elif "Danıştay Saldırısı" in title:
                options_map[eid] = [
                    {"label": "Saldırgan Alparslan Arslan ve arkasındaki çete irtibatlarını DGM ve Ağır Ceza Mahkemesi'nde derinlemesine soruşturt.",
                     "effects": {"justice": 9, "people": 7, "treasury": -2, "military": 0, "authority": -3},
                     "log": "Yargı süreci tavizsiz işletildi; menfur saldırının arkasındaki karanlık provokasyon ağı ortaya çıkarıldı."},
                    {"label": "Danıştay üyeleri ve yüksek yargı ricaliyle Başbakanlıkta taziye ve dayanışma zirvesi düzenleyerek devlette birlik mesajı ver.",
                     "effects": {"justice": -6, "people": 8, "treasury": -2, "military": 0, "authority": 7},
                     "log": "Yargı camiası teskin edildi; devlet kurumları arasındaki çatışma algısı yatıştırıldı."},
                    {"label": "Yargı mensuplarının güvenliği ve adliye binalarının x-ray ve güvenlik sistemleri için Hazine'den acil ödenek aktar.",
                     "effects": {"justice": -2, "people": -6, "treasury": 8, "military": 0, "authority": 4},
                     "log": "Yüksek yargı binalarının güvenlik açığı kapatıldı; Hazine kaynaklarıyla adliye güvenliği tahkim edildi."},
                    {"label": "Cenaze töreninde hükümete karşı yapılan provokatif eylemlerin sokak isyanına dönüşmesini çevik kuvvetle engelle.",
                     "effects": {"justice": -3, "people": -8, "treasury": 0, "military": 9, "authority": 8},
                     "log": "Cenazedeki kalkışma girişimi bastırıldı; devlet nizamı provokatörlere teslim edilmedi."},
                    {"label": "Yargı mensuplarının can güvenliği ve lojman korumasını özel yasal statüye bağlayan 'Hâkim ve Savcılar Koruma Kanunu' çıkar.",
                     "effects": {"justice": 8, "people": 3, "treasury": -6, "military": 0, "authority": 8},
                     "log": "Yargıçların bağımsızlığı ve can güvenliği yasal güvenceye kavuşturuldu."}
                ]
            elif "Hrant Dink" in title:
                options_map[eid] = [
                    {"label": "Ogün Samast ve arkasındaki Trabzon-İstanbul istihbarat ihmali ağını savcılık marifetiyle en ince detayına kadar soruşturt.",
                     "effects": {"justice": 9, "people": 8, "treasury": -2, "military": 0, "authority": -3},
                     "log": "Suikastın adli tahkikatı derinleştirildi; istihbari ihmaller ve cinayet şebekesi sanık sandalyesine oturtuldu."},
                    {"label": "'Hepimiz Hrant'ız, Hepimiz Ermeniyiz' diyen yüz binlerin vicdani feryadını sahiplen; cenazede devlet adına en üst düzeyde yer al.",
                     "effects": {"justice": -6, "people": 9, "treasury": -2, "military": 0, "authority": 6},
                     "log": "Toplumsal infial sükûnete dönüştürüldü; Türkiye'nin kardeşlik iklimi suikastçıların hedefine kurban edilmedi."},
                    {"label": "Cinayetin uluslararası diplomaside yaratacağı tazminat ve dava risklerini bertaraf edecek hukuki savunma bütçesi ayır.",
                     "effects": {"justice": -2, "people": -6, "treasury": 8, "military": 0, "authority": 3},
                     "log": "Uluslararası hukuk ve AİHM nezdindeki tazminat süreçleri yönetildi; kamu bütçesi korundu."},
                    {"label": "Emniyet ve Jandarma İstihbaratında cinayeti önceden bilip gizleyen kamu görevlilerini derhal açığa alıp tutuklat.",
                     "effects": {"justice": -3, "people": -8, "treasury": 0, "military": 9, "authority": 9},
                     "log": "İhmali olan kamu personeli görevden uzaklaştırıldı; devlet içindeki odaklara sert mesaj verildi."},
                    {"label": "Nefret suçları ve azınlık haklarını koruma altına alan 'Ayrımcılık ve Nefret Suçlarıyla Mücadele Kanunu'nu kabul et.",
                     "effects": {"justice": 8, "people": 4, "treasury": -6, "military": 0, "authority": 7},
                     "log": "Azınlıkların can ve mal güvenliği modern ceza mevzuatıyla tahkim edildi."}
                ]
            elif "Kozmik Oda" in title:
                options_map[eid] = [
                    {"label": "Devlet sırrı niteliğindeki askeri belgelerin sadece hakim Kadir Kayan tarafından incelenmesi ve dışarı sızmaması için tutanak tuttur.",
                     "effects": {"justice": 8, "people": 6, "treasury": -2, "military": 0, "authority": -4},
                     "log": "Hukuki arama prosedürü işletildi; ancak askeri arşivin gizliliği konusunda tarihi tartışmalar başladı."},
                    {"label": "Genelkurmay Başkanı İlker Başbuğ ile Başbakanlıkta baş başa görüşerek askeri karargah ile yargı arasındaki gerilimi düşür.",
                     "effects": {"justice": -6, "people": 8, "treasury": -2, "military": 0, "authority": 7},
                     "log": "Kriz diyalogla yönetilmeye çalışıldı; ordu içinde infial oluşması engellendi."},
                    {"label": "Seferberlik Tetkik Kurulu'nun faaliyetlerinin ifşa olması sonucu doğabilecek askeri lojistik kayıpları Hazine bütçesinden karşıla.",
                     "effects": {"justice": -2, "people": -6, "treasury": 8, "military": 0, "authority": 3},
                     "log": "Askeri tesislerin ve gizli planların revizyonu için kaynak tahsis edildi."},
                    {"label": "Seferberlik Tetkik Kurulu çevresinde inzibat ve polis birlikleriyle güvenlik kordonu kurup evrak kaçırılmasını engelle.",
                     "effects": {"justice": -3, "people": -8, "treasury": 0, "military": 9, "authority": 8},
                     "log": "Karargah çevresinde mutlak güvenlik sağlandı; belgelerin dışarı kaçırılması önlendi."},
                    {"label": "Devlet sırrı kavramını ve askeri mahallerde adli arama usullerini kanunlaştıran 'Devlet Sırrı ve Milli Güvenlik Kanunu' çıkar.",
                     "effects": {"justice": 8, "people": 3, "treasury": -6, "military": 0, "authority": 8},
                     "log": "Kozmik belgelerin korunması ve savcılık inceleme sınırları kalıcı kanuni çerçeveye bağlandı."}
                ]
            else:
                options_map[eid] = [
                    {"label": f"{title} hadisesinde anayasal meşruiyet ve yargı güvencesini tavizsiz işleterek hukukun üstünlüğünü sağla.",
                     "effects": {"justice": 8, "people": 7, "treasury": -2, "military": 0, "authority": -3},
                     "log": f"{title} meselesinde hukuk devleti ilkeleri korundu; adli ve idari süreçler meşruiyet zemininde işletildi."},
                    {"label": f"{title} sürecinde meclis içi partiler, sivil toplum ve bürokrasiyle istişare masası kurarak uzlaşı sağla.",
                     "effects": {"justice": -6, "people": 8, "treasury": -3, "military": 0, "authority": 7},
                     "log": f"{title} geriliminde siyasi diyalog işletildi; taraflar teskin edilerek kriz ötelendi."},
                    {"label": f"{title} sebebiyle oluşabilecek mali riskleri ve Hazine harcamalarını sıkı tasarruf tedbirleriyle sınırla.",
                     "effects": {"justice": -2, "people": -6, "treasury": 8, "military": 0, "authority": 4},
                     "log": f"{title} kapsamında kamu maliyesi korundu; kaynak israfının önüne geçildi."},
                    {"label": f"{title} karşısında emniyet ve güvenlik bürokrasisini teyakkuza geçirerek kamu düzenini tavizsiz sağla.",
                     "effects": {"justice": -3, "people": -8, "treasury": 0, "military": 8, "authority": 8},
                     "log": f"{title} karşısında asayiş korundu; devletin otoritesi hissettirildi."},
                    {"label": f"TBMM'de {title} konusunu kökten çözecek demokratik bir reform kanununu yürürlüğe koy.",
                     "effects": {"justice": 8, "people": 4, "treasury": -7, "military": 0, "authority": 7},
                     "log": f"Kabul edilen yasal reform ile kurumsal nizam sağlandı; benzer krizlerin tekerrürü kanunla önlendi."}
                ]

        # DOMAIN 5 (indices 220 to 249: tr_vaka_221 to tr_vaka_250)
        elif 220 <= i <= 249:
            if "İlker Başbuğ" in title:
                options_map[eid] = [
                    {"label": "Eski Genelkurmay Başkanı'nın terör örgütü yöneticiliğiyle değil, varsa Anayasa'nın 148. maddesi gereğince Yüce Divan'da yargılanmasını savun.",
                     "effects": {"justice": 9, "people": 8, "treasury": -2, "military": 0, "authority": -3},
                     "log": "Hukukun meşruiyeti ve Anayasa hükümleri savunuldu; Genelkurmay Başkanı'nın terörist sayılamayacağı vurgulandı."},
                    {"label": "Komuta kademesi ve toplumun infialini dindirmek için askeri heyetlerle görüş; tansiyonu düşürecek itidal mesajları ver.",
                     "effects": {"justice": -6, "people": 8, "treasury": -2, "military": 0, "authority": 7},
                     "log": "TSK içindeki infial yatıştırıldı; ordu ile hükümet arasında doğrudan çatışma yaşanması önlendi."},
                    {"label": "Davanın ordu morali ve savunma ihaleleri üzerinde yaratabileceği ekonomik aksamaları Hazine fonlarıyla telafi et.",
                     "effects": {"justice": -2, "people": -6, "treasury": 8, "military": 0, "authority": 3},
                     "log": "Milli savunma sanayii yatırımlarının yargı çalkantısından etkilenmesi önlendi."},
                    {"label": "Silivri Cezaevi çevresinde olağanüstü güvenlik tedbirleri alarak duruşma sırasında kitlesel baskın ve taşkınlıkları engelle.",
                     "effects": {"justice": -3, "people": -8, "treasury": 0, "military": 9, "authority": 8},
                     "log": "Silivri'de güvenlik çemberi kuruldu; duruşma salonunun basılması engellendi."},
                    {"label": "Genelkurmay Başkanı ve Kuvvet Komutanlarının sadece Başbakan izniyle ve Yüce Divan'da yargılanmasını emreden yasa çıkar.",
                     "effects": {"justice": 8, "people": 4, "treasury": -6, "military": 0, "authority": 9},
                     "log": "Komuta kademesine yasal yargılama zırhı getirildi; yerel savcıların keyfi tutuklama yetkisi kaldırıldı."}
                ]
            elif "TÜBİTAK Sahte Raporları" in title or "5 No'lu Harddisk" in title or "Dijital Delil" in title:
                options_map[eid] = [
                    {"label": "TÜBİTAK ve adli tıp raporlarındaki çelişkileri bağımsız uluslararası adli bilişim kuruluşlarına inceletip sahteciliği tescille.",
                     "effects": {"justice": 9, "people": 8, "treasury": -2, "military": 0, "authority": -3},
                     "log": "Uluslararası bilirkişi raporuyla dijital kumpas belgelendi; delillerin sonradan harddiske yüklendiği kanıtlandı."},
                    {"label": "Tutuklu subayların aileleri ve Vardiya Bizde platformuyla Adalet Bakanlığı'nda görüşüp hak ihlallerini dinle.",
                     "effects": {"justice": -6, "people": 9, "treasury": -2, "military": 0, "authority": 6},
                     "log": "Mağdur ailelerinin sesine kulak verildi; kumpas davalarının üzerindeki kamuoyu şüphesi büyüdü."},
                    {"label": "Sahte bilirkişi raporları hazırlayan görevlilerin kurumdan aldıkları haksız maaş ve ödenekleri faiziyle Hazine'ye tahsil ettir.",
                     "effects": {"justice": -2, "people": -6, "treasury": 8, "military": 0, "authority": 4},
                     "log": "Hileli rapor düzenleyenlerin mali kazançlarına el konuldu; kamu bütçesi korundu."},
                    {"label": "Kumpas kuran emniyet bilişim şube polisleri ve sahte raporcu TÜBİTAK uzmanları hakkında derhal adli yakalama kararı çıkart.",
                     "effects": {"justice": -3, "people": -7, "treasury": 0, "military": 9, "authority": 9},
                     "log": "Kumpas çetesine operasyon yapıldı; dijital delil imal eden sahteciler adliyeye sevk edildi."},
                    {"label": "Ceza Muhakemesi Kanunu'nda dijital delil arama, hash değeri alma ve kopyalama usullerini katı kurallara bağlayan reform yap.",
                     "effects": {"justice": 8, "people": 4, "treasury": -6, "military": 0, "authority": 8},
                     "log": "Dijital delil sahteciliği yasal olarak imkansız kılındı; imajı alınmayan diskin delil sayılamayacağı kanunlaştı."}
                ]
            elif "Ali Tatar" in title or "Kuddusi Okkır" in title or "Türkan Saylan" in title:
                options_map[eid] = [
                    {"label": "Haksız yakalama ve tutuklama kararlarıyla insan hayatına kasteden özel yetkili savcılar hakkında HSYK teftişi başlat.",
                     "effects": {"justice": 9, "people": 8, "treasury": -2, "military": 0, "authority": -3},
                     "log": "Yargı terörüne karşı adli teftiş devreye girdi; keyfi tutuklama kararı veren hakim ve savcılar incelemeye alındı."},
                    {"label": "Cezaevindeki hasta ve kanserli tutukluların tahliyesini sağlamak için Adli Tıp Kurumu ve Sağlık Bakanlığı'nı acil alarma geçir.",
                     "effects": {"justice": -6, "people": 9, "treasury": -3, "military": 0, "authority": 6},
                     "log": "İnsani ve vicdani koruma sağlandı; hasta tutukluların hastanelere nakli hızlandırıldı."},
                    {"label": "Kumpas mağdurlarının ailelerine ve vefat edenlerin yakınlarına Hazinece devlet tazminatı ödenmesini karara bağla.",
                     "effects": {"justice": -2, "people": -6, "treasury": 8, "military": 0, "authority": 4},
                     "log": "Devletin kusur sorumluluğu gereği tazminat ödendi; ailelerin mağduriyeti kısmen tanzim edildi."},
                    {"label": "Cezaevlerinde ve gözaltı merkezlerinde delil karartma veya intihara sürükleme vakalarına karşı teftiş heyetleri görevlendir.",
                     "effects": {"justice": -3, "people": -8, "treasury": 0, "military": 8, "authority": 8},
                     "log": "Gözaltı merkezlerinde disiplin ve asayiş sağlandı; tutukluların can güvenliği teminat altına alındı."},
                    {"label": "Hasta tutukluların infaz ertelemesini kolaylaştıran ve keyfi yakalamayı engelleyen 'Tutuklu Hakları Kanunu' çıkar.",
                     "effects": {"justice": 8, "people": 4, "treasury": -6, "military": 0, "authority": 8},
                     "log": "İnfaz mevzuatına insani standartlar getirildi; hasta tutukluların cezaevinde vefat etmesi önlendi."}
                ]
            elif "Işık Koşaner" in title or "YAŞ" in title:
                options_map[eid] = [
                    {"label": "Silah arkadaşlarının hukukunu korumak adına istifa eden komutanların gerekçelerini anayasal meşruiyet sınırlarında incele.",
                     "effects": {"justice": 8, "people": 7, "treasury": -2, "military": 0, "authority": -3},
                     "log": "Komutanların mektubu kayıtlara girdi; TSK komuta kademesinin endişeleri hukuki çerçevede değerlendirildi."},
                    {"label": "Genelkurmay Karargahı ile acil zirve toplayarak YAŞ terfilerinde kilitlenen dosyaları uzlaşmayla çöz.",
                     "effects": {"justice": -6, "people": 8, "treasury": -2, "military": 0, "authority": 7},
                     "log": "Askeri kriz uzlaşıyla yatıştırıldı; TSK'da emir-komuta zincirinin felç olması engellendi."},
                    {"label": "Komutanların istifası sonrası piyasalarda oluşabilecek döviz ve faiz baskısını Hazine kaynaklarıyla dizginle.",
                     "effects": {"justice": -2, "people": -6, "treasury": 8, "military": 0, "authority": 4},
                     "log": "Piyasalara güven verildi; komutanların istifasının ekonomik krizi tetiklemesi engellendi."},
                    {"label": "Jandarma Genel Komutanı Necdet Özel'i derhal Genelkurmay Başkanlığı'na atayarak ordu hiyerarşisinde boşluk bırakma.",
                     "effects": {"justice": -3, "people": -7, "treasury": 0, "military": 9, "authority": 9},
                     "log": "Devletin kararlılığı gösterildi; TSK komutası saatler içinde doldurularak güvenlik zafiyeti önlendi."},
                    {"label": "Yüksek Askeri Şura'nın yapısını sivilleştiren ve Başbakan'a bağlayan 'YAŞ Teşkilat Reform Kanunu' çıkar.",
                     "effects": {"justice": 8, "people": 4, "treasury": -7, "military": 0, "authority": 8},
                     "log": "Askeri şurada sivil irade hakim kılındı; sivil-asker dengesi modern standartlara kavuştu."}
                ]
            elif "AYM'nin Balyoz Hak İhlali" in title or "Tahliyeler" in title or "Beraatler" in title:
                options_map[eid] = [
                    {"label": "Anayasa Mahkemesi'nin oybirliğiyle verdiği tarihi hak ihlali kararını adli mahkemelerde gecikmeksizin uygulatıp tahliyeleri başlat.",
                     "effects": {"justice": 10, "people": 8, "treasury": -2, "military": 0, "authority": -2},
                     "log": "Adalet yerini buldu; yüzlerce vatansever subay, general ve amiral yıllar sonra alkışlarla özgürlüğüne kavuştu."},
                    {"label": "Tahliye olan askerler ve aileleriyle devlet adına helalleşme süreci başlat; toplumda adalet duygusunu onar.",
                     "effects": {"justice": -5, "people": 9, "treasury": -3, "military": 0, "authority": 6},
                     "log": "Toplumsal vicdan rahatladı; haksız yere hapis yatan kahramanların itibarı millet nezdinde tescillendi."},
                    {"label": "Kumpas mağduru subayların cezaevinde geçen yıllarına ait tüm maaş, özlük hakları ve tazminatlarını Hazine'den defaten öde.",
                     "effects": {"justice": -2, "people": -6, "treasury": 8, "military": 0, "authority": 4},
                     "log": "Mali haklar eksiksiz iade edildi; haksız tutukluluk tazminatları hak sahiplerine ödendi."},
                    {"label": "Beraat eden denizci ve havacı komutanları derhal TSK'daki aktif görevlerine iade ederek Mavi Vatan ve sınırlara sevk et.",
                     "effects": {"justice": -2, "people": -7, "treasury": 0, "military": 10, "authority": 9},
                     "log": "TSK'nın vurucu gücü ve tecrübesi geri döndü; ordu kumpasın yaralarını sararak yeniden ayağa kalktı."},
                    {"label": "Özel Yetkili Mahkemeleri (ÖYM) ve Terörle Mücadele Kanunu'nun 10. maddesini tamamen kaldıran reformu yasalaştır.",
                     "effects": {"justice": 9, "people": 4, "treasury": -7, "military": 0, "authority": 8},
                     "log": "Özel yetkili mahkeme garabetine son verildi; adli yargı olağan hukuk düzenine döndü."}
                ]
            else:
                options_map[eid] = [
                    {"label": f"{title} davasında sahte delilleri ve usulsüz dinlemeleri yargı denetimiyle ayıkla; hukukun üstünlüğünü ve masumiyet karinesini savun.",
                     "effects": {"justice": 8, "people": 7, "treasury": -2, "military": 0, "authority": -3},
                     "log": f"{title} dosyasında adil yargılanma hakkı gözetildi; kumpas ve sahtecilik iddiaları teftişe alındı."},
                    {"label": f"{title} sebebiyle kutuplaşan toplum kesimleri ve sivil toplumla istişare yürüt; toplumsal vicdanı rahatlatacak uzlaşı sağla.",
                     "effects": {"justice": -6, "people": 8, "treasury": -3, "military": 0, "authority": 7},
                     "log": f"{title} hadisesinde gerilim düşürüldü; mağduriyetler dinlenerek toplumsal barış korundu."},
                    {"label": f"{title} davalarının Hazineye yüklediği tazminat ve dava masraflarını mali disiplinle sınırla.",
                     "effects": {"justice": -2, "people": -6, "treasury": 8, "military": 0, "authority": 4},
                     "log": f"{title} sürecinde mali dengeler korundu; kamu bütçesi haksız harcamalardan arındırıldı."},
                    {"label": f"{title} sürecinde TSK ve emniyet içindeki yasadışı hiziplere karşı devlet otoritesini kararlılıkla koru.",
                     "effects": {"justice": -3, "people": -8, "treasury": 0, "military": 9, "authority": 8},
                     "log": f"{title} karşısında disiplin sağlandı; ordunun operasyonel kabiliyeti korundu."},
                    {"label": f"Bilirkişilik ve adli bilişim standartlarını baştan yazan 'Adil Yargılanma ve Delil Güvenliği Reform Kanunu'nu çıkar.",
                     "effects": {"justice": 8, "people": 4, "treasury": -7, "military": 0, "authority": 8},
                     "log": f"Yasal güvence getirildi; {title} benzeri manipülasyonların önü kalıcı olarak kesildi."}
                ]

        # DOMAIN 6 (indices 250 to 279: tr_vaka_251 to tr_vaka_280)
        elif 250 <= i <= 279:
            if "12 Eylül 2010" in title or "Bireysel Başvuru" in title:
                options_map[eid] = [
                    {"label": "Vatandaşların temel hak ihlallerini doğrudan AYM'ye taşıyabileceği 'Bireysel Başvuru' hakkını en geniş standartta işlet.",
                     "effects": {"justice": 10, "people": 8, "treasury": -2, "military": 0, "authority": -2},
                     "log": "Türk hukuk devriminde tarihi adım atıldı; vatandaşın devlete karşı hak arama hürriyeti AYM zırhına kavuştu."},
                    {"label": "Referandum sürecinde sendikalar ve sivil toplumla görüşerek memurlara toplu sözleşme ve kadınlara pozitif ayrımcılık maddelerini öne çıkar.",
                     "effects": {"justice": -6, "people": 9, "treasury": -3, "military": 0, "authority": 7},
                     "log": "Halkın %58 desteğiyle paket onaylandı; sivil anayasa yolunda büyük bir meşruiyet sağlandı."},
                    {"label": "AİHM'e giden yüz binlerce tazminat dosyasını AYM bünyesinde çözerek Türkiye'nin döviz tazminatı ödemesini önle.",
                     "effects": {"justice": -2, "people": -6, "treasury": 9, "military": 0, "authority": 4},
                     "log": "Hazine kasası kurtarıldı; AİHM tazminatlarının önüne yerel başvuru yoluyla geçildi."},
                    {"label": "12 Eylül askeri darbesini yapan generallerin yargılanmasını engelleyen geçici 15. maddeyi kaldırıp adli hesap sor.",
                     "effects": {"justice": -3, "people": -7, "treasury": 0, "military": 8, "authority": 9},
                     "log": "Darbecilere yargı yolu açıldı; Kenan Evren ve cuntacılar sanık sandalyesine oturtuldu."},
                    {"label": "Anayasa Mahkemesi ve HSYK'nın yeni yapısını düzenleyen 5982 Sayılı Anayasa Değişikliği Kanunu'nu yürürlüğe koy.",
                     "effects": {"justice": 8, "people": 4, "treasury": -7, "military": 0, "authority": 8},
                     "log": "Yargı kurumlarının yapısı dönüştürüldü; askeri yargının sivilleri yargılama yetkisi tamamen kaldırıldı."}
                ]
            elif "7 Şubat 2012 MİT Krizi" in title or "Hakan Fidan" in title or "MİT Kanunu" in title:
                options_map[eid] = [
                    {"label": "Devletin barış ve terörle mücadele politikalarını yürüten istihbarat teşkilatının yetkisiz savcılarca tasfiye edilmesine diren.",
                     "effects": {"justice": 8, "people": 7, "treasury": -2, "military": 0, "authority": -3},
                     "log": "Devlet aklı ve meşruiyet korundu; özel yetkili savcının yargı darbesi teşebbüsü boşa çıkarıldı."},
                    {"label": "Krizin hükümet ile bürokrasi arasında topyekun çatışmaya dönüşmesini önlemek için meclisteki partileri gizli oturumda bilgilendir.",
                     "effects": {"justice": -6, "people": 8, "treasury": -2, "military": 0, "authority": 7},
                     "log": "Meclis bilgilendirildi; krizin milli güvenlik boyutu partilere anlatılarak gerilim düşürüldü."},
                    {"label": "MİT operasyonel bütçesi ve sahadaki istihbari varlıkların ifşa olmasını önlemek için örtülü ödenek kaynaklarını koru.",
                     "effects": {"justice": -2, "people": -6, "treasury": 8, "military": 0, "authority": 4},
                     "log": "İstihbarat ağı güvenceye alındı; saha ajanlarının finansmanı kesintisiz sürdürüldü."},
                    {"label": "Başbakan'ın talimatıyla MİT Müsteşarı'na 'Savcılığa gitme, gerekirse kapıda çatışın' emrini vererek Ankara ve İstanbul'da koruma kalkanı kur.",
                     "effects": {"justice": -3, "people": -8, "treasury": 0, "military": 10, "authority": 10},
                     "log": "Müsteşarlık binası korumaya alındı; polisin MİT'i basması silahlı güç gösterisiyle engellendi."},
                    {"label": "TBMM'de gece yarısı acil kanun teklifi vererek MİT mensuplarının soruşturulmasını doğrudan Başbakan iznine bağla.",
                     "effects": {"justice": 8, "people": 4, "treasury": -6, "military": 0, "authority": 9},
                     "log": "2937 Sayılı MİT Kanunu revize edildi; yargı üzerinden hükümete kurulan tuzak kanunla dağıtıldı."}
                ]
            elif "17 Aralık" in title or "25 Aralık" in title or "Bakan Çocukları" in title:
                options_map[eid] = [
                    {"label": "Yolsuzluk iddiaları, ayakkabı kutuları ve para kasaları hakkında adli sürecin ve Sayıştay denetiminin şeffaf işlemesini sağla.",
                     "effects": {"justice": 9, "people": 8, "treasury": -3, "military": 0, "authority": -4},
                     "log": "Adalet arayışı öne çıkarıldı; istifa eden bakanların Yüce Divan'da aklanması talep edildi."},
                    {"label": "Halkbank ve kamu bankalarının itibarını korumak için iş dünyası ve esnafla toplantı yap; reel sektöre kredi musluğunu açık tut.",
                     "effects": {"justice": -6, "people": 8, "treasury": -4, "military": 0, "authority": 7},
                     "log": "Piyasa paniği yatıştırıldı; esnaf ve KOBİ'lerin bankacılık sistemine güveni tazelendi."},
                    {"label": "Operasyonların tetiklediği döviz spekülasyonu ve borsa çöküşünü engellemek için Hazine likiditesini devreye sok.",
                     "effects": {"justice": -2, "people": -7, "treasury": 9, "military": 0, "authority": 4},
                     "log": "Mali darbe püskürtüldü; kur şokunun reel sektörü batırmasının önüne geçildi."},
                    {"label": "Hükümete haber vermeden gizli operasyon yapan emniyet müdürleri ve paralel klikleri derhal görevden uzaklaştır.",
                     "effects": {"justice": -3, "people": -8, "treasury": 0, "military": 9, "authority": 9},
                     "log": "Emniyet teşkilatında hızlı bir iç tasfiye yapıldı; hiyerarşi dışına çıkan amirler açığa alındı."},
                    {"label": "Adli Kolluk Yönetmeliği'ni değiştirerek polisin savcı talimatlarını mülki amirine bildirmesini zorunlu kılan reform yap.",
                     "effects": {"justice": 8, "people": 3, "treasury": -7, "military": 0, "authority": 9},
                     "log": "Yargı-kolluk ilişkileri sivil idareye bağlandı; savcıların habersiz şafak operasyonları engellendi."}
                ]
            elif "TIR Krizleri" in title or "MİT TIR'ları" in title:
                options_map[eid] = [
                    {"label": "Devlet sırrı ve milli güvenlik doktrini kapsamında Suriye Türkmenlerine gönderilen yardımların dokunulmazlığını savun.",
                     "effects": {"justice": 8, "people": 7, "treasury": -2, "military": 0, "authority": -3},
                     "log": "Milli savunma ve dış politika sırrı savunuldu; devletin beka operasyonuna hukuki sahip çıkıldı."},
                    {"label": "Bölgedeki aşiretler, Türkmen meclisi ve sivil toplum temsilcileriyle görüşerek insani yardımların güvenli intikalini sağla.",
                     "effects": {"justice": -6, "people": 8, "treasury": -2, "military": 0, "authority": 7},
                     "log": "Bölge halkı teskin edildi; Türkmenlerin insani yardıma erişimi güvence altına alındı."},
                    {"label": "MİT lojistiğinin ve sınır ötesi yardım tırlarının güvenliği için Hazine'den ek sınır ötesi yardım bütçesi tahsis et.",
                     "effects": {"justice": -2, "people": -6, "treasury": 8, "military": 0, "authority": 4},
                     "log": "Sınır hattındaki insani operasyonlar kesintisiz sürdürüldü."},
                    {"label": "MİT görevlilerini darp edip yere yatıran jandarma ve savcılık ekibine karşı Adana Valisi ve Özel Harekat polislerini sahaya sür.",
                     "effects": {"justice": -3, "people": -8, "treasury": 0, "military": 10, "authority": 10},
                     "log": "Tırların zorla açılması ve aranması engellendi; tırlar emniyet kordonunda sınır boyuna ulaştırıldı."},
                    {"label": "Devlet sırrı niteliğindeki askeri ve istihbari taşımaların aranamayacağını emreden 'Milli İstihbarat Hizmetleri Kanunu' çıkar.",
                     "effects": {"justice": 8, "people": 4, "treasury": -6, "military": 0, "authority": 9},
                     "log": "MİT'in sınır ötesi operasyonel yetkileri kanunlaştı; ajan ve sevkiyat dokunulmazlığı tescillendi."}
                ]
            elif "Bank Asya" in title or "Koza İpek" in title or "Zaman Gazetesi" in title:
                options_map[eid] = [
                    {"label": "Terörün finansmanı ve kara para aklama şüphelerini MASAK ve BDDK murakıplarıyla belgelendirip bağımsız mahkemeye sun.",
                     "effects": {"justice": 9, "people": 7, "treasury": -2, "military": 0, "authority": -3},
                     "log": "Hukuki prosedürler eksiksiz tamamlandı; terör örgütüne para aktaran mekanizmalar adli delillerle çöktü."},
                    {"label": "Banka mudileri ve şirket çalışanlarının mağdur olmaması için TMSF bünyesinde şeffaf bilgilendirme ve ödeme masası kur.",
                     "effects": {"justice": -6, "people": 8, "treasury": -3, "military": 0, "authority": 7},
                     "log": "Küçük mudilerin paraları ödendi; krizin bankacılık sistemine sirayet etmesi önlendi."},
                    {"label": "Kayyuma devredilen şirket ve holding varlıklarını TMSF portföyüne alıp şeffaf ihalelerle satarak Hazineye gelir kaydet.",
                     "effects": {"justice": -2, "people": -6, "treasury": 10, "military": 0, "authority": 5},
                     "log": "Terörün mali kaynakları devlete irad kaydedildi; Hazine kasasına devasa gelir girdi."},
                    {"label": "Kayyum atamalarına karşı holding binaları önünde toplanan örgüt sempatizanlarına karşı çevik kuvvetle barikat kur.",
                     "effects": {"justice": -3, "people": -8, "treasury": 0, "military": 9, "authority": 8},
                     "log": "Bina işgalleri ve taşkınlıklar önlendi; kayyum heyetleri göreve başlatıldı."},
                    {"label": "Terör örgütlerinin şirketlerine kayyum atanmasını ve tasfiyesini hızlandıran 'Terörün Finansmanıyla Mücadele Kanunu' çıkar.",
                     "effects": {"justice": 8, "people": 4, "treasury": -7, "military": 0, "authority": 8},
                     "log": "Mali terörle mücadelede yasal altyapı tamamlandı; himmet çarkları kanunen parçalandı."}
                ]
            elif "Mehmet Selim Kiraz" in title:
                options_map[eid] = [
                    {"label": "Şehit savcının yürüttüğü Berkin Elvan soruşturmasını hiçbir boşluk bırakmadan adaletin gerektirdiği şekilde sonuçlandır.",
                     "effects": {"justice": 9, "people": 8, "treasury": -2, "military": 0, "authority": -3},
                     "log": "Hukukun üstünlüğü ve adalet kararlılıkla savunuldu; teröristlerin davayı rehin almasına izin verilmedi."},
                    {"label": "Tüm adliye çalışanları ve barolarla ortak teröre lanet mitingi düzenleyerek yargı camiasında birlik ve beraberlik sağla.",
                     "effects": {"justice": -5, "people": 9, "treasury": -2, "military": 0, "authority": 7},
                     "log": "Yargı camiası kenetlendi; terör eylemine karşı tüm hakim, savcı ve avukatlar ortak ses verdi."},
                    {"label": "Şehit savcının ailesine devlet övünç madalyası ve en üst baremden şehitlik maaşı/konutu tahsis et.",
                     "effects": {"justice": -2, "people": -6, "treasury": 8, "military": 0, "authority": 4},
                     "log": "Şehidin geride kalan ailesine devlet sahip çıktı; maddi ve manevi güvence sağlandı."},
                    {"label": "Savcıyı makamında rehin alan DHKP-C'li teröristlere karşı Polis Özel Harekat timleriyle operasyon emri ver.",
                     "effects": {"justice": -3, "people": -8, "treasury": 0, "military": 10, "authority": 9},
                     "log": "Operasyonla teröristler etkisiz hale getirildi; devlet terörle pazarlık yapmayacağını gösterdi."},
                    {"label": "Tüm adalet saraylarının girişlerinde avukatlar dahil çantaların x-ray'den geçmesini zorunlu kılan 'Adliye Güvenlik Kanunu' çıkar.",
                     "effects": {"justice": 8, "people": 4, "treasury": -7, "military": 0, "authority": 8},
                     "log": "Adliyelerdeki güvenlik zafiyetleri kapatıldı; duruşma salonlarına silah sokulması imkansız kılındı."}
                ]
            else:
                options_map[eid] = [
                    {"label": f"{title} meselesinde yargı bağımsızlığı ve anayasal meşruiyet kurallarını tavizsiz işleterek adaleti sağla.",
                     "effects": {"justice": 8, "people": 7, "treasury": -2, "military": 0, "authority": -3},
                     "log": f"{title} konusunda adil yargılanma ve hukuk kuralları gözetildi; idari işlemler hukuka bağlandı."},
                    {"label": f"{title} sürecinde ilgili kurumlar, sivil toplum ve halkla istişare yürüterek toplumsal uzlaşıyı sağla.",
                     "effects": {"justice": -6, "people": 8, "treasury": -3, "military": 0, "authority": 7},
                     "log": f"{title} hususunda taraflar dinlendi; diyalog kanalları açılarak gerilim yatıştırıldı."},
                    {"label": f"{title} ile bağlantılı kamu kaynaklarını ve Hazine fonlarını sıkı tasarruf tedbirleriyle koru.",
                     "effects": {"justice": -2, "people": -6, "treasury": 8, "military": 0, "authority": 4},
                     "log": f"{title} hadisesinde mali disiplin korundu; kamu bütçesi olası zararlardan korundu."},
                    {"label": f"{title} karşısında emniyet ve istihbarat birimlerini görevlendirerek kamu düzenini ve devlet otoritesini koru.",
                     "effects": {"justice": -3, "people": -8, "treasury": 0, "military": 9, "authority": 8},
                     "log": f"{title} karşısında kamu nizamı sağlandı; devletin kararlılığı gösterildi."},
                    {"label": f"TBMM'de {title} sorununu kurumsal olarak çözecek reform kanununu kabul ettir.",
                     "effects": {"justice": 8, "people": 4, "treasury": -7, "military": 0, "authority": 8},
                     "log": f"Kabul edilen yasal reform ile kurumsal düzen kuruldu; benzer krizlerin tekerrürü önlendi."}
                ]

    print(f"Total options generated for Batch 2: {len(options_map)}")
    updated_deck = apply_options_to_deck(deck, options_map)
    save_modern_deck(updated_deck)

if __name__ == '__main__':
    generate_domains_4_to_6()
