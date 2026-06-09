number_str = input("Enter a number: ")

# Method 1: Using character loop
digit_sum = 0
for char in number_str:
  digit_sum = digit_sum + int(char)

print("Sum of digits (Loop):", digit_sum)

# Method 2 (Bonus): Using Mathematical logic (Modulo & Division)
num_val = int(number_str)
math_sum = 0

while num_val > 0:
  last_digit = num_val % 10
  math_sum = math_sum + last_digit
  num_val = num_val // 10

print("Sum of digits (Mathematical):", math_sum)
