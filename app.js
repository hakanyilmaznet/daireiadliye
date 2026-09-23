// =================================================================
    // 1. WEB AUDIO API SES MOTORU (Harici Dosya Gerektirmez)
    // =================================================================
    class SoundEngine {
      constructor() {
        this.ctx = null;
        this.muted = false;
      }

      init() {
        if (!this.ctx) {
          const AudioContext = window.AudioContext || window.webkitAudioContext;
          this.ctx = new AudioContext();
        }
        if (this.ctx.state === "suspended") {
          this.ctx.resume();
        }
      }

      toggle() {
        this.muted = !this.muted;
        const btn = document.getElementById("soundToggle");
        btn.innerHTML = this.muted ? "🔇 Ses: Kapalı" : "🔊 Ses: Açık";
      }

      playTone(freq, type = "sine", duration = 0.3, gainVal = 0.15) {
        if (this.muted) return;
        this.init();
        try {
          const osc = this.ctx.createOscillator();
          const gain = this.ctx.createGain();
          osc.type = type;
          osc.frequency.setValueAtTime(freq, this.ctx.currentTime);
          
          gain.gain.setValueAtTime(gainVal, this.ctx.currentTime);
          gain.gain.exponentialRampToValueAtTime(0.0001, this.ctx.currentTime + duration);

          osc.connect(gain);
          gain.connect(this.ctx.destination);

          osc.start();
          osc.stop(this.ctx.currentTime + duration);
        } catch(e) {}
      }

      // Karar anında zarif tınlama
      playGong() {
        if (this.muted) return;
        this.init();
        [220, 440, 660].forEach((f, i) => {
          setTimeout(() => this.playTone(f, "triangle", 0.6, 0.08), i * 35);
        });
      }

      // Kritik tehlike alarmı
      playWarning() {
        if (this.muted) return;
        this.init();
        this.playTone(130, "sawtooth", 0.7, 0.15);
      }

      // Oyun sonu çöküş akoru
      playDoom() {
        if (this.muted) return;
        this.init();
        [110, 116, 123].forEach(f => this.playTone(f, "sawtooth", 1.4, 0.18));
      }
    }

    const soundFX = new SoundEngine();

    // =================================================================
    // 2. ÇEKİRDEK DESTE (event_deck.json henüz seçilmemişse zengin fallback)
    // =================================================================
    const FALLBACK_DECK = [
      {
        id: "fb_01",
        source: "Başdefterdarlık",
        title: "Celâlî Tehdidi ve İmdâdiyye Vergisi",
        desc: "Sefere çıkan ordu için hazinede nakit tükendi. Defterdar, reayadan acil ek 'imdâdiyye' toplanmasını teklif ediyor.",
        options: [
          { label: "Vergiyi topla; ordu akçesiz sefere çıkamaz!", preview: "Hazine +20, Ordu +10 | Adalet -20, Reaya -20", effects: { justice: -20, people: -20, treasury: 20, military: 10, authority: 0 }, log: "Reayaya ağır vergi yüklendi; köylüler tarlayı terk etmeye başladı." },
          { label: "Reddet; saray harcamaları kısılsın, reaya ezilmesin!", preview: "Adalet +15, Reaya +15 | Hazine -15, Ordu -15", effects: { justice: 15, people: 15, treasury: -15, military: -15, authority: -5 }, log: "Halk rahat nefes aldı fakat ulufe gecikince ocakta homurdanma başladı." }
        ]
      },
      {
        id: "fb_02",
        source: "Divan-ı Mezalim",
        title: "Bursa Kadısı Hakkında Rüşvet Davası",
        desc: "Bursa tüccarları, tayin edilen kadının rüşvet almadan hüküm vermediğini, vakıf arazilerini gasp ettiğini bildirdi.",
        options: [
          { label: "Kadıyı derhal azlet ve mal varlığını müsadere et!", preview: "Adalet +25, Reaya +15, Hazine +10 | Otorite +5", effects: { justice: 25, people: 15, treasury: 10, military: 0, authority: 5 }, log: "Rüşvetçi kadı sürüldü; tebaanın mahkemelere güveni tazelendi." },
          { label: "İlmiye sınıfını karşına alma; meseleyi örtbas et.", preview: "Adalet -30, Reaya -25 | Otorite -15", effects: { justice: -30, people: -25, treasury: 0, military: 0, authority: -15 }, log: "Zulüm cezasız kaldı; taşrada adalet kapısına olan itikat sarsıldı." }
        ]
      },
      {
        id: "fb_03",
        source: "Yeniçeri Ocağı",
        title: "Kırpık Akçe ile Ulufe Dağıtımı",
        desc: "Ayarı düşürülmüş gümüş akçeyi kabul etmeyen yeniçeriler çarşıda kepenk kapattırıp kazan kaldırdı.",
        options: [
          { label: "Kasayı aç; tam ayar saf akçe ile maaşları öde.", preview: "Ordu +25, Hazine -25 | Otorite -10", effects: { justice: 5, people: 0, treasury: -25, military: 25, authority: -10 }, log: "Kazanlar indi fakat hazinede neredeyse hiç para kalmadı." },
          { label: "Taviz verme; elebaşıları zindana at!", preview: "Otorite +20 | Ordu -35, Adalet -15", effects: { justice: -15, people: 0, treasury: 0, military: -35, authority: 20 }, log: "İsyan güçle bastırıldı ancak ordunun nizama bağlılığı ağır yara aldı." }
        ]
      },
      {
        id: "fb_04",
        source: "Sadaret Tezkiresi",
        title: "Sadrazamın Liyakatsiz Akraba Tayinleri",
        desc: "Sadrazam, ehliyetli defterdar kâtiplerini azledip yerlerine genç ve tecrübesiz yeğenlerini getirdi.",
        options: [
          { label: "Sadrazamı azarla ve liyakatli eski kâtipleri görevlerine iade et.", preview: "Adalet +20, Otorite +10 | Ordu -5", effects: { justice: 20, people: 5, treasury: 0, military: -5, authority: 10 }, log: "Devlet kalemlerinde liyakat korundu, vezirler hizbe çekildi." },
          { label: "Bürokrasinin iç işine karışma, sadrazama serbestiyet ver.", preview: "Adalet -20, Hazine -10 | Otorite -10", effects: { justice: -20, people: -5, treasury: -10, military: 0, authority: -10 }, log: "Kalemlerde rüşvet ve liyakatsizlik yayıldı, hesaplar şaştı." }
        ]
      },
      {
        id: "fb_05",
        source: "Şeyhülislam Fetvası",
        title: "Vakıf Arazisinin Bey Tarafından Gasbı",
        desc: "Bir sancak beyi, darüşşifaya ait gelir getiren zeytinlikleri kendi şahsi çiftliğine katarak gelirlerine el koydu.",
        options: [
          { label: "Şeriat gereği arazileri derhal vakfa iade et, beye ceza kes.", preview: "Adalet +20, Reaya +10, Hazine +5 | Ordu -10", effects: { justice: 20, people: 10, treasury: 5, military: -10, authority: 0 }, log: "Vakıf hukuku korundu, taşra beylerinin zorbalığı dizginlendi." },
          { label: "Sancak beyi sınır muhafızıdır; ses çıkarma.", preview: "Adalet -25, Reaya -15 | Ordu +10", effects: { justice: -25, people: -15, treasury: 0, military: 10, authority: -5 }, log: "Vakıf çökertildi; halkın devlete olan itikadı sarsıldı." }
        ]
      },
      {
        id: "fb_06",
        source: "Mültezim Maruzu",
        title: "Haksız Salgun Vergisi Dayatması",
        desc: "Diyarbakır valisi, sefere mühimmat tedariki bahanesiyle köylüden kanunsuz ek harç toplamaktadır.",
        options: [
          { label: "Adâletnâme ilan et: Fazla toplanan akçeler köylüye iade edilsin!", preview: "Adalet +20, Reaya +20 | Hazine -10, Ordu -10", effects: { justice: 20, people: 20, treasury: -10, military: -10, authority: 5 }, log: "Adalet fermanı okundu, çiftçiler tarlalarına geri döndü." },
          { label: "Valiyi serbest bırak; ordunun nakde ihtiyacı vardır.", preview: "Adalet -25, Reaya -25 | Hazine +15, Ordu +15", effects: { justice: -25, people: -25, treasury: 15, military: 15, authority: -10 }, log: "Köylüler dağlara kaçtı; ziraat durma noktasına geldi." }
        ]
      },
      {
        id: "fb_07",
        source: "Tersane-i Âmire",
        title: "Akdeniz Donanmasının Kereste İhtiyacı",
        desc: "Kaptan-ı Derya, Karadeniz ormanlarından acil kadırga kerestesi kesilmesini ve kürekçi reayanın toplanmasını talep ediyor.",
        options: [
          { label: "Tersaneye tam bütçe ve ferman tahsis et; denizler boş bırakılamaz.", preview: "Ordu +20, Otorite +10 | Hazine -20, Reaya -10", effects: { justice: 0, people: -10, treasury: -20, military: 20, authority: 10 }, log: "Donanma Akdeniz'e açıldı; sahil kaleleri emniyete alındı." },
          { label: "Seferi ertele; köylüyü çift sürüm vaktinde angaryaya boğma.", preview: "Reaya +15, Hazine +10 | Ordu -20, Otorite -10", effects: { justice: 5, people: 15, treasury: 10, military: -20, authority: -10 }, log: "Tersane yavaşladı fakat reaya mahsulünü zamanında hasat etti." }
        ]
      },
      {
        id: "fb_08",
        source: "Ahi Loncası Meclisi",
        title: "İstanbul Çarşısında Narh İhlali",
        desc: "Ekmekçi ve kasap loncaları, buğday kıtlığı nedeniyle narh fiyatlarının üzerinde fahiş satış yapmaktadır.",
        options: [
          { label: "Muhtesibi vazifelendir; sıkı teftiş yapıp narha uymayanı cezalandır.", preview: "Adalet +20, Reaya +15 | Hazine +5, Otorite +10", effects: { justice: 20, people: 15, treasury: 5, military: 0, authority: 10 }, log: "Çarşıda nizam sağlandı; fukara reaya ucuz ekmeğe kavuştu." },
          { label: "Tüccarı serbest bırak; piyasa kendi dengesini bulsun.", preview: "Adalet -25, Reaya -30 | Hazine +10, Otorite -15", effects: { justice: -25, people: -30, treasury: 10, military: 0, authority: -15 }, log: "Pahalılık halkı ezdi; payitahtta fırınlar önünde kargaşa patlak verdi." }
        ]
      },
      {
        id: "fb_09",
        source: "Darphane Teftişi",
        title: "Sahte Venedik Dukası ve Sikkelerin Tağşişi",
        desc: "Frenk tüccarlarının piyasaya sürdüğü ayarı düşük gümüşler iç pazardaki has akçeleri eritip kaçırmaktadır.",
        options: [
          { label: "Sikke tashihine git: Eski paraları toplatıp has ayarla yeniden bastır.", preview: "Hazine +20, Otorite +15, Adalet +10 | Reaya -5", effects: { justice: 10, people: -5, treasury: 20, military: 5, authority: 15 }, log: "Mali itibar korundu; akçenin değeri yabancı paralara karşı dirildi." },
          { label: "Göz yum; darphane masrafına girmeyelim.", preview: "Hazine -20, Otorite -20 | Adalet -15", effects: { justice: -15, people: -15, treasury: -20, military: -10, authority: -20 }, log: "Enflasyon fırladı; devletin mali otoritesi ağır sarsıntı geçirdi." }
        ]
      },
      {
        id: "fb_10",
        source: "Serhad Gazileri",
        title: "Mohaç ve Uyvar Kalesi İmdadı",
        desc: "Sınır boyundaki muhafızlar kış yaklaşırken erzak ve cephane takviyesi bekliyor; aksi takdirde kaleyi tahliye edecekler.",
        options: [
          { label: "Derhal cebehaneden barut ve mühimmat kervanını yola çıkar.", preview: "Ordu +25, Otorite +10 | Hazine -20", effects: { justice: 0, people: 0, treasury: -20, military: 25, authority: 10 }, log: "Serhad muhafızları kaleyi savundu; sınır boylarında ezan susmadı." },
          { label: "Hazine müsait değil; kaleyi kendi imkânlarıyla müdafaa etsinler.", preview: "Hazine +15 | Ordu -30, Otorite -20", effects: { justice: -10, people: -10, treasury: 15, military: -30, authority: -20 }, log: "Kale düştü; düşman akıncıları sınır kasabalarını yağmaladı." }
        ]
      }
    ];

    // =================================================================
    // 3. TEKRARSIZ AKILLI DESTE YÖNETİCİSİ (DeckManager Engine)
    // =================================================================
    class DeckManager {
      constructor(masterDeck = []) {
        this.masterDeck = [];
        this.drawPile = [];
        this.discardPile = [];
        this.seenIds = new Set();
        this.recentSources = [];
        this.cycle = 1;
        if (masterDeck.length > 0) {
          this.init(masterDeck);
        }
      }

      // Dosya içeriğini (JavaScript veya saf JSON) güvenle ayrıştıran parser
      static parseDeckData(raw) {
        if (!raw || typeof raw !== "string") return null;
        let content = raw.trim();
        // const EVENT_DECK = [...] veya var EVENT_DECK_MODERN = [...] temizliği
        if (/^(const|var|let)\s+EVENT_DECK(?:_MODERN)?\s*=/.test(content)) {
          content = content.replace(/^(const|var|let)\s+EVENT_DECK(?:_MODERN)?\s*=\s*/, '').replace(/;\s*$/, '');
        }
        try {
          const fn = new Function('return ' + content);
          const res = fn();
          if (Array.isArray(res)) return res;
        } catch (e) {
          try {
            const res = JSON.parse(content);
            if (Array.isArray(res)) return res;
          } catch (e2) {}
        }
        return null;
      }

      // Fisher-Yates (Knuth) karıştırma algoritması
      shuffle(array) {
        const arr = [...array];
        for (let i = arr.length - 1; i > 0; i--) {
          const j = Math.floor(Math.random() * (i + 1));
          [arr[i], arr[j]] = [arr[j], arr[i]];
        }
        return arr;
      }

      init(cards) {
        if (!Array.isArray(cards)) return;
        this.masterDeck = cards.filter(c => c && c.title && Array.isArray(c.options));
        this.reset();
      }

      reset() {
        this.drawPile = this.shuffle(this.masterDeck);
        this.discardPile = [];
        this.seenIds.clear();
        this.recentSources = [];
        this.cycle = 1;
      }

      get remainingCount() {
        return this.drawPile.length;
      }

      get totalCount() {
        return this.masterDeck.length;
      }

      get playedCount() {
        return this.discardPile.length;
      }

      // Kritik metriği tespit et (en düşük ve 35 altı olan)
      identifyCrisis(stats) {
        if (!stats) return null;
        const threshold = 35;
        const criticals = [];
        const keys = ["treasury", "justice", "military", "people", "authority"];
        for (const k of keys) {
          if (stats[k] < threshold) {
            criticals.push({ key: k, val: stats[k] });
          }
        }
        if (criticals.length === 0) return null;
        criticals.sort((a, b) => a.val - b.val);
        return criticals[0].key;
      }

      // Bir vakanın kriz konusuyla eşleşme durumu
      matchesCrisis(event, crisisKey) {
        if (!crisisKey || !event) return false;
        const text = `${event.source || ''} ${event.title || ''} ${event.desc || ''}`.toLowerCase();
        
        const keywords = {
          treasury: ["hazine", "akçe", "vergi", "maliye", "defterdar", "altın", "kese", "sarraf", "imdadiyye", "salgun", "bedel", "cizye", "harç"],
          military: ["ordu", "asker", "yeniçeri", "sipahi", "sefer", "kale", "serhad", "ocak", "kazan", "tüfek", "donanma", "paşa", "cebehane"],
          justice: ["adalet", "kadı", "mahkeme", "hukuk", "rüşvet", "mezalim", "şeriat", "kaza", "dava", "zulüm", "müfettiş", "fetva", "haksız"],
          people: ["reaya", "köylü", "halk", "çiftçi", "kıtlık", "salgın", "veba", "kuraklık", "aşar", "esnaf", "ahiler", "lonca", "göç", "celali"],
          authority: ["mülk", "otorite", "sadrazam", "isyan", "divan", "vezir", "taht", "ferman", "ayan", "fitne", "darbe", "azil", "tuğra"]
        };

        const list = keywords[crisisKey] || [];
        for (const kw of list) {
          if (text.includes(kw)) return true;
        }

        if (Array.isArray(event.options)) {
          for (const opt of event.options) {
            if (opt.effects && opt.effects[crisisKey] > 0) return true;
          }
        }
        return false;
      }

      // Tekrara düşmeyen akıllı çekim fonksiyonu
      drawNext(stats = null) {
        if (this.masterDeck.length === 0) return null;

        // Çekme destesi bittiyse ıskarta destesini karıştırıp yeni döngüye geç
        if (this.drawPile.length === 0) {
          if (this.discardPile.length > 0) {
            this.cycle++;
            this.drawPile = this.shuffle(this.discardPile);
            this.discardPile = [];
            this.seenIds.clear();
          } else {
            this.drawPile = this.shuffle(this.masterDeck);
          }
        }

        const crisisKey = this.identifyCrisis(stats);
        let chosenIndex = -1;

        // 1. Kriz Duyarlı Çekim (Kriz varsa %70 ihtimalle çekme destesindeki ilgili unplayed vakayı çek)
        if (crisisKey && Math.random() < 0.70) {
          const matchingIndices = [];
          for (let i = 0; i < this.drawPile.length; i++) {
            if (this.matchesCrisis(this.drawPile[i], crisisKey)) {
              matchingIndices.push(i);
            }
          }
          if (matchingIndices.length > 0) {
            // Son kaynaktan farklı olanları tercih et (konu çeşitliliği)
            const filtered = matchingIndices.filter(idx => {
              const src = this.drawPile[idx].source;
              return !this.recentSources.slice(-1).includes(src);
            });
            const pool = filtered.length > 0 ? filtered : matchingIndices;
            chosenIndex = pool[Math.floor(Math.random() * pool.length)];
          }
        }

        // 2. Konu Yorgunluğunu Önleme (Ardı ardına aynı kaynaktan kart gelmesini engelle)
        if (chosenIndex === -1) {
          const candidates = [];
          const lastSource = this.recentSources.length > 0 ? this.recentSources[this.recentSources.length - 1] : null;
          const searchWindow = Math.min(25, this.drawPile.length);
          for (let i = 0; i < searchWindow; i++) {
            if (!lastSource || this.drawPile[i].source !== lastSource) {
              candidates.push(i);
            }
          }

          if (candidates.length > 0) {
            chosenIndex = candidates[Math.floor(Math.random() * candidates.length)];
          } else {
            chosenIndex = 0;
          }
        }

        // Seçilen kartı çekme destesinden ÇIKAR (Kesinlikle Tekrarsız)
        const event = this.drawPile.splice(chosenIndex, 1)[0];
        this.discardPile.push(event);
        if (event.id) this.seenIds.add(event.id);
        if (event.source) {
          this.recentSources.push(event.source);
          if (this.recentSources.length > 5) this.recentSources.shift();
        }

        return event;
      }
    }

    // =================================================================
    // 3.5. KULLANICI KİMLİK DOĞRULAMA & OTURUM ARAYÜZÜ (AuthUI)
    // =================================================================
    class AuthUI {
      constructor() {
        this.user = null;
        this.isLoggedIn = false;
        this.init();
      }

      async init() {
        await this.checkMe();
      }

      async checkMe() {
        try {
          const resp = await fetch("api/auth.php?action=me");
          if (resp.ok) {
            const data = await resp.json();
            if (data.success && data.logged_in && data.user) {
              this.user = data.user;
              this.isLoggedIn = true;
              this.updateUserUI();
              return;
            }
          }
        } catch (e) {}
        this.user = null;
        this.isLoggedIn = false;
        this.updateUserUI();
      }

      updateUserUI() {
        const btn = document.getElementById("userAuthBtn");
        const label = document.getElementById("userBtnLabel");
        if (!btn || !label) return;

        if (this.isLoggedIn && this.user) {
          label.innerText = this.user.username;
          btn.classList.add("user-logged-pill");
          btn.title = `Profil: ${this.user.username} (${this.user.total_answers || 0} Hüküm)`;
        } else {
          label.innerText = "Giriş Yap";
          btn.classList.remove("user-logged-pill");
          btn.title = "Kullanıcı Girişi / Kayıt";
        }
      }

      openModal() {
        const modal = document.getElementById("authModal");
        if (!modal) return;
        modal.style.display = "flex";

        const tabs = document.getElementById("authTabs");
        const loginForm = document.getElementById("loginForm");
        const regForm = document.getElementById("registerForm");
        const profPanel = document.getElementById("userProfilePanel");

        if (this.isLoggedIn && this.user) {
          if (tabs) tabs.style.display = "none";
          if (loginForm) loginForm.style.display = "none";
          if (regForm) regForm.style.display = "none";
          if (profPanel) {
            profPanel.style.display = "flex";
            const uEl = document.getElementById("profUsername");
            const eEl = document.getElementById("profEmail");
            const aEl = document.getElementById("profTotalAnswers");
            if (uEl) uEl.innerText = this.user.username;
            if (eEl) eEl.innerText = this.user.email;
            if (aEl) aEl.innerText = this.user.total_answers || 0;
          }
        } else {
          if (tabs) tabs.style.display = "flex";
          if (profPanel) profPanel.style.display = "none";
          this.switchTab("login");
        }
      }

      closeModal() {
        const modal = document.getElementById("authModal");
        if (modal) modal.style.display = "none";
      }

      switchTab(tab) {
        const tabLogin = document.getElementById("authTabLogin");
        const tabReg = document.getElementById("authTabRegister");
        const formLogin = document.getElementById("loginForm");
        const formReg = document.getElementById("registerForm");
        const errLogin = document.getElementById("loginError");
        const errReg = document.getElementById("registerError");

        if (errLogin) errLogin.style.display = "none";
        if (errReg) errReg.style.display = "none";

        if (tab === "register") {
          if (tabLogin) tabLogin.classList.remove("active");
          if (tabReg) tabReg.classList.add("active");
          if (formLogin) formLogin.style.display = "none";
          if (formReg) formReg.style.display = "flex";
        } else {
          if (tabLogin) tabLogin.classList.add("active");
          if (tabReg) tabReg.classList.remove("active");
          if (formLogin) formLogin.style.display = "flex";
          if (formReg) formReg.style.display = "none";
        }
      }

      async handleLogin(e) {
        e.preventDefault();
        const login = document.getElementById("loginUsername").value.trim();
        const password = document.getElementById("loginPassword").value;
        const errEl = document.getElementById("loginError");
        if (errEl) errEl.style.display = "none";

        try {
          const resp = await fetch("api/auth.php?action=login", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ username: login, password })
          });
          const data = await resp.json();
          if (data.success && data.user) {
            this.user = data.user;
            this.isLoggedIn = true;
            this.updateUserUI();
            this.closeModal();
            if (window.game) {
              await window.game.checkSavedProgress();
            }
          } else {
            if (errEl) {
              errEl.innerText = data.error || "Giriş başarısız.";
              errEl.style.display = "block";
            }
          }
        } catch (err) {
          if (errEl) {
            errEl.innerText = "Sunucuya bağlanılamadı.";
            errEl.style.display = "block";
          }
        }
      }

      async handleRegister(e) {
        e.preventDefault();
        const username = document.getElementById("regUsername").value.trim();
        const email = document.getElementById("regEmail").value.trim();
        const password = document.getElementById("regPassword").value;
        const errEl = document.getElementById("registerError");
        if (errEl) errEl.style.display = "none";

        try {
          const resp = await fetch("api/auth.php?action=register", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ username, email, password })
          });
          const data = await resp.json();
          if (data.success && data.user) {
            this.user = data.user;
            this.isLoggedIn = true;
            this.updateUserUI();
            this.closeModal();
            if (window.game) {
              await window.game.checkSavedProgress();
            }
          } else {
            if (errEl) {
              errEl.innerText = data.error || "Kayıt başarısız.";
              errEl.style.display = "block";
            }
          }
        } catch (err) {
          if (errEl) {
            errEl.innerText = "Sunucuya bağlanılamadı.";
            errEl.style.display = "block";
          }
        }
      }

      async handleLogout() {
        try {
          await fetch("api/auth.php?action=logout", { method: "POST" });
        } catch (e) {}
        this.user = null;
        this.isLoggedIn = false;
        this.updateUserUI();
        this.closeModal();
        if (window.game) {
          window.game.restart();
        }
      }
    }

    // =================================================================
    // 4. SİMÜLASYON VE OYUN MOTORU
    // =================================================================
    class DaireSimulation {
      constructor() {
        this.deckManager = new DeckManager(FALLBACK_DECK);
        this.canvas = document.getElementById("hudCanvas");
        this.ctx = this.canvas.getContext("2d");
        this.angleOffset = 0;
        this.particles = [];
        this.initParticles();

        const urlParams = typeof window !== "undefined" && window.location ? new URLSearchParams(window.location.search) : null;
        this.currentMode = urlParams && urlParams.get("mode") === "ottoman" ? "ottoman" : "modern";
        this.ottomanDeck = null;
        this.modernDeck = null;

        this.stats = {
          justice: 60,
          people: 60,
          treasury: 50,
          military: 55,
          authority: 60
        };
        this.rulerTraits = {
          adli: 0,
          sulh: 0,
          mali: 0,
          otorite: 0,
          nizam: 0
        };
        this.turn = 1;
        this.isGameOver = false;
        this.isApiAvailable = false;
        this.apiPlayedCount = 0;
        this.apiTotalCount = 0;
        this.savedProgressData = null;

        this.loadDecks();
        this.startRenderLoop();
      }

      // API ve Veritabanı Desteğini Test Et
      async detectApi() {
        try {
          const resp = await fetch("api/events.php?action=counts");
          if (resp.ok) {
            const data = await resp.json();
            if (data.success && data.counts) {
              this.isApiAvailable = true;
              console.log("✓ Dâire-i Adliyye PHP API & MySQL Veritabanı aktif.");
              return true;
            }
          }
        } catch (e) {}
        this.isApiAvailable = false;
        return false;
      }

      // Her iki desteyi (Osmanlı & Modern) otomatik yükle ve hazırla
      async loadDecks() {
        await this.detectApi();
        // 1. Klasik Osmanlı Destesi
        if (typeof EVENT_DECK !== "undefined" && Array.isArray(EVENT_DECK) && EVENT_DECK.length > 0) {
          this.ottomanDeck = EVENT_DECK;
        } else if (window.EVENT_DECK && Array.isArray(window.EVENT_DECK)) {
          this.ottomanDeck = window.EVENT_DECK;
        } else {
          try {
            const resp = await fetch("event_deck.js");
            if (resp.ok) {
              const text = await resp.text();
              this.ottomanDeck = DeckManager.parseDeckData(text);
            } else {
              const resp2 = await fetch("event_deck.json");
              if (resp2.ok) {
                const text2 = await resp2.text();
                this.ottomanDeck = DeckManager.parseDeckData(text2);
              }
            }
          } catch (e) {
            try {
              const resp2 = await fetch("event_deck.json");
              if (resp2.ok) {
                const text2 = await resp2.text();
                this.ottomanDeck = DeckManager.parseDeckData(text2);
              }
            } catch (e2) {}
          }
        }

        // 2. Modern Türkiye Destesi (Son 30 Yıl)
        if (typeof EVENT_DECK_MODERN !== "undefined" && Array.isArray(EVENT_DECK_MODERN) && EVENT_DECK_MODERN.length > 0) {
          this.modernDeck = EVENT_DECK_MODERN;
        } else if (window.EVENT_DECK_MODERN && Array.isArray(window.EVENT_DECK_MODERN)) {
          this.modernDeck = window.EVENT_DECK_MODERN;
        } else {
          try {
            const resp = await fetch("event_deck_modern.js");
            if (resp.ok) {
              const text = await resp.text();
              this.modernDeck = DeckManager.parseDeckData(text);
            } else {
              const resp2 = await fetch("event_deck_modern.json");
              if (resp2.ok) {
                const text2 = await resp2.text();
                this.modernDeck = DeckManager.parseDeckData(text2);
              }
            }
          } catch (e) {
            try {
              const resp2 = await fetch("event_deck_modern.json");
              if (resp2.ok) {
                const text2 = await resp2.text();
                this.modernDeck = DeckManager.parseDeckData(text2);
              }
            } catch (e2) {}
          }
        }

        // Kaydedilmiş ilerleme var mı kontrol et
        if (this.isApiAvailable) {
          await this.checkSavedProgress();
        }

        // Başlangıç destesi olarak varsayılan modu etkinleştir
        this.setDeckMode(this.currentMode, false);
      }

      // Dönem Modunu Değiştir (Osmanlı Klasik <-> Modern Türkiye Son 30 Yıl)
      setDeckMode(mode, resetGame = false) {
        this.currentMode = mode;
        const statusEl = document.getElementById("deckStatus");
        const tabOttoman = document.getElementById("tabOttoman");
        const tabModern = document.getElementById("tabModern");
        const brandTitle = document.getElementById("brandTitle");
        const brandSub = document.getElementById("brandSub");
        const wisdomText = document.getElementById("wisdomText");
        const wisdomAuthor = document.getElementById("wisdomAuthor");
        const eqTitle = document.getElementById("eqTitle");

        const chipPeopleLbl = document.querySelector("#chip-people .lbl");
        const chipMilitaryLbl = document.querySelector("#chip-military .lbl");
        const chipAuthorityLbl = document.querySelector("#chip-authority .lbl");

        let activeDeck = null;
        if (mode === "modern") {
          activeDeck = this.modernDeck || (typeof EVENT_DECK_MODERN !== "undefined" ? EVENT_DECK_MODERN : null);
          if (tabOttoman) tabOttoman.classList.remove("active");
          if (tabModern) tabModern.classList.add("active");
          if (brandTitle) brandTitle.innerHTML = "🇹🇷 DÂİRE-İ ADLİYYE";
          if (brandSub) brandSub.innerText = "Modern Türkiye (Son 30 Yıl) Kriz Simülasyonu";
          if (chipPeopleLbl) chipPeopleLbl.innerText = "Halk";
          if (chipMilitaryLbl) chipMilitaryLbl.innerText = "Güvenlik";
          if (chipAuthorityLbl) chipAuthorityLbl.innerText = "Otorite";
          if (eqTitle) eqTitle.innerText = "CUMHURİYET & DEVLET İSTİKRARI";
          if (wisdomText) wisdomText.innerText = '"Egemenlik kayıtsız şartsız milletindir. Adalet mülkün temelidir; hukukun üstünlüğü ve iktisadi istikrar, cumhuriyetin yegâne teminatıdır."';
          if (wisdomAuthor) wisdomAuthor.innerText = "— Hukuk Devleti İlkesi & Anayasa";
          if (statusEl) {
            statusEl.className = "deck-pill";
            statusEl.innerText = `Deste: Modern Türkiye (${activeDeck ? activeDeck.length : 0} Vaka)`;
          }
        } else {
          activeDeck = this.ottomanDeck || (typeof EVENT_DECK !== "undefined" ? EVENT_DECK : null);
          if (tabOttoman) tabOttoman.classList.add("active");
          if (tabModern) tabModern.classList.remove("active");
          if (brandTitle) brandTitle.innerHTML = "⚜️ DÂİRE-İ ADLİYYE";
          if (brandSub) brandSub.innerText = "Hüküm, Adalet ve Asabiye Simülasyonu";
          if (chipPeopleLbl) chipPeopleLbl.innerText = "Reaya";
          if (chipMilitaryLbl) chipMilitaryLbl.innerText = "Ordu";
          if (chipAuthorityLbl) chipAuthorityLbl.innerText = "Mülk";
          if (eqTitle) eqTitle.innerText = "DÂİRE-İ ADLİYYE İSTİKRARI";
          if (wisdomText) wisdomText.innerText = '"Adl ile mülk ber-karar olur, reaya mülkün aslıdır; hazine reayanın refahından hâsıl olur; ordu hazine ile beslenir; adalet olmazsa cihan harab olur."';
          if (wisdomAuthor) wisdomAuthor.innerText = "— Kınalızâde Ali Çelebi, Ahlâk-ı Alâî";
          if (statusEl) {
            statusEl.className = "deck-pill";
            statusEl.innerText = `Deste: Klasik Osmanlı (${activeDeck ? activeDeck.length : 0} Vaka)`;
          }
        }

        if (Array.isArray(activeDeck) && activeDeck.length > 0) {
          this.deckManager.init(activeDeck);
        } else {
          this.deckManager.init(FALLBACK_DECK);
        }

        if (resetGame) {
          this.stats = { justice: 60, people: 60, treasury: 50, military: 55, authority: 60 };
          this.rulerTraits = { adli: 0, sulh: 0, mali: 0, otorite: 0, nizam: 0 };
          this.turn = 1;
          this.isGameOver = false;
          const modalEl = document.getElementById("gameOverModal");
          if (modalEl) modalEl.style.display = "none";
          this.log(mode === "modern" ? 
            "🇹🇷 Cumhuriyet dönemine geçildi. Son 30 yılın krizleri, siyasi, askeri ve ekonomik olayları devrede." :
            "⚜️ Klasik Osmanlı nizamına dönüldü. Dâire-i Adliyye çarkı yeniden dönüyor.");
        }

        this.updateUI();
        this.nextEvent();
      }

      toggleDeckMode() {
        soundFX.playGong();
        const newMode = this.currentMode === "ottoman" ? "modern" : "ottoman";
        this.setDeckMode(newMode, true);
      }

      // setupFileInput() {
      //   const fileInput = document.getElementById("fileInput");
      //   fileInput.addEventListener("change", (e) => {
      //     const file = e.target.files[0];
      //     if (!file) return;

      //     const reader = new FileReader();
      //     reader.onload = (event) => {
      //       try {
      //         const parsed = DeckManager.parseDeckData(event.target.result);
      //         if (Array.isArray(parsed) && parsed.length > 0) {
      //           this.deckManager.init(parsed);
      //           const statusEl = document.getElementById("deckStatus");
      //           statusEl.className = "deck-pill";
      //           statusEl.innerText = `Deste: ${parsed.length} Vaka Yüklendi (Tekrarsız)`;
      //           this.log(`Harici deste başarıyla yüklendi: ${parsed.length} adet vaka tekrarsız havuzda devrede.`);
      //           this.updateDeckCounter();
      //           this.nextEvent();
      //         } else {
      //           alert("Geçersiz dosya formatı! Dosya geçerli bir vaka dizisi içermelidir.");
      //         }
      //       } catch (err) {
      //         alert("Deste okunurken hata oluştu: " + err.message);
      //       }
      //     };
      //     reader.readAsText(file);
      //   });

      //   // Sürükle-bırak desteği
      //   window.addEventListener("dragover", (e) => e.preventDefault());
      //   window.addEventListener("drop", (e) => {
      //     e.preventDefault();
      //     if (e.dataTransfer.files.length > 0) {
      //       fileInput.files = e.dataTransfer.files;
      //       fileInput.dispatchEvent(new Event("change"));
      //     }
      //   });
      // }

      initParticles() {
        this.particles = [];
        for (let i = 0; i < 24; i++) {
          this.particles.push({
            progress: Math.random(),
            speed: 0.002 + Math.random() * 0.003,
            size: 2 + Math.random() * 2
          });
        }
      }

      clamp(val) {
        return Math.max(0, Math.min(100, val));
      }

      getSourceIcon(source) {
        if (/cumhurbaşkanlığı|başbakanlık|bakanlar kurulu/i.test(source)) return "🏛️";
        if (/merkez bankası|hazine|maliye|bddk|spk|borsa/i.test(source)) return "🪙";
        if (/genelkurmay|tsk|mgk|savunma|mit|emniyet|asayiş/i.test(source)) return "🛡️";
        if (/yargı|dgm|mahkeme|adliye|anayasa|danıştay|yargıtay/i.test(source)) return "⚖️";
        if (/tbmm|meclis|komisyon/i.test(source)) return "📜";
        if (/afad|kriz masası|kızılay|sağlık/i.test(source)) return "🚨";
        if (/diplomasi|dışişleri|nato|ab|avrupa/i.test(source)) return "🌐";
        if (/sanayi|teknoloji|tübitak|savunma sanayii/i.test(source)) return "⚙️";
        if (/sivil toplum|barolar|sendika|oda/i.test(source)) return "🤝";
        if (/kaza|kadı/i.test(source)) return "⚖️";
        if (/fetva|şeyhülislam/i.test(source)) return "📜";
        if (/sadaret|sadrazam|divan/i.test(source)) return "🏛️";
        if (/hazine|maliye|darphane|defterdar|gümrük/i.test(source)) return "🪙";
        if (/serhat|ordu|asker|donanma|kale/i.test(source)) return "⚔️";
        if (/esnaf|lonca|ahi|çarşı/i.test(source)) return "🔨";
        if (/vakıf|darüşşifa|cami|imar/i.test(source)) return "🕌";
        if (/tahrir|reaya|köylü/i.test(source)) return "🌾";
        return "✦";
      }

      getCharacterIcon(id) {
        // Modern roller
        if (/cumhurbaskani|basbakan/i.test(id)) return "🏛️";
        if (/icisleri|emniyet/i.test(id)) return "👮";
        if (/genelkurmay|savunma/i.test(id)) return "🎖️";
        if (/hazine|merkez_bankasi|ticaret|tusiad/i.test(id)) return "🪙";
        if (/tbmm|milletvekili/i.test(id)) return "🏛️";
        if (/saglik/i.test(id)) return "🩺";
        if (/afad/i.test(id)) return "🚨";
        if (/sehir_plancisi|cevre_sehircilik/i.test(id)) return "🏗️";
        if (/sanayi/i.test(id)) return "⚙️";
        if (/goc_idaresi/i.test(id)) return "🛂";
        if (/esnaf/i.test(id)) return "🛒";
        if (/tuketici/i.test(id)) return "👥";

        // Klasik Osmanlı rolleri
        if (/kadi|hakim/i.test(id)) return "⚖️";
        if (/padisah|hukumdar|sultan/i.test(id)) return "👑";
        if (/sadrazam|vezir/i.test(id)) return "📜";
        if (/seyhulislam|muftu|imam/i.test(id)) return "🕌";
        if (/yeniceri|sipahi|asker|muhafiz|serdar|dizdar/i.test(id)) return "⚔️";
        if (/tuccar|sarraf|kuyumcu|bezirgan/i.test(id)) return "🪙";
        if (/ciftci|koylu|reaya|coban/i.test(id)) return "🌾";
        if (/tabip|hekim|cerrah/i.test(id)) return "🩺";
        if (/mimar|muhendis/i.test(id)) return "📐";
        if (/lonca|ahi|usta|debbag/i.test(id)) return "🔨";
        if (/elci|sefir|banker/i.test(id)) return "🌐";
        return "👤";
      }

      getRoleCategory(id) {
        // Modern kurumlar
        if (/icisleri_bakani/i.test(id)) return "İçişleri & Emniyet";
        if (/adli_yargi|anayasa_mahkemesi|adalet_bakani/i.test(id)) return "Yüksek Yargı & Adalet";
        if (/genelkurmay|savunma_bakani/i.test(id)) return "Milli Savunma & TSK";
        if (/diplomat/i.test(id)) return "Hariciye & Diplomasi";
        if (/cumhurbaskani/i.test(id)) return "Cumhurbaşkanlığı";
        if (/basbakan/i.test(id)) return "Başbakanlık & Hükümet";
        if (/afad_baskani/i.test(id)) return "Afet & Acil Durum";
        if (/hazine_bakani/i.test(id)) return "Maliye & Hazine";
        if (/merkez_bankasi/i.test(id)) return "Merkez Bankası";
        if (/tbmm_baskani/i.test(id)) return "Yasama & Meclis";
        if (/milletvekili/i.test(id)) return "TBMM Grubu";
        if (/tusiad_baskani/i.test(id)) return "İş Dünyası & Reel Sektör";
        if (/sehir_plancisi/i.test(id)) return "Şehircilik & Mimarlık";
        if (/goc_idaresi/i.test(id)) return "Sınır & Göç İdaresi";
        if (/savunma_sanayii/i.test(id)) return "Milli Teknoloji & Savunma";
        if (/saglik_bakani/i.test(id)) return "Halk Sağlığı";
        if (/esnaf_odasi/i.test(id)) return "Esnaf & Sanatkârlar";
        if (/cevre_sehircilik/i.test(id)) return "Çevre & Şehircilik";
        if (/ticaret_bakani/i.test(id)) return "Ticaret & Piyasa";
        if (/tuketici_dernekleri/i.test(id)) return "Sivil Toplum & Tüketici";
        if (/sanayi_bakani/i.test(id)) return "Sanayi & Teknoloji";

        // Klasik Osmanlı kurumları
        if (/kadi|hakim|kassam|mufettis/i.test(id)) return "İlmiye & Kaza";
        if (/padisah|hukumdar/i.test(id)) return "Hânedân-ı Âl-i Osman";
        if (/sadrazam|vezir|defterdar|nisanci|reisulkuttab|katip/i.test(id)) return "Kalemiye & Sadaret";
        if (/seyhulislam|muftu|imam/i.test(id)) return "Fetvahane & Din";
        if (/yeniceri|sipahi|asker|serdar|dizdar|levend/i.test(id)) return "Seyfiye & Ordu";
        if (/tuccar|sarraf|kuyumcu/i.test(id)) return "Bezirgân & Ticaret";
        if (/ciftci|koylu|reaya|coban/i.test(id)) return "Reaya & Üretici";
        if (/tabip|hekim|cerrah/i.test(id)) return "Tababet & Sıhhat";
        if (/lonca|ahi|usta|debbag|firinci/i.test(id)) return "Ahi & Lonca";
        if (/elci|sefir|banker/i.test(id)) return "Hariciye & Diplomasi";
        return "Mülk Tebası";
      }

      renderCharacterStage(characters) {
        const stage = document.getElementById("characterStage");
        if (!stage) return;
        stage.innerHTML = "";

        if (!Array.isArray(characters) || characters.length === 0) {
          stage.style.display = "none";
          return;
        }

        stage.style.display = "flex";

        characters.forEach(ch => {
          const card = document.createElement("div");
          card.className = "character-card";
          
          const icon = this.getCharacterIcon(ch.id);
          const roleCat = this.getRoleCategory(ch.id);

          card.innerHTML = `
            <div class="char-avatar-frame">
              <img class="char-avatar-img" src="assets/characters/${ch.id}.png" alt="${ch.name}" 
                   onerror="if (!this.dataset.triedJpg) { this.dataset.triedJpg = '1'; this.src = 'assets/characters/${ch.id}.jpg'; } else { this.style.display='none'; this.nextElementSibling.style.display='flex'; }">
              <div class="char-avatar-fallback" style="display:none;">${icon}</div>
            </div>
            <div class="char-info">
              <span class="char-name">${ch.name}</span>
              <span class="char-role-tag">${roleCat}</span>
            </div>
          `;
          stage.appendChild(card);
        });
      }

      renderOptions(options) {
        const stack = document.getElementById("optionsStack");
        if (!stack) return;
        stack.innerHTML = "";

        const isModern = this.currentMode === "modern";
        const strategyBadges = isModern ? [
          { icon: "⚖️", title: "Hukuki Yaptırım", tagClass: "badge-adli" },
          { icon: "🤝", title: "Uzlaşı & Sulh", tagClass: "badge-sulh" },
          { icon: "🪙", title: "Mali & İktisadi Karar", tagClass: "badge-mali" },
          { icon: "🛡️", title: "Kamu Otoritesi", tagClass: "badge-otorite" },
          { icon: "📜", title: "Mevzuat & Reform", tagClass: "badge-nizam" }
        ] : [
          { icon: "⚖️", title: "Şer'i Hüküm", tagClass: "badge-adli" },
          { icon: "🤝", title: "Maslahat & Sulh", tagClass: "badge-sulh" },
          { icon: "🪙", title: "Mali Tedbir", tagClass: "badge-mali" },
          { icon: "⚔️", title: "Sert Otorite", tagClass: "badge-otorite" },
          { icon: "📜", title: "Nizamnâme", tagClass: "badge-nizam" }
        ];

        const statNames = isModern ? {
          justice: "Adalet",
          people: "Halk",
          treasury: "Hazine",
          military: "Güvenlik",
          authority: "Otorite"
        } : {
          justice: "Adalet",
          people: "Reaya",
          treasury: "Hazine",
          military: "Ordu",
          authority: "Mülk"
        };

        const strategyKeys = ["adli", "sulh", "mali", "otorite", "nizam"];

        options.forEach((opt, idx) => {
          opt.index = idx;
          const sKey = strategyKeys[idx % strategyKeys.length];
          opt.strategyKey = sKey;
          const badge = strategyBadges[idx % strategyBadges.length];
          const btn = document.createElement("button");
          btn.className = "choice-btn";

          let chipsHtml = "";
          if (opt.effects) {
            for (const [key, val] of Object.entries(opt.effects)) {
              if (val !== 0) {
                const isPos = val > 0;
                const sign = isPos ? "+" : "";
                const tagClass = isPos ? "pos" : "neg";
                const label = statNames[key] || key.toUpperCase();
                chipsHtml += `<span class="delta-tag ${tagClass}">${label} ${sign}${val}</span>`;
              }
            }
          }

          btn.innerHTML = `
            <div class="choice-top">
              <span class="strategy-badge ${badge.tagClass}">${badge.icon} ${badge.title}</span>
            </div>
            <span class="choice-label">${opt.label}</span>
            <div class="preview-chips">${chipsHtml}</div>
          `;

          btn.onclick = () => this.applyChoice(opt, btn);
          stack.appendChild(btn);
        });
      }

      log(msg) {
        const entries = document.getElementById("chronicleEntries");
        const box = document.getElementById("chronicleBox");
        if (entries) {
          entries.innerHTML = `<div>✦ <b>Sene ${this.turn}:</b> ${msg}</div>` + entries.innerHTML;
        } else if (box) {
          box.innerHTML = `<div>✦ <b>Sene ${this.turn}:</b> ${msg}</div>` + box.innerHTML;
        }
      }

      applyChoice(choice, btnElement) {
        if (this.isGameOver) return;
        soundFX.playGong();

        // 1. Karakter / Meşrep Puanını Artır
        if (choice.strategyKey && this.rulerTraits && this.rulerTraits[choice.strategyKey] !== undefined) {
          this.rulerTraits[choice.strategyKey]++;
        }

        // 2. Sayısal Etkiler & Uçan Sayı Efekti (Floating Deltas)
        let hasCriticalDrop = false;

        if (choice.effects) {
          for (let key in choice.effects) {
            const delta = choice.effects[key];
            if (delta !== 0) {
              this.stats[key] = this.clamp(this.stats[key] + delta);
              this.spawnFloater(btnElement, key, delta);
              if (this.stats[key] < 30) hasCriticalDrop = true;
            }
          }
        }

        if (choice.log) {
          this.log(choice.log);
        }
        this.turn++;

        // 2. Dâire-i Adliyye Geri Besleme Döngüsü (Feedback Loop)
        if (this.currentMode === "modern") {
          if (this.stats.justice < 35) {
            this.stats.people = this.clamp(this.stats.people - 5);
            this.log("<span style='color:var(--danger)'>Hukuka güven azaldığı için sermaye çıkışı ve beyin göçü hızlandı!</span>");
          }
          if (this.stats.treasury < 30) {
            this.stats.authority = this.clamp(this.stats.authority - 6);
            this.log("<span style='color:var(--danger)'>Döviz krizi ve bütçe açığı siyasi istikrara ağır darbe vurdu!</span>");
          }
        } else {
          if (this.stats.justice < 35) {
            this.stats.people = this.clamp(this.stats.people - 6);
            this.log("<span style='color:var(--danger)'>Adaletsizlik yüzünden reaya çiftini çubuğunu terk ediyor!</span>");
          }
          if (this.stats.treasury < 30) {
            this.stats.military = this.clamp(this.stats.military - 8);
            this.log("<span style='color:var(--danger)'>Ulufe geciktiği için kapıkulunda isyan fısıltıları arttı!</span>");
          }
        }

        // 3. Kritik Eşik Efektleri
        if (hasCriticalDrop) {
          soundFX.playWarning();
          this.triggerScreenShake();
        }

        // 4. Veritabanına Hükmü ve İlerlemeyi Kaydet (API üzerinden)
        if (this.isApiAvailable) {
          const choiceLabel = choice.label || "";
          const effects = choice.effects || {};
          const logText = choice.log || "";
          const reasonEl = document.getElementById("goReason");
          const gameOverReason = this.isGameOver ? (reasonEl ? reasonEl.innerText : "Mülk nizamı muhafaza edilemedi.") : "";

          fetch("api/game.php?action=save_answer", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({
              era: this.currentMode,
              event_id: this.currentEvent ? this.currentEvent.id : "",
              turn_number: this.turn - 1,
              choice_index: choice.index !== undefined ? choice.index : 0,
              choice_label: choiceLabel,
              effects: effects,
              log: logText,
              stats: this.stats,
              traits: this.rulerTraits,
              is_game_over: this.isGameOver,
              game_over_reason: gameOverReason
            })
          }).catch(err => console.warn("Save answer error:", err));
        }

        this.checkGameOver();
        this.updateUI();

        if (!this.isGameOver) {
          if (btnElement) {
            btnElement.classList.add("choice-btn-selected");
          }
          // 1. Seçim yapıldıktan sonra sayfayı derhal olay kutusunun başına götür
          this.scrollToEventBox();

          // 2. Sayfa olay kutusunun başına yöneldikten sonra yeni olayı yükle ve kutuyu vurgula
          setTimeout(() => {
            this.nextEvent(true);
          }, 240);
        }
      }

      // Sayfayı olay kutusunun başına pürüzsüzce kaydır
      scrollToEventBox() {
        const targetEl = document.getElementById("eventDossier") || document.getElementById("cardPanel");
        if (targetEl) {
          const rect = targetEl.getBoundingClientRect();
          const scrollTop = window.pageYOffset || document.documentElement.scrollTop;
          // Üstten 18px ferah pay bırakarak kaydır
          const targetY = Math.max(0, rect.top + scrollTop - 18);
          window.scrollTo({
            top: targetY,
            behavior: "smooth"
          });
        }
      }

      // Uçan Sayı Efekti (Floating Text)
      spawnFloater(targetEl, statKey, delta) {
        if (!targetEl) return;
        const rect = targetEl.getBoundingClientRect();
        const floater = document.createElement("div");
        floater.className = "delta-floater";
        
        const isPos = delta > 0;
        floater.style.color = isPos ? "var(--success)" : "var(--danger)";
        
        const isModern = this.currentMode === "modern";
        const statNames = isModern ? {
          justice: "ADALET",
          people: "HALK",
          treasury: "HAZİNE",
          military: "GÜVENLİK",
          authority: "OTORİTE"
        } : {
          justice: "ADALET",
          people: "REAYA",
          treasury: "HAZİNE",
          military: "ORDU",
          authority: "MÜLK"
        };
        const label = statNames[statKey] || statKey.toUpperCase();
        floater.innerText = `${isPos ? "+" : ""}${delta} ${label}`;

        // Butonun üzerine rastgele hafif ofsetle yerleştir
        const x = rect.left + rect.width / 2 + (Math.random() * 80 - 40);
        const y = rect.top + window.scrollY;

        floater.style.left = `${x}px`;
        floater.style.top = `${y}px`;

        document.body.appendChild(floater);
        setTimeout(() => floater.remove(), 1200);
      }

      triggerScreenShake() {
        const screen = document.getElementById("gameScreen");
        if (!screen) return;
        screen.classList.remove("shake-screen");
        void screen.offsetWidth; // Reflow tetikle
        screen.classList.add("shake-screen");
        setTimeout(() => screen.classList.remove("shake-screen"), 450);
      }

      checkGameOver() {
        let reason = "";
        if (this.currentMode === "modern") {
          if (this.stats.justice <= 0) {
            reason = "Hukukun üstünlüğü ve adalet mekanizması tamamen çöktü. Toplumsal güven sıfırlandı ve anayasal düzen sarsıldı.";
          } else if (this.stats.people <= 0) {
            reason = "Halkın geçim ve refah düzeyi tükendi. Enflasyon ve hayat pahalılığı kitleleri sokaklara döktü; toplumsal barış kayboldu.";
          } else if (this.stats.treasury <= 0) {
            reason = "Hazine ve Merkez Bankası rezervleri tükendi. Ağır kur şoku ve ödemeler dengesi krizi ile ekonomi iflas etti.";
          } else if (this.stats.military <= 0) {
            reason = "Güvenlik ve savunma zafiyeti baş gösterdi. Sınır güvenliği ve kamu düzeni tamamen kaybedildi.";
          } else if (this.stats.authority <= 0) {
            reason = "Devlet otoritesi ve yürütme erki işlevsiz kaldı. Hükümet meşruiyetini yitirdi ve erken seçime gidilmek zorunda kalındı.";
          }
        } else {
          if (this.stats.justice <= 0) {
            reason = "Adalet mülkün temelidir düsturu çiğnendi. Zulüm ayyuka çıktı, reaya ve ordu sarayı bastı.";
          } else if (this.stats.people <= 0) {
            reason = "Reaya kalmadı; köyler boşaldı, tarlalar kurudu. Devleti besleyecek tek bir üretici nefer kalmadı.";
          } else if (this.stats.treasury <= 0) {
            reason = "Hazine tamtakır oldu. Devlet iflas etti, asker maaş alamayınca payitaht yağmalandı.";
          } else if (this.stats.military <= 0) {
            reason = "Asker itaatten çıktı; kazanlar devrildi, serhat boyları düşman ordularına teslim oldu.";
          } else if (this.stats.authority <= 0) {
            reason = "Hükümdarın otoritesi sıfırlandı; ayânlar ve vezirler mülkü parçalayarak tahtı devirdi.";
          }
        }

        if (reason) {
          this.isGameOver = true;
          soundFX.playDoom();
          this.triggerScreenShake();
          const reasonEl = document.getElementById("goReason");
          if (reasonEl) reasonEl.innerText = reason;
          const modalEl = document.getElementById("gameOverModal");
          if (modalEl) modalEl.style.display = "flex";
        }
      }

      getEventCategoryTag(ev) {
        if (!ev) return "";
        const s = ((ev.source || "") + " " + (ev.title || "") + " " + (ev.desc || "")).toLowerCase();
        if (this.currentMode === "modern") {
          if (/deprem|afad|sel |yangın|maden|afet|kızılay/i.test(s)) return "🚨 AFET & ACİL DURUM";
          if (/terör|tsk|operasyon|mehmetçik|asker|emniyet|kom |tem |mit |jandarma|savunma sanayii|darbe/i.test(s)) return "🛡️ GÜVENLİK & ASAYİŞ";
          if (/enflasyon|faiz|döviz|kur |imf|banka|hazine|maliye|borsa|bütçe|vergi|ihracat/i.test(s)) return "🪙 İKTİSAT & MALİYE";
          if (/yargı|dgm|anayasa|danıştay|yargıtay|mahkeme|savcılık|hukuk|yolsuzluk|susurluk/i.test(s)) return "⚖️ HUKUK & YARGI";
          if (/ab |diplomat|dışişleri|kıbrıs|nato|uluslararası|zengezur|kalkınma yolu/i.test(s)) return "🌐 DIŞ POLİTİKA";
          if (/sendika|grev|işçi|sağlık|eğitim|sanat|kültür|çevre|sinema/i.test(s)) return "👥 TOPLUM & KÜLTÜR";
          return "🇹🇷 DEVLET BRİFİNGİ";
        } else {
          if (/fetva|şeyhülislam|şeriat/i.test(s)) return "📜 FETVA & ŞER'İAT";
          if (/kadı|mahkeme|kaza|kassam|müfettiş/i.test(s)) return "⚖️ İLMİYE & KAZA";
          if (/hazine|akçe|defterdar|darphane|cibayet/i.test(s)) return "🪙 HAZİNE & MALİYE";
          if (/yeniçeri|ordu|serhat|donanma|kale|sipahi/i.test(s)) return "⚔️ SEYFİYE & SERHAT";
          if (/reaya|çiftçi|vergi|aşar|salgun/i.test(s)) return "🌾 REAYA & İNTİZAM";
          return "👑 DÎVÂN-I HÜMÂYÛN";
        }
      }

      // Sıradaki Olayı Çek (Veritabanından Tek Tek veya Yerel Desteden)
      async nextEvent(isVerdictTransition = false) {
        let ev = null;

        // 1. API aktifse veritabanından tekil olay çek
        if (this.isApiAvailable) {
          try {
            const crisisKey = this.deckManager ? this.deckManager.identifyCrisis(this.stats) : null;
            const excludeParam = this.currentEvent ? `&exclude_id=${encodeURIComponent(this.currentEvent.id)}` : '';
            const crisisParam = crisisKey ? `&crisis_key=${encodeURIComponent(crisisKey)}` : '';
            const resp = await fetch(`api/events.php?action=next&era=${this.currentMode}${crisisParam}${excludeParam}`);
            if (resp.ok) {
              const data = await resp.json();
              if (data.success && data.event) {
                ev = data.event;
                this.apiPlayedCount = data.played_count || 0;
                this.apiTotalCount = data.total_count || 0;
              }
            }
          } catch (e) {
            console.warn("API nextEvent hatası, yerel desteye geçiliyor:", e);
          }
        }

        // 2. API çevrimdışıysa yerel desteden çek
        if (!ev && this.deckManager) {
          ev = this.deckManager.drawNext(this.stats);
        }

        if (!ev) return;
        this.currentEvent = ev;

        const sourceTextEl = document.getElementById("sourceText");
        const eventSourceEl = document.getElementById("eventSource");
        if (sourceTextEl) sourceTextEl.innerText = ev.source || "Dîvân-ı Hümâyûn Maruzu";
        else if (eventSourceEl) eventSourceEl.innerText = ev.source || "Dîvân-ı Hümâyûn Maruzu";

        const sourceIconEl = document.getElementById("sourceIcon");
        if (sourceIconEl) sourceIconEl.innerText = this.getSourceIcon(ev.source);

        const badgeEl = document.getElementById("eventBadge");
        if (badgeEl) {
          const vNum = this.isApiAvailable ? (this.apiPlayedCount + 1) : (this.deckManager.playedCount + 1);
          badgeEl.innerText = `Vaka #${String(vNum).padStart(3, '0')}`;
        }

        const catBadgeEl = document.getElementById("eventCategoryBadge");
        if (catBadgeEl) {
          catBadgeEl.innerText = this.getEventCategoryTag(ev);
        }

        const sealIconEl = document.getElementById("eventSealIcon");
        if (sealIconEl) {
          sealIconEl.innerText = this.getSourceIcon(ev.source);
        }

        const titleEl = document.getElementById("eventTitle");
        const descEl = document.getElementById("eventDesc");
        if (titleEl) titleEl.innerText = ev.title;
        if (descEl) descEl.innerText = ev.desc;

        this.renderCharacterStage(ev.characters);
        this.renderOptions(ev.options);

        this.updateDeckCounter();

        // Bir olaya hüküm verildikten sonra yeni olay kutusunu ışıltı ve nabızla vurgula
        const dossierBox = document.getElementById("eventDossier");
        if (dossierBox && isVerdictTransition) {
          dossierBox.classList.remove("highlight-event-pulse");
          void dossierBox.offsetWidth; // CSS animasyonunu yeniden tetiklemek için reflow zorla
          dossierBox.classList.add("highlight-event-pulse");
          setTimeout(() => {
            if (dossierBox) dossierBox.classList.remove("highlight-event-pulse");
          }, 1100);
        }
      }

      // Kayıtlı İlerlemeyi Kontrol Et
      async checkSavedProgress() {
        if (!this.isApiAvailable) return;
        try {
          const resp = await fetch(`api/game.php?action=progress&era=${this.currentMode}`);
          if (resp.ok) {
            const data = await resp.json();
            if (data.success && data.has_progress && data.progress) {
              const p = data.progress;
              if (!p.is_game_over && p.turn_number > 1) {
                this.savedProgressData = data;
                const banner = document.getElementById("resumeBanner");
                const textEl = document.getElementById("resumeText");
                if (banner && textEl) {
                  const sName = this.currentMode === "modern" ? "Yıl" : "Sene";
                  textEl.innerHTML = `Kaydedilmiş oturumunuz bulundu: <b>${sName} ${p.turn_number}</b> (Adalet: ${p.stats.justice}, Hazine: ${p.stats.treasury})`;
                  banner.style.display = "flex";
                }
                return;
              }
            }
          }
        } catch (e) {}
      }

      // Kayıtlı İlerlemeyi Yükle ve Devam Et
      resumeSavedProgress() {
        const banner = document.getElementById("resumeBanner");
        if (banner) banner.style.display = "none";

        if (!this.savedProgressData || !this.savedProgressData.progress) return;
        const p = this.savedProgressData.progress;
        this.stats = { ...p.stats };
        this.turn = p.turn_number;
        if (p.traits) this.rulerTraits = { ...p.traits };
        this.isGameOver = !!p.is_game_over;

        // Geçmiş kronik loglarını yükle
        if (Array.isArray(this.savedProgressData.recent_logs) && this.savedProgressData.recent_logs.length > 0) {
          const entries = document.getElementById("chronicleEntries");
          if (entries) {
            entries.innerHTML = "";
            this.savedProgressData.recent_logs.forEach(l => {
              entries.innerHTML = `<div>✦ <b>Sene ${l.turn_number}:</b> ${l.log_text}</div>` + entries.innerHTML;
            });
          }
        }

        this.updateUI();
        this.nextEvent();
        this.log(`💾 Veritabanındaki oturum yüklendi. ${this.currentMode === "modern" ? "Yıl" : "Sene"} ${this.turn} üzerinden devlete hükmediliyor.`);
      }

      // Kayıtlı İlerlemeyi Reddet ve Sıfırla
      async dismissSavedProgress() {
        const banner = document.getElementById("resumeBanner");
        if (banner) banner.style.display = "none";
        this.savedProgressData = null;

        if (this.isApiAvailable) {
          try {
            await fetch(`api/game.php?action=reset_progress&era=${this.currentMode}`, { method: "POST" });
          } catch (e) {}
        }

        this.restart();
      }

      updateDeckCounter() {
        const counterEl = document.getElementById("deckCounter");
        if (counterEl) {
          if (this.isApiAvailable && this.apiTotalCount > 0) {
            const played = this.apiPlayedCount || (this.turn - 1);
            counterEl.innerText = `Vaka: ${played + 1} / ${this.apiTotalCount}`;
          } else {
            const rem = this.deckManager.remainingCount;
            const total = this.deckManager.totalCount;
            const played = this.deckManager.playedCount;
            const cycle = this.deckManager.cycle;
            counterEl.innerText = `Kalan: ${rem}/${total} | Hüküm: ${played}${cycle > 1 ? ` (Devir ${cycle})` : ""}`;
          }
        }
      }

      restart() {
        soundFX.playGong();
        this.stats = {
          justice: 60,
          people: 60,
          treasury: 50,
          military: 55,
          authority: 60
        };
        this.rulerTraits = {
          adli: 0,
          sulh: 0,
          mali: 0,
          otorite: 0,
          nizam: 0
        };
        this.turn = 1;
        this.isGameOver = false;

        if (this.isApiAvailable) {
          fetch(`api/game.php?action=reset_progress&era=${this.currentMode}`, { method: "POST" })
            .catch(e => console.warn("Reset progress error:", e));
        }

        if (this.deckManager) {
          this.deckManager.reset();
        }

        const modalEl = document.getElementById("gameOverModal");
        if (modalEl) modalEl.style.display = "none";

        const entries = document.getElementById("chronicleEntries");
        if (entries) {
          entries.innerHTML = `<div>✦ <b>Sene 1:</b> ${this.currentMode === "modern" ? "Cumhuriyet nizamı yeniden tesis edildi. Sene 1'den başlanıyor." : "Yeni bir hükümdar cülus etti. Adalet çarkı yeniden dönüyor."}</div>`;
        }

        this.updateUI();
        this.nextEvent();
      }

      updateUI() {
        const reignBadge = document.getElementById("reignBadge");
        if (reignBadge) {
          reignBadge.innerText = this.currentMode === "modern" ? 
            `Hükümet Yılı: ${this.turn}` : 
            `Cülûs Yılı: ${this.turn}`;
        }
        
        const keys = ["justice", "people", "treasury", "military", "authority"];
        keys.forEach(k => {
          const val = this.stats[k];
          const elVal = document.getElementById(`val-${k}`);
          const chip = document.getElementById(`chip-${k}`);
          const bar = document.getElementById(`bar-${k}`);
          
          if (elVal) elVal.innerText = val;
          if (bar) {
            bar.style.width = `${val}%`;
            bar.className = "stat-bar-fill";
            if (val >= 55) bar.classList.add("healthy");
            else if (val >= 35) bar.classList.add("warning");
            else bar.classList.add("critical");
          }

          if (chip) {
            if (val < 30) chip.classList.add("critical");
            else chip.classList.remove("critical");
          }
        });

        // 5 Sütunun Genel Muvazenesi / İstikrar Endeksi Hesabı
        const avg = (this.stats.justice + this.stats.people + this.stats.treasury + this.stats.military + this.stats.authority) / 5;
        const eqScoreEl = document.getElementById("eqScore");
        const eqFillEl = document.getElementById("eqFill");
        if (eqFillEl && eqScoreEl) {
          eqFillEl.style.width = `${Math.min(100, Math.max(0, avg))}%`;
          eqFillEl.className = "eq-fill";
          const isModern = this.currentMode === "modern";
          if (avg >= 70) {
            eqScoreEl.innerText = `%${Math.round(avg)} • ${isModern ? "Yüksek İstikrar" : "Âbâd & Mükemmel"}`;
            eqScoreEl.style.color = "var(--success)";
          } else if (avg >= 48) {
            eqScoreEl.innerText = `%${Math.round(avg)} • ${isModern ? "Dengeli Yönetim" : "Muvazeneli & Dengeli"}`;
            eqScoreEl.style.color = "var(--gold-bright)";
          } else if (avg >= 30) {
            eqFillEl.classList.add("warning");
            eqScoreEl.innerText = `%${Math.round(avg)} • ${isModern ? "Hassas Denge" : "Tehlike Eşiği"}`;
            eqScoreEl.style.color = "#f59e0b";
          } else {
            eqFillEl.classList.add("critical");
            eqScoreEl.innerText = `%${Math.round(avg)} • ${isModern ? "Kriz & Bunalım!" : "Fetret Tehlikesi!"}`;
            eqScoreEl.style.color = "var(--danger)";
          }
        }

        this.updatePersonalityCard();
        this.updateDeckCounter();
      }

      updatePersonalityCard() {
        const isModern = this.currentMode === "modern";
        const traits = this.rulerTraits || { adli: 0, sulh: 0, mali: 0, otorite: 0, nizam: 0 };
        const total = (traits.adli || 0) + (traits.sulh || 0) + (traits.mali || 0) + (traits.otorite || 0) + (traits.nizam || 0);

        // 1. Başlık & İkon & Karar Sayacı
        const personaIconEl = document.getElementById("personaIcon");
        const personaTitleLabelEl = document.getElementById("personaTitleLabel");
        const personaTotalDecisionsEl = document.getElementById("personaTotalDecisions");
        const personaArchetypeEl = document.getElementById("personaArchetype");

        if (personaIconEl) personaIconEl.innerText = isModern ? "🏛️" : "👑";
        if (personaTitleLabelEl) personaTitleLabelEl.innerText = isModern ? "LİDERLİK PROFİLİ & ÜSLUP" : "HÜKÜMDAR ŞAHSİYETİ";
        if (personaTotalDecisionsEl) personaTotalDecisionsEl.innerText = `${total} Karar`;

        // 2. Trait Tanımları (Osmanlı vs Modern)
        const traitDefs = {
          adli: {
            icon: "⚖️",
            ottoman: "Şer'i Adalet",
            modern: "Hukuk & Adalet"
          },
          sulh: {
            icon: "🤝",
            ottoman: "Sulh & Maslahat",
            modern: "Uzlaşı & Diyalog"
          },
          mali: {
            icon: "🪙",
            ottoman: "Mali Basiret",
            modern: "Mali Disiplin"
          },
          otorite: {
            icon: isModern ? "🛡️" : "⚔️",
            ottoman: "Sert Otorite",
            modern: "Kamu Düzeni"
          },
          nizam: {
            icon: "📜",
            ottoman: "Nizam & Ferman",
            modern: "Mevzuat & Reform"
          }
        };

        const keys = ["adli", "sulh", "mali", "otorite", "nizam"];

        // 3. Tablo Satırlarını Güncelle
        keys.forEach(k => {
          const count = traits[k] || 0;
          const pct = total > 0 ? Math.round((count / total) * 100) : 20;

          const nameEl = document.getElementById(`traitName-${k}`);
          const countEl = document.getElementById(`traitCount-${k}`);
          const fillEl = document.getElementById(`traitFill-${k}`);
          const pctEl = document.getElementById(`traitPct-${k}`);
          const rowEl = document.getElementById(`row-${k}`);

          if (nameEl) nameEl.innerText = isModern ? traitDefs[k].modern : traitDefs[k].ottoman;
          if (rowEl) {
            const iconEl = rowEl.querySelector(".trait-icon");
            if (iconEl) iconEl.innerText = traitDefs[k].icon;
          }
          if (countEl) countEl.innerText = count;
          if (fillEl) fillEl.style.width = `${pct}%`;
          if (pctEl) pctEl.innerText = `%${pct}`;
        });

        // 4. Hükümdar / Lider Karakter Şahsiyeti (Dominant Archetype)
        if (personaArchetypeEl) {
          if (total === 0) {
            personaArchetypeEl.innerText = isModern ? "✦ Dengeli Devlet Adamı" : "✦ Muvazene Kutbu (Dengeli)";
            return;
          }

          // Çoktan aza sırala
          const sorted = [...keys].sort((a, b) => (traits[b] || 0) - (traits[a] || 0));
          const topKey = sorted[0];
          const secondKey = sorted[1];

          // İlk iki eşit ise birleşik unvan
          const isTied = (traits[topKey] === traits[secondKey]) && traits[topKey] > 0;

          if (isTied) {
            const pairKey = [topKey, secondKey].sort().join("+");
            const titlesOttoman = {
              "adli+sulh": "✦ Âdil & Sulhperver",
              "adli+mali": "✦ Âdil & İktisatçı Hakan",
              "adli+otorite": "✦ Yavuz-ı Âdil (Sert ve Âdil)",
              "adli+nizam": "✦ Kānûnî-i Sânî",
              "sulh+mali": "✦ Müşfik & Müdebbir",
              "sulh+otorite": "✦ İtidal & İrade Sahibi",
              "sulh+nizam": "✦ Sulh Meclisi Banisi",
              "mali+otorite": "✦ Demir Yumruklu Hazinedar",
              "mali+nizam": "✦ Defterhâne Müceddidi",
              "otorite+nizam": "✦ Devlet-i Ebed-Müddet Muhafızı"
            };
            const titlesModern = {
              "adli+sulh": "✦ Hukukçu & Demokrat Lider",
              "adli+mali": "✦ Şeffaf & Hesap Verebilir",
              "adli+otorite": "✦ Anayasal Disiplin Savunucusu",
              "adli+nizam": "✦ Kurumsal Hukukçu Reformist",
              "sulh+mali": "✦ Sosyal Piyasa Savunucusu",
              "sulh+otorite": "✦ Mutedil Kriz Yöneticisi",
              "sulh+nizam": "✦ Meşveretçi & Katılımcı",
              "mali+otorite": "✦ Mali Disiplinci Otoriter",
              "mali+nizam": "✦ Teknokrasist & Rasyonel İdareci",
              "otorite+nizam": "✦ Güçlü Devlet & Kurumsal Düzen"
            };

            const tiedDict = isModern ? titlesModern : titlesOttoman;
            if (tiedDict[pairKey]) {
              personaArchetypeEl.innerText = tiedDict[pairKey];
              return;
            }
          }

          const singleOttoman = {
            adli: "✦ Sultan-ı Âdil (Adaletperver)",
            sulh: "✦ Müşfik & Sulhperver Hakan",
            mali: "✦ Müdebbir Hazine Sahibi",
            otorite: "✦ Sahib-Kıran (Yavuz Meşrep)",
            nizam: "✦ Kānûnî & Nizamperver"
          };

          const singleModern = {
            adli: "✦ Hukuk Devleti Savunucusu",
            sulh: "✦ Uzlaşmacı & Meşveretçi Lider",
            mali: "✦ Rasyonel İktisatçı & Maliyeci",
            otorite: "✦ Güvenlikçi & Şahin İdareci",
            nizam: "✦ Kurumsal Reformist & Bürokrat"
          };

          personaArchetypeEl.innerText = isModern ? singleModern[topKey] : singleOttoman[topKey];
        }
      }

      restart() {
        this.stats = { justice: 60, people: 60, treasury: 50, military: 55, authority: 60 };
        this.rulerTraits = { adli: 0, sulh: 0, mali: 0, otorite: 0, nizam: 0 };
        this.turn = 1;
        this.isGameOver = false;
        this.deckManager.reset();
        document.getElementById("gameOverModal").style.display = "none";
        this.log(this.currentMode === "modern" ?
          "Yeni bir hükümet dönemi başladı. Kriz çekme destesi tekrarsız olarak yeniden karıştırıldı." :
          "Yeni bir cülûs ile mülk yeniden dirildi. Çekme destesi tekrarsız olarak yeniden karıştırıldı.");
        this.updateUI();
        this.nextEvent();
      }

      // ===============================================================
      // 4. ANIMASYONLU DÂİRE-İ ADLİYYE HUD ÇİZİMİ (Canvas 60 FPS)
      // ===============================================================
      startRenderLoop() {
        const render = () => {
          this.drawHUD();
          requestAnimationFrame(render);
        };
        requestAnimationFrame(render);
      }

      drawHUD() {
        const ctx = this.ctx;
        const w = this.canvas.width;
        const h = this.canvas.height;
        const cx = w / 2;
        const cy = h / 2;
        const radius = 200;

        ctx.clearRect(0, 0, w, h);
        this.angleOffset += 0.003; // Dönen usturlab açısı

        // Dış Usturlab Dişli Çemberi
        ctx.save();
        ctx.translate(cx, cy);
        ctx.rotate(this.angleOffset);
        ctx.beginPath();
        ctx.arc(0, 0, radius + 40, 0, Math.PI * 2);
        ctx.strokeStyle = "rgba(201, 151, 56, 0.15)";
        ctx.lineWidth = 1;
        ctx.stroke();

        // Astronomik Derece Çizgileri
        for (let a = 0; a < Math.PI * 2; a += Math.PI / 18) {
          const x1 = (radius + 34) * Math.cos(a);
          const y1 = (radius + 34) * Math.sin(a);
          const x2 = (radius + 44) * Math.cos(a);
          const y2 = (radius + 44) * Math.sin(a);
          ctx.beginPath();
          ctx.moveTo(x1, y1);
          ctx.lineTo(x2, y2);
          ctx.strokeStyle = "rgba(201, 151, 56, 0.25)";
          ctx.lineWidth = 1.5;
          ctx.stroke();
        }
        ctx.restore();

        // Ana Daire Yolu
        ctx.beginPath();
        ctx.arc(cx, cy, radius, 0, Math.PI * 2);
        ctx.strokeStyle = "rgba(255, 255, 255, 0.08)";
        ctx.lineWidth = 16;
        ctx.stroke();

        // 5 Metrik Düğümü (Adalet Çemberi)
        const isModern = this.currentMode === "modern";
        const nodes = [
          { key: "justice", name: "ADALET", val: this.stats.justice, angle: -Math.PI / 2 },
          { key: "people", name: isModern ? "HALK" : "REAYA", val: this.stats.people, angle: -Math.PI / 2 + (2 * Math.PI / 5) },
          { key: "treasury", name: "HAZİNE", val: this.stats.treasury, angle: -Math.PI / 2 + (4 * Math.PI / 5) },
          { key: "military", name: isModern ? "GÜVENLİK" : "ORDU", val: this.stats.military, angle: -Math.PI / 2 + (6 * Math.PI / 5) },
          { key: "authority", name: isModern ? "OTORİTE" : "MÜLK", val: this.stats.authority, angle: -Math.PI / 2 + (8 * Math.PI / 5) }
        ];

        // Yayları ve Enerji Akışını Çiz
        for (let i = 0; i < nodes.length; i++) {
          const next = (i + 1) % nodes.length;
          const avg = (nodes[i].val + nodes[next].val) / 2;

          ctx.beginPath();
          ctx.arc(cx, cy, radius, nodes[i].angle, nodes[next].angle);
          ctx.strokeStyle = avg < 32 ? "rgba(239, 68, 68, 0.7)" : "rgba(201, 151, 56, 0.4)";
          ctx.lineWidth = avg < 32 ? 6 : 4;
          ctx.stroke();
        }

        // Akış Yapan Parçacıklar (Particles)
        this.particles.forEach(p => {
          p.progress = (p.progress + p.speed) % 1;
          const curAngle = -Math.PI / 2 + p.progress * (Math.PI * 2);
          const px = cx + radius * Math.cos(curAngle);
          const py = cy + radius * Math.sin(curAngle);

          ctx.beginPath();
          ctx.arc(px, py, p.size, 0, Math.PI * 2);
          ctx.fillStyle = "rgba(243, 207, 122, 0.75)";
          ctx.shadowColor = "#f3cf7a";
          ctx.shadowBlur = 8;
          ctx.fill();
          ctx.shadowBlur = 0;
        });

        // Merkez: Yazı
        const avgTotal = (this.stats.justice + this.stats.people + this.stats.treasury + this.stats.military + this.stats.authority) / 5;
        ctx.fillStyle = avgTotal < 35 ? "#ef4444" : "#f3cf7a";
        ctx.font = isModern ? "bold 28px 'Cinzel', 'Outfit', sans-serif" : "bold 38px 'Amiri', 'Georgia', serif";
        ctx.textAlign = "center";
        ctx.textBaseline = "middle";
        ctx.shadowColor = avgTotal < 35 ? "rgba(239, 68, 68, 0.8)" : "rgba(201, 151, 56, 0.8)";
        ctx.shadowBlur = 16;
        ctx.fillText(isModern ? "ADALET" : "عَدْل", cx, cy - 8);
        ctx.shadowBlur = 0;

        ctx.font = "12px sans-serif";
        ctx.fillStyle = "#94a3b8";
        ctx.letterSpacing = "2px";
        ctx.fillText(isModern ? "MÜLKÜN TEMELİ" : "NİZÂM-I ÂLEM", cx, cy + 24);

        // Gezegen Düğümleri (Nodes)
        nodes.forEach(node => {
          const nx = cx + radius * Math.cos(node.angle);
          const ny = cy + radius * Math.sin(node.angle);
          const isCritical = node.val < 32;

          // Dış Işıma
          ctx.beginPath();
          ctx.arc(nx, ny, 28, 0, Math.PI * 2);
          ctx.fillStyle = isCritical ? "rgba(239, 68, 68, 0.2)" : "rgba(201, 151, 56, 0.15)";
          ctx.fill();

          // Düğüm Gövdesi
          ctx.beginPath();
          ctx.arc(nx, ny, 23, 0, Math.PI * 2);
          ctx.fillStyle = "#0d131f";
          ctx.fill();
          ctx.lineWidth = 2.5;
          ctx.strokeStyle = isCritical ? "#ef4444" : "#c99738";
          ctx.stroke();

          // Değer Yazısı
          ctx.fillStyle = "#ffffff";
          ctx.font = "bold 14px sans-serif";
          ctx.textAlign = "center";
          ctx.textBaseline = "middle";
          ctx.fillText(node.val, nx, ny - 3);

          // Etiket
          ctx.fillStyle = isCritical ? "#fca5a5" : "#cbd5e1";
          ctx.font = "9px sans-serif";
          ctx.fillText(node.name, nx, ny + 11);
        });
      }
    }

    // Kullanıcı Kimlik Arayüzü ve Uygulamayı Başlat
    const authUI = new AuthUI();
    window.authUI = authUI;

    const game = new DaireSimulation();
    window.game = game;
