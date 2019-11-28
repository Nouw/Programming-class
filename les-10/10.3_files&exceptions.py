while True:
    try:
        naamBestand = input("Wat is de naam van het bestand?")
        file = open(naamBestand)
    except:
        print("Onjuiste bestands naam")
    else:
        break

i = 0
lines = file.readlines()
kaartnummers = []

for line in lines:
    i += 1
    kaartnummer = line[:6]
    kaartnummers.append(kaartnummer)

maxKaartnummer = max(kaartnummers)
indexMaxKaartnummer = kaartnummers.index(maxKaartnummer) + 1

print('Deze file telt ' + str(i) + ' regels')
print('Het grootste kaartnummer is: ' + str(maxKaartnummer) + ' en dat staat op regel ' + str(indexMaxKaartnummer))
