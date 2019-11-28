# Variables van vorige opdracht
a = 6
b = 7
c = (a + b) / 2
voornaam = "Fabio"
tussenvoegsel = ""
achternaam = "Dijkshoorn"
mijnnaam = voornaam + " " + tussenvoegsel + " " + achternaam

# 75 groter is dan a en kleiner b.
print(75 >= a and 75 > b)
#  lengte van mijnnaam even groot is als de som van de lengte van voornaam, tussenvoegsel en achternaam.
print(len(mijnnaam) == len(voornaam + tussenvoegsel + achternaam))
# de lengte van mijnnaam 5 maal groter is dan de lengte van variabele tussenvoegsel.
print(len(tussenvoegsel) * 5 > len(mijnnaam))
# de waarde van variabele tussenvoegsel voorkomt in de waarde van variabele achternaam.
print(tussenvoegsel in achternaam)
