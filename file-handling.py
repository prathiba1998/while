#s=open('demo.txt',mode="r")
#print(s.tell())
#print(s.read(3))


#s=open('demo.txt',mode="w")
#s.write("hii prathibha")


#s=open('demo.txt',mode="a")
#s.write("how r u")

#s=open('demo.txt',mode="r+")
#print(s.read())
#s.write("i am fine")
#s.close()


#s=open('demo.txt',mode="a+")
#s.write("i am fine")
#print(s.read())
#s.close()


##handling csv file (comma seprated values)

import csv

with open("student.csv",'w',newline='') as a:
    w=csv.writer(a)
    w.writerow(["stu_name","stu_roll",'stu_phy',"stu_che","stu_eng","stu_math","stu_scie","stu_tot","stu_avg","stu_per","stu_result"])
    n=int(input("enter number of students to entry details "))
    for i in range(1,n+1):
        print(i," student DEATILS ")
        stu_name=input("enter the stu name : ")
        stu_roll=input("enter the stu roll :")
        stu_phy=input("enter the stu phy :")
        stu_che=input("enter the stu che :")
        stu_eng=input("enter the stu eng :")
        stu_math=input("enter the stu math :")
        stu_scie=input("enter the stu scie :")
        b=(stu_phy+stu_che+stu_eng+stu_math+stu_scie)
        stu_tot=b
        c=b/5
        stu_avg=c
        d=b/500*100
        stu_per=d
        stu_result="pass" if stu_per>=36 else "fail"
        w.writerow([stu_name,stu_roll,stu_phy,stu_che,stu_eng,stu_math,stu_scie,stu_tot,stu_avg,stu_per,stu_result])
    print("totsl students data written to csv file ")