# Write a Python program to count how many times each character appears in a string.

def count_characters(input_string):
    char_count = {}
    for char in input_string:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count

user_input = input("Enter a string: ")
result = count_characters(user_input)

print("Character count:")
for char, count in result.items():
    print(f"'{char}': {count}")

