#positional arguments


def person(name,age):
    print(name)
    print(age)
person("prathi",20)

def f(roll,name,section):
    print("hello",name,"your roll no is",roll,"your sec",section)
f(1224,"prathiobha",1)


def sum(a,b):
    c=a+b
    print(c)
sum(12,74)


def name(id,location):
    print("your id is",id,location)
name("02348","hyderabad")
    
    
#keyword argument

def person(name,age):
    print(name,age)
person(age=25,name="ram")


def vacant(rmno,name):
    print("hello your name",name,rmno)
vacant(name="ram",rmno=8)

def mul(a,b,c):
    print(a*b*c)
mul(a=5,b=9,c=5)


def area(len,breadth):
    print("area is",len*breadth)
area(len=7,breadth=9)


#default argument


def f(roll,id,name="prathi"):
    print("hello",name,roll,id)
f(roll=123,id=12345)

def person(name,age=29):
    print("hello",name,age)
person(age=76,name="ram")

def total(a,b,d,k=56):
    c=a+b+d+k
    print(c)
total(10,39,587,62)


def volume(l,b,h=6):
    print("volume is",l*b*h)
volume(8,4.9,2)


#variable length arguments


def f(x,*y):
    c=x
    for i in y:
        c=c+i
    print(c)

f(12,74,2,8,3)


def person(name,age,*a):
    print("hello",name,age,*a)
person("ram",23,38,74,682)

def tickets(a,b,c,*d):
    k=a,b,c,d
    print("tickets are",k)
tickets(1,3,4,5,4,33,5,2,4)


   
#global variable

name="prathi"
def f():
    global name
    print("name of the person",name)
f()


a=10
b=32
def sum():
    global a,b
    c=45
    print("sum",a+b)
sum()
    
    
def dif():
    d=78
    print("diff",a-b)
dif()


def mul():
    global dif
    d=78
    print("mul",a*b)
mul()



#local variable
name="prathi"
def f():
    name="ram"
    print("name of the person",name)
f()


a=10
b=32
def sum():
    c=45
    print("sum",a+b)
sum()
    
    
def dif():
    d=78
    print("diff",a-b)
dif()





  