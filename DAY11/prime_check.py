def is_prime(number):
    if number <= 1:
        return False
        
    for i in range(2, number):
        if number % i == 0:
            return False # Found a divisor
            
    return True # No divisors found

num = int(input("Enter a number: "))

if is_prime(num):
    print("Prime")
else:
    print("Not Prime")