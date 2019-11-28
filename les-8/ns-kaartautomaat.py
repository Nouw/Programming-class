stations = ['Schagen', 'Heerhugowaard', 'Alkmaar', 'Castricum', 'Zaandam', 'Amsterdam sloterdijk', 'Amsterdam Centraal', 'Amsterdam Amstel', 'Utrecht Centraal', "'s-Hertogenbosch", 'Eindhoven', 'Weert', 'Roermond', 'Sittard', 'Maastricht']

def inlezen_beginstation(stations):
    running = True
    while running:
        station_input = input('Wat is uw begin station?')

        if station_input in stations:
            running = False
            return stations.index(station_input)
        else:
            print('Het opgegeven station bestaat niet!')


def inlezen_eindstation(stations, beginstation):
    running = True
    while running:
        station_input = input('Wat is uw eind station?')

        if station_input in stations:
            if beginstation < stations.index(station_input):
                running = False
                return stations.index(station_input)
            else:
                print("Het station is de verkeerde kant op!")
        else:
            print('Het opgegeven station bestaat niet!')


def omroepen_reis(stations, beginstation, eindstation):
    nameBeginstation = stations[beginstation]
    nameEndstation = stations[eindstation]
    distance = eindstation - beginstation
    price = distance * 5

    print("Het beginstation " + nameBeginstation + " is het " + str(beginstation) + "e station in het traject \n" +
          "Het eindstation " + nameEndstation + " is het " + str(eindstation) + "e station in het traject \n" +
          "De afstand bedraagt " + str(distance) + " station(s) \n" +
          "De prijs van het kaartje is " + str(price) + " euro")
    print("Jij stapt in de trein in: " + nameBeginstation)
    for stationIndex in range((len(stations))):
        if eindstation > stationIndex > beginstation:
            print("-" + stations[stationIndex])

    print("Jij stapt uit in: " + nameEndstation)


beginstation = inlezen_beginstation(stations)
eindstation = inlezen_eindstation(stations, beginstation)
omroepen_reis(stations, beginstation, eindstation)