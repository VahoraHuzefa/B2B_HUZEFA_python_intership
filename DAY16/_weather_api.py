import requests

url = "https://api.open-meteo.com/v1/forecast?latitude=51.5085&longitude=-0.1257&current_weather=true"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    
    # Accessing nested dictionaries
    current_temp = data["current_weather"]["temperature"]
    
    print(f"Temperature in London: {current_temp}°C")
else:
    print("Failed to fetch weather data.")