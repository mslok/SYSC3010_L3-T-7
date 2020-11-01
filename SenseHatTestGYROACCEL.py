from sense_hat import SenseHat
import time

sense = SenseHat()

red = (255, 0, 0)

#code example from Device Plus Editorial Team

while True:
    orientation = sense.get_orientation()
    p = round(orientation["pitch"], 0)
    r = round(orientation["roll"], 0)
    y = round(orientation["yaw"], 0)
    
    #print("p: %s, r: %s, y: %s" % (p,r,y))
    
    #raw = sense.get_accelerometer_raw()
    #print("x: {x}, y: {y}, z: {z}".format(**raw))
    
    accel = sense.get_accelerometer_raw()
    x = accel['x']
    y = accel['y']
    z = accel['z']
    
    x = abs(x)
    y = abs(y)
    z = abs(z)
    
    if z > 1:
        sense.show_letter("!", red)
    else:
        sense.clear()
    #print("x: %s, y: %s, z: %s" % (x,y,z))
    
    raw = sense.get_compass_raw()
    #print("x: {x}, y: {y}, z: {z}".format(**raw))
    #time.sleep(0.1)