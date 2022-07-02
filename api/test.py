from matplotlib.pyplot import get
import requests
import time
import json

while True:
    resp = requests.get('http://localhost:8000/piGet')
    print(type(json.loads(resp.json())))
    time.sleep(0.125)


#ahttps://wfevbii2w47dcqjn3tkwyf6evq0pbckw.lambda-url.us-west-2.on.aws/piGet