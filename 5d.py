from sense_hat import SenseHat
import time
import math

sense = SenseHat()
sense.low_light = True

y = (255, 255, 0)
b = (0, 0, 0)
image_pixels = [
 b, b, b, b, b, b, b, b,
 b, b, b, y, b, b, b, b,
 b, b, y, y, y, b, b, b,
 b, y, b, y, b, y, b, b,
 b, b, b, y, b, b, b, b,
 b, b, b, y, b, b, b, b,
 b, b, b, y, b, b, b, b,
 b, b, b, b, b, b, b, b
 ]

while True:
    acceleration = sense.get_accelerometer_raw()
    x = round(acceleration['x'], 0)
    y = round(acceleration['y'], 0)
    z = round(acceleration['z'], 0)
    print(x,y,z)
    if x == -1:
        sense.set_rotation(180)
    elif y == 1:
        sense.set_rotation(90)
    elif y == -1:
        sense.set_rotation(270)
    else:
        sense.set_rotation(0)
    sense.set_pixels(image_pixels)
    time.sleep(1)