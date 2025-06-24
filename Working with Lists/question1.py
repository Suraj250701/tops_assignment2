# Write a Python program to iterate over a list using a for loop.

usr_lst = []
lst_size = int(input("Enter the size of the list: "))
for i in range(lst_size):
    element = input(f"Enter element {i + 1}: ")
    usr_lst.append(element)

# Iterating over the list using a for loop
for item in usr_lst:
    print(item)
    
