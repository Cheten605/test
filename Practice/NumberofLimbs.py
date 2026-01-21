class Animal:
    def __init__(self, arms, legs):
        self.arms = arms 
        self.legs = legs
        
    def limbs(self):
        return self.legs + self.arms
spider = Animal (4, 4)
spidlimbs = spider.limbs()
print (spidlimbs)
