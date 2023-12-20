#Try-except-finally


#try:
#     statement-1
#     statement-2
#     statement-3
#except:
#     statment-4
#statment-5
#finally:
#     statment-6
   
    
    
    
#Case:1
#If no exception raised at try block-Normal Termination


try :
    a=3
    b=6
    print(a+b)
    print("prathi")
    print(20/5)
except TypeError :
    print("typeerror is occured")
finally:
    print("finally closing block")
    
    
    
#Case-2
#If exception raised at stamen 2 and matched the except block-Normal Termination


try :
    print("prathi")
    a=3
    b="ram"
    print(a+b)
    print(20/5)
except TypeError :
     print("typeerror is occured")
finally:
    print("finally closing block")
    
    
    
#Case-3 
#If  exception raised at stamen 2 and not matched the except block-abnormal termination


try :
    print("prathi")
    a=3
    b="ram"
    print(a+b)
    print(20/5)
except ValueError :
    print("valueerror is occured")
finally:
    print("finally closing block")
    
#Case-4
#Exception raised at stm 1 and If an except rasied at 4 it is always ab T, but before ab T stmt-5 (finally ) will excecute.


try :
    a=3
    b="ram"
    print(a+b)
    print("prathi")
    print(20/5)
except TypeError :
    c=3
    d="ram"
    print(c+d)
    print("typeerror is occured")
finally:
    print("finally closing block")  
    
#Case 5:
#If an exception raised at stmt 5 -abnormal termination


try :
    a=3
    b=6
    print(a+b)
    print("prathi")
    print(20/5)
except ValueError:
    print("valueerror is occured")
finally:
    c=3
    d="ram"
    print(c+d)
print("finally closing block")









#case-2-exception in outer try
try:
    print(50/0)
    print("outer try block")#
    try:
        print("inner try block")#
    except ZeroDivisionError:
        print("inner except block")#
    finally:
        print("inner finally block")#
    print("outside the inner block")#
except ZeroDivisionError:
    print("outer except block")
finally:
    print("outer finally block")#
print("outside the all block")#



