# Weather-App-Tkinter
How can you get openweathermap API key?

The API key is all you need to call any of our weather APIs. Once you sign up using your email, the API key (APPID) will be sent to you in a confirmation email. Your API keys can always be found on your account page, where you can also generate additional API keys if needed.

1.	Login or sign up into https://home.openweathermap.org/
2.	Then click on “API keys” and create new key.


Required packages and How to install: 

1. Tkinter:  Standard GUI library for python
    Installation:
    pip install tk

2. Matplotlib:  Python Package for data visualization
    Installation:
    pip install matplotlib 

3. Requests - Module which allows to send HTTP requests using Python
    Installation: 
    pip install requests

4. CSV Reader - The csv module's reader object allow us to write into the file
    from csv import reader    -    Write the data into csv file using reader
    import csv                   

5. PIL Image - The Image module allows us to load images from files.
    Installation:
    pip install Pillow

6. JSON - It is used to parse the JSON string using json.loads() and results in a python   
                 dictionary.
    Installation:
    pip install simplejson

7. Datetime - This module supplies classes for manipulating dates and times
    from datetime import datetime




Functionalities Used:

1.	Exception Handling:
•	Invalid city name: requests.exceptions.HTTPError:
•	Internet connection failure: requests.exceptions.ConnectionError:
•	Time out error: requests.exceptions.Timeout as errt:
•	Other exceptions: requests.exceptions.RequestException as err:

2.	Matplot Library:
•	Current Weather parameters plotting
•	7-Days forecasting of different parameters of Weather plotting

3.	CSV Reader/Writer:
•	Data stored in CSV file from Internet (API)
•	Data was converted from JSON format to .csv format
•	Data reading from CSV file for plotting graphs

4.	TKinter GUI:
•	Main window of interaction
•	Textbox, buttons, labels and other features are used to make application more interactable
•	Image feature is used for displaying symbols corresponding to weather conditions
 
Features of our Project:

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
6.	The Data Analysis of weather shown by the Application:-
•	Graph of 7-Days current temperature, min/max temperature, humidity, pressure.
 
Input and Output of Our project:
•	Run the weather.py into terminal. 
python weather.py
