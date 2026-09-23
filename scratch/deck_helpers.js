const fs = require('fs');
const path = require('path');

const charsRaw = JSON.parse(fs.readFileSync(path.join(__dirname, '..', 'characters_modern.json'), 'utf8'));
const charMap = {};
charsRaw.forEach(c => {
  charMap[c.id] = c.name;
});

function formatPreview(effects) {
  const statLabels = {
    justice: "Adalet",
    people: "Halk",
    treasury: "Hazine",
    military: "Güvenlik",
    authority: "Otorite"
  };
  const pos = [];
  const neg = [];
  ['justice', 'people', 'treasury', 'military', 'authority'].forEach(key => {
    const val = effects[key] || 0;
    if (val > 0) pos.push(`${statLabels[key]} +${val}`);
    else if (val < 0) neg.push(`${statLabels[key]} ${val}`);
  });
  if (pos.length > 0 && neg.length > 0) {
    return `${pos.join(', ')} | ${neg.join(', ')}`;
  } else if (pos.length > 0) {
    return pos.join(', ');
  } else if (neg.length > 0) {
    return neg.join(', ');
  }
  return "";
}

function createEvent(idNum, item) {
  const idStr = idNum < 10 ? `tr_vaka_00${idNum}` : (idNum < 100 ? `tr_vaka_0${idNum}` : `tr_vaka_${idNum}`);
  
  const char1Id = item.char1 || "char_cumhurbaskani";
  const char2Id = item.char2 || "char_adalet_bakani";

  const characters = [
    { id: char1Id, name: charMap[char1Id] || "Devlet Temsilcisi" },
    { id: char2Id, name: charMap[char2Id] || "Bürokrasi Temsilcisi" }
  ];

  const options = item.options.map(opt => ({
    label: opt.label,
    preview: formatPreview(opt.effects),
    effects: {
      justice: opt.effects.justice || 0,
      people: opt.effects.people || 0,
      treasury: opt.effects.treasury || 0,
      military: opt.effects.military || 0,
      authority: opt.effects.authority || 0
    },
    log: opt.log
  }));

  return {
    id: idStr,
    characters: characters,
    source: item.source,
    title: item.title,
    desc: item.desc,
    options: options
  };
}

module.exports = {
  charMap,
  formatPreview,
  createEvent
};
