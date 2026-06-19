import json

try:
    with open("students_list.json", "r") as file:
        students = json.load(file)
        
    search_name = input("Enter student name to search: ")
    found = False
    
    for student in students:
        if student["name"].lower() == search_name.lower():
            print("\nStudent Found!")
            print(f"Marks: {student['marks']}")
            found = True
            break
            
    if not found:
        print("\nStudent not found.")

except FileNotFoundError:
    print("Error: 'students_list.json' not found. Run task 3 first.")