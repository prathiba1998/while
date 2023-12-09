def prathi():
    print("hello prathibha")
prathi()


def odd(x):
    if x%2!=0:
        print("odd")
    else:
        print("even")
odd(18)
odd(64)
odd(86)
odd(65)
odd(32)
odd(55)


def fact(n):
    a=1
    while n>=1:
        a=a*n
        n=n-1
    return a
print(fact(10))



def cal(a,b):
    sum=a+b
    sub=a-b
    mul=a*b
    div=a/b
    return sum,sub,mul,div
print(cal(56,28))
print(cal(65,87))


def average(marks):
    sum_of_marks=sum(marks)
    total=len(marks)
    average=sum/total
    return average
marks=[10,76,85,84,36]
print("your avg marks is: ",average)


def greet(name):
    print("hello! i hope doing well.",name)
    
greet("ram")


def function(name):
    print("this is function",name)
function("prathibha")


def list(a):
    for i in a:
        print(i)
list([3,875,35,985,643])


def tuple(a):
    for i in a:
        print(i)
tuple((3,875,35,985,643))


def happy_birthday(name):
    print("happy birthday to you",name)
happy_birthday("prathi")


def fact(n):
    a=1
    while n>=1:
        a=a*n
        n=n-1
    return a
print(fact(15))


def display():
    a=1
    for i in range(20):
      print("*",end=" ")
display()


#def area():
  #  l=int(input("enter length: "))
  #  b=int(input("enter breadth: "))
  #  a=l*b
  #  print("area= ",a)
#area()


def volume():
    l=int(input("enter length: "))
    b=int(input("enter breadth: "))
    h=int(input("enter height: "))
    a=l*b*h
    print("volume= ",a)
volume()    
                 


def wishes(name):
    print("happy cristmas",name)
    return name
wishes("prathibha")
    
    
        