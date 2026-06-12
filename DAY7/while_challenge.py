count = 0         # Tracks how many numbers were entered
number = -1       # Starting value, just to enter the loop (any non-zero number works)

print("Keep entering numbers. Enter 0 to stop.")
print("-" * 40)

while number != 0:
    number = int(input("Enter a number (0 to stop): "))
    
    if number != 0:
        print(f"  You entered: {number}")
        count += 1   # count += 1 is the same as count = count + 1

print("-" * 40)
print(f"You entered {count} number(s) before stopping.")