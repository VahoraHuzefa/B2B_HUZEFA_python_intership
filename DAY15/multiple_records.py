import json

# Python List containing multiple Dictionaries
students = [
    {"name": "John", "marks": 85},
    {"name": "Alice", "marks": 92},
    {"name": "Bob", "marks": 78}
]

# Write to JSON
with open("students_list.json", "w") as file:
    json.dump(students, file, indent=4)
print("Saved 3 students to students_list.json")

# Read back from JSON
print("\n--- Reading Data Back ---")
with open("students_list.json", "r") as file:
    loaded_data = json.load(file)
    
# Loop through the list we just loaded
for student in loaded_data:
    print(f"{student['name']} scored {student['marks']}")
