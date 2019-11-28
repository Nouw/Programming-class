# Schrijf (en test) de functie kwadraten_som() die 1 parameter heeft: grondgetallen.
# Dit is een list is met integers. De return-waarde van de functie is de som van de kwadraten van alle positieve getallen in de lijst!
# Een lijst van [ 4, 5, 3, -81 ] heeft als return-waarde dus 50 (namelijk 16 + 9 + 25).
lst = [4, 5, 3, -81]


def kwadrateren_som(grondgetallen):
    som = 0
    for getal in grondgetallen:
        if getal > 0:
            kwadraat = getal ** 2
            som = som + kwadraat
    return som


print(kwadrateren_som(lst))
