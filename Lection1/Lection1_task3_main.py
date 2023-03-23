fisrtnumber=float(input("Enter your first number: "))
secondnumber=float(input("Enter your second number: "))
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
    case "^":
        print(fisrtnumber**secondnumber)
    