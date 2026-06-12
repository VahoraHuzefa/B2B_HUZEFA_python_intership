number = input("Enter a number: ")

# Method 1: Using Python String Slicing (Easy & Powerful!)
reversed_number = number[::-1]
print("Reversed (String Slicing):", reversed_number)

# Method 2 (Bonus): Using Mathematical logic (Loop-based)
num_val = int(number)
rev_val = 0

while num_val > 0:
  last_digit = num_val % 10
  rev_val = (rev_val * 10) + last_digit
  num_val = num_val // 10

print("Reversed (Mathematical):", rev_val)
