# Schrijf (en test) de functie som() die 1 parameter heeft: getallenLijst.
# Ga ervan uit dat dit een list is met integers. De return-waarde van de functie moet de som (optelling) van de getallen in de lijst zijn!
# Tip: bekijk nog eens de list-functies (Perkovic, blz. 28).

lst = [1, 4, 6, 9]


def som(lijst):
    a = sum(lijst)
    return a


print(som(lst))
