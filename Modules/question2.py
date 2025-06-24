# Write a Python program to generate random numbers using the random module.
import random
usr_num = int(input("Enter the number of random numbers to generate: "))
random_numbers = [random.randint(1, 1000) for i in range(usr_num)]
print("Generated numbers:", random_numbers)