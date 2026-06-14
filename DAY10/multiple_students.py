students = [
    {"Name": "John", "Marks": 85},
    {"Name": "Alice", "Marks": 92},
    {"Name": "Bob", "Marks": 78}
]

# Loop through the list
for student in students:
    name = student["Name"]
    marks = student["Marks"]
    print(f"Student: {name}, Marks: {marks}")