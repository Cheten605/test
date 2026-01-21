#L = ["Cherry", "Apple", "Blueberry"]
#print(sorted(L))
#print (sorted(L, key = len))
#print (sorted (L, key = lambda L: len(L)))

#class Fruit:
#    def __init__ (self, name, price):
#        self.name = name
#        self.price = price
#L =[Fruit("Cherry", 10), Fruit("Apple", 5), Fruit("Banana", 20)]
#for f in sorted(L, key = lambda x : x.price):
#   print (f.name)# f.name so here we need to make make name object to used it therefore  def __init__ (self, name, price): is used
    
#L =[Fruit("Cherry", 10), Fruit("Apple", 5), Fruit("Banana", 20)]
class Fruit:
    def __init__ (self, name, price):
        self.name = name
        self.price = price
    def sort_priority (self):
       return self.price
L =[Fruit("Cherry", 10), Fruit("Apple", 5), Fruit("Banana", 20)]
print ("one more way to do the same thing ")
for f in sorted(L, key = Fruit.sort_priority):
    print (f.name)




