file = open('kaartnummers')
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
