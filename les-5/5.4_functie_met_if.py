# Schrijf (en test) een functie new_password() die 2 parameters heeft: oldpassword en newpassword.
# De return-waarde is True als het nieuwe password voldoet aan de eisen.
# Het nieuwe password wordt alleen geaccepteerd als het verschilt van het oude password èn als het minimaal 6 tekens lang is.
# Als dat niet zo is, is de return-waarde False.
#
# Optioneel: zorg dat het nieuwe password minstens 1 cijfer moet bevatten!

oldPassword = input('Vul uw oude wachtwoord in.')
newPassword = input('Vul uw nieuwe wachtwoord in.')


def new_password(old, new):
    try:
        digitExists = any(char.isdigit() for char in new)
        if old != new and len(new) > 6 and digitExists:
            return True
        else:
            return False
    except:
        print('Uw nieuwe wachtwoord moet een cijfer bevatten!')


print(new_password(oldPassword, newPassword))
