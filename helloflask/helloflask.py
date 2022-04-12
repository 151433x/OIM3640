from base64 import decode
from flask import flask, render_template
import urllib.request
import json
APIKEY = '4556eaeaddb1841c659074ec8cf6d1af'
def get_temp(city):
    country_code='us'
    url=f'https://api.openweathermap.org/data/2.5/weater?q={city},{country_code}&APPID={APIKEY}'
    print(url)
    f=urllib.request.urlopen(url)
    response_text=f.read().decode('utf-8')
    response_data=json.loads(response_text)
    temp=response_data['main']['temp']

