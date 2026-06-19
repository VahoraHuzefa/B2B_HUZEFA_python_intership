from tkinter import *
from tkinter import ttk
import requests

city_name ="Mumbai"
data = requests.get("https://api.openweathermap.org/data/2.5/weather?q="+city_name+"&appid=e2766dedfcfa4ceac8ef0afff9634de8").json()
print(data)