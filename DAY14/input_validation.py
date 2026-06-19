try:
    age = int(input("Enter your age: "))
    print(f"You are {age} years old.")
except ValueError:
    print("Error: Please enter a valid numerical age (e.g., 20).")