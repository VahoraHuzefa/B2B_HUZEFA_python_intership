from tkinter import *
from tkinter import ttk
import requests


def data_get():
    
      city = city_name.get()
 data= requests.get("https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=e2766dedfcfa4ceac8ef0afff9634de8").json()
      w_label7.config(text=data["weather"][0]["main"])
  wb_label7.config(text=data["weather"][0]["description"])
      temp_label7.config(text=str(int(data["main"]["temp"]-273.15)))
 per_label7.config(text=data["main"]["pressure"])



win = Tk()
win.title("Vahora Huzefa")
win.config(bg = "cyan")
win.geometry("500x570")

name_label = Label(win,text="Huzefa weather App",
                   font=("Time New Roman",32,"bold"))
name_label.place(x=25,y=50,height=50,width=450)                  

city_name = StringVar()
list_name = ["Andhra Pradesh","Arunachal Pradesh","Assam","Bihar","Chhattisgarh","Goa","Gujarat","Haryana","Himachal Pradesh","Jharkhand","Karnataka","Kerala","Madhya Pradesh","Maharashtra","Manipur","Meghalaya","Mizoram","Nagaland","Odisha","Punjab","Rajasthan","Sikkim","Tamil Nadu","Telangana","Tripura","Uttar Pradesh","Uttarakhand","West Bengal"]
com = ttk.Combobox(win, text="Huzefa weather App",values=list_name,
                    font=("Time New Roman", 20, "bold"),textvariable=city_name)
com.place(x=25,y=120,height=50,width=450)      



w_label = Label(win,text="weather climate",
                   font=("Time New Roman",20))
w_label.place(x=25,y=260,height=50,width=210)

w_label7 = Label(win,text="",
                   font=("Time New Roman",20))
w_label7.place(x=250,y=260,height=50,width=210)




wb_label = Label(win,text="weather Description",
                   font=("Time New Roman",17))
wb_label.place(x=25,y=330,height=50,width=210)

wb_label7 = Label(win,text="",
                   font=("Time New Roman",17))
wb_label7.place(x=250,y=330,height=50,width=210)




temp_label = Label(win,text="Temperature",
                   font=("Time New Roman",20,))
temp_label.place(x=25,y=400,height=50,width=210)

temp_label7 = Label(win,text="",
                   font=("Time New Roman",20,))
temp_label7.place(x=250,y=400,height=50,width=210)




per_label = Label(win,text="Pressure",
                   font=("Time New Roman",20,))
per_label.place(x=25,y=470,height=50,width=210)

per_label7 = Label(win,text="",
                   font=("Time New Roman",20,))
per_label7.place(x=250,y=470,height=50,width=210)


done_button = Button(win,text="Done",
                     font=("Time New Roman", 20, "bold"),command=data_get)
done_button.place(x=200,y=190,height=50,width=100)

win.mainloop()