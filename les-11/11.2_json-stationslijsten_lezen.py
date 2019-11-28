import json

with open('stations.json', 'r') as file:
    objects = json.load(file)
    firstLong = 0
    for object in objects["payload"]:
        print("{name} -  {code} : {type}".format(name=object["namen"]["lang"], code=object["code"], type=object["stationType"]))
        compLong = object["lng"]
        if firstLong < compLong:
            firstLong = compLong
            mostEasternStation = object["namen"]["lang"]
    print("Het meest oostelijk gelegen station is: " + mostEasternStation)
