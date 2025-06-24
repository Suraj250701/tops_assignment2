# Write a Python program to generate random numbers between 1 and 100 using the random module.
import random
usr_num = int(input("Enter the number of random numbers to generate: "))
random_numbers = [random.randint(1, 100) for i in range(usr_num)]
print("Generated numbers between 1 and 100:", random_numbers)