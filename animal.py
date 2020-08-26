#defining a animal class
class animal:
    

    def is_aquatic(self):

        return self.aquatic

    def get_numberoflegs(self):

        return self.legs
    
    def __init__(self,legs,aquatic,eating_type,bird):
        self.legs = legs
        self.aquatic = aquatic
        self.eating_type = eating_type
        self.bird = bird


#dog = animal(legs,aquatic,eating_type,bird)
#dog.is_aquatic()
#dog.legs
spider = animal(8,False,'cornivorus',False)
print(spider)
#print(spider.legs)
print(spider.get_numberoflegs())
