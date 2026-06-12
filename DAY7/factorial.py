n = int(input("Enter a number: "))
result = 1  # Accumulator must start at 1 for multiplication!

for i in range(1, n + 1):
    result = result * i

print(f"Factorial = {result}")