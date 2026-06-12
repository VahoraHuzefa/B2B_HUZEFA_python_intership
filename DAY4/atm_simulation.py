balance = 5000

print("Welcome to Python Bank ATM")
print("1. Check Balance")
print("2. Withdraw Amount")

choice = int(input("Enter choice (1-2): "))

if choice == 1:
  print(f"Your Balance: {balance}")
elif choice == 2:
  withdraw_amount = float(input("Enter amount to withdraw: "))
  
  if withdraw_amount <= balance:
    balance = balance - withdraw_amount
    print("Transaction Successful")
    print(f"Remaining Balance: {int(balance)}")
  else:
    print("Insufficient Balance")
else:
  print("Invalid Choice")
