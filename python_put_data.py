import requests
import json

url = 'https://jsonplaceholder.typicode.com/posts/1'
data = {'id':1, 'userId':2, 'title':'drink water', 'body':'drinking water is important'}
headers = {'Content-Type':'application/json; charset=UTF-8'}
response = requests.put(url, data=json.dumps(data), headers=headers)
print(response.status_code)
print(response.ok)
print(response.content)