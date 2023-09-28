from phew.phew import logging, server, access_point, dns
from phew.phew.template import render_template
from phew.phew.server import redirect
import json

import machine
SECRET_FILE = "secrets.json"


def save_secrets(secrets):
    with open(SECRET_FILE,"w") as f:
        json.dump(secrets,f)

DOMAIN = "pico.wireless"  # This is the address that is shown on the Captive Portal

@server.route("/settings",methods=["POST"])
async def setSettings(request):
    settings = request.form
    jsonSettings = {'SSRID':settings['SSRID'], "PASSWORD":settings['password']}
    print("jsonSettings ",jsonSettings)
    save_secrets(jsonSettings)
    machine.reset()
    return "Got them"
    

@server.route("/", methods=['GET'])
def index(request):
    """ Render the Index page"""
    if request.method == 'GET':
        logging.debug("Get request")
        return render_template("index.html")

# microsoft windows redirects
@server.route("/ncsi.txt", methods=["GET"])
def hotspot(request):
    print(request)
    print("ncsi.txt")
    return "", 200


@server.route("/connecttest.txt", methods=["GET"])
def hotspot(request):
    print(request)
    print("connecttest.txt")
    return "", 200


@server.route("/redirect", methods=["GET"])
def hotspot(request):
    print(request)
    print("****************ms redir*********************")
    return redirect(f"http://{DOMAIN}/", 302)

# android redirects
@server.route("/generate_204", methods=["GET"])
def hotspot(request):
    print(request)
    print("******generate_204********")
    return redirect(f"http://{DOMAIN}/", 302)

# apple redir
@server.route("/hotspot-detect.html", methods=["GET"])
def hotspot(request):
    print(request)
    """ Redirect to the Index Page """
    return render_template("index.html")


@server.catchall()
def catch_all(request):
    print("***************CATCHALL***********************\n" + str(request))
    return redirect("http://" + DOMAIN + "/")


def start_portal():
    # Set to Accesspoint mode
    # Change this to whatever Wifi SSID you wish
    ap = access_point("Glowanus Setup")
    ip = ap.ifconfig()[0]
    # Grab the IP address and store it
    logging.info(f"starting DNS server on {ip}")
    # # Catch all requests and reroute them
    dns.run_catchall(ip)
    server.run()                            # Run the server
    logging.info("Webserver Started")
