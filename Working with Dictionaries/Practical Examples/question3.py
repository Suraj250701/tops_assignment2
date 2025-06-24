# Write a Python program to convert two lists into one dictionary using a for loop

keys = ["name", "age", "Degree", "major", "university", "email"]
values = ["Suraj Singh", 23, "B.Tech", "Information Technology", "Ganpat University", "surajsingh88597@gmail.com"]

student_info = {}
for i in range(len(keys)):
    student_info[keys[i]] = values[i]

print("Student Information : ")
for key, value in student_info.items():
    print(f"{key}: {value}")
print("\nStudent Information : ", student_info)