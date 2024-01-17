
# delete of static variable


class student:
    a=10
    @classmethod
    def m2(cls):
        del cls.a

student.m2()
print(student.__dict__)



#
class Test:
    a=10
    def __init__(self):
        Test.b=20
        del Test.a
    def m1(self):
        Test.c=30
        del Test.b
    @classmethod
    def m2(cls):
        cls.d=677
        del Test.c
    @staticmethod
    def m3():
        Test.r=60
        

t=Test()
t.m1()
t.m3()
print(Test.__dict__)



#
class prathi:
    a=10
    def __init__(self):
        prathi.b=20
        del prathi.a
    def m1(self):
        prathi.c=30
        del prathi.b
    @classmethod
    def m2(cls):
        cls.d=677
        del prathi.c
    @staticmethod
    def m3():
        prathi.r=60
        

p=prathi()
p.m1()
p.m2()
p.m3()
print(prathi.__dict__)


