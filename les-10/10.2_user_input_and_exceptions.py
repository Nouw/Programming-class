

while True:
    try:
        loonPerUur = int(input("Hoeveel verdien je per uur?"))
        urenGewerkt = int(input("Hoeveel uur heb je gewerkt?"))
        break
    except:
        print("Er is iets fout gegegaan")

print(str(urenGewerkt) + " uur werken levert " + str((loonPerUur * urenGewerkt)) + " Euro op")
