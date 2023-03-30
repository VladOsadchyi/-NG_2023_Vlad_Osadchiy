from collections import Counter
print("This program will return the list with non-unique from all your lists")
firstlist=input("Enter your first list: ").split()
secondlist=input("Enter your second list: ").split()
thirdlist=input("Enter your third list: ").split()
finallist=(firstlist+secondlist+thirdlist)
notunlist=[]
counter=Counter(finallist)
for i, count in counter.items():
    if count>1:
        notunlist.append(i)
print(notunlist)



