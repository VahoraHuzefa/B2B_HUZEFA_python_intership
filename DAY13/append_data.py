new_name = input("Enter another name: ")

with open("user.txt", "a") as file:
    file.write(f"Name: {new_name}\n")

print("Data appended to user.txt successfully!")

# Let's read it back to verify
print("\nCurrent file contents:")
try:
    with open("user.txt", "r") as file:
        print(file.read())
except FileNotFoundError:
    pass
