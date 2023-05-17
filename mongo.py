from pymongo import MongoClient
from pymongo.errors import DuplicateKeyError

# mongodb://user:pass@host/Database - если к внешнему хосту, если localhost, то ничего передавать не надо
cluster = MongoClient("mongodb://91.190.239.132:27027")
# Выбираем базу данных
db = cluster.shad112_spynu  # или cluster['test_db'] кто как хочет

# Подключаемся к коллекции (таблице), если она не создана, она создаётся автоматически
test_collection = db.pupils  # или db['members'] кто как хочет

test = test_collection.find()
for i in test:
    print(i["name"])
