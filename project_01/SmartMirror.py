#-*- coding: utf-8 -*-
"""
--------------------------------------------------------------------------
Smart Mirror
--------------------------------------------------------------------------
License:   
Copyright 2021 Nneoma Ome

Redistribution and use in source and binary forms, with or without 
modification, are permitted provided that the following conditions are met:

1. Redistributions of source code must retain the above copyright notice, this 
list of conditions and the following disclaimer.

2. Redistributions in binary form must reproduce the above copyright notice, 
this list of conditions and the following disclaimer in the documentation 
and/or other materials provided with the distribution.

3. Neither the name of the copyright holder nor the names of its contributors 
may be used to endorse or promote products derived from this software without 
specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" 
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE 
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE 
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE 
FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL 
DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR 
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER 
CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, 
OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE 
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
--------------------------------------------------------------------------

Smart mirror that will:
  - Use unique city ID to retreive daily weather forecast
  - Use inputted url to retreive daily news updates from internet
  - Output the relevant information to the user using alerts and windows in a GUI
Error conditions:
  - Alert Message not closed --> Cannot re-run program in Cloud9 terminal
  - Window not closed --> Cannot re-run program in Cloud9 terminal
  
--------------------------------------------------------------------------
"""

#Import necessary packages for retrieving weather data
from pyowm import OWM

#Import necessary packages for retrieving news data
import requests 
from bs4 import BeautifulSoup
import json
import datetime
import textwrap

#Import necessary packages for creating GUI
import sys
from PyQt5.QtWidgets import *


#-------------------------------------------------------------------------------
# Get weather data for city
#-------------------------------------------------------------------------------

# Retrieve weather information from OpenWeatherMap API
API_key = '7c564fe1392176d69668415db351e21b' #insert your unique API key
owm = OWM(API_key)

my_city_id = 4699066 #insert unique city ID
obs = owm.weather_at_id(my_city_id)

w = obs.get_weather() # Get current, low, and high temperature
temp = w.get_temperature('fahrenheit') #Covert from Kelvin to Farenheit

#Create Farenheit symbol
m_symbol = '\xb0' + 'F'

#Set up strings for displaying the daily forecast
curr = "Current Temp: {0} {1}".format(temp['temp'], m_symbol)
high = "Daily High: {0} {1}".format(temp['temp_max'], m_symbol)
low = "Daily Low: {0} {1}".format(temp['temp_min'], m_symbol)

#Combined string with headline
weather = "Todays Weather\n{0}\n{1}\n{2}\n".format(curr,high,low) 


#-------------------------------------------------------------------------------
# Get news updates 
#-------------------------------------------------------------------------------

url = "https://www.nytimes.com/" #news website url
headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/601.3.9 (KHTML, like Gecko) Version/9.0.2 Safari/601.3.9'}

r   = requests.get(url, headers=headers) #Retrieve data from New York Times
now = datetime.datetime.now() #Retreives current date and time
now = now.strftime('%A, %B %d, %I:%M %p') #convert date and tijme to string

#Initialize varizbles
r_html = r.text 
article = [] 
count = 0 #Initialize counter

soup=BeautifulSoup(r_html,'lxml') #Parses html 
for item in soup.select('.story-wrapper'): #Search for story wrapper key word in NYT text
    try: 
        headline = item.find('h3').get_text() #Search for h3 heading to locate headlines
        article.append(headline) #Adds headlines to list
        count += 1
    except Exception as e: 
        pass
    if count > 10: #Breaks loop after the first 10 headlines
        break 


#Set up strings for displaying the news headlines
header  = ('%s\n%s\n\nHeadlines\n' %(now, url)) #creates header with date, time, website url, and title 
 
H1 = article[1] #Separates each element of list into individual variable
H2 = article[2]
H3 = article[3]
H4 = article[4]
H5 = article[5]
H6 = article[6]
H7 = article[7]
H8 = article[8]
H9 = article[9]
H10 = article[10]

#Combined string with header
news = "{0}\n{1}\n{2}\n{2}\n{3}\n{4}\n{5}\n{6}\n{7}\n{8}\n{8}\n{9}\n{10}\n".format(header,H1,H2,H3,H4,H5,H6,H7,H8,H9,H10)


#-------------------------------------------------------------------------------
# Main Script - Display Weather and News on LCD display
#-------------------------------------------------------------------------------

def window():
   app = QApplication(sys.argv) #calls the constructor and initializes QT application
   window = QWidget() #intializes window 
	
   b1 = QPushButton("Weather") #Creates second button for weather data
   b2 = QPushButton("News") #Creates second button for news data

   vbox = QVBoxLayout() #Creates vertically aligned box
   
   vbox.addWidget(b1) #adds weather button to the home box
   vbox.addWidget(b2) #adds news button to the home box
   
   #Displays weather when 'Weather' button is clicked
   def on_b1_clicked():
     alert = QMessageBox() #Creates pop up message where data is displayed
     alert.setText(weather) #Outputs the temperature data 
     alert.exec_() #Runs the alert until it is closed out
   b1.clicked.connect(on_b1_clicked)

   #Displays headlines when 'News' button is clicked
   def on_b2_clicked():
     alert = QMessageBox() #Creates pop up message where data is displayed
     alert.setText(news) #Outputs the headlines  
     alert.exec_() #Runs the alert until it is closed out
   b2.clicked.connect(on_b2_clicked)
   
   window.setLayout(vbox)
   window.resize(250,250) #Resizes the Home pop-up box from default size to a larger size
   window.setWindowTitle("Home")
   window.show()
   sys.exit(app.exec_()) #Runs the application until it is closed out

if __name__ == '__main__':
   window()
