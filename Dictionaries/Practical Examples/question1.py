# Write a Python program to create a dictionary of 6 key-value pairs.

student_info = {
    "name": "Suraj Singh",
    "age": 23,
    "Degree": "B.Tech",
    "major": "Information Technology",
    "university": "Ganpat University",
    "email": "surajsingh88597@gmail.com"
}

print("Student Information Dictionary : ")
for key, value in student_info.items():
    print(f"{key}: {value}")
print("\nStudent Information Dictionary : ", student_info)
