# Glowanus project 

This repo contains the code for the Glowanus project. It has two directories 

-  glowanus\_monitor: which has the code for the website that helps us tell which
   of the lanterns is active through their heartbeat pings 
-  pico\_code: which is the actual code that runs on the Pi Pico W 


## Loading the Pi Pico W

We are using [Thonny](https://thonny.org/) to upload the program to the Pico. Simply 
upload the contents of the pico\_code folder to the Pi and it should start running.

## Monitoring ID 

We have a small heartbeat ping to a monitoring site, just to see if the application is 
up and functioning. The id for each lantern can be set in the running.py file by changing 
the deviceId on this line

```python
  result = urequests.get("https://glowanus-monitor.vercel.app/api/record_ping?deviceId=12").json()
```


