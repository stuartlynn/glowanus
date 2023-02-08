# Complete project details at https://RandomNerdTutorials.com
from setup import load_secrets, save_secrets, clear_secrets, start_setup_server
from running import start_running_server
from pixels import set_setup_lights, fill, GREEN, cycle_color

import time
from machine import Pin
from np import Neopixel

print("Starting up")
secrets = load_secrets()

led = machine.Pin('LED', machine.Pin.OUT)
led.on()


#set_setup_lights('connecting')
if(secrets):
    print("Have Secrets ", secrets)
    start_running_server(secrets)
else:
    print("No secrets")
    start_setup_server()
    



