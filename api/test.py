import requests
resp = requests.get('http://127.0.0.1:8000/noahsGirlfriend').json()
print(resp['message'])

url = 'http://127.0.0.1:8000/vrPost'
json = {"left":"true", "right":"true", "forward":"true", "back":"true", "lookLeft":"true", "lookRight":"true", "lookDown":"true", "lookUp":"true"}
resp = requests.post(url = url, json = json)
print(resp.json())