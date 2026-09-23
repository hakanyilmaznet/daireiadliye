// Unit test for personality scoring and archetype calculation
const assert = require('assert');

// Simulate the logic from app.js
function calculatePersonality(traits, isModern) {
  const total = (traits.adli || 0) + (traits.sulh || 0) + (traits.mali || 0) + (traits.otorite || 0) + (traits.nizam || 0);
  const keys = ["adli", "sulh", "mali", "otorite", "nizam"];
  
  if (total === 0) {
    return {
      archetype: isModern ? "✦ Dengeli Devlet Adamı" : "✦ Muvazene Kutbu (Dengeli)",
      totalDecisions: 0,
      percentages: { adli: 20, sulh: 20, mali: 20, otorite: 20, nizam: 20 }
    };
  }

  const pcts = {};
  keys.forEach(k => {
    pcts[k] = Math.round(((traits[k] || 0) / total) * 100);
  });

  const sorted = [...keys].sort((a, b) => (traits[b] || 0) - (traits[a] || 0));
  const topKey = sorted[0];
  const secondKey = sorted[1];

  const isTied = (traits[topKey] === traits[secondKey]) && traits[topKey] > 0;

  let archetype = "";
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
      archetype = tiedDict[pairKey];
    }
  }

  if (!archetype) {
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
    archetype = isModern ? singleModern[topKey] : singleOttoman[topKey];
  }

  return { archetype, totalDecisions: total, percentages: pcts };
}

// 1. Initial State
const resInitOttoman = calculatePersonality({ adli: 0, sulh: 0, mali: 0, otorite: 0, nizam: 0 }, false);
assert.strictEqual(resInitOttoman.archetype, "✦ Muvazene Kutbu (Dengeli)");
assert.strictEqual(resInitOttoman.totalDecisions, 0);

const resInitModern = calculatePersonality({ adli: 0, sulh: 0, mali: 0, otorite: 0, nizam: 0 }, true);
assert.strictEqual(resInitModern.archetype, "✦ Dengeli Devlet Adamı");

// 2. Dominant Adli (Justice)
const resJustice = calculatePersonality({ adli: 5, sulh: 1, mali: 0, otorite: 1, nizam: 1 }, false);
assert.strictEqual(resJustice.archetype, "✦ Sultan-ı Âdil (Adaletperver)");
assert.strictEqual(resJustice.percentages.adli, 63);

// 3. Dominant Modern Fiscal
const resFiscal = calculatePersonality({ adli: 1, sulh: 0, mali: 6, otorite: 1, nizam: 0 }, true);
assert.strictEqual(resFiscal.archetype, "✦ Rasyonel İktisatçı & Maliyeci");

// 4. Tied Ottoman (adli + nizam)
const resTied = calculatePersonality({ adli: 4, sulh: 1, mali: 1, otorite: 0, nizam: 4 }, false);
assert.strictEqual(resTied.archetype, "✦ Kānûnî-i Sânî");

// 5. Dominant Otorite
const resOtorite = calculatePersonality({ adli: 0, sulh: 0, mali: 1, otorite: 7, nizam: 1 }, false);
assert.strictEqual(resOtorite.archetype, "✦ Sahib-Kıran (Yavuz Meşrep)");

console.log("All personality calculation tests passed successfully!");
