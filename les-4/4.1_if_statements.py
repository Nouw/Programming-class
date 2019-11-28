# Schrijf een programma dat de gebruiker vraagt om de score van een multiplechoice toets. Het programma bepaalt of het resultaat voldoende is. Bij meer dan 15 punten is de deelnemer geslaagd!
score = input('Wat is je score op de multiplechoice toets?')

if int(score) > 15:
    print('Je bent geslaagd!')
    print('Met een score van: ' + score + ' ben je geslaagd!')
# Waarschijnlijk heb je de bovenstaande uitvoer geprogrammeerd met 2 print()-opdrachten.
# Wat gebeurt er als je de tweede print()-opdracht niet recht onder de eerste zou plaatsen maar bijvoorbeeld recht onder de ‘i’ van het if-statement?

# Wat er dan zou gebeuren is dat de tweede print opdracht sowieso wordt uitgevoerd ookal heeft de gebruiker een te laag aantal punten.
