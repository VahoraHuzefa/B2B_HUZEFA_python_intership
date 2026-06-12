numbers = [10, 20, 30, 40, 50]
print(f"List: {numbers}\n")

# --- Method 1: Built-in function ---
built_in_sum = sum(numbers)
print("--- Method 1 (Built-in) ---")
print(f"Total = {built_in_sum}\n")

# --- Method 2: Manual Loop ---
total = 0
for num in numbers:
    total += num  # Add each element to total

print("--- Method 2 (Manual Loop) ---")
print(f"Total = {total}")
