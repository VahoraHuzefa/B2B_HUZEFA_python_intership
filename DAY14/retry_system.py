while True:
    try:
        age = int(input("Enter your age: "))
        break # This line only runs if the line above succeeds!
    except ValueError:
        print("Invalid input. Please enter numbers only.")

print(f"Thank you. Your age is {age}.")