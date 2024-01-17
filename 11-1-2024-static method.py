#
class prathi:
    a=10
    def __init__(self): 
        prathi.b=20
        
    def m1(self):
        prathi.c=80
        self.u=499
    
    @classmethod
    def m2(cls):
        prathi.d=700
        cls.e=200
        cls.y=90
print(prathi.__dict__)


#
class student:
   def __init__(self): 
        pass
        
   def m1(self):
        print("student name")
        
   @classmethod 
   def m2(cls):
        print("student id")
        
   @staticmethod
   def m3():
        print("student rollno")
   
#   
class Test:
    a=10
    def __init__(self):
        Test.b=20
        
    def m1(self):
        Test.c=80
        self.u=499
    
    @classmethod
    def m2(cls):
        Test.d=700
        cls.e=200
        cls.y=90
    
    @staticmethod
    def m3():
        Test.f=500



t=Test()
t.m1()
Test.m2()
Test.m3()
print(t.__dict__)



#
class Test:
    a=10
    def __init__(self):
        print(self.a)
        print(Test.a)
    
    def m1(self):
        print(self.a)
        print(Test.a)

    @classmethod
    def m2(self):
        print(self.a)
        print(Test.a)

    @staticmethod
    def m3():
        print(Test.a)

print(Test.a)
print(Test.__dict__)
t=Test()
t.m1()
t.m2()
t.m3()




#
class Test:
    a=10
    def __init__(self):
        self.a=999
    
    def m1(self):
        Test.a=800
    @classmethod
    def m2(cls):
        cls.a=600
    @staticmethod
    def m3():
        Test.a=200
    
t=Test()
t.m1()
t.m2()
t.m3()
print(t.a)




#
class Test:
    a=10
    def __init__(self):
        self.b=999
    
    def m1(self):
        Test.a=800
    @classmethod
    def m2(cls):
        cls.a=600
    @staticmethod
    def m3():
        Test.a=200
    
t=Test()
t.m1()
t.m2()
t.m3()
t.a=489
print(t.a)
print(Test.a)