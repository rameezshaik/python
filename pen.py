class pen:
    def __init__(self,name,price,type):
        self.name=name
        self.price=price
        self.type=type
    def pens_is(self):
        print('pen is of ',self.name,self.price,self.type)
p=pen("cello","$2","gel")
p.pens_is()
