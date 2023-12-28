
#decorate function
#
def mul(func):
    def inner(a):
        x=func(a)
        return x*x
    return inner
def multwo(func):
    def inner(a):
        x=func(a)
        return 2*x
    return inner
@multwo
@mul
def num(a):
    return a
print(num(10))



#
def divi(func):
    def inner(a,b):
         if b==0:
             print("it cannot divided by zero")
         else: func(a,b)
    return inner

@divi   
def d(a,b):
     print(a/b)
d(10,2)


#nested functions
def outer():
    print("this is outer")
    def inner():
        print("this is inner")
    inner()
outer()


#function alising

#
def f(name):
    print("good mrng",name)
a=f
del f
#f("ram")
a("prathi")



#
def h1(a):
    def rrr(name):
        print("this is dec1")
        a(name)
    return rrr

def h2(a):
    def qqq(name):
        print("this is dec")
        a(name)
    return qqq
@h1
@h2
def b(name):
    print("hi ",name,"how are you ")

b("prathi")



#
def dec1(func):
     def inner(name):
         print("this is dec1 executing")
         func(name)
     return inner

def dec2(func):
     def ram(name):
         print("this is dec2 executing")
         func(name)
     return ram

@dec2
@dec1
def hello(name):
    print("hi",name,"good girl")
hello("prathi")