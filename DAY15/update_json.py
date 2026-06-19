import json

try:
    # Step 1: Read the existing data
    with open("student.json", "r") as file:
        student = json.load(file)
        
    print(f"Original: {student}")
    
    # Step 2 & 3: Modify the Python dictionary
    student["marks"] = 95
    student["grade"] = "A"
    
    # Step 4: Write it back (overwriting the file)
    with open("student.json", "w") as file:
        json.dump(student, file, indent=4)
        
    print(f"Updated: {student}")
    print("Updates saved successfully!")

except FileNotFoundError:
    print("Error: Run task1_write_json.py first to create the file.")