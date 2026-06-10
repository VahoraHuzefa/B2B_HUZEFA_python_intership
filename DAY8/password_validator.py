password = input("Enter password: ")

# Check condition 1: Length
has_min_length = len(password) >= 8

# Check condition 2: Contains a digit
has_digit = False
for char in password:
    if char.isdigit():
        has_digit = True
        break  # Found a digit, no need to keep checking!

# Final validation check
if has_min_length and has_digit:
    print("Valid Password")
else:
    print("Invalid Password")
    # Helpful feedback for the user:
    if not has_min_length:
        print("  - Password must be at least 8 characters long.")
    if not has_digit:
        print("  - Password must contain at least one number.")