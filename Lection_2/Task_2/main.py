print("This progran will return your unique elements!Good luck!")
yourelements=input("Enter your elements: ").split()
finallist=[]
for el in yourelements:
    if yourelements.count(el)==1:
        finallist.append(el)
print(finallist)
