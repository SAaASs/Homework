from pymongo import MongoClient
import random
import datetime
from bson.son import SON
from pymongo.errors import DuplicateKeyError

# mongodb://user:pass@host/Database - если к внешнему хосту, если localhost, то ничего передавать не надо
cluster = MongoClient("mongodb://91.190.239.132:27027")
# Выбираем базу данных
db = cluster.shad112_spynu  # или cluster['test_db'] кто как хочет

comps_mass = [{"name": "comp1", "adress": "adress1", "money_amount": 1000000},{"name": "comp2", "adress": "adress2", "money_amount": 1000000},{"name": "comp3", "adress": "adress3", "money_amount": 1000000},{"name": "comp4", "adress": "adress4", "money_amount": 1000000},{"name": "comp5", "adress5": "adress", "money_amount": 1000000}]
places_mass = [{"cont_comp": "comp1", "name": "place1", "price": 50000.23, "value": 200.8},{"cont_comp": "comp2", "name": "place2", "price": 50000.23, "value": 200.8},{"cont_comp": "comp3", "name": "place3", "price": 50000.23, "value": 200.8},{"cont_comp": "comp4", "name": "place4", "price": 50000.23, "value": 200.8},{"cont_comp": "comp5", "name": "place5", "price": 50000.23, "value": 200.8},{"cont_comp": "comp1", "name": "place6", "price": 50000.23, "value": 200.8},{"cont_comp": "comp1", "name": "place7", "price": 50000.23, "value": 200.8},{"cont_comp": "comp3", "name": "place8", "price": 50000.23, "value": 200.8},{"cont_comp": "comp4", "name": "place9", "price": 50000.23, "value": 200.8},{"cont_comp": "comp5", "name": "place10", "price": 50000.23, "value": 200.8}]
comps = db.control_companies
places = db.work_places
queries = db.work_queries

def insert_in(collection, data):
    x = collection.insert_one(data)



def initDB():
    comps.drop()
    places.drop()
    queries.drop()
    for i in range(len(comps_mass)):
        insert_in(comps, comps_mass[i])
        print("В список компаний добавлена компания", comps_mass[i])
    for i in range(len(places_mass)):
        insert_in(places, places_mass[i])
        print("В список мест добавлено место", places_mass[i])
def piss(target_name):
    cursor = comps.find({"name": "{0}".format(target_name)})
    for cur in cursor:
        print(cur)
def take_money(target_name, money_amount):
    cursor = comps.find_one({"name": "{0}".format(target_name)})
    if float(cursor["money_amount"]) - float(money_amount)>0:
        target_money_amount = float(cursor["money_amount"]) - float(money_amount)
    else:
        print("Ошибкастоп ноль0ноль0ноль0ноль0ноль0ноль0ноль0ноль0ноль0")
        print("Недостаточно денег на счете компании {0}".format(target_name))
        return 0
    myquery = {"name": "{0}".format(target_name)}
    newvalues = {"$set": {"money_amount": target_money_amount}}

    x = comps.update_many(myquery, newvalues)
    return 1

def create_query(target_place, date):
    cursor = places.find_one({"name": "{0}".format(target_place)})
    if cursor is None:
        print("Создание заказа прервано. Причина: место {0} не существует".format(target_place))
    else:
        ccomp=cursor["cont_comp"]
        price=cursor["price"]
        value = cursor["value"]
        x = take_money(ccomp, price)
        if x==1:
            insert_in(queries,{"place":target_place,"comp":ccomp,"check":price,"value":value,"date":date})
            print("Запрос на уборку места {0}, объемом {1} м^3, компанией {2}, на сумму {3} рублIв принят и скоро будет исполнен, ожидайте".format(target_place,value,ccomp,price))
        else:
            print("заказ отменен")
            return 0
def make_job(operation_amount):
    for i in range(0, operation_amount):
        create_query(places_mass[random.randint(0,9)]["name"],str(datetime.datetime.now().date()+datetime.timedelta(random.randint(1,200))))
#initDB()
#make_job(30)
