import json

try:
    with open("student.json", "r") as file:
        data = json.load(file)
        
    print("--- Reading JSON Data ---")
    print(f"Name: {data['name']}")
    print(f"Marks: {data['marks']}")

except FileNotFoundError:
    print("Error: 'student.json' not found. Please run task1_write_json.py first.")
except json.JSONDecodeError:
    print("Error: The file is not a valid JSON format.")