# Schrijf functie gemiddelde(), die de gebruiker vraagt om een willekeurige zin in te voeren. De functie berekent vervolgens de gemiddelde lengte van de woorden in de zin en print dit uit.

def gemiddelde(zin):
    words = zin.split()
    print(words)
    totalLength = 0
    wordCount = 0
    for word in words:
        length = len(word)
        totalLength += length
        wordCount += 1
    return print(totalLength / wordCount)

zin = input('Tik een willekeurige zin')
gemiddelde(zin)