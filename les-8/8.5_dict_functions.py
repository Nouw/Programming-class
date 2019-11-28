def namen():
    running = True
    dictionary = {}
    while running:
        naam = input('Volgende naam:')


        if naam == '':
            for naam, aantal in dictionary.items():
                if aantal <= 1:
                    print("Er is " + str(aantal) + " student met de naam " + naam)
                    running = False
                else:
                    print("Er zijn " + str(aantal) + " studenten met de naam " + naam)
                    running = False
        else:
            if naam in dictionary:
                dictionary[naam] += 1
            else:
                dictionary[naam] = 1

namen()