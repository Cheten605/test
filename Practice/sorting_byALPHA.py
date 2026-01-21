class Fruit():
    def __init__ (self , name, price):
        self.name = name
        self.price = price
    def __lt__ (self, other):
        return self.name < other.name
L =[Fruit("Cherry", 10), Fruit("Apple", 5), Fruit("Banana", 20)]
for f in sorted(L):
    print (f.name)