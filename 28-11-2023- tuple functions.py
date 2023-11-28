#sum of tuple
#t=(10,39,18,76,254)
#sum=0
#for i in t:
 #   sum=sum+i
#print("sum of tuple is: ",sum)


#average
#t=(10,20,30,40)
#a=sum(t)
#b=len(t)
#avg=a/b
#print("average of given numbers in tuple: ",avg)


#len
#t=(30,57,91,"ram",49.87,"prathibha")
#print(len(t))

#t=(1,2,3,3,4,5,6)
#print(len(t))
 
 
#count 
#t=(30,57,91,"ram",49.87,"prathibha",57,"ram",91)
#print(t.count(91))
#print(t.count("ram"))
#print(t.count(30))
#print(t.count("prathibha"))
#print(t.count(30))


#index
#t=(30,57,91,"ram",49.87,"prathibha",10.69,"shyam")
#print(t.index(30))
#print(t.index("ram"))
#print(t.index(91))
#print(t.index("prathibha"))
#print(t.index(100))



#sort
#t=(30,57,91,49.87)
#print(sorted(t))

#t=(1,3,44,6,7,84,3,65,9.87,49.5)
#print(sorted(t))

#t=("ram","prathibha","Shyam")
#print(sorted(t))

#t=(10.4,49.29,45.65)
#print(sorted(t))



#tuple comprehensive
#t=(x for x in range(20))
#for i in t:
 #   print(i)
#print(t)


#t=(x*x for x in range(1,20))
#for i in t:
 #   print(i)
#print(t)


#t=(x+1 for x in range(10) if x%2==0)
#for i in t:
 #   print(i)
#print(t)


#t=(x if x>3 else x+x for x in range(10))
#for i in t:
 #   print(i)
#print(t)


#t=(x+2 for x in range(10) if x%2!=0)
#for i in t:
 #   print(i)
#print(t)


#tuple to set
#t=(30,59,38,"ram",67)
#s=set(t)
#print(s)


#add to set
#s={10,20,30,40,"prathibha",98}
#s.add(20.65)
#s.add("ram")
#s.add(109.47)
#s.add("shyam")
#s.add(987)
#print(s)



#update()
#s={587,284,26965,284}
#l=["ram","prathi","vizag"]
#s.update(l)
#print(s)


#={587,284,26965,284}
#l=["ram","prathi","vizag","apple",10]
#s.update(l)
#print(s)

#s={587,284,26965,284,"banana",20.65}
#l=["ram","prathi","vizag","apple",10,"cherry",35.76]
#s.update(l)
#print(s)



#s={"ram","prathi","vizag","apple",10,"cherry",35.76,1,2,3,5,6}
#print(s.pop())
#print(s.pop())
#print(s.pop())
#print(s.pop())
#print(s.pop())
#print(s)


