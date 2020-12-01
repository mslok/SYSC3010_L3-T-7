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

wait = [
r,r,r,r,r,r,r,r,
r,r,r,r,r,r,r,r,
r,r,r,r,r,r,r,r,
r,r,r,r,r,r,r,r,
r,r,r,r,r,r,r,r,
r,r,r,r,r,r,r,r,
r,r,r,r,r,r,r,r,
r,r,r,r,r,r,r,r,
]

sense = SenseHat()
pressed = sense_hat.ACTION_PRESSED
sense.set_pixels(wait)
run = 0

def readString():
    while 1:
        while ser.read().decode("utf-8") != '$':  # Wait for the begging of the string
            pass  # Do nothing
        line = ser.readline().decode("utf-8")  # Read the entire string
        return line
    
def getLatLng(latString, lngString):
    lat = latString[:2].lstrip('0')+"."+"%.7s"%str(float(latString[2:])*1.0/60.0).lstrip("0.")
    lng = lngString[:3].lstrip('0')+"."+"%.7s"%str(float(lngString[3:])*1.0/60.0).lstrip("0.")
    return lat, lng
    
def getBumpData():
    while True:
        
        accel = sense.get_accelerometer_raw()
        z = abs(accel['z'])
        if z > 1.2:
            sense.show_letter("!", r)
            lat1 = uniform(40, 50)
            long1 = (uniform(60, 70)*-1)
#           latlng = getLatLng(lines[3], lines[5])
#           lat1 = float(latlng[0])
#           long1 = (float(latlng[1])*-1)
            update='&field1={}&field2={}&field3={}'.format(z, lat1, long1)
            #Update channel data with HTTP GET or POST
            write_key='OBGBKNICJSMTDX1G'          #'UU2HQ2WXR5L56DDK' Alex's channel
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
        
        for event in sense.stick.get_events():
                if event.action == pressed:
                    if run == 1:
                        break
        
        
def Start():
    sense.set_pixels(ready)
    run = 1
    
def Stop():
    sense.set_pixels(wait)
    run = 0
     
if __name__ == "__main__":
    ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)  # Open Serial port
    try:
        while True:  
            line = readString()
            lines = line.split(",")
            for event in sense.stick.get_events():
                if event.action == pressed:
                    if run == 0:
                        Start()
                        getBumpData()
                        Stop()
                                                
    except KeyboardInterrupt:
        print('Exiting Script')
        