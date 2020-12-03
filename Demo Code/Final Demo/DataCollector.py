


from sense_hat import SenseHat
import sense_hat
import http.client
import urllib.parse
import requests
import json
import time
import serial
from random import uniform
#key = "OBGBKNICJSMTDX1G"

r = (255, 0, 0)
g = (0, 255, 0)

ready = [
g,g,g,g,g,g,g,g,
g,g,g,g,g,g,g,g,
g,g,g,g,g,g,g,g,
g,g,g,g,g,g,g,g,
g,g,g,g,g,g,g,g,
g,g,g,g,g,g,g,g,
g,g,g,g,g,g,g,g,
g,g,g,g,g,g,g,g,
]

sense = SenseHat()
pressed = sense_hat.ACTION_PRESSED
sense.clear()
run = 1

def readString():
    while 1:
        while ser.read().decode("utf-8") != '$':  # Wait for the begging of the string
            pass  # Do nothing
        line = ser.readline().decode("utf-8")  # Read the entire string
        return line
    
def getLatLng(latString, lngString):
    while True:
        try:
            lat = latString[:2].lstrip('0')+"."+"%.7s"%str(float(latString[2:])*1.0/60.0).lstrip("0.")
            lng = lngString[:3].lstrip('0')+"."+"%.7s"%str(float(lngString[3:])*1.0/60.0).lstrip("0.")
            print("Current GPS Location")
            return lat, lng
        except ValueError:
            print("Couldn't get a GPS lock. Using Random Ottawa values")
            lat1 = uniform(45.45, 45.46)
            long1 = (uniform(75.51, 75.52)*-1)
            return lat1, long1
            
    
def getBumpData():
        accel = sense.get_accelerometer_raw()
        z = abs(accel['z'])
        if z > 1.2:
            sense.show_letter("!", r)
#             lat1 = uniform(40, 50)
#             long1 = (uniform(60, 70)*-1)
            latlng = getLatLng(lines[3], lines[5])           
            lat1 = float(latlng[0])
            long1 = float(latlng[1])
            update='&field1={}&field2={}&field3={}'.format(z, lat1, long1)
            #Update channel data with HTTP GET or POST
            write_key='UU2HQ2WXR5L56DDK' #Alex's channel 'OBGBKNICJSMTDX1G' Michael Channel          
            url='https://api.thingspeak.com/update?api_key='
            #write custom header parse later 
            header=update
            url_ac=url + write_key + header
            print(url_ac)

            data=urllib.request.urlopen(url_ac)
            print(data)
            print(z)
            print(long1)
            print(lat1)
            sense.set_pixels(ready)
            
def startStop():
    for event in sense.stick.get_events():
        if event.action == pressed:
            global run
            if run == 1:
                sense.set_pixels(ready)
                run = 2
            elif run == 2:
                sense.clear()
                run = 1

     
if __name__ == "__main__":
    ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)  # Open Serial port
    try:
        while True:
            startStop()
            line = readString()
            lines = line.split(",")
            if run == 2:
                getBumpData()
            
                    
    except KeyboardInterrupt:
        print('Exiting Script')
        