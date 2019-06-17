
number1 = int(input("Please enter first number: "))
number2 = int(input("Please enter second number: "))

operation = int(input("Press 1 to add, press 2 to subtract, press 3 to multiply, press 4 to divide, press 9 to quit:"))

if (operation == 1):
    print("Result: ", int(number1+number2))
elif (operation == 2):
    print("Result: ", int(number1-number2))
elif (operation == 3):
    print("Result: ", int(number1*number2))
elif (operation == 4):
    print("Result: ", float(number1/number2))
elif (operation == 9) :
    print("Bye")
else:
    print("Wrong input!")
