import numpy as np
import requests
import re
from  bs4 import BeautifulSoup as bs
url = "https://financesonline.com/number-of-gamers-worldwide/"
temperature_list = []
headers_ = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
data = requests.get(url, headers=headers_)
data_ =bs(data.content, 'html.parser')
newdata = data_.find("script", id="charts44235805")
billions_of_players = []
newdata = str(newdata)
numbers = re.findall(r'\d+(?:\.\d+)?', newdata)
for i in range(4,len(numbers), 3):
    billions_of_players.append(float(numbers[i]))
print(billions_of_players)
