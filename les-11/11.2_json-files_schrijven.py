import json
import os


def store(name, firstl, birthdate, email):
    # Basically checks if the data.json file exists if not then create data.json file
    files = []
    for f_name in os.listdir('.'):
        files.append(f_name)
    if 'data.json' not in files:
        with open('data.json', 'w') as file:
            file.write('[]')

    # get all the data from the json file and add the login to it
    with open('data.json') as data_file:
        old_data = json.load(data_file)
        old_data.append({"naam": name, "voorletters": firstl, "geb_datum": birthdate, "e-mail": email})
    with open('data.json', 'w') as outfile:
        json.dump(old_data, outfile, indent=4)


while True:
    naam = input("Wat is je achternaam? ")

    if naam == "einde":
        break

    voorl = input("Wat zijn je voorletters? ")
    gbdatum = input("Wat is je geboortedatum? ")
    email = input("Wat is je e-mail adres? ")
    store(naam, voorl, gbdatum, email)

