def standaardprijs(afstandKM):
    if afstandKM > 0:
        if afstandKM > 50:
            prijs = afstandKM * 0.6 + 15
        else:
            prijs = afstandKM * 0.8
    else:
        prijs = 0

    return prijs

def ritprijs(leeftijd, weekendrit, afstandKM):
    prijs = standaardprijs(afstandKM)
    if weekendrit:
        if leeftijd < 12 or leeftijd >= 65:
            prijs = prijs - (prijs * 0.35)
        else:
            prijs = prijs - (prijs * 0.4)
    else:
        if leeftijd < 12 or leeftijd >= 65:
            prijs = prijs - (prijs * 0.30)
    return leeftijd, weekendrit, afstandKM, prijs


print(ritprijs(11, True, 20))
print(ritprijs(11, False, 20))
print(ritprijs(11, True, 20))
print(ritprijs(11, False, -12))
print(ritprijs(12, True, -12))
print(ritprijs(12, False, 20))
print(ritprijs(12, True, -12))
print(ritprijs(12, False, -12))
print(ritprijs(64, True, 20))
print(ritprijs(64, False, 20))
print(ritprijs(64, True, -12))
print(ritprijs(64, False, -12))
print(ritprijs(65, True, 20))
print(ritprijs(65, False, 20))
print(ritprijs(65, True, -12))
print(ritprijs(65, False, -12))

