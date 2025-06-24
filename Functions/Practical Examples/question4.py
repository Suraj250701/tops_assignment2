# Write a Python program to create a lambda function with two expressions.

multiply_func = lambda num1, num2: num1 * num2

usr_input1 = int(input("Enter first number: "))
usr_input2 = int(input("Enter second number: "))
print("Product of two numbers :", multiply_func(usr_input1, usr_input2))