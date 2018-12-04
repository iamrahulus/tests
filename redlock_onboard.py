import requests
import os
import json
url = "https://api.redlock.io/login"
data = {}
data['username']=os.environ['REDLOCK_USER']
data['password']=os.environ['REDLOCK_PASSWORD']
data['customerName']=os.environ['REDLOCK_CUSTOMER']
headers = {'Content-Type': "application/json", 'Accept': "application/json"}
response = requests.request("POST", url, json=data, headers=headers)
print(response.text)
print(response.text['token'])
