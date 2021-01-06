import requests
import json

URL = 'http://127.0.0.1:8000/apis_create/'
data = {
    'name': 'arohi',
    'roll': 136,
    'city': 'solu',
}
json_data = json.dumps(data)
r = requests.post(url=URL, data=json_data)
data = r.json()
print(data)
