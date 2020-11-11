from sense_hat import SenseHat
import http.client
import urllib.parse
import time
key = "OBGBKNICJSMTDX1G"


sense = SenseHat()

red = (255, 0, 0)

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
        params = urllib.parse.urlencode({'field1': z, 'key':key }) 
        headers = {"Content-typZZe": "application/x-www-form-urlencoded","Accept": "text/plain"}
        conn = http.client.HTTPConnection("api.thingspeak.com:80")
        try:
            conn.request("POST", "/update", params, headers)
            response = conn.getresponse()
            print (z)
            print (response.status,    response.reason)
            data = response.read()
            conn.close()
        except:
            print ("connection failed")
        break
if __name__ == "__main__":
        while True:
            getBumpData()
            time.sleep(0.125)   