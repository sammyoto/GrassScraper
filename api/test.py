import requests
import time

while True:
    resp = requests.get('http://127.0.0.1:8000/piGet').json()
    print(resp)
    time.sleep(0.125)



