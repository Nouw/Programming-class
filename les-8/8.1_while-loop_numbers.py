running = True
som = 0
getallen = -1

while running:
    getal = int(input("Geef en getal:"))
    som += getal
    getallen += 1

    if getal == 0:
        running = False
        print("Er zijn " + str(getallen) + " getallen ingevoerd, de som is: " + str(som))

