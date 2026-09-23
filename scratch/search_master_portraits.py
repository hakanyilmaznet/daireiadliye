# -*- coding: utf-8 -*-
"""
Search and find authentic public domain master portraits on Wikimedia Commons
for the remaining 12 modern Turkish characters.
"""

import urllib.request
import urllib.parse
import json

queries = {
    "char_hazine_bakani": ["Portrait of a financier oil on canvas", "Portrait of a banker oil on canvas", "Leon Maitre Henri Fantin-Latour"],
    "char_merkez_bankasi_baskani": ["Portrait of economist oil on canvas", "Portrait of scholar with glasses oil on canvas", "Portrait of gentleman with glasses oil on canvas"],
    "char_ticaret_bakani": ["Portrait of merchant oil on canvas 19th century", "Portrait of shipowner oil on canvas", "Portrait of trader oil on canvas"],
    "char_sanayi_bakani": ["Portrait of engineer oil on canvas", "Portrait of inventor oil on canvas", "Portrait of industrialist oil on canvas"],
    "char_tusiad_baskani": ["Portrait of industrialist Philip de Laszlo", "Portrait of gentleman pinstripe oil on canvas", "Portrait of tycoon oil on canvas"],
    "char_esnaf_odasi_baskani": ["Portrait of artisan oil on canvas", "Portrait of craftsman oil on canvas", "Portrait of shopkeeper oil on canvas"],
    "char_tuketici_dernekleri_baskani": ["Portrait of lawyer oil on canvas", "Portrait of writer with glasses oil on canvas", "Portrait of professor oil on canvas"],
    "char_afad_baskani": ["Portrait of commander in dark coat oil on canvas", "Portrait of captain oil on canvas", "Portrait of officer in overcoat oil on canvas"],
    "char_cevre_sehircilik_bakani": ["Portrait of statesman with map oil on canvas", "Portrait of surveyor oil on canvas", "Portrait of geographer oil on canvas"],
    "char_sehir_plancisi": ["Portrait of an architect oil on canvas", "Architect with blueprints oil on canvas", "Johann Baptist Lampi the Elder Portrait of the Architect La Tour"],
    "char_saglik_bakani": ["Portrait of a physician oil on canvas", "Portrait of doctor oil on canvas", "Portrait of a Physician in His Library"],
    "char_goc_idaresi_baskani": ["Portrait of customs officer oil on canvas", "Portrait of official in uniform oil on canvas", "Portrait of inspector oil on canvas"],
}

def search_commons(query, limit=3):
    url = 'https://commons.wikimedia.org/w/api.php?action=query&list=search&srsearch=' + urllib.parse.quote(query + ' filetype:bitmap') + '&srnamespace=6&format=json'
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    try:
        with urllib.request.urlopen(req) as resp:
            data = json.loads(resp.read().decode('utf-8'))
            return [item['title'] for item in data.get('query', {}).get('search', [])[:limit]]
    except Exception as e:
        return []

for cid, q_list in queries.items():
    print(f"\nSearching for {cid}:")
    for q in q_list:
        res = search_commons(q, 2)
        if res:
            print(f"  [{q}]: {res}")
