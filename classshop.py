import random
based = {
    "ProductNames": ["apricot"],
    "ShopNames": ["Perecrestok","Magnit","Auchan","Lenta","Dicksea","Spar"]
}
class products:
    def __init__(self, name,shops,price,id):
        self.name = name
        self.shops = shops
        self.price = price
        self.id = id

s = "Perecrestok.Magnit.Auchan.Lenta.Dicksea.Spar"
print(s)
choosenshops = "Magnit"

product1 = products("flour","Perecrestok.Spar",1500,1)
product2 = products("water","Magnit.Auchan",2500,2)
product3 = products("milk","Dicksea.Spar",500,3)
product4 = products("honey","Magnit.Lenta",6000,4)
product5 = products("sugar","Auchan.Lenta.Dicksea.Spar",2038,5)
list = [product1,product2,product3,product4,product5]
list2 = []
class warehouses:
    def __init__(self,mass):
        self.productslist = mass
    def createProduct(self):
        name = input("Введите название товара")
        if name in based["ProductNames"]:
            theId = based["ProductNames"].index(name)
        else:
            theId = 0 - int(input("Введите свой ид"))
        location = input("Где можно найти этот товар?")
        Price = int(input("Введите цену товара"))
        theProduct = products(name, location, Price, theId)
        self.productslist.append(theProduct)
    def createRandomProduct(self):
        name = based["ProductNames"][random.randint(0, len(based["ProductNames"]) - 1)]
        theId = based["ProductNames"].index(name)
        location = based["ShopNames"][random.randint(0, len(based["ShopNames"]) - 1)]
        Price = random.randint(1, 1000000)
        theProduct = products(name, location, Price, theId)
        self.productslist.append(theProduct)
    def youShouldPrintYourselfNOW(self):
        for i in range(0,len(self.productslist)):
            print(i,self.productslist[i].name, self.productslist[i].shops,self.productslist[i].price,self.productslist[i].id)
    def printbyid(self,ids):
        for i in range (0,len(self.productslist)):
            if self.productslist[i].id == int(ids):
                print(self.productslist[i].name, self.productslist[i].shops,self.productslist[i].price)
    def printbyname(self,names):
        for i in range (0,len(self.productslist)):
            if self.productslist[i].name == names:
                print(self.productslist[i].name, self.productslist[i].shops,self.productslist[i].price)
    def sortbyprice(self):
        pricelist = []
        for i in range (0,len(self.productslist)):
            pricelist.append(self.productslist[i].price)
        pricelist.sort()
        for i in range (0, len(pricelist)):
            for u in range (0,len(self.productslist)):
                if self.productslist[u].price == pricelist[i]:
                    print(self.productslist[u].name, self.productslist[u].shops,self.productslist[u].price)
    def sortbyname(self):
        namelist = []
        for i in range (0,len(self.productslist)):
            namelist.append(self.productslist[i].name)
        namelist.sort()
        for i in range (0, len(namelist)):
            for u in range (0,len(self.productslist)):
                if self.productslist[u].name == namelist[i]:
                    print(self.productslist[u].name, self.productslist[u].shops,self.productslist[u].price)
    def sortbyshops(self):
        shopslist = choosenshops.split('.')
        for i in range (0, len(self.productslist)):
            for u in  range (0,len(shopslist)):
                if shopslist[u] in self.productslist[i].shops:
                    print(self.productslist[i].name, self.productslist[i].shops, self.productslist[i].price)
class uselesshouse(warehouses):
    def findcheap(self,inpu):
        listik = []
        for i in range (0, len(self.productslist)):
            if self.productslist[i].name == inpu:
                listik.append(self.productslist[i].price)
        for i in range (0, len(self.productslist)):
            if self.productslist[i].name == inpu and self.productslist[i].price == min(listik):
                print(i,self.productslist[i].shops, self.productslist[i].price)
warehouse = warehouses(list)
warehouse2 = warehouses(list2)
warehouse2.createRandomProduct()
warehouse2.createRandomProduct()
warehouse2.createRandomProduct()
warehouse2.youShouldPrintYourselfNOW()
print("---------------------------------")
ttte = uselesshouse(list2)
ttte.createRandomProduct()
ttte.createRandomProduct()
ttte.createRandomProduct()
ttte.createRandomProduct()
ttte.youShouldPrintYourselfNOW()
ttte.findcheap(ttte.productslist[2].name)