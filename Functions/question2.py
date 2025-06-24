# Write a Python program to create a calculator using functions.

def add(num1, num2):
    return num1 + num2
def subtract(num1, num2):
    return num1 - num2
def multiply(num1, num2):
    return num1 * num2
def divide(num1, num2):
    if num2 == 0:
        return "Error! Division by zero."
    return num1 / num2

def calculator():
    print("Select operation you want to do :")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    choice = int(input("Enter choice (1/2/3/4): "))
    if choice in range(1, 5):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        if choice == 1:
            print("Result:", add(num1, num2))
        elif choice == 2:
            print("Result:", subtract(num1, num2))
        elif choice == 3:
            print("Result:", multiply(num1, num2))
        elif choice == 4:
            print("Result:", divide(num1, num2))
    else:
        print("Invalid input")

calculator()
