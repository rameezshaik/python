class room:
    def __init__(self,type,floor):
        self.type=type
        self.floor=floor
    def roomtype(self):
        print('room type is : ',self.type)
        print('room floor is : ',self.floor)
c=room("ac/nonac","marble")
c.roomtype()