#import A as a
#print(a.y)
#a.add(10,56)

def volume():
    l=int(input("enter length: "))
    b=int(input("enter breadth: "))
    h=int(input("enter height: "))
    a=l*b*h
    print("volume= ",a)
volume() 

from A import x as a,y as b,add as c,divi as d,mul as e
print(a)
print(b)
c(14,67)
d(54,2)
e(4,8)