import requests

BASE = "http://127.0.0.1:5000/"

data = [
  {"likes": 5600, "name": "Blue Balloon", "views": 10000}, 
  {"likes": 7500, "name": "Red Balloon", "views": 10000}, 
  {"likes": 3000, "name": "Yellow Balloon", "views": 10000}, 
  {"likes": 9904, "name": "Black Balloon", "views": 10000},
  {"likes": 5600, "name": "Purple Balloon", "views": 10000}, 
  {"likes": 7500, "name": "Green Balloon", "views": 10000}, 
  {"likes": 3000, "name": "Pink Balloon", "views": 10000}, 
  {"likes": 9904, "name": "Brown Balloon", "views": 10000}
]

for i in range(len(data)):
  response = requests.put(BASE + "video/" + str(i), data[i])
  print(response.json())

input()

response = requests.get(BASE + "video/6")
print(response.json())
