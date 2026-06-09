n = int(input("Enter value of n: "))
total = 0  # Accumulator starts at zero

for i in range(1, n + 1):  # range(1, n+1) so that i goes up to n (inclusive)
    total = total + i       # Add each number to total

print(f"Sum = {total}")
