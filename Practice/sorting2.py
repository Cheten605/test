class Fruit:
    def __init__ (self, name, price):
        self.name = name
        self.price = price

    def __lt__ (self, other):#It stands for less than
        return self.price < other.price
L =[Fruit("Cherry", 10), Fruit("Apple", 5), Fruit("Banana", 20)]
for f in sorted(L):#when there is no key parameter in sorted function then it will look for __It__ function in the class
    print (f.name)

        