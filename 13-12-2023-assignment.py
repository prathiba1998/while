#recursive fun

def fac(x):
    if x==1:
        result=1
    else:
        result=x*fac(x-1)
    return result
print(fac(6))


def fac(x):
    if x==1:
        result=8
    else:
        result=x*fac(x-1)
    return result
print(fac(8))


def fac(x):
    if x==1:
        result=0
    else:
        result=x*fac(x-1)
    return result
print(fac(6))


def fac(x):
    if x==1:
        result=5
    else:
        result=x*fac(x-1)
    return result
print(fac(10))

def fac(x):
    if x==1:
        result=10
    else:
        result=x*fac(x-1)
    return result
print(fac(10))


#lamda function

a=lambda a,b:a+b
print(a(4,6))

a=lambda a,b:a if a%2==0 else b
print(a(4,6))

a=lambda l,b:l*b
print(a(4,6))

a=lambda a,b:a+b-a-b
print(a(4,6))

a=lambda a,b:a if a>b else b
print(a(4,6))


#filter()
l=["ram",12,3.76,8,2]
x=list(filter(lambda a:a,l))
print(x)


t=("ram",12,3.76,8,2)
x=list(filter(lambda a:a,l))
print(x)


l=[12,3.76,8,2]
x=list(filter(lambda a:a%2!=0,l))
print(x)


t=(12,3.76,8,2)
x=list(filter(lambda a:a*a,l))
print(x)


l=[12,3.76,8,2]
x=list(filter(lambda a:a>5,l))
print(x)



#map() 

t=(1,4,3,5,9,3,85,10,65)
l=[23.5,98,3,5,2,8]
a=list(map(lambda a,b:a-b,t,l))
print(a)


t=(1,4,3,5,9,3,85,10,65)
l=[23.5,98,3,5,2,8]
a=list(map(lambda a,b:a*a,t,l))
print(a)


t=(1,4,3,5,9,3,85,10,65)
l=[23.5,98,3,5,2,8]
a=list(map(lambda a,b:a%2==0,t,l))
print(a)


t=(1,4,3,5,9,3,85,10,65)
l=[23.5,98,3,5,2,8]
a=list(map(lambda a,b:a-b+a*b,t,l))
print(a)


t=(1,4,3,5,9,3,85,10,65)
l=[23.5,98,3,5,2,8]
a=list(map(lambda a,b:a>b,t,l))
print(a)


#reduce()


from functools import *
t=(1,4.5,36,38,6,2)
print(reduce(lambda a,b:a+b,t))


t=(1,4.5,36,38,6,2)
print(reduce(lambda a,b:a+b-a*b+a*a,t))

l=[1,4.5,36,38,6,2]
print(reduce(lambda a,b:a<b,t))

t=(1,4.5,36,38,6,2)
print(reduce(lambda a,b:a%2!=0,t))

a=[2,6,18,9,83,72,90]
print(reduce(lambda x,y:y==2,a))


#arguments

def f(arg1,arg2,arg3=4,arg4=8):
    print(arg1,arg2,arg3,arg4)
f(3,5)#valid
f(10,20,30,40)#valid
f(11,6,arg4=1000)#valid
f(arg4=6,arg1=7,arg2=9)#valid
f(arg3=90,arg4=80)#invalid-missing of arg1,arg2
f(6,8,arg2=89)#invalid-multiple arg2
f(4,5,arg3=7,arg5=78)#invalid-unexpected arg5
f()#invalid-missing positinal values