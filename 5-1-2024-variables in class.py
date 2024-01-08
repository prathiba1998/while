#types of variables:
#1.static var  2.non static var  3.local var

#static var:


class employee:
    sname="marolix"
    def __init__(self,emp_name,emp_id,emp_loc):
        self.name=emp_name
        self.id=emp_id
        self.loc=emp_loc
    def display(self):
        print(self.sname,"----",self.name,"----",self.id,"----",self.loc)

    

a=employee("prathibha","02348","hyderabad")
b=employee("ram","0234","benguluru")
c=employee("shyam","1234","chennai")

a.display()
b.display()
c.display()

#constructer in constructer


class student:
    def __init__(prathibha):
     print("it is prathibha")
    def __init__(prathibha):
     print("this is ram")
s=student()

#

class employee:
    def __init__(self,emp_name,emp_id,emp_loc):
        self.name=emp_name
        self.id=emp_id
        self.loc=emp_loc
    def info(self):
        print("name",self.name)
        print("id",self.id)
        print("loc",self.loc)
        
s=[employee("prathi",1234,"vizag"),employee("ram",4567,"hyd")]

for i in s:
    i.info()
    
#inside the constructer
class student:
    def __init__(self):
        self.sname="ram"
        self.scity="vizag"
e=student()
print(e.__dict__)

#
class test:
    def __init__(self):
        self.t_one=95
        self.t_two=85
e=test()
print(e.__dict__)

#
class employee:
    def __init__(self):
        self.empname="prathi"
        self.emcitycity="vizag"
e=employee()
print(e.__dict__)



# inside the instance method
class student:
    def __init__(self):
       self.sname="ram"
       self.scity="vizag"
    def m1(prathi):
        prathi.a=100
        
e=student()
e.m1()
print(e.a)
print(e.__dict__)


#
class student:
    def __init__(self):
        self.sname="ram"
        self.scity="vizag"
    def m1(prathi):
        prathi.a=100
        prathi.b=200
        
e=student()
e.m1()
print(e.a)
print(e.b)
print(e.sname)
print(e.__dict__)


#
class employee:
    def __init__(self):
        self.empname="prathi"
        self.empcity="vizag"
    def m1(prathi):
        prathi.a=50000
        prathi.b=20000
e=employee()
e.m1()
print(e.a)
print(e.b)
print(e.empcity)
print(e.__dict__)


#
class test:
    def __init__(self):
        self.t_one=95
        self.t_two=85
    def m1(prathi):
        prathi.a=5
        prathi.b=2
e=test()
e.m1()
print(e.a)
print(e.b)
print(e.t_one)
print(e.__dict__)


# outside the class by using reference variable
class test:
    def __init__(self):
        self.t_one=95
        self.t_two=85  
e=test()
e.c=100
print(e.c)
print(e.__dict__)


#
class employee:
    def __init__(self):
        self.empname="prathi"
        self.empcity="vizag"
    def m1(prathi):
        prathi.a=50000
        prathi.b=20000
e=employee()
e.c=300
e.m1()
print(e.c)
print(e.__dict__)


#
class student:
    def __init__(self):
        self.sname="ram"
        self.scity="vizag"
    def m1(prathi):
        prathi.a=100
        prathi.b=200
        
e=student()
e.c=3
print(e.c)
e.m1()
print(e.a)
print(e.b)
print(e.sname)
print(e.__dict__)



#
class student:
    def __init__(self):
       self.sname="ram"
       self.scity="vizag"
    def m1(prathi):
        prathi.a=100
        
p=student()
p1=student()
p.b=200
p.m1()
p1.c=500
print(p.a)
print(p.__dict__)
print(p1.__dict__)



#
class test:
    def __init__(self):
        self.t_one=95
        self.t_two=85
    def m1(prathi):
        prathi.a=5
        prathi.b=2
e=test()
e.m1()
e.a=45
e.b=67
print(e.__dict__)


#
class test:
    c=400  #static variable
    def __init__(self):
        self.a=95   #instance variable
        self.b=85
p=test()
print(p.__dict__)






#
class student:
    def __init__(self):
        self.mark_one=95
        self.mark_two=85
    def m1(prathi):
        prathi.a=5
        prathi.b=2
e=student()
e.m1()
print(e.__dict__)



#
class employee:
    c=400  
    def __init__(self):
        self.a=95   #instance variable
    def write(prathi):
        prathi.b=85
print(employee.c)


#####
class employee:
    c=400  
    def __init__(self):
        self.a=95   #instance variable
m1=employee()
m1.b=78
m1.d=98
m2=employee()
m2.e=89
print(m1.a,m1.d)
print(m2.e,m1.a)