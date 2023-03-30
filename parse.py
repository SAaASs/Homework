import numpy as np
import requests
from  bs4 import BeautifulSoup as bs
url = "https://world-weather.ru/pogoda/china/beijing/"
months = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december']
temperature_list = []
headers_ = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
for month in months:
    url_ = url + month + '-2022/'
    data = requests.get(url_, headers=headers_)
    data_ =bs(data.content, 'html.parser')
    month_data = data_.find('ul', class_='ww-month')
    temperature_list = [int(elem.text[:-1]) for elem in month_data.find_all('span')]
    temperature_array = np.array(temperature_list)
    print(f"Для месяца {month}: \n"
          f"Максимальная температура: {np.max(temperature_array)}\n"
          f"Максимальная температура: {np.mean(temperature_array)}\n"
          f"Максимальная температура: {np.min(temperature_array)}\n"
          f"Дисперсия: {np.var(temperature_array)}\n"
          f"Стандартное отклонение: {np.std(temperature_array)}")
