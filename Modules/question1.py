# Write a Python program to import the math module and use functions like sqrt(), ceil(), floor().

import math

usr_num = float(input("Enter a number to find its square root, ceiling, and floor: "))
print(f"The square root of {usr_num} is: {math.sqrt(usr_num)}")
print(f"The ceiling of {usr_num} is: {math.ceil(usr_num)}")
print(f"The floor of {usr_num} is: {math.floor(usr_num)}")
