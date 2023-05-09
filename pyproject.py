import numpy as np
import requests
import re
from  bs4 import BeautifulSoup as bs
url = "https://steamcharts.com/app/4000"
temperature_list = []
headers_ = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
data = requests.get(url, headers=headers_)
data_ =bs(data.content, 'html.parser')
newdata = data_.find("tbody")
newdata = newdata.find_all('tr')
mass = [[],[]]
for month_data in newdata:
    mass[0].append(month_data.find('td', class_="left").text[:-1].rstrip().lstrip())
    mass[1].append(float(month_data.find('td', class_="right").text[:-1]))
for i in range(0, len(mass[0])):
    print(mass[0][i], mass[1][i])
