# Je reist met een grote groep en hebt een hotel afgehuurd. Dat kost € 4356,-.
# Dit is kostbaar, daarom wil je weten hoeveel dit per persoon kost. Schrijf een programma dat de gebruiker vraagt om het aantal personen dat mee op reis gaat.
# Deel het bedrag door het aantal reizigers en print dat uit! Gebruik een try-except; zorg dat bij foute invoer deze verschillende foutmeldingen geprint worden:


def prijsPP():
    try:
        people = int(input('Hoeveel mensen gaan er mee op reis?'))
        prijs = 4356

        if people < 0:
            raise TypeError

        print("Bedrag per persoon is: " + str(4356 / people))
    except ZeroDivisionError:
        print("Delen door nul kan niet!")
    except ValueError:
        print("Gebruik cijfers voor het invoeren van het aantal!")
    except TypeError:
        print("Negatieve getallen zijn niet toegestaan!")
    except:
        print("Onjuiste invoer!")


prijsPP()
