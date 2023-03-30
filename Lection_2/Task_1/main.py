yourel=input("Enter your elements: ").split()
countel=0
counter=0
for i in yourel:
    countel+=1
print("All your elements: "+str(countel))
yourchoice=input("Enter your choice: ")
if yourchoice in yourel:
    counter+=1
print("How many el of your choice in yourlist"+str(counter))