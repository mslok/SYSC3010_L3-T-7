import time
import serial #enables the serial port for access the GPS USB

#decodes the data from the GPS into readable NMEA messages.

def readString():
    while 1:
        while ser.read().decode("utf-8") != '$':  # Wait for the begging of the string
            pass  # Do nothing
        line = ser.readline().decode("utf-8")  # Read the entire string
        return line
    
    
# Aquires the raw NMEA data from the GPS and converts it into Latidue and Longitude coordinates

def getLatLng(latString, lngString):
    lat = latString[:2].lstrip('0')+"."+"%.7s"%str(float(latString[2:])*1.0/60.0).lstrip("0.")
    lng = lngString[:3].lstrip('0')+"."+"%.7s"%str(float(lngString[3:])*1.0/60.0).lstrip("0.")
    return lat, lng

def getGPS():
    while True:
        latlng = getLatLng(lines[3], lines[5])
        # convert the data from the latlng array into floats 
        lat1 = float(latlng[0]) 
        long1 = (float(latlng[1])*-1) #converts coordinate to negative for correct directional data.(data recorded in West, required in East) 
        print("Latitude: ")
        print(lat1)
        print("Longitude: ")
        print(long1)
        time.sleep(0.5)



if __name__ == "__main__":
    ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)  # Open Serial port for GPS
    try:
        while True:
            line = readString()
            lines = line.split(",")
            getGPS()
            
    except KeyboardInterrupt:
        print('Exiting Script')     