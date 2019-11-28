# Schrijf een functie seizoen(maand) die als parameter maandnummer meekrijgt. Het functie-resultaat is het seizoen die bij die maand hoort. Nummers 3 t/m 5 horen bij 'lente', 9 t/m 11 bij ‘herfst’, etc.
inputMonth = int(input('Which month is it?'))


def season(month):
    if month in range(1, 2):
        return 'Winter'
    elif month == 12:
        return 'Winter'
    if month in range(3, 5):
        return 'Spring'
    if month in range(6, 8):
        return 'Summer'
    if month in range(9, 12):
        return 'Autumn'


print(season(inputMonth))
