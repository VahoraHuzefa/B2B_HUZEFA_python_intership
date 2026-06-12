age = int(input("Enter your age: "))
has_id = input("Do you have a valid ID? (yes/no): ").lower()

if age > 18 and has_id == "yes":
  print("Eligible")
else:
  print("Not Eligible")