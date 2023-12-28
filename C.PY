#import A
#A.add(25,98)
#A.divi(64,8)

def odd(x):
    if x%2!=0:
        print("odd")
    else:
        print("even")
odd(24)
odd(43)
odd(76)



#reloading module in python
import time
from imp import reload
import A
print("program entering into the sleep mode: ",A.y)
time.sleep(20)
reload(A)
print("this is last line: ",A.y)