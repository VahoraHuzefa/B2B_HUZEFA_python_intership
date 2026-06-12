name = input("Enter your name: ")
city = input("Enter your city: ")

# Standardize values using string methods
formatted_name = name.strip().title()
formatted_city = city.strip().title()

# Format the final string
message = f"My name is {formatted_name} and I live in {formatted_city}"

print(message)