fruit=input("enter the fruits to check: ")
fruits_list=["apple","banana","pomagranian","mango","grapes"]
if fruit.rstrip() in fruits_list:
    print("this",fruit,"is available")
else:
    print("this",fruit,"is not available")