numbers = [45, 10, 89, 3, 56, 90, 12]
print(f"List: {numbers}\n")

# --- Method 1: Using Built-in Functions ---
built_in_max = max(numbers)
built_in_min = min(numbers)
print("--- Method 1 (Built-in) ---")
print(f"Max = {built_in_max}")
print(f"Min = {built_in_min}\n")

# --- Method 2: Manual Logic with Loops ---
# Initialize largest and smallest with the first element
largest = numbers[0]
smallest = numbers[0]

# Loop through the list to compare
for num in numbers:
    if num > largest:
        largest = num
    if num < smallest:
        smallest = num

print("--- Method 2 (Manual Loop) ---")
print(f"Max = {largest}")
print(f"Min = {smallest}")
