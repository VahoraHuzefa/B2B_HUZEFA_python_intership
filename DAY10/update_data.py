student_record = {
    "Name": "John",
    "Age": 20,
    "Marks": 85.5
}

print(f"Original record: {student_record}")

# Update existing value
student_record["Marks"] = 92.0

# Add new key-value pair
student_record["Grade"] = "A"

print(f"Updated record: {student_record}")