def check_even_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"

# Call the function and store the result
result1 = check_even_odd(10)
print(f"10 is {result1}")

result2 = check_even_odd(7)
print(f"7 is {result2}")
