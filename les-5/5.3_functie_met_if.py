# Schrijf (en test) de functie lang_genoeg() die voor Efteling-attracties bepaalt of een gebruiker in een attractie mag.
# De functie heeft één parameter, namelijk de lengte van de gebruiker in centimeters.
# Als de gebruiker 120 centimeter of langer is de return-waarde van de functie “Je bent lang genoeg voor de attractie!”, anders is de melding “Sorry, je bent te klein!”.
lengthUser = input('Hoeveel centimeters lang bent u?')


def minlength(length):
    if int(length) > 120:
        print('U bent lang genoeg voor de attractie!')
    else:
        print('Sorry, U bent te klein!')


minlength(lengthUser)
