import requests
import json

URL = 'http://127.0.0.1:8000/apis_create/'
data = {
    'name': 'anup',
    'roll': 137,
    'city': 'Kathmandu',
}
json_data = json.dumps(data)
r = requests.post(url=URL, data=json_data)
data = r.json()
print(data)
