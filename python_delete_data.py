import requests
import json

url = 'https://jsonplaceholder.typicode.com/posts/1'

headers = {'Content-Type': 'application/json; charset=UTF-8'}

response = requests.delete(url, headers=headers)

print(response.status_code) # 200

print(response.ok)