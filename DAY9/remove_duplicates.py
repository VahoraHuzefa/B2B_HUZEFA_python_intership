original_list = [1, 2, 2, 3, 4, 4, 5, 1, 3]
print(f"Original List: {original_list}\n")

# --- Method 1: Using a Loop (Preserves Order) ---
unique_list = []
for item in original_list:
    if item not in unique_list:
        unique_list.append(item)

print("--- Method 1 (Loop) ---")
print(f"Clean List: {unique_list}\n")

# --- Method 2: Using set() (Simplest, doesn't guarantee order) ---
clean_set_list = list(set(original_list))
print("--- Method 2 (set) ---")
print(f"Clean List: {clean_set_list}")