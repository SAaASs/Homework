from pymongo import MongoClient
from pymongo.errors import DuplicateKeyError

# mongodb://user:pass@host/Database - если к внешнему хосту, если localhost, то ничего передавать не надо
cluster = MongoClient("mongodb://91.190.239.132:27027")
# Выбираем базу данных
db = cluster.shad112_spynu  # или cluster['test_db'] кто как хочет

comps_mass = [{"name": "comp1", "adress": "adress1", "money_amount": 1000000},{"name": "comp2", "adress": "adress2", "money_amount": 1000000},{"name": "comp3", "adress": "adress3", "money_amount": 1000000},{"name": "comp4", "adress": "adress4", "money_amount": 1000000},{"name": "comp5", "adress5": "adress", "money_amount": 1000000}]
places_mass = [{"cont_comp": "comp1", "name": "place1", "price": 50000.23, "value": 200.8},{"cont_comp": "comp2", "name": "place2", "price": 50000.23, "value": 200.8},{"cont_comp": "comp3", "name": "place3", "price": 50000.23, "value": 200.8},{"cont_comp": "comp4", "name": "place4", "price": 50000.23, "value": 200.8},{"cont_comp": "comp5", "name": "place5", "price": 50000.23, "value": 200.8},]
comps = db.control_companies
places = db.work_places

def insert_in(collection, data):
    x = collection.insert_one(data)


def initDB():
    comps.drop()
    places.drop()
    for i in range(5):
        insert_in(comps, comps_mass[i])
        insert_in(places, places_mass[i])
initDB()
