# Write a Python program to sort a list using both sort() and sorted().
usr_lst = []
lst_size = int(input("Enter the size of the list: "))
for i in range(lst_size):
    element = input(f"Enter element {i + 1}: ")
    usr_lst.append(element)

# Sorting the list using sort()
usr_lst.sort()
print("List after sort():", usr_lst)

# Sorting the list using sorted()
print("List after sorted():", sorted(usr_lst))
