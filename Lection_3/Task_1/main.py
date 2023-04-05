print("This program is a calculator!Good luck!")
def calculation(fisrtnumber,secondnumber):
    youraction=input("Enter your action: ")
    match youraction:
        case "+":
          print(fisrtnumber+secondnumber)
        case "-":
          print(fisrtnumber-secondnumber)
        case "*":
          print(fisrtnumber*secondnumber)
        case "/":
          print(fisrtnumber/secondnumber)

def mainpartofp():
    print("This program is a calculator!Good luck!")
    fisrtnumber=float(input("Enter your first number: "))
    secondnumber=float(input("Enter your second number: "))
    calculation(fisrtnumber,secondnumber)
mainpartofp()