print("This program will return the list with non-unique from all your lists!Good luck")
firstlist=input("Enter your first list: ").split()
secondlist=input("Enter your second list: ").split()
thirdlist=input("Enter your third list: ").split()
finallist=(firstlist+secondlist+thirdlist)
notunlist=[]
for el in finallist:
    if finallist.count(el)>1:
        notunlist.append(el)
print(set(notunlist))



