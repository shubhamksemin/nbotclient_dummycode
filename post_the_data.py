import requests
import json
print("Enter the data od sensor :")
currentThreshould=input("Enter the CurrentThreshould : ")
id=input("Enter the id: ")
sensorId=input("Enter the sensorid: ")
sensorname=input("Enter the sensorname: ")
threshould=input("Enter the threshould: ")
data={
  "creationTime": 0,
  "currentThreshold": currentThreshould,
  "id": id,
  "orgId": "1234",
  "sensorId": sensorId,
  "sensorName": sensorname,
  "status": True,
  "threshold": threshould
  }
# data={
#   "creationTime": 0,
#   "currentThreshold": 'abc32',
#   "id": 'gdfe32',
#   "orgId": "1234",
#   "sensorId": 'avcfd32',
#   "sensorName":'tempreture sensor',
#   "status": True,
#   "threshold": 'avfdr32'
# }
headers={"Content-type":"application/json"}
response_API = requests.post('http://192.168.0.111:8083/sensors',json=data,headers=headers )
print(response_API.content)
print(response_API.status_code)
print(response_API.headers)

# # print(response_API.status_code)

# name=input("enter the name")
# d={1:name }
# print(d) 