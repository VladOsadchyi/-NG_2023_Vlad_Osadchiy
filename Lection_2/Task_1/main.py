print("This program will count the number of your elements in yourlist")
print("After this it will find element which you must write if you want to know the number of that element in your list!Good luck!")
yourel=input("Enter your elements: ").split()
countel=0
for i in yourel:
    countel+=1
print("All your elements: "+str(countel))
yourchoice=input("Enter your choice: ")
counter=yourel.count(yourchoice)
print("How many el of your choice in yourlist: "+str(counter))