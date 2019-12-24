import json

with open("data.json") as file:
    #data = file.read()
    #z = json.loads(data)
    z = json.loads(file.read())
    president = z["pres"]
    #name = president["name"]
    #country = president["contry"]
    #print(f"President: {name}")
    #print(f"Country: {country}")
    for key, value in president.items():
        print(f"{key}: {value}")

contries = []
contries.append(president)
contries.append(
    {
        "name": "Trump",
        "contry": "USA"
    })
z["pres"] = contries
print(z)

with open("data.json", "w") as file:
    json.dump(z, file)

    
