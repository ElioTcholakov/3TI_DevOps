import requests
import json

access_token = 'YmNiMDQwZmEtYjU3OS00ZTU5LWFiMTItOWJmNzM3ZTFjODBkNTIwNmMzOTMtYWRl_PF84_consumer' 
room_id = "Y2lzY29zcGFyazovL3VzL1JPT00vYjExOTg4YTAtMDA1YS0xMWVjLTliNDMtM2ZkODU3OTE1NjU2"
message = 'Here are my screenshots of netacad-devasc skills-based exam'
url = 'https://webexapis.com/v1/messages'

headers = {
    'Authorization': 'Bearer {}'.format(access_token),
    'Content-Type': 'application/json'
}

params = {'roomId': room_id, 'markdown': message}
res = requests.post(url, headers=headers, json=params)
print(json.dumps(res.json(), indent=4))