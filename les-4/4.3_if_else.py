# Pas de uitwerking van Practice Exercise 4.2 aan en geef ook een melding als de gebruiker niet mag stemmen!
age = input('Hoe oud bent u?')
dutchId = input('Heeft u een nederlands paspoort? True / False')

if int(age) >= 18 and dutchId == 'True':
    print('Gefeliciteerd! U mag stemmen!')
else:
    print('U mag helaas niet stemmen!')
