numbers = [12, 45, 78, 23, 56, 89]
print(f"Available numbers: {numbers}")

target = int(input("Enter number to search: "))

# --- Method 1: Using 'in' operator ---
print("\n--- Method 1 (in Operator) ---")
if target in numbers:
    # .index(value) returns the index of the first occurrence of that value
    position = numbers.index(target)
    print(f"Found at index {position}!")
else:
    print("Not Found")

# --- Method 2: Manual Loop (Linear Search) ---
print("\n--- Method 2 (Manual Loop) ---")
found = False
found_index = -1

for i in range(len(numbers)):
    if numbers[i] == target:
        found = True
        found_index = i
        break  # Exit loop immediately since we found it

if found:
    print(f"Found at index {found_index}!")
else:
    print("Not Found")
