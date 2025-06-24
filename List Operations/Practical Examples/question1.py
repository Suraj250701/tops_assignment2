# Write a Python program to update a list using insert() and append().

usr_lst = []
lst_size = int(input("Enter the size of the list: "))
for i in range(lst_size):
    element = input(f"Enter element {i + 1}: ")
    usr_lst.append(element)

print("Original list:", usr_lst)

# Updating the list using append()
usr_append = input("Enter an element to append to the list: ")
usr_lst.append(usr_append)
print("List after append:", usr_lst)

# Updating the list using insert()
usr_index = int(input(f"Enter the index at which you want to insert item within range of 0 to {len(usr_lst) - 1}: "))
if usr_index < 0 or usr_index >= len(usr_lst):
    print("Index out of range. Please enter a valid index.")
else:
    usr_input = input("Enter the element to insert: ")
    usr_lst.insert(usr_index, usr_input)
    print("List after insert:", usr_lst)
    