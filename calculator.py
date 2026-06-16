import math

history = []

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero"
    return a / b

def power(a, b):
    return a ** b

def modulus(a, b):
    return a % b

def square_root(a):
    if a < 0:
        return "Error: Negative number"
    return math.sqrt(a)

while True:
    print("\n===== ADVANCED CALCULATOR =====")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Power")
    print("6. Modulus")
    print("7. Square Root")
    print("8. View History")
    print("9. Exit")

    choice = input("Enter choice (1-9): ")

    if choice == "9":
        print("Calculator Closed.")
        break

    elif choice == "8":
        print("\n===== HISTORY =====")
        if len(history) == 0:
            print("No calculations yet.")
        else:
            for item in history:
                print(item)
        continue

    elif choice == "7":
        try:
            num = float(input("Enter a number: "))
            result = square_root(num)

            record = f"√{num} = {result}"
            history.append(record)

            print("Result:", result)

        except ValueError:
            print("Invalid Input")

    elif choice in ["1","2","3","4","5","6"]:

        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if choice == "1":
                result = add(num1, num2)
                record = f"{num1} + {num2} = {result}"

            elif choice == "2":
                result = subtract(num1, num2)
                record = f"{num1} - {num2} = {result}"

            elif choice == "3":
                result = multiply(num1, num2)
                record = f"{num1} * {num2} = {result}"

            elif choice == "4":
                result = divide(num1, num2)
                record = f"{num1} / {num2} = {result}"

            elif choice == "5":
                result = power(num1, num2)
                record = f"{num1}^{num2} = {result}"

            elif choice == "6":
                result = modulus(num1, num2)
                record = f"{num1} % {num2} = {result}"

            history.append(record)

            print("Result:", result)

        except ValueError:
            print("Invalid Input")

    else:
        print("Invalid Choice")