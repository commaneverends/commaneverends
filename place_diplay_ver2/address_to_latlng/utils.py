import requests
import json
from csv import reader
import re


def filter_address(address: str):
    filtered_address = re.sub(r'[^a-zA-Z0-9-_*]',' ', address)
    spaced_address = re.compile(r"\s+").sub(" ", filtered_address).strip()
    formatted_address = re.sub(r' ','+', spaced_address)
    translations = (
    (u'\N{LATIN SMALL LETTER U WITH DIAERESIS}', u'ue'),
    (u'\N{LATIN SMALL LETTER O WITH DIAERESIS}', u'oe'),
    (u'\N{LATIN SMALL LETTER SHARP S}', u'ss'),
    )
    for old_str, new_str in translations: 
        translated_address = formatted_address.replace(old_str, new_str)
        return translated_address   


def load_place_dict_from_csv(file_path):
    with open(file_path, 'r') as address_data:
        csv_reader = reader(address_data)
        place_dict = {}
        for row in csv_reader:
            place_address_filtered = filter_address(row[2])
            place_lat, place_lon = get_lat_lng_from_address(row[1], place_address_filtered)
            if place_lat is None or place_lon is None:
                pass
            place_dict.update({row[1]: {"name": row[1], "category": row[0],  "website": row[3],
                                "address_original": row[2], "address": place_address_filtered, 
                                "lat": place_lat, "lon": place_lon}})
    return place_dict 


def get_lat_lng_from_address(name: str, address: str):
    base_url_start = "https://nominatim.openstreetmap.org/search.php?q="
    base_url_end = "&format=jsonv2"
    address_full_url = base_url_start + address + base_url_end 
    address_page = requests.get(address_full_url).json()
    if not len(address_page):
        return None, None
    return address_page[0]['lat'], address_page[0]['lon']


file_path = "./table_place/data/place-2022-01-31.csv"
place_dict = load_place_dict_from_csv(file_path)

with open('./table_place/data/place-2022-01-31-lat-lng.json', 'w') as outfile:
    json.dump(place_dict, outfile, indent=4)


