class Person:
    def __init__(self,name):
        self.name = name
    
    def say_hi(self):
        print('Hello , my name is ', self.name)
    
p1 = Person('saif')
p2 = Person('rameez')

p1.say_hi()
p2.say_hi()