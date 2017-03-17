import requests 
import json
import time

def get_token(email, password): 
  url = 'http://smartplug.host/api/v1/auth/login'
  data = {'email': email, 'password': password}

  resp = requests.post(url, data=data)  
  parsed_json = resp.json()
  return parsed_json

def add_device(token, device_id): 
  url = 'http://smartplug.host/api/v1/devices/'
  headers = {'Token-Authorization':token} 
  data = {'device_id':device_id} 
  resp = requests.post(url, headers=headers, data=data) 
  parsed_json = resp.json()
  return parsed_json

def get_devices(token): 
  url = 'http://smartplug.host/api/v1/devices/'
  headers = {'Token-Authorization':token} 
  resp = requests.get(url, headers=headers) 
  parsed_json = resp.json()
  return parsed_json


def add_light(token, device_id, light): 
  url = 'http://smartplug.host/api/v1/devices/'+device_id+'/light'
  headers = {'Token-Authorization':token} 
  data = {'data':light} 
  resp = requests.post(url, headers=headers, data=data) 
  parsed_json = resp.json()
  return parsed_json
  
def get_light(token, device_id): 
  url = 'http://smartplug.host/api/v1/devices/'+device_id+'/light'
  headers = {'Token-Authorization':token} 
  resp = requests.get(url, headers=headers) 
  parsed_json = resp.json()
  return parsed_json
  

if __name__ == "__main__":
  device = 'b8-27-eb-4f-b9-f6'
  email = raw_input("Email: ") 
  password = raw_input("Password: ")
  token = get_token(email, password) 
  token = token['token']
  print token
  print add_device(token, device)
  devices = get_devices(token)
  #print json.dumps(devices, indent=4)

  print add_light(token,device,10)
  print get_light(token,device)

  '''
  mins = 0 

  mcp_channel = 0 

  mcp = SmartMCP3008()

  mcp_readings = []

  while mins < 60: 

    print "min = ",mins

    light_reading = mcp.read(mcp_channel)
    print "light_reading = ",light_reading
    add_light(token,device,light_reading)

    print "Sleeping for 60 seconds" 
    time.sleep(60)

    mins = mins + 1 

  '''
