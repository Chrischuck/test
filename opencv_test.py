import overpy
import requests

useragent = 'Nauto`'
headers = {
    'Connection': 'keep-alive',
    'sec-ch-ua': '"Google Chrome 80"',
    'Accept': '*/*',
    'Sec-Fetch-Dest': 'empty',
    'User-Agent': useragent,
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Origin': 'https://overpass-turbo.eu',
    'Sec-Fetch-Site': 'cross-site',
    'Sec-Fetch-Mode': 'cors',
    'Referer': 'https://overpass-turbo.eu/',
    'Accept-Language': '',
    'dnt': '1',
}

latitude = 37.672660
longitude = -122.468230

# roughly 110m per 0.001
area_constant = 0.002

max_lat = latitude + area_constant
min_lat = latitude - area_constant
min_lon = longitude - area_constant
max_lon = longitude + area_constant

query = f"""
[out:xml][timeout:25]
[bbox:{min_lat},{min_lon},{max_lat},{max_lon}];
(
 way[highway~"^(motorway|trunk|primary|secondary|tertiary|unclassified|residential|living_street|pedestrian)$"];
);
out;
"""

data = {
  'data': query
}
response = requests.post('https://overpass-api.de/api/interpreter', headers=headers, data=data)

with open('/tmp/myquery.osm', 'w') as f:
    f.write(response.text)


print(response.text)