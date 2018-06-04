from urllib.request import urlopen
from bs4 import BeautifulSoup
from collections import defaultdict
import time
from urllib.request import Request, urlopen
import re


req = Request('https://www.google.com/search?q=define+all', headers={'User-Agent': 'Mozilla/5.0'})
page = urlopen(req).read()

sub = 'Definition'
soup = BeautifulSoup(page, 'html.parser')
#name_box =soup.find("")# soup.find("div", attrs={"data-dobid":"dfn"})
# box=soup.find_all(attrs={"data-dobid": "dfn"})
# print(box)
spans = soup.find_all('span')

# create a list of lines corresponding to element texts
lines = [span.get_text() for span in spans if sub in span.get_text()]
#[s for s in list if sub in s]
dfn=lines[0].split('-')[1]
print(dfn)

# import requests
# url = 'https://googledictionaryapi.eu-gb.mybluemix.net/?define=library'
# resp = requests.get(url=url)
# data = resp.json()
# print(data["meaning"]["noun"][0]["definition"])
# print(data["meaning"]["noun"][0]["example"])