# Neem deze tuple over, en schrijf code waarmee je een nieuwe lijst maakt met het aantal voorkomens van de letters in alfabetische volgorde.
# Tuple letters bevat 2 keer ‘A’, 3 keer ‘B’ en 4 keer ‘C’. De lijst die dit programma maakt (en print) is dan: [2, 3, 4].

letters = ('A', 'C', 'B', 'B', 'C', 'A', 'C', 'C', 'B')
list = [letters.count('A'), letters.count('B'), letters.count('C')]

print(list)

blokA = 'PROG', 'CSN', 'ICOR'
print(type(blokA))