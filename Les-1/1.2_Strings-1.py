word = "Supercalifragilisticexpialidocious"
# Hoeveel letters zijn er in 'Supercalifragilisticexpialidocious'?
print(len(word))
# Komt in 'Supercalifragilisticexpialidocious' de tekst 'ice' voor?
print("ice" in word)
# het woord 'Antidisestablishmentarianism' langer dan 'Honorificabilitudinitatibus'?
wordX = len("Antidisestablishmentarianism")
wordY = len("Honorificabilitudinitatibus")
print(wordX > wordY)
# Welke componist komt in alfabetische volgorde het eerst: 'Berlioz', 'Borodin', 'Brian', 'Bartok', 'Bellini', 'Buxtehude', 'Bernstein'? Welke het laatst?
listNames = ['Berlioz', 'Borodin', 'Brian', 'Bartok', 'Bellini', 'Buxtehude', 'Bernstein']
namesAlphabetical = sorted(listNames)
namesReverseAlphabetical = sorted(listNames, reverse=True)
print(namesAlphabetical[0])
print(namesReverseAlphabetical[0])
