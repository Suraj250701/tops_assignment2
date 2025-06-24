# Write a Python program to remove elements from a list using pop() and remove().

usr_lst = []
lst_size = int(input("Enter the size of the list: "))
for i in range(lst_size):
    element = input(f"Enter element {i + 1}: ")
    usr_lst.append(element)

print("Original list:", usr_lst)

# Removing elements using pop()
usr_append = input("Enter an element to pop from the list: ")
if usr_append not in usr_lst:
    print("Element not in the list.")
else:
    usr_lst.remove(usr_append)
    print("List after pop:", usr_lst)

# Removing elements using remove()
usr_index = int(input(f"Enter the index of the element you want to remove (0 to {len(usr_lst) - 1}): "))
if usr_index < 0 or usr_index >= len(usr_lst):
    print("Index out of range. Please enter a valid index.")
else:
    usr_lst.pop(usr_index)
    print("List after remove:", usr_lst)
