import requests

url = "https://jsonplaceholder.typicode.com/posts"

response = requests.get(url)

if response.status_code == 200:
    posts = response.json() # This is a LIST of dictionaries
    
    print("--- Top 5 Latest Headlines ---")
    
    # Loop through the first 5 items using slicing
    for index, post in enumerate(posts[:5], start=1):
        # post["title"] accesses the title key of the current dictionary
        print(f"{index}. {post['title'].title()}")
else:
    print("Failed to fetch news data.")