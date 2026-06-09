print("========================================")
print("   PYTHON SMART CALCULATOR   ")
print("========================================")

while True:
  print("\n--- Main Menu ---")
  print("1. Add (+)")
  print("2. Subtract (-)")
  print("3. Multiply (*)")
  print("4. Divide (/)")
  print("5. Exit")
  
  choice = input("Enter choice (1-5): ")
  
  # Check for exit first
  if choice == '5':
    print("\nThank you for using Smart Calculator. Goodbye! ")
    break
    
  # Validation of choices
  if choice in ['1', '2', '3', '4']:
    try:
      num1 = float(input("Enter first number: "))
      num2 = float(input("Enter second number: "))
    except ValueError:
      print(" Invalid input! Please enter numbers only.")
      continue
      
    if choice == '1':
      print(f"Result: {num1} + {num2} = {num1 + num2}")
    elif choice == '2':
      print(f"Result: {num1} - {num2} = {num1 - num2}")
    elif choice == '3':
      print(f"Result: {num1} * {num2} = {num1 * num2}")
    elif choice == '4':
      # Handling division by zero
      if num2 == 0:
        print(" Error: Division by zero is not allowed!")
      else:
        print(f"Result: {num1} / {num2} = {num1 / num2}")
  else:
    print(" Invalid Choice! Please choose a valid operation (1-5).")