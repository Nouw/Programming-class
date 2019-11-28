# Schrijf (en test) de functie wijzig() met één parameter: letterlijst. Zorg dat de functie de lijst leegt en de letters [ ‘d’, ‘e’, ‘f’ ] toevoegt.
# Er is geen return-waarde! Test je programma als volgt:
lijst = ['a', 'b', 'c']


def wijzig(letterlijst):
    letterlijst.clear
    letterlijst[0] = 'e'
    letterlijst[1] = 'f'
    letterlijst[2] = 'g'

print(lijst)
wijzig(lijst)
print(lijst)

# Waarom kun je in de functie niet de opdracht lijst = ['d', 'e', 'f'] geven?
# Antwoord: Een functie kan niet de een variable aanpassen, omdat lijst een immutable object is.

# Werkt jouw functie ook met een string-parameter? Probeer dit! Waarom werkt het wel/niet?
# Antwoord: Het zou niet werken, want de .clear werkt niet op een string.

# Welke rol speelt (im)mutabiliteit in deze vraag?
# Antwoord: de lijst is een immutable object, als het een mutable object was kon je het heel makkelijk veranderen.