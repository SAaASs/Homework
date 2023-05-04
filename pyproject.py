import numpy as np
import requests
import re
from  bs4 import BeautifulSoup as bs
url = "https://financesonline.com/number-of-gamers-worldwide/"
temperature_list = []
headers_ = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
data = requests.get(url, headers=headers_)
data_ =bs(data.content, 'html.parser')
print(data_)
thedata = str(data_)
ind1 = thedata.find(":[{")
ind2 = thedata.find("]}")
thedata = thedata[ind1:ind2]
billions_of_players = []
numbers = re.findall(r'\d+(?:\.\d+)?', thedata)
for i in range(0,len(numbers),3):
    billions_of_players.append(numbers[i])
print(billions_of_players)
