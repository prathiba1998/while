#try except


# try:
#     #risky code
# except BaseException :
#     #handling code


try :
    a=10
    print(a+b)
except NameError :
    print("NameError is occured")
    print(10/2)
    
try:
    a=10
    b="ram"
    print(a+b)
except TypeError:
    print("typeerror is occured")
    print(a)
    
try:
    a=10
    b=20
    print(a+b)
except ValueError:
    print("valueerror is occured")
    
    
#control flow in try except block
#case-1
#if there is no error in try block in-Normal termination

try :
    a=3
    b=6
    print(a+b)
    print("prathi")
    print(20/5)
except TypeError :
    print("typeerror is occured")
print(a*b)
print("ram")

##case-2
#if an excep raised at stat-2 and corresponding except block is matched
#normal termination

try :
    print("prathi")
    a=3
    b="ram"
    print(a+b)
    print(20/5)
except TypeError :
     print("typeerror is occured")
print("ram")



#case -3
#if an excep raised at stat-2 and corresponding except block is not matched
#abnormal termination
try :
    print("prathi")
    a=3
    b="ram"
    print(a+b)
    print(20/5)
except ValueError :
    print("valueerror is occured")
    
    
#case-4    
#if an excep raised at stat-2 and corresponding except block is matched and at statement 4
#abnormal termination 
    
try :
    print("prathi")
    a=3
    b="ram"
    print(a+b)
    print(20/5)
except TypeError :
    c=3
    d="ram"
    print(c+d)
    print("typeerror is occured")  
    
      
#
try:
    a=int(input("enter the num: "))
    b=int(input("enter the num: "))
    print(a+b)
    print(a/b)
except (ValueError,ZeroDivisionError):
    print("please give valid value")
   
   
#   
try:
    a=int(input("enter the num: "))
    b=int(input("enter the num: "))
    print(a+b)
    print(a/b)
except (ValueError,ZeroDivisionError) as m:
    print(m)