print("This progran will return your unique elements!Good luck!")
yourelements=input("Enter your elements: ").split()
for el in yourelements:
    if yourelements.count(el)==1:
        print(el)