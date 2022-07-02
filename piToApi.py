import json
import requests
import time
from gpiozero import LED

rX = LED(17)
rY = LED(19)
lX = LED(16)
lY = LED(20)

while True:
    resp = requests.get('https://wfevbii2w47dcqjn3tkwyf6evq0pbckw.lambda-url.us-west-2.on.aws/piGet')
    json_dict = json.loads(resp.json())
    print(json_dict)
    
    if len(json_dict.keys()) < 2:
        print(json_dict["message"])
    else:  
        if json_dict["handy"] == "Right":
            if float(json_dict["stickX"]) > 0.3:
                rX.on()
            if float(json_dict["stickY"]) > 0.3:
                rY.on()
        
        if json_dict["handy"] == "Left":
            if float(json_dict["stickX"]) > 0.3:
                lX.on()
            if float(json_dict["stickY"]) > 0.3:
                lY.on()
    
    time.sleep(0.125)
    rX.off()
    rY.off()
    lX.off()
    lY.off()
    
    
