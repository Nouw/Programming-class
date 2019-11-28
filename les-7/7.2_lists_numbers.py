# Gegeven is variabele invoer = "5-9-7-1-7-8-3-2-4-8-7-9". Schrijf een nieuw programma waarin je deze variabele splitst in een lijst van getallen en print de gesorteerde lijst.
# Bepaal en print na het opsplitsen de grootste waarde, kleinste waarde, aantal getallen, de som en het gemiddelde!

invoer = "5-9-7-1-7-8-3-2-4-8-7-9"

def sort(inputString):
    lst = list(inputString.split("-"))

    aantal = len(lst)
    som = 0

    for item in lst:
        som += int(item)

    average = som / aantal

    print("Gesorteerde list van ints: " + str(lst) + "\n"
          + "Grootste getal: " + str(max(lst)) + " en Kleinste getal: " + str(min(lst)) + "\n"
          + "Aantal getallen: " + str(aantal) + " en Som van de getallen: " + str(som) + "\n"
          + "Gemiddelde: " + str(average))


sort(invoer)
