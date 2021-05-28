"""
--------------------------------------------------
            Weather App - Tkinter GUI
--------------------------------------------------
"""
import matplotlib.pyplot as plt
import PIL.Image
from PIL import ImageTk
from tkinter import *
from tkinter import messagebox
import tkinter as tk
import requests
import json
from csv import reader
import csv
from datetime import datetime

x = datetime.now() # Configure Date and time
weekday_short = x.strftime("%a") # Getting Day i.e., Mon , Tue , Wed ......
weekday_long = x.strftime("%A") # Getting Day i.e., Monday , Tuesday , Wednesday ......
today_date = x.strftime("%d/%m/%y") # Getting current date

user_api = "4c789----------------------cfad3" #take API of Weather from "https://openweathermap.org/api" 

# Defining the window dimension
height = 650 
width = 406
root = tk.Tk()
root.title("Weather")
root.resizable(height=False, width=False)
canvas = tk.Canvas(root, height=height, width=width, bg="#76D5DB")
canvas.pack()

# City Name label
mini = Label(root, text="CITY:", width=0, bg='#76D5DB', font=("bold",13),fg="#154B5C")
mini.place(x=34, y=28)

# City name textbox
city_n=tk.StringVar()
city=Entry(root,font=30,textvariable=city_n,bg='#F7F7F7',relief="flat",fg="#1489AE")
city.place(x=85, y=23,relwidth=0.5,relheight=0.05)
edit = Entry(city,font=30,relief="flat",fg="#008B8B")

# A user defined function for plotting various graphs
def PLOT_GRAPH(city_name):
    Plot_row = []
    with open('Plot_data.csv', 'r') as read_obj: #Reading Plot_data csv file
        csv_reader = reader(read_obj)
        next(csv_reader)
        for row in csv_reader:
            if len(row) != 0:
                Plot_row.append(row)
    
    # Defining different list for storing the data
    temp = [] 
    temp_min = []
    temp_max = []
    pressure = []
    humidity = []
    day = []
    date = []
    day_date = []

    # For loop for storing different datas from the CSV File 
    for i in range(1,8):
        date.append(Plot_row[i][0])
        day.append(Plot_row[i][1])
        temp.append(float(Plot_row[i][2]))
        temp_min.append(float(Plot_row[i][3]))
        temp_max.append(float(Plot_row[i][4]))
        pressure.append(int(Plot_row[i][5]))
        humidity.append(int(Plot_row[i][6]))

    # For loop for concatenating the day and date
    # For eg : "Sun" + "11/04" = "Sun\n11/04" 
    for i in range(7):
        day_date.append(str(day[i])+"\n"+str(date[i]))
    
    # Plotting a PyPlot which contains the Temperature, Minimum Temperature and Maximum Temperature of next 7 days
    plt.grid(True)
    plt.plot(day_date,temp,marker = 'o',label = "Avg. Temp")
    plt.plot(day_date,temp_max,marker = 'o', color = 'r', label = "Max. Temp")
    plt.plot(day_date,temp_min,marker = 'o', color = 'g', label = "Min. Temp")
    plt.legend(loc=2)
    plt.xlabel("Day")
    plt.ylabel("Temperature(°C)")
    plt.title(today_date+" "+weekday_long+"\nSeven days Forecasting(Temp) : "+city_name) 
    x=min(temp_min)-2
    y=max(temp_max)+8
    plt.ylim(x,y)
    plt.show()
    
    # Plotting a PyPlot which contains the Pressure of next 7 days
    plt.grid(True)
    plt.plot(day_date,pressure,marker = 'o')
    plt.xlabel("Day")
    plt.ylabel("Pressure(mbar)")
    plt.title(today_date+" "+weekday_long+"\nSeven days Forecasting(Pressure) : "+city_name) 
    plt.show()

    # Plotting a PyPlot which contains the Humidity of next 7 days
    plt.grid(True)
    plt.plot(day_date,humidity,marker = 'o')
    plt.xlabel("Day")
    plt.ylabel("Humidity(%)")
    plt.title(today_date+" "+weekday_long+"\nSeven days Forecasting(Humidity) : "+city_name)
    plt.show()
    

# A user defined function for fetching data from the API for analyzing the data and storing it locally
def city_name():
    # Exception handling block for the requests 
    try:
        complete_api_link_1 = "https://api.openweathermap.org/data/2.5/weather?q=" + city.get() + "&appid=" + user_api
        api_link_1 = requests.get(complete_api_link_1)
        api_link_1.raise_for_status()
            
        # Storing API data in variable
        api_data_1 = api_link_1.json()

        # Storing the longitude and latitude in variable for another API request
        lon = api_data_1["coord"]['lon']
        lat = api_data_1["coord"]['lat']

        # Fetching more data from another API using latitude and longitude
        complete_api_link_2 = "https://api.openweathermap.org/data/2.5/onecall?lat="+str(lat)+"&lon="+str(lon)+"&appid="+user_api
        api_link_2 = requests.get(complete_api_link_2)
        api_link_2.raise_for_status()
        
        # Storing API data in variable
        api_data_2 = api_link_2.json()
    except requests.exceptions.HTTPError:
        messagebox.showerror("Error", "City not found")
        return
    except requests.exceptions.ConnectionError:
        messagebox.askretrycancel("Warning", "Please check your internet connection")
        return
    except requests.exceptions.Timeout as errt:
        messagebox.askretrycancel("Warning", "Timeout error")
        return
    except requests.exceptions.RequestException as err:
        messagebox.askretrycancel("Warning", "Something Wrong")
        return

    
    # Storing different data in their respective variable 
    city_name = api_data_1['name']
    current_temperature = str(int(api_data_1['main']['temp'] - 273.15)) + "°C"
    feels_like = api_data_1['main']['feels_like']
    humidity = str(api_data_1['main']['humidity'])+"%"
    windspeed = str(api_data_1['wind']['speed']) + " m/s"
    tempmin = str("{:.2f}".format(api_data_2['daily'][0]['temp']['min']- 273.15))+ "°C"
    tempmax = str("{:.2f}".format(api_data_2['daily'][0]['temp']['max']- 273.15))+ "°C"
    description = api_data_1['weather'][0]['main']
    icon = api_data_1['weather'][0]['icon']
    timezone = api_data_2['timezone']
    uvi = str(api_data_2['current']['uvi'])
    pressure = str(api_data_1['main']['pressure']) + " mbar"

    # Displaying different icons for the respective weather conditions
    image=PIL.Image.open(f"icon\\{icon}.png")
    image = image.resize((150, 150), PIL.Image.ANTIALIAS)
    img1 = ImageTk.PhotoImage(image)
    label = Label(image=img1)
    label.image = img1
    label['bg'] = '#76D5DB'
    label.place(x=220,y=112)

    # Configuring different labels
    cityGet = city.get()
    city_view.configure(text=city_name)
    description_view.configure(text=description)
    wind_speed_view.configure(text=windspeed)
    label_temp.configure(text=current_temperature)
    label_humidity.configure(text=humidity)
    max_temp.configure(text=tempmax)
    min_temp.configure(text=tempmin)
    uvi_data.configure(text=uvi)
    pressure_data.configure(text=pressure)


    #Writing Today's weather data in Today_data CSV file
    with open('Today_data.csv', mode='w') as file: 
        writer = csv.writer(file, delimiter=',')
        writer.writerow([today_date,weekday_short,'',"City : ",api_data_1['name']])
        writer.writerow(["Temperature",'',current_temperature])
        writer.writerow(["Description",'',description])
        writer.writerow(["Windspeed",'',windspeed])
        writer.writerow(["Humidity",'',humidity])
        writer.writerow(["Max Temperature",'',tempmax])
        writer.writerow(["Min Temperature",'',tempmin])
        writer.writerow(["Uvi",'',uvi])
        writer.writerow(["Pressure",'',pressure])

    # Writing Forecasting data in Forecasting_data CSV file
    with open('Forecasting_data.csv', mode='w') as file:
        writer = csv.writer(file, delimiter=',')
        writer.writerow([today_date,weekday_short,'',"City : ",api_data_1['name']])
        for i in range(8):
            dt = api_data_2['daily'][i]['dt']
            date = datetime.fromtimestamp(dt)
            day_T = date.strftime("%a")
            date_T = date.strftime("%d")
            day_Temp = str("{:.1f}".format(api_data_2['daily'][i]['temp']['day']- 273.15))+ "°C"
            icon_T = api_data_2['daily'][i]['weather'][0]['icon']
            description_T = api_data_2['daily'][i]['weather'][0]['main']
            writer.writerow([day_T,date_T,icon_T,description_T,day_Temp])

    # Writing the data needed for plotting Temperature, Pressure, Humidity in Plot_data CSV file
    with open('Plot_data.csv', mode='w') as file:
        writer = csv.writer(file, delimiter=',')
        writer.writerow([today_date,weekday_short,'',"City : ",api_data_1['name']])
        for i in range(8):
            dt = api_data_2['daily'][i]['dt']
            date = datetime.fromtimestamp(dt)
            day_T = date.strftime("%a")
            date_T = date.strftime("%d/%m")
            day_Temp = "{:.2f}".format(api_data_2['daily'][i]['temp']['day']- 273.15)
            min_Temp = "{:.2f}".format(api_data_2['daily'][i]['temp']['min']- 273.15)
            max_Temp = "{:.2f}".format(api_data_2['daily'][i]['temp']['max']- 273.15)
            pressure_T = api_data_2['daily'][i]['pressure']
            humidity_T = api_data_2['daily'][i]['humidity']
            writer.writerow([date_T,day_T,day_Temp,min_Temp,max_Temp,pressure_T,humidity_T])

    # Reading the Forecasting_data CSV File for displaying the data in Tkinter Window
    forecastingData = []
    with open('Forecasting_data.csv', 'r') as read_obj:
        csv_reader = reader(read_obj)
        next(csv_reader)
        for row in csv_reader:
            if len(row) != 0:
                forecastingData.append(row)

    # Displaying Day 1 data
    day_T_1.configure(text=forecastingData[1][0])
    desc_T_1.configure(text=forecastingData[1][3])
    temp_T_1.configure(text=forecastingData[1][4])
    image=PIL.Image.open(f"icon\\{forecastingData[1][2]}.png")
    img1 = ImageTk.PhotoImage(image)
    label = Label(image=img1)
    label.image = img1
    label['bg'] = '#76D5DB'
    label.place(x=2,y=510)

    # Displaying Day 2 data
    day_T_2.configure(text=forecastingData[2][0])
    desc_T_2.configure(text=forecastingData[2][3])
    temp_T_2.configure(text=forecastingData[2][4])
    image=PIL.Image.open(f"icon\\{forecastingData[2][2]}.png")
    img1 = ImageTk.PhotoImage(image)
    label = Label(image=img1)
    label.image = img1
    label['bg'] = '#76D5DB'
    label.place(x=102,y=510)

    # Displaying Day 3 data
    day_T_3.configure(text=forecastingData[3][0])
    desc_T_3.configure(text=forecastingData[3][3])
    temp_T_3.configure(text=forecastingData[3][4])
    image=PIL.Image.open(f"icon\\{forecastingData[3][2]}.png")
    img1 = ImageTk.PhotoImage(image)
    label = Label(image=img1)
    label.image = img1
    label['bg'] = '#76D5DB'
    label.place(x=202,y=510)

    # Displaying Day 4 data
    day_T_4.configure(text=forecastingData[4][0])
    desc_T_4.configure(text=forecastingData[4][3])
    temp_T_4.configure(text=forecastingData[4][4])
    image=PIL.Image.open(f"icon\\{forecastingData[4][2]}.png")
    img1 = ImageTk.PhotoImage(image)
    label = Label(image=img1)
    label.image = img1
    label['bg'] = '#76D5DB'
    label.place(x=302,y=510)

    # Displaying the currrent Day and Date on the Tkinter window
    date_str = x.strftime("%d") + " " + x.strftime("%B") + " " + x.strftime("%Y") +  "\t       " + x.strftime("%A") 
    date_view = Label(root, text=date_str , width=0, bg='#76D5DB', font=("bold", 18),fg="#41696F")
    date_view.place(x=10, y=70)

    canvas.create_line(0,111,406,111,fill = "#008B8B") # For creating a horizontal line

    # Displaying different text on the Tkinter window
    mini = Label(root, text="Min Temp", width=0, bg='#76D5DB', font=("bold", 10),fg="#22947D")
    mini.place(x=10, y=290)
    maxi = Label(root, text="Max Temp", width=0, bg='#76D5DB', font=("bold", 10),fg="#22947D")
    maxi.place(relx=0.5, y=290)
    humi = Label(root, text="Humidity", width=0, bg='#76D5DB', font=("bold", 10),fg="#22947D")
    humi.place(x=10, y=340)
    wind_speed = Label(root, text="Wind Speed", width=0, bg='#76D5DB', font=("bold", 10),fg="#22947D")
    wind_speed.place(relx=0.5, y=340)
    uv_name = Label(root, text="UV Index", width=0, bg='#76D5DB', font=("bold", 10),fg="#22947D")
    uv_name.place(x=10,y=390)
    pressure_name = Label(root, text="Pressure", width=0, bg='#76D5DB', font=("bold", 10),fg="#22947D")
    pressure_name.place(relx=0.5,y=390)
    canvas.create_line(0,450,406,450,fill = "#008B8B")

    # Calling the PLOT_GRAPH function
    PLOT_GRAPH(city_name)

# Search Button 
button=Button(root,command = city_name,relief="flat",text='Search',fg="#1489AE",bg='#F7F7F7',font=('arial', 13, 'normal')).place(x=294, y=23)


# Displaying different values on the Tkinter window
city_view = Label( root , width=0 , bg='#76D5DB' , font=("Helvetica", 20), fg='#154B5C')
city_view.place(x=10,y=125)

description_view = Label( root , width=0 , bg='#76D5DB' , font=("Helvetica", 11), fg='#154B5C' )
description_view.place(x=10,y=162)

label_temp = Label(root, width=0, bg='#76D5DB', font=("Helvetica", 60), fg='#154B5C')
label_temp.place(x=10,y=180)

min_temp = Label(root, width=0, bg='#76D5DB', font=("bold", 15),fg='#154B5C')
min_temp.place(x=10,y=310)

max_temp = Label(root, width=0, bg='#76D5DB', font=("bold", 15),fg='#154B5C')
max_temp.place(relx=0.5, y=310)

label_humidity = Label(root, width=0, bg='#76D5DB', font=("bold", 15),fg='#154B5C')
label_humidity.place(x=10, y=360)

wind_speed_view = Label(root, width=0, bg='#76D5DB', font=("bold", 15),fg='#154B5C')
wind_speed_view.place(relx=0.5, y=360)

uvi_data = Label(root, width=0, bg='#76D5DB', font=("bold", 15),fg='#154B5C')
uvi_data.place(x=10,y=410)

pressure_data = Label(root, width=0, bg='#76D5DB', font=("bold", 15),fg='#154B5C')
pressure_data.place(relx=0.5,y=410)

# Displaying the next 4 days forecasting data on the Tkinter Window 
day_T_1 = Label(root, width=0, bg='#76D5DB', font=("bold", 14),fg='#154B5C')
day_T_1.place(x=30,y=468)
desc_T_1 = Label(root, width=0, bg='#76D5DB', font=("bold", 9),fg='#1F8594')
desc_T_1.place(x=30,y=492)
temp_T_1 = Label(root, width=0, bg='#76D5DB', font=("bold", 13),fg='#154B5C')
temp_T_1.place(x=30,y=620)
day_T_2 = Label(root, width=0, bg='#76D5DB', font=("bold", 14),fg='#154B5C')
day_T_2.place(x=130,y=468)
desc_T_2 = Label(root, width=0, bg='#76D5DB', font=("bold", 9),fg='#1F8594')
desc_T_2.place(x=130,y=492)
temp_T_2 = Label(root, width=0, bg='#76D5DB', font=("bold", 13),fg='#154B5C')
temp_T_2.place(x=130,y=620)
day_T_3 = Label(root, width=0, bg='#76D5DB', font=("bold", 14),fg='#154B5C')
day_T_3.place(x=230,y=468)
desc_T_3 = Label(root, width=0, bg='#76D5DB', font=("bold", 9),fg='#1F8594')
desc_T_3.place(x=230,y=492)
temp_T_3 = Label(root, width=0, bg='#76D5DB', font=("bold", 13),fg='#154B5C')
temp_T_3.place(x=230,y=620)
day_T_4 = Label(root, width=0, bg='#76D5DB', font=("bold", 14),fg='#154B5C')
day_T_4.place(x=330,y=468)
desc_T_4 = Label(root, width=0, bg='#76D5DB', font=("bold", 9),fg='#1F8594')
desc_T_4.place(x=330,y=492)
temp_T_4 = Label(root, width=0, bg='#76D5DB', font=("bold", 13),fg='#154B5C')
temp_T_4.place(x=330,y=620)

root.mainloop()