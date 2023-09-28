import os
import json
from pixels import set_setup_lights
import uasyncio
from portal import start_portal
import machine

try:
  import usocket as socket
except:
  import socket


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

    



def start_setup_server():
    set_setup_lights("connecting")
    
    set_setup_lights("connected")
    start_portal()
  
 #   while True:
 #     conn, addr = s.accept()
 #     print('Got a connection from %s' % str(addr))
 #     request = conn.recv(1024)
 #     print('Content = %s' % str(request))
 #     response = web_page()
 #     conn.send(response)
 #     conn.close()
