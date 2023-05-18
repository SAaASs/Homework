import matplotlib.pyplot as plt
import numpy as np
import requests
import re
import psycopg2
import random
import datetime
from  bs4 import BeautifulSoup as bs
gmod_url = "https://steamcharts.com/app/4000"
csgo_url = "https://steamcharts.com/app/730"
dota2_url = "https://steamcharts.com/app/570"
warframe_url = "https://steamcharts.com/app/230410"


def parse_data(url):
    headers_ = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    data = requests.get(url, headers=headers_)
    data_ = bs(data.content, 'html.parser')
    newdata = data_.find("tbody")
    newdata = newdata.find_all('tr')
    mass = [[], []]
    for month_data in newdata:
        mass[0].append(month_data.find('td', class_="left").text[:-1].rstrip().lstrip())
        mass[1].append(float(month_data.find('td', class_="right").text[:-1]))
    mass[0].pop()
    mass[1].pop()
    return mass

gmod_data = parse_data(gmod_url)
gmod_data[0].reverse()
gmod_data[1].reverse()


csgo_data = parse_data(csgo_url)
csgo_data[0].reverse()
csgo_data[1].reverse()


dota2_data = parse_data(dota2_url)
dota2_data[0].reverse()
dota2_data[1].reverse()


warframe_data = parse_data(warframe_url)
warframe_data[0].reverse()
warframe_data[1].reverse()

"""connection1 = psycopg2.connect(
    database="SHAD112_V9",
    user="shad112_V9",
    password="123",
    host="91.190.239.132",
    port="5432"
)
def fill_database(data_to_use, table_name):
    cur = connection1.cursor()
    cur.execute('''
            DROP TABLE IF EXISTS {0}
            '''.format(table_name))
    cur.execute('''
            CREATE TABLE {0} (
              month VARCHAR(100),
              online INT
           );
            '''.format(table_name))
    for i in range(0, len(data_to_use[0])):
        cur.execute('''
                INSERT INTO {0} (month, online) VALUES
                ('{1}', {2})
                '''.format(table_name, data_to_use[0][i], data_to_use[1][i]))
    cur.execute("select * from {}".format(table_name))
    connection1.commit()
    return cur.fetchall()
print(fill_database(gmod_data, "gmod_data"))
print(fill_database(csgo_data, "csgo_data"))
print(fill_database(dota2_data, "dota2_data"))
print(fill_database(warframe_data, "warframe_data"))"""

a = []
for i in range(0+1, len(gmod_data[0])+1):
    a.append(i)
x = np.array(a)
y = np.array(gmod_data[1])
a = list(filter(lambda x: x % 2 != 0, a))
plt.plot(x, y)
plt.xticks(a)

print("Дисперсия онлайна для Gmod " + str(np.log10(np.var(y))))
plt.title("gmod")
plt.show()
a = []
for i in range(0+1, len(csgo_data[0])+1):
    a.append(i)
x = np.array(a)
y = np.array(csgo_data[1])
a = list(filter(lambda x: x % 2 != 0, a))
plt.plot(x, y)
plt.xticks(a)

print("Дисперсия онлайна для csgo " + str(np.log10(np.var(y))))
plt.title("csgo")
plt.show()
a = []
for i in range(0+1, len(dota2_data[0])+1):
    a.append(i)
x = np.array(a)
y = np.array(dota2_data[1])
a = list(filter(lambda x: x % 2 != 0, a))
plt.plot(x, y)
plt.xticks(a)
print("Дисперсия онлайна для dota2 " + str(np.log10(np.var(y))))
plt.title("dota2")
plt.show()
a = []
for i in range(0+1, len(warframe_data[0])+1):
    a.append(i)
x = np.array(a)
y = np.array(warframe_data[1])
a = list(filter(lambda x: x % 2 != 0, a))
plt.plot(x, y)
plt.xticks(a)
print("Дисперсия онлайна для warframe " + str(np.log10(np.var(y))))
plt.title("warframe")
plt.show()
