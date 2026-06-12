marks = int(input("Enter Marks: "))

if marks >= 90:
  grade = "A"
elif marks >= 80:
  grade = "B"
elif marks >= 70:
  grade = "C"
else:
  grade = "F"

print("Grade:", grade)
