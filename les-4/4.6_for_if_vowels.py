# Schrijf een for-loop die langs alle letters van een string loopt en de letter uitprint, maar alleen als het een klinker is ('aeiou').
s = "Guido van Rossum heeft programmeertaal Python bedacht."
klinkers = ['a', 'e', 'i', 'o', 'u']

for letter in s:
    for klinker in klinkers:
        if klinker == letter:
            print(letter)
