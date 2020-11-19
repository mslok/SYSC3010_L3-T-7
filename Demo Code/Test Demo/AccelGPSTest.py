from sense_hat import SenseHat
import http.client
import urllib.parse
import requests
import json
import time
import serial
#key = "OBGBKNICJSMTDX1G"


sense = SenseHat()

red = (255, 0, 0)

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

# return the Lattidue as a seperate float
def getLat():
    latlng = getLatLng(lines[3], lines[5])
    lat1 = float(latlng[0])
    print(lat1)
    return lat1

# return the Longitude as a seperate float  
def getLong():
    latlng = getLatLng(lines[3], lines[5])
    long1 = (float(latlng[1])*-1)
    print(long1)
    return long1
    
def getAccel():
    accel = sense.get_accelerometer_raw()
    z = abs(accel['z'])
    if z > 1:
        sense.show_letter("!", red)
    else:
        sense.clear()
        
    print(z)
    return z
    
def write_to_thing():
    accelerometer = getAccel()
    latitude = getLat()
    longitude = getLong()
    update='&field1={}&field2={}&field3={}'.format(accelerometer, latitude, longitude)
    #Update channel data with HTTP GET or POST
    write_key='UU2HQ2WXR5L56DDK'
    url='https://api.thingspeak.com/update?api_key='
    #write custom header parse later 
    header=update
    url_ac=url + write_key + header
    print(url_ac)

    data=urllib.request.urlopen(url_ac)
    print(data)   
    
def getBumpData():
    while True:
        
        accel = sense.get_accelerometer_raw()
        #x = abs(accel['x'])
        #y = abs(accel['y'])
        z = abs(accel['z'])
        if z > 1:
            sense.show_letter("!", red)
        else:
            sense.clear()
        latlng = getLatLng(lines[3], lines[5])
        lat1 = float(latlng[0])
        long1 = (float(latlng[1])*-1)
#         update='&field1={}&field2={}&field3={}'.format(z, lat1, long1)
#         #Update channel data with HTTP GET or POST
#         write_key='UU2HQ2WXR5L56DDK'
#         url='https://api.thingspeak.com/update?api_key='
#         #write custom header parse later 
#         header=update
#         url_ac=url + write_key + header
#         print(url_ac)
# 
#         data=urllib.request.urlopen(url_ac)
#         print(data)
        print(z)
        print(long1)
        print(lat1)
        time.sleep(0.125)
     
if __name__ == "__main__":
    ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)  # Open Serial port
    try:
        while True:
            line = readString()
            lines = line.split(",")
            getBumpData()
            
    except KeyboardInterrupt:
        print('Exiting Script')        