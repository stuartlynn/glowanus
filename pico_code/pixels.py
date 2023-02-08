from np import Neopixel
from machine import Pin
from math import sin
#pixels = Neopixel(12,0,13,"GRB")
pixels = Neopixel(1,0,16,"GRB")

GREEN = pixels.colorHSV(10000,255,255)
RED = pixels.colorHSV(60000,255,255)
PURPLE = pixels.colorHSV(50437,255,255)


def cycle_color(i):
    return pixels.colorHSV((i*50)%65535,255,255)

def cycle_brightness(i):
    v = int(245*(sin(i/100.0)+1)/2) + 10
    return [v,v,v]
                           
def fill(color):
    pixels.fill(color)
    pixels.show()
    
def set_setup_lights(phase):
    if(phase=="connecting"):
        print("Showing lights for connecting phase")
        fill(GREEN)
        #pixels.set_pixel(0,RED)
    elif(phase=="connected"):
        print("Showing lights for setup phase")
        fill(PURPLE)
    else:
        pixels.clear()
