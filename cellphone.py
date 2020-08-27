class cellphone:
    def __init__(self,name,price):
        self.name=name
        self.price=price
    def brand(self):
        print('Brand is ',self.name)
        print('price is ', self.price)

c=cellphone('iphone',10000)
c.brand()