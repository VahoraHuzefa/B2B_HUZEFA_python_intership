age = int(input("Enter age: "))

if age < 12:
  print("Ticket Category: Child")
  print("Price: Rs 100")
elif age < 60:
  print("Ticket Category: Adult")
  print("Price: Rs 250")
else:
  print("Ticket Category: Senior")
  print("Price: Rs 150")