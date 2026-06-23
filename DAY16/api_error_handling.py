import requests

url = "https://invalid-url-example.com/api"

print(f"Attempting to connect to: {url}")

try:
    # timeout=5 ensures the program doesn't hang forever if the site is slow
    response = requests.get(url, timeout=5)
    
    if response.status_code == 200:
        print("Success! Data fetched.")
    else:
        print(f"Server returned error code: {response.status_code}")
        
except requests.exceptions.RequestException as e:
    # This catches ANY error related to the requests library (ConnectionError, Timeout, etc.)
    print("Error fetching data. Please check your internet connection or the URL.")