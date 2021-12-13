# Portable Smart Vanity Mirror using BeagleBone Black
## ENGI 301 Course

This repository contains the code and instructions required to construct a portable, touchscreen smart mirror that allows you to receive weather and news updates for the day.

For more detailed instructions on the motivation for this project, schematics, and instructions visit: https://www.hackster.io/nome2/portable-smart-vanity-mirror-using-beaglebone-black-9d8d6f

## Instructions

#### To assemble device hardware:
1) Connect BeagleBone Black to computer by inserting miniUSB side of cable into USB Client port and USB side of cable into Computer port
2) Connect HDMI adapter to HDMI port of BeagleBone. Connect one end of Male to Male HDMI Cable into female end of HDMI adapter and the other end of Male to Male HDMI Cable into the HDMI port of the LCD
3) Connect USB cable into USB port of BeagleBone Black and end of cable into 4-port USB hub
4) Connect microUSB end of cable into "Touch" port of LCD and USB end into 4-port USB hub
5) Connect Wi-Fi adapter into 4-port USB hub
6) Connect wall adapter of USB hub into standard power outlet outputting 100-240V

##### To initialize the Beagle Bone Black:
1) Begin by flashing the SD card that will be used in the BeagleBone
2) Enter the cloud9 IDE terminal (192.168.7.2:300)
3) Connect to Wi-Fi using "sudo connmanctl" and "enable Wi-Fi"
4) Update using "sudo apt-get update"
5) Install PyOWM for weather data by entering "sudo pip3 install pyowm"
6) Install BeautifulSoup by entering "sudo pip3 install beautifulsoup4"
7) Install pyqt GUI by entering "sudo apt-get install python3-pyqt5"

#### To execute code and operate device:
1) Assemble device using instructions in above section
2) Turn on/start computer and BeagleBone Black
3) Download SmartMirror.py (main code) and RunSmartMirror (run script) from this repository and upload to cloud9
4) In terminal window, change into appropriate directories (var/lib/cloud9/ENGI301/Project1/code)
5) Change settings of run script to make executable (chmod 755 RunSmartMirror)
6) Ensure hardware connections are in place and correct using instructions in the section above and the linked Hackster.io page
7) Enter ./RunSmartMirror to run the SmartMirror.py program since it is a set path in the run script
8) Observe the window on the LCD display for a Home button with Weather and News buttons
9) Interact with button of choice for updates: Click the "Weather" to receive forecast and "News" to receive news for the day via alert messages
10) Close alert messages by clicking "Ok" and then close window by clicking red "X" in upper-right corner of the window
11) To run program again, repeat steps 7-10
