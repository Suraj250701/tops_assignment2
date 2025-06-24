# Write a Python program to iterate through a list and print each element.

usr_lst = []
lst_size = int(input("Enter the size of the list: "))
for i in range(lst_size):
    element = input(f"Enter element {i + 1}: ")
    usr_lst.append(element)

# printing each element
for item in usr_lst:
    print(item)
