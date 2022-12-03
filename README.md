# Weather-App-Tkinter
### How can you get openweathermap API key?
The API key is all you need to call any of our weather APIs. Once you [sign up](https://home.openweathermap.org/users/sign_up) using your email, the API key (APPID) will be sent to you in a confirmation email. Your API keys can always be found on your [account page](https://home.openweathermap.org/api_keys), where you can also generate additional API keys if needed.
- Login or sign up into https://home.openweathermap.org/
- Then click on “API keys” and create new key.
![image](https://user-images.githubusercontent.com/61119120/119944037-69cb9b80-bfb1-11eb-95e3-24bf12ec2f8d.png)


https://api.openweathermap.org/data/2.5/onecall?lat=21.1667&lon=72.8333&appid=4c789006adcee867f33acd79750cfad3
https://api.openweathermap.org/data/2.5/weather?q=surat&appid=4c789006adcee867f33acd79750cfad3

## Required packages and How to install: 
1. Tkinter:  Standard GUI library for python
    ```
    pip install tk
    ```
2. Matplotlib: Python Package for data visualization
    ```
     pip install matplotlib 
    ```
3. Requests - Module which allows to send HTTP requests using Python
    ```
    pip install requests
    ```
4. CSV Reader - The csv module's reader object allow us to write into the file
   - from csv import reader    -    Write the data into csv file using reader
    ```
    import csv  
    ```
5. PIL Image - The Image module allows us to load images from files.
   ```
    pip install Pillow 
    ```
6. JSON - It is used to parse the JSON string using json.loads() and results in a python dictionary.
   ```
    pip install simplejson
    ```
7. Datetime - This module supplies classes for manipulating dates and times
    ```
    from datetime import datetime
    ```
    
## Functionalities Used:

### 1.	Exception Handling:
    •	Invalid city name: requests.exceptions.HTTPError:
    •	Internet connection failure: requests.exceptions.ConnectionError:
    •	Time out error: requests.exceptions.Timeout as errt:
    •	Other exceptions: requests.exceptions.RequestException as err:
    
### 2.	Matplot Library:
    •	Current Weather parameters plotting
    •	7-Days forecasting of different parameters of Weather plotting

### 3.	CSV Reader/Writer:
    •	Data stored in CSV file from Internet (API)
    •	Data was converted from JSON format to .csv format
    •	Data reading from CSV file for plotting graphs

### 4.	TKinter GUI:
    •	Main window of interaction
    •	Textbox, buttons, labels and other features are used to make application more interactable
    •	Image feature is used for displaying symbols corresponding to weather conditions
    

## Features of our Project:
    1.	It is an interactive GUI which is very User-Friendly.
    2.	User can enter City’s name whose weather information they want see.
    3.	It checks whether city name is correct or not.
    4.	It also checks for internet connection or any timeout error.
    5.	The following are the data shown by the Application: -
            •	Day-Date
            •	Current Temperature
            •	Min/Max temperature
            •	Weather description.
            •	Corresponding Weather icon
            •	Humidity
            •	Windspeed
            •	UV-Index
            •	Pressure.
            •	4-Days forecast of:
                    o	Temperature
                    o	Weather description
                    o	Corresponding Weather icon.
    6.	The Data Analysis of weather shown by the Application:
            •	Graph of 7-Days current temperature, min/max temperature, humidity, pressure.

# Input and Output of Our project:
    •	Run the weather.py into terminal. 
            python weather.py
            
### Input: Melbourne
### Output: 
![2021-04-11_Melbourne](https://user-images.githubusercontent.com/70934443/119979403-87602b80-bfd8-11eb-905a-fbcb37690b98.png) 
![Plot_temp](https://user-images.githubusercontent.com/70934443/119979506-aeb6f880-bfd8-11eb-9dd8-4fb45d06735d.png) 
![Plot_Pressure](https://user-images.githubusercontent.com/70934443/119979527-b5457000-bfd8-11eb-9671-c0d04e2bb021.png) 
![Plot_humidity](https://user-images.githubusercontent.com/70934443/119979544-b9718d80-bfd8-11eb-8400-e1b66c5c0dc6.png)

### Input: London
### Output: 
![2021-04-11_London](https://user-images.githubusercontent.com/70934443/119979894-2553f600-bfd9-11eb-9156-d4276d20bdba.png)
![Plot_temp](https://user-images.githubusercontent.com/70934443/119979907-2a18aa00-bfd9-11eb-81eb-3f66a9dda564.png)
![Plot_pressure](https://user-images.githubusercontent.com/70934443/119979920-2f75f480-bfd9-11eb-91c7-513dcb2d16c7.png)
![Plot_humidity](https://user-images.githubusercontent.com/70934443/119979960-3e5ca700-bfd9-11eb-9a58-5e0856cbb54d.png)

