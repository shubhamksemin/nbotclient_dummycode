# import requests
# import json
# response_API = requests.get('http://192.168.0.106:8083')
# data=response_API.text
# parse_json=json.loads(data)
# # print('Status code: ',response_API.status_code)
# # print(data)
# # print('json Format: \n',parse_json)
import requests
response_API = requests.get('http://192.168.0.111:8083/')
print(response_API.content)
print(response_API.status_code)
