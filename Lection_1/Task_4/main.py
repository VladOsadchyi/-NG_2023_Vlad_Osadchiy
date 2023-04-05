print("This program will solve a quadratic equation!Good luck!")
fisrtnumber=float(input("Enter your a(first number): "))
secondnumber=float(input("Enter your b(second number): "))
thirdnumber=float(input("Enter your c(third number): "))
Dis=secondnumber**2-(4*fisrtnumber*thirdnumber)
print("Your D= "+str(Dis))
if Dis>0:
    firstx1=(-secondnumber+Dis**0.5)/(2*fisrtnumber)
    secondx2=(-secondnumber-Dis**0.5)/(2*fisrtnumber)
    print("x1= "+str(firstx1))
    print("x2= "+str(secondx2))
if Dis<0:
    print("There are no D")