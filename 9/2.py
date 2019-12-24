import json

with open("data.json") as file:
    #файл открыт
    data = json.load(file)
    print(data)
#файл закрыт

    
