import datetime

# Bonus: Add timestamp to make it realistic
time_now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# First action
with open("log.txt", "a") as file:
    file.write(f"[{time_now}] User logged in\n")

# Second action (simulating another event)
with open("log.txt", "a") as file:
    file.write(f"[{time_now}] User performed action\n")

print("Logs written. Current logs:\n")

# Read logs
try:
    with open("log.txt", "r") as file:
        print(file.read())
except FileNotFoundError:
    pass