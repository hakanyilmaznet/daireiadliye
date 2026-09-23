# -*- coding: utf-8 -*-
import urllib.request
import urllib.parse
import json

queries = [
    ("char_tusiad_baskani", "John Singer Sargent Portrait of Henry Lee Higginson"),
    ("char_tusiad_baskani", "John Singer Sargent Asher Wertheimer"),
    ("char_tusiad_baskani", "Philip de Laszlo George Eastman"),
    ("char_saglik_bakani", "Portrait of a Physician in His Library"),
    ("char_saglik_bakani", "Thomas Eakins Portrait of Dr"),
    ("char_sehir_plancisi", "Johann Baptist Lampi the Elder Portrait of the Architect La Tour"),
    ("char_sehir_plancisi", "Portrait of an architect oil painting"),
    ("char_esnaf_odasi_baskani", "Portrait of an artisan oil painting"),
    ("char_esnaf_odasi_baskani", "Portrait of a craftsman oil on canvas"),
    ("char_tuketici_dernekleri_baskani", "Portrait of a lawyer oil on canvas"),
    ("char_afad_baskani", "Portrait of a sea captain oil on canvas"),
    ("char_cevre_sehircilik_bakani", "Portrait of a surveyor oil on canvas"),
    ("char_cevre_sehircilik_bakani", "Portrait of a naturalist oil on canvas"),
    ("char_goc_idaresi_baskani", "Portrait of a port captain oil on canvas"),
    ("char_goc_idaresi_baskani", "Portrait of a customs officer oil on canvas"),
]

def search_commons(query):
    url = 'https://commons.wikimedia.org/w/api.php?action=query&list=search&srsearch=' + urllib.parse.quote(query + ' filetype:bitmap') + '&srnamespace=6&format=json'
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    try:
        with urllib.request.urlopen(req) as resp:
            data = json.loads(resp.read().decode('utf-8'))
            return [item['title'] for item in data.get('query', {}).get('search', [])[:2]]
    except:
        return []

for tag, q in queries:
    res = search_commons(q)
    print(f"{tag} [{q}]: {res}")
