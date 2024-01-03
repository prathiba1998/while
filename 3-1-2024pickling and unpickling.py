#pickling and unpickling

#some times we have to write total state of object and we 
# have to read the state of the object from the file


# class --> blue print of model
#object --> each AC (each instance is a one object )
#reference var --> is remote to operat object 
import pickle

class student:
    def __init__(self,srollno,sname,smark):
        self.srollno=srollno
        self.sname=sname
        self.smark=smark
    def display(self):
        print(self.srollno,"/t",self.sname,"/t",self.smark)

with open("student.data","wb") as p:
    e=student(233,"prathi",100)
    b=student(244,"ram",200)   
    pickle.dump(e,p)
    pickle.dump(b,p)
    print("pickle of student object is done ")

#unpickle

with open("student.data","rb") as f:
    obj=pickle.load(f)
    print("student info after the unpickling")
    obj.display()
