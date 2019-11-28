# Schrijf een programma met twee for-loops in elkaar (nested) om de tafels van 1 t/m 10 uit te printen.

tafels = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for tafel in tafels:
    for multiplier in tafels:
        print(str(tafel) + " x " + str(multiplier) + " = " + str(tafel * multiplier))
