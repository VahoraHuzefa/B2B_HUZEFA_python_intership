print("--- Method 1: String Multiplication ---")
for i in range(1, 6):
    print("*" * i)

print()  # Blank line between methods

# Method 2: Using a nested loop (shows the concept step by step)
print("--- Method 2: Nested Loop ---")
for i in range(1, 6):       # Outer loop: row number
    for j in range(i):      # Inner loop: runs i times for row i
        print("*", end="")  # Print star without newline
    print()                 # After inner loop, move to next line
