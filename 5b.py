from sense_hat import SenseHat
import time

s = SenseHat()
s.low_light = True

green = (0, 255, 0)
yellow = (255, 255, 0)
blue = (0, 0, 255)
red = (255, 0, 0)
white = (255,255,255)
nothing = (0,0,0)
pink = (255,105, 180)

def heart(val):
    P = pink
    O = nothing
    G = green
    Y = yellow
    R = red
    W = white
    B = blue
    logo = [
    O, O, O, O, O, O, O, O,
    O, P, P, O, P, P, O, O,
    P, P, P, P, P, P, P, O,
    P, P, P, P, P, P, P, O,
    O, P, P, P, P, P, O, O,
    O, O, P, P, P, O, O, O,
    O, O, O, P, O, O, O, O,
    O, O, O, O, O, O, O, O,
    ]
    if val % 2 == 0:
        logo = map(lambda x: O if x == P else P, logo)
    return logo

images = [heart, heart, heart, heart]
count = 0

while True: 
    val = count % 2
    s.set_pixels(heart(val))
    time.sleep(1)
    count += 1