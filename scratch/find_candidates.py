import json

with open('event_deck_modern.json', 'r', encoding='utf-8') as f:
    text = f.read().strip()
if text.startswith('const EVENT_DECK_MODERN ='):
    text = text[len('const EVENT_DECK_MODERN ='):].strip()
if text.endswith(';'):
    text = text[:-1].strip()

events = json.loads(text)

# Let's inspect events where specific characters would be much more appropriate:
# 1. Göç İdaresi Başkanı (char_goc_idaresi_baskani)
# 2. İş Dünyası / TÜSİAD Başkanı (char_tusiad_baskani)
# 3. Anayasa Mahkemesi Başkanı (char_anayasa_mahkemesi_baskani)
# 4. Sağlık Bakanı (char_saglik_bakani)
# 5. Savunma Sanayii Başkanı (char_savunma_sanayii_baskani)
# 6. Çevre ve Şehircilik Bakanı (char_cevre_sehircilik_bakani)

for i, ev in enumerate(events):
    title = ev['title']
    desc = ev['desc']
    chars = [c['id'] for c in ev['characters']]
    
    # Check if migration-related
    if any(k in title.lower() or k in desc.lower() for k in ['göçmen', 'mülteci', 'sığınmacı', 'geri gönderme', 'mobil göç', 'sınır duvarı', 'hudut', 'iltica']):
        if 'char_goc_idaresi_baskani' not in chars:
            print(f"[GÖÇ ADAYI] {ev['id']}: {title} | Şu anki: {chars}")

    # Check if TÜSİAD / Big Business / Employer / Privatization related
    if any(k in title.lower() or k in desc.lower() for k in ['tüsiad', 'holding', 'özel sektör', 'yabancı yatırım', 'özelleştir', 'tisk', 'asgari ücret tespit', 'kıdem tazminatı', 'işveren', 'borsa istanbul', 'bist', 'tüpraş', 'erdemir', 'telekom ihalesi']):
        if 'char_tusiad_baskani' not in chars:
            print(f"[TÜSİAD ADAYI] {ev['id']}: {title} | Şu anki: {chars}")
