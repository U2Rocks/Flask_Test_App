import requests

BASE = "http://127.0.0.1:5000/"

#data = [{"likes": 10, "name": "How to Cook", "views": 100000}, 
#        {"likes": 898, "name": "Leopard", "views": 1000}, 
#        {"likes": 345, "name": "Turtle", "views": 500}, 
#        {"likes": 1000, "name": "Hare", "views": 15000},
#        {"likes": 5442, "name": "Zebra", "views": 20100}]

#for i in range(len(data)):
#    response = requests.put(BASE + "video/" + str(i), data[i])
#    print(response.json())

response = requests.patch(BASE + "video/3", {})
print(response.json())