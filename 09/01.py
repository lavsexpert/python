import json

data = {
    "pres":{
        "name": "Putin",
        "contry": "Russia"
        }
    }

with open("data.json", "w") as file:
    json.dump(data, file)
