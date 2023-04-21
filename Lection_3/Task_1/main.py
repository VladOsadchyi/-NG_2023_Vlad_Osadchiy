def plus(fisrtnumber,secondnumber):
    print(fisrtnumber+secondnumber)
def mines(fisrtnumber,secondnumber):
    print(fisrtnumber-secondnumber)
def mult(fisrtnumber,secondnumber):
    print(fisrtnumber*secondnumber)
def division(fisrtnumber,secondnumber):
    print(fisrtnumber/secondnumber)
def mainpartofp():
    print("This program is a calculator!Good luck!")
    fisrtnumber=float(input("Enter your first number: "))
    secondnumber=float(input("Enter your second number: "))
    youraction=input("Enter your action: ")
    match youraction:
      case "+":
        plus(fisrtnumber,secondnumber)
      case "-":
        mines(fisrtnumber,secondnumber)
      case "*":
        mult(fisrtnumber,secondnumber)
      case "/":
        division(fisrtnumber,secondnumber)
mainpartofp()