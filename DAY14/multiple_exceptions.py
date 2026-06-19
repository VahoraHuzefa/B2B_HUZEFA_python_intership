try:
    num1 = float(input("Enter numerator: "))
    num2 = float(input("Enter denominator: "))
    
    result = num1 / num2
    print(f"Result: {result}")
    
except ValueError:
    print("Error: Input must be a valid number.")
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")