def temp(c):
    f=(9/5)*c + 32
    return print(f)
c=input("enter a temp")
c=int(c)
temp(c)

def hour(m,s):
    h = int(m)/60 + int(s)/3600
    return print(h)
m=input("enter min : ")
s=input("enter seconds : ")
m=int(m)
s=int(s)
hour(m,s)
