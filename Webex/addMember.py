import requests
import json

access_token = 'YmNiMDQwZmEtYjU3OS00ZTU5LWFiMTItOWJmNzM3ZTFjODBkNTIwNmMzOTMtYWRl_PF84_consumer' 
room_id = "Y2lzY29zcGFyazovL3VzL1JPT00vYjExOTg4YTAtMDA1YS0xMWVjLTliNDMtM2ZkODU3OTE1NjU2"
person_email = 'yvan.rooseleer@biasc.be'
url = 'https://webexapis.com/v1/memberships'

headers = {
    'Authorization': 'Bearer {}'.format(access_token),
    'Content-Type': 'application/json'
}

params = {'roomId': room_id, 'personEmail': person_email}
res = requests.post(url, headers=headers, json=params)
print(json.dumps(res.json(), indent=4))