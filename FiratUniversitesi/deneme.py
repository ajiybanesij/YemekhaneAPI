# -*- coding : utf-8 -*-
from bs4 import BeautifulSoup
import requests

page = requests.get("http://uevi.firat.edu.tr/")
soup = BeautifulSoup(page.content, 'html.parser')
menu = soup.select("div > div > div > div > div.views-field.views-field-body > div")
tarih=soup.select("div > div > div > div > div.views-field.views-field-created > span")
menu_liste=(menu[0].text.split('\n'))
print(tarih[0].text)
returnList=[]
for item in menu_liste:
    if(len(item)>2):
        returnList.append(item)


