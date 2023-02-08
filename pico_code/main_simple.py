import machine
from np import Neopixel
import time

pixels = Neopixel(12,0,15,"GRB")
blue = pixels.colorHSV(1000,10,100)

led = machine.Pin("LED",machine.Pin.OUT)
led.on()

i = 0
while True:
    red = pixels.colorHSV(i%60000,255,255)
    pixels.set_pixel(0,red)
    pixels.show()
    i = i +100
    print("i is ",i)
    time.sleep(0.01)