class products:
    def __init__(self, name,shops,price,id):
        self.name = name
        self.shops = shops
        self.price = price
        self.id = id

s = "Perecrestok.Magnit.Auchan.Lenta.Dicksea.Spar"
print(s)
choosenshops = input("Выберите магазины из списка выше, если их несколько, разделите их ТОЧКОЙ")

product1 = products("flour","Perecrestok.Spar",1500,1)
product2 = products("water","Magnit.Auchan",2500,2)
product3 = products("milk","Dicksea.Spar",500,3)
product4 = products("honey","Magnit.Lenta",6000,4)
product5 = products("sugar","Auchan.Lenta.Dicksea.Spar",2038,5)
list = [product1,product2,product3,product4,product5]
class warehouses:
    def __init__(self,mass):
        self.productslist = mass
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

warehouse = warehouses(list)
warehouse.printbyid(3)
print("-------------------------")
warehouse.printbyname("flour")
print("-------------------------")
warehouse.sortbyprice()
print("-------------------------")
warehouse.sortbyname()
print("-------------------------")
warehouse.sortbyshops()