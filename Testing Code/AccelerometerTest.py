from sense_hat import SenseHat
import time

sense = SenseHat()

red = (255, 0, 0)

def getAccelerometer():
        accel = sense.get_accelerometer_raw() # gather the raw data of the Accelerotmeter fro the SenseHat
        z = abs(accel['z'])
        if z > 1: # lights if if more than 1 g of force is acted upon the RPI
            sense.show_letter("!", red)
        else:
            sense.clear()
        print(z)
        time.sleep(0.125)

if __name__ == "__main__":
        while True:
            getAccelerometer()
            
       