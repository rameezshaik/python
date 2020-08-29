class laptop:
    def __init__(self,name,price):
        self.name=name
        self.price=price
    def brand(self):
            print('name of the laptop is :', self.name)
            print('price of the laptop is :', self.price)
c=laptop('lenoveo',10000)
c.brand()
