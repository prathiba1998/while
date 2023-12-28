#a=open("fruits.txt","w")
#b=open("flowers.txt","w")
#c=open("names.txt","w")





#from zipfile import *
#f=ZipFile("prathibha.zip","w")
#f.write("fruits.txt")
#f.write("flowers.txt")
#f.write("names.txt")
#f.write("student.csv")
#f.close()
#print("zip file is created")



from zipfile import *

f=ZipFile("prathibha.zip","r")
names=f.namelist()
for i in names:
    print("filename is ", i)
    f1=open(i,"r")
    print(f1.read())
    print()
f=ZipFile("prathibha.zip","w")
f.write("fruits.txt")
f.write("flowers.txt")
f.write("names.txt")
f.write("student.csv")
f.close()
print("zip file is created")




#import os
#cwd=os.mkdir("prathibha/file")


#import os
#cwd=os.makedirs("prathibha/file/file1/file2/file3")


#import os
#os.mkdir("prathibha/file1")
#os.mkdir("prathibha/file2")
#os.mkdir("prathibha/file3")
#os.mkdir("prathibha/file4")


#import os
#os.rmdir("prathibha/file1")


#import os
#print(os.listdir("prathibha"))




    
    
