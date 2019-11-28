bruin = {"Deurne", "Helmond Brouwhuis", "Helmond", "Helmond 't Hout", "Eindhoven", "Beukenlaan", "Best", "Boxtel"}
groen = {"Weert", "Heeze", "Geldrop", "Eindhoven", "Beukenlaan", "Best", "Boxtel"}

# Print daarna eerst met een set-functie welke plaatsen in beide trajecten worden aangedaan (de overeenkomst).
print(bruin.intersection(groen))

# Gebruik vervolgens opnieuw een set-functie om te printen hoe het traject “bruin” verschilt van het traject “groen”.
# Je moet dan dus op het scherm zien welke plaatsen van traject “bruin” ze niet allebei aandoen!
print(bruin.difference(groen))

# Print ook alle stations op beide trajecten uit. Print elk station maar 1! Gebruik weer een set-functie!
print(bruin.union(groen))