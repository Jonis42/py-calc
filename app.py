


def menu_function():
    print('PyCalc v.1.0')
    print('------------')
    print('1. Add 2 numbers')
    print('2. Subtract 2 numbers')
    print('3. Divide 2 numbers')
    print('4. Multiply 2 numbers')
    print('5. Exit Application')
    print('------------')

menu_function()

while True:
    choice = 0
    try:
        choice = int(input("Select a number to continue: "))
        print('------------')
    except ValueError:
        print("Please enter a number.")
        menu_function()

    if choice == 1:
        try:
            firstNum = float(input("Enter first number: "))
            secondNum = float(input("Enter second number: "))
            print("\n", "Sum: ", firstNum + secondNum, "\n")
            menu_function()
        except ValueError:
            print("Please enter a number.")
            menu_function()

    if choice == 2:
        try:
            firstNum = float(input("Enter first number: "))
            secondNum = float(input("Enter second number: "))
            print("\n", "Difference: ", firstNum - secondNum, "\n")
            menu_function()
        except ValueError:
            print("Please enter a number.")
            menu_function()

    if choice == 3:
        try:
            firstNum = float(input("Enter first number: "))
            secondNum = float(input("Enter second number: "))
            print("\n", "Quotient: ", firstNum / secondNum, "\n")
            menu_function()
        except ValueError:
            print("Please enter a number.")
            menu_function()
        except ZeroDivisionError:
            print("Cannot divide by Zero.")
            menu_function()

    if choice == 4:
        try:
            firstNum = float(input("Enter first number: "))
            secondNum = float(input("Enter second number: "))
            print("\n", "Product: ", firstNum * secondNum, "\n")
            menu_function()
        except ValueError:
            print("Please enter a number.")
            menu_function()

    if choice == 5:
        print("Bye bye!")
        print('------------')
        break
