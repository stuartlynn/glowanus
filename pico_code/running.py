import os
import json
from pixels import cycle_color, fill, GREEN, RED,cycle_brightness
import uasyncio
from setup import clear_secrets
from microdot_asyncio import Microdot, Response
import machine
import urequests
import time

try:
  import usocket as socket
except:
  import socket

import network
import ubinascii

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
mac = ubinascii.hexlify(wlan.config('mac'),':').decode()

print("mac address")
print(mac)

runningApp = Microdot()

CHECK_INTERVAL = 60.0*2.0/0.01 # in secconds

@runningApp.get('/')
async def setup(request):
    return "RUNNING"

def ping_server():
    try:
        result = urequests.get("https://glowanus-monitor.vercel.app/api/record_ping?deviceId={0}".format(mac)).json()
        print(result)
    except Exception as e:
        print(e)


def get_status():
    try:
        result = urequests.get("https://services.arcgis.com/at3rDjch5X7i9Bag/arcgis/rest/services/cso_prd/FeatureServer/0/query?f=json&returnGeometry=false&where=&objectIds=41&outFields=advisory%2CWaterbod_1").json()
        print(result)
        return result["features"][0]["attributes"]["Advisory"]==1
    except Exception as e:
        print(e)
        return False


def start_active():
    advisory = False
    i = 0
    button_press_count = 0
    button = machine.Pin(28,machine.Pin.IN)

    while True:
        if(i%int(CHECK_INTERVAL) ==0):
            print("checking advisory")
            advisory = get_status()
            print("ping server")
            ping_server()
        if(advisory):
            fill(cycle_color(i))
        else:
            fill([255,255,255])
       # if(i>65535*20):
        #    i=0
        i=i+1



        time.sleep(0.01)



def start_running_server(secrets):
    fill(GREEN)

    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(secrets["SSRID"], secrets["PASSWORD"])

    # Try to connect for 20 secconds
    max_wait = 20
    while max_wait > 0:
        if (wlan.isconnected()):
            break
        else:
            max_wait -= 1
            time.sleep(1)

    # If connection failed after 20 s
    # Show red status for 4 s
    # The delete the secrets and reset machine

    if(not wlan.isconnected()):
        fill(RED)
        restart_delay = 4
        while restart_delay>0:
            restart_delay -=1
            time.sleep(1)

        clear_secrets()
        machine.reset()


    print(wlan.ifconfig())

    #s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #s.bind(('', 80))
    #s.listen(5)
    start_active()

 #   while True:
 #     conn, addr = s.accept()
 #     print('Got a connection from %s' % str(addr))
 #     request = conn.recv(1024)
 #     print('Content = %s' % str(request))
 #     response = web_page()
 #     conn.send(response)
 #     conn.close()
