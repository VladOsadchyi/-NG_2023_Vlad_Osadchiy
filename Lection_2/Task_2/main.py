from collections import Counter
print("This progran will return your unique elements!Good luck!")
yourelements=input("Enter your elements: ").split()
finallist=[]
counterel=Counter(yourelements)
for i, count in counterel.items():
    if count==1:
        finallist.append(i)
print(finallist)
