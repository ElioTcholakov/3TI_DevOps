import requests
import json

access_token = 'YmNiMDQwZmEtYjU3OS00ZTU5LWFiMTItOWJmNzM3ZTFjODBkNTIwNmMzOTMtYWRl_PF84_consumer' 
url = 'https://webexapis.com/v1/rooms'

headers = {
    'Authorization': 'Bearer {}'.format(access_token),
    'Content-Type': 'application/json'
}
params = {
    'title': 'Netacad_devasc_skills_ET'
}

res = requests.post(url, headers=headers, json=params)
print(json.dumps(res.json(), indent=4))