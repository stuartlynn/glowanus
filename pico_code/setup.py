import os
import json
from pixels import set_setup_lights
import uasyncio
from microdot_asyncio import Microdot, Response
import machine

try:
  import usocket as socket
except:
  import socket

import network

SECRET_FILE = "secrets.json"

def load_secrets():
    try:
        with open(SECRET_FILE,"r") as f:
            return json.load(f)
    except:
        return None
    
def save_secrets(secrets):
    with open(SECRET_FILE,"w") as f:
        json.dump(secrets,f)

def clear_secrets():
    os.remove(SECRET_FILE)
    
    
startupApp = Microdot()

@startupApp.get('/')
async def setup(request):
    return Response(body=web_page(),status_code=200, headers={"Content-Type":"text/html"})
    
@startupApp.post("/settings")
async def setSettings(request):
    settings = request.form
    jsonSettings = {'SSRID':settings['SSRID'], "PASSWORD":settings['password']}
    print("jsonSettings ",jsonSettings)
    save_secrets(jsonSettings)
    machine.reset()
    return "Got them"
    
def web_page():
    html = """
        <html>
            <head>
                <meta name="viewport" content="width=device-width, initial-scale=1">
                <style>
                    body {background-color: powderblue;}
                    h1   {color: blue;}
                    p    {color: red;}
                    #full{
                        display:flex;
                        flex-direction:column;
                        align-items:center;
                        justify-content: center;
                        width:100vw;
                        height:100vh;
                    }
                </style>
            </head>
            <body>
            <div id="full">
                <form action="/settings" method="POST">
                    <p>SSRID</p>
                    <input type="text" name="SSRID" id="SSRID">
                    <p>Password</p>
                    <input type="password" id="password" name="password" required/>
                    <button type='submit'>Submit</button>
                </form>
            </div>
            </body>
        </html>"""
    return html
    

def start_server():
    print('Starting microdot app')
    try:
        startupApp.run(port=80)
    except:
        startupApp.shutdown()

def start_setup_server():
    set_setup_lights("connecting")
    ssid = 'glowanus'
    password = '123456789'

    ap = network.WLAN(network.AP_IF)
    ap.config(essid=ssid, password=password)
    ap.active(True)

    while ap.active() == False:
      pass

    print("ssid is ",ssid)

    print('Connection successful')
    print(ap.ifconfig())

    #s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #s.bind(('', 80))
    #s.listen(5)
    
    set_setup_lights("connected")
    start_server()
  
 #   while True:
 #     conn, addr = s.accept()
 #     print('Got a connection from %s' % str(addr))
 #     request = conn.recv(1024)
 #     print('Content = %s' % str(request))
 #     response = web_page()
 #     conn.send(response)
 #     conn.close()
