import json
import urllib
import requests
from bs4 import BeautifulSoup
import xml.etree.ElementTree as ET
#robot.txt

url = 'https://mdn.github.io/learning-area/javascript/oojs/json/superheroes.json'
myfile = urllib.request.urlopen( url ).read().decode('euc-kr')
#print(myfile)

root =  ET.fromstring(myfile)

for items in root :
    print(items.tag)
    print(items.text)

