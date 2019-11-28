# De Hogeschool Utrecht wil studenten financieel ondersteunen bij hun studie, afhankelijk van de cijfers die een student haalt.
# Voor elk cijferpunt krijg je € 30,-. Voor een 1,0 krijg je dus 30 euro, voor een 2,5 krijg je 75 euro en voor een 10,0 beloont de HU een student met € 300,-.
#
# Maak variabelen cijferICOR, cijferPROG en cijferCSN. Geef ze alle drie de waarde die jij verwacht dat je voor de betreffende vakken in blok 1 zult gaan halen.
# Maak nu vervolgens ook de volgende variabelen aan, en bereken de bijbehorende waarden m.b.v. een Python expressie:
cijferICOR = 6.3
cijferPROG = 7.8
cijferCSN = 6.8

gemiddelde = (cijferICOR + cijferPROG + cijferCSN) / 3

beloning = cijferICOR * 30 + cijferPROG * 30 + cijferCSN * 30

overzicht = "Je gemiddelde van je tentamens is: " + str(gemiddelde) + " " + "Je belong is: " + str(beloning) + " euro"

print(overzicht)
