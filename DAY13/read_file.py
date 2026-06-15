print("Reading from user.txt:\n" + "-"*20)

try:
    with open("user.txt", "r") as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("Error: The file 'user.txt' was not found. Run task 1 first!")