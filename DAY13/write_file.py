name = input("Enter your name: ")

with open("user.txt", "w") as file:
    file.write(f"Name: {name}\n")

print("Data saved to user.txt successfully!")