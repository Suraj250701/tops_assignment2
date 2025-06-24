# Write a Python program to update a value at a particular key in a dictionary.

student_info = {
    "name": "Suraj Singh",
    "age": 23,
    "Degree": "B.Tech",
    "major": "Information Technology",
    "university": "Ganpat University",
    "email": "surajsingh88597@gmail.com"
}

# key which value needs to be updated
usr_input = input("Enter the key you want to update (name, age, Degree, major, university, email): ")
new_value = input(f"Enter the new value for {usr_input}: ")
student_info[usr_input] = new_value

# Print the updated dictionary
print("Updated Student Information Dictionary : ")
for key, value in student_info.items():
    print(f"{key}: {value}")
