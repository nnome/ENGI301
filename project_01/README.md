# Portable Smart Vanity Mirror using BeagleBone Black
## ENGI 301 Course

This repository contains the code and instructions required to construct a portable, touchscreen smart mirror that allows you to receive weather and news updates for the day.

For more detailed instructions on the motivation for this project, schematics, and instructions visit: https://www.hackster.io/nome2/portable-smart-vanity-mirror-using-beaglebone-black-9d8d6f

## Instructions

#### To initialize the Beagle Bone Black:
1) Begin by flashing the SD card that ill be used in the BeagleBone
2) Enter the cloud9 IDE temrinal (192.168.7.2:300)
3) Connect to wifi and enable wifi
4) Update using "sudo apt-get update"
5) Download PyOWM for weather data by entering "sudo pip3 install pyowm"
6) Dowlonad pyqt GUI by entering "sudo apt-get install python3-pyqt5"

#### To execute code and operate device:
1) Download SmartMirror.py (main code) and RunSmartMirror (run script) from this repository and upload to cloud9
2) In temrinal window, change into appropriate directories (var/lib/cloud9/ENGI301/Project1/code)
3) Change settings of run script to make executable (chmod 755 RunSmartMirror)
4) Ensure hardware connections are in place and correct using instructions in Hackster.io page linked above
5) Enter ./RunSmartMirror to run the SmartMirror.py program since it is a set path in the run script
6) Observe the window on the LCD display for a Home button with Weather and News buttons
7) Interact with button of choice for updates: Click the "Weather" to receive forecast and "News" to receive news for the day via alert messages
9) Close alert meesgaes by clicking "Ok" and then clsoe window by clicking red "X" in upper-right corner of the window
10) With all the necessary hardware components, the user should plug the device into an external power source or a computer.
