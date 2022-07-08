import json
import requests
import time
from gpiozero import LED

#initialize the IO ports
rX = LED(17)
rY = LED(19)
lY = LED(16)
lX = LED(20)

#run while pi is on
while True:
    resp = requests.get('https://wfevbii2w47dcqjn3tkwyf6evq0pbckw.lambda-url.us-west-2.on.aws/piGet')
    json_dict = json.loads(resp.json())
    print(json_dict)
    
#if there is nothing in the queue
    if len(json_dict.keys()) < 2:
        print(json_dict["message"])

#else parse JSON for left stick data
    else:
        if json_dict["handy"] == "Left":
            if float(json_dict["stickX"]) > 0.5:
                lX.on()
            if float(json_dict["stickY"]) > 0.5:
                lY.on()
            if float(json_dict["stickX"]) < -0.5:
                rX.on()
            if float(json_dict["stickY"]) < -0.5:
                rY.on()
            if float(json_dict["stickX"]) < 0.5 and float(json_dict["stickX"]) > -0.5:
                lX.off()
                rX.off()
            if float(json_dict["stickY"]) < 0.5 and float(json_dict["stickY"]) > -0.5:
                lY.off()
                rY.off()
#turn on led/motor if stick is past a treshhold, turn it off otherwise
    time.sleep(0.05)
