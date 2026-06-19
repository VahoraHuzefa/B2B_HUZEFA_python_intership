import json

student_dict = {
    "name": "John1",
    "marks": 85
}

# Open file in write mode
with open("student1.json", "w") as file:
    # Dump the dictionary into the file
    json.dump(student_dict, file, indent=4)

print("Data successfully saved to student.json!")