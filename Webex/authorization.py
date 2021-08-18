### From labo 8.6.7

import requests
import json

access_token = 'YmNiMDQwZmEtYjU3OS00ZTU5LWFiMTItOWJmNzM3ZTFjODBkNTIwNmMzOTMtYWRl_PF84_consumer' 
url = 'https://webexapis.com/v1/people/me'

headers = {
    'Authorization': 'Bearer {}'.format(access_token)
    }
res = requests.get(url, headers=headers)
print(json.dumps(res.json(), indent=4))