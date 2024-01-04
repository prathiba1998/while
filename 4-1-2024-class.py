#class-object-reference variable


#normal method:
class student:
    def read(prathibha):
     print("it is python")

a=student()
a.read()


#
class student:
    def read(prathibha):
     print("it is python")
    def write(prathibha):
     print("this is prathibha")

a=student()
a.read()
a.write()

#
class student:
    def read(prathibha,x,y):
        prathibha.name=x
        prathibha.city=y
        print("it is python")

a=student()
a.read("ram","vizianagaram")


#
class student:
    def read(prathibha,x,y):
        prathibha.name=x
        prathibha.city=y
        print("it is python")
        
    def display(prathibha):
        print(prathibha.name,"...........",prathibha.city)

s=student()
s.read("ram","vizag")
s.display()




#constructer:_init_
class student:
    def _init_(prathibha,x,y):
        prathibha.name=x
        prathibha.city=y
        print("it is python")
        print(prathibha.name,"...........",prathibha.city)

s=student("ram","vizag")


#types of variables:
#1.static var  2.non static var  3.local var
#
class student:
    def _init_(self):
        self.sname="ram"
        self.scity="vizag"
        print("it is python")
    def display(self):
        print(self.sname,"...........",self.scity)

student().display()



#static var
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

#s=student()
#print(s.name)--object reference
#print(student.name)--class reference


  