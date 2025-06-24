# Write a Python program to separate keys and values from a dictionary using keys() and values() methods.

student_info = {
    "name": "Suraj Singh",
    "age": 23,
    "Degree": "B.Tech",
    "major": "Information Technology",
    "university": "Ganpat University",
    "email": "surajsingh88597@gmail.com"
}


keys = student_info.keys()
values = student_info.values()
print(f"Keys : , {list(keys)} \nValues: , {list(values)}")

