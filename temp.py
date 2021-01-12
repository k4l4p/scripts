#!/usr/bin/env python3
import requests
import json

url = 'https://data.weather.gov.hk/weatherAPI/opendata/weather.php?dataType=rhrread&lang=tc'

req = requests.get(url)

j = req.json()

for i in j['temperature']['data']:
    if i['place'] == '屯門':
        print(i['value'])
