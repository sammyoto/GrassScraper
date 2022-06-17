import requests
resp = requests.get('http://127.0.0.1:8000/noahsGirlfriend').json()
print(resp['message'])