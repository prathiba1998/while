#types of exceptions:

class PassException(Exception):
    def __init__(self,arg):
        self.msg=arg

class FailException(Exception):
    def __init__(self,arg):
        self.msg=arg
try:
    marks=int(input("enter you total marks: "))
except ValueError:
    print("please enter the vaild number")
if marks>=50:
    raise PassException("congrats you cleared this semester ")
elif marks <50:
    raise FailException("sorry better luck next time")
elif marks != int():
    raise ValueError("vaild enter")
else:
 print("please enter vaild input")
 
 