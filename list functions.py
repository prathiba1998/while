#reverse sort()
l=[1,3,53,65,24,600,-6,-34,98,74,-98]
print(sorted(l,reverse=True))


#copy()
l1=[1,2,3,4,5,6]
l2=l1.copy()
print(l2)


# compare list
l1=[10,20,30,40,50]
l2=[10,20,30,40,50]
print(l1==l2)
print(l1 is l2)
print(l1!=l2)
print(l1 is not l2)


#nested list matrix form
matrix=[[10,20,30],[40,50,60],[70,80,90]]
for i in range(3):
    for j in range(3):
        print(matrix[i][j],end=" ")
    print()
   
   
#list comprehensive  
l=[x for x in range(10)]
print(l)

l=[x for x in range(20) if x%2==0]
print(l)


l=[x if x>3 else x+1 for x in range(1,20)]
print(l)