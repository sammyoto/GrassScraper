import requests
import time

while True:
    resp = requests.get('https://wfevbii2w47dcqjn3tkwyf6evq0pbckw.lambda-url.us-west-2.on.aws/piGet').json()
    print(resp)
    time.sleep(0.125)



