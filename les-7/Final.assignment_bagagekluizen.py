
def toonAantalKluizenVrij():
#     Laat het aantal lege kluizen zien
    file = open("kluizen.txt", 'r')

    i = 0
    for line in file:
        i += 1

    vrijeKluizen = 12 - i

    return "\033[92m" + "Er zijn momenteel nog zoveel kluizen over: " + str(vrijeKluizen)


def newKluis():
    file = open('kluizen.txt', 'r+')
    kluizen = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

    for line in file:
        takenKluis = line[:line.index(";")]
        kluizen.remove(int(takenKluis))

    # Check of er nog kluizen zijn anders continue
    if not kluizen:
        return "\033[91m" + "Er zijn geen kluizen meer beschikbaar!"

    kluisNummer = kluizen[0]
    wachtwoordNietIngevuld = True

    # blijf loopen tot dat de gebruiker een correct wachtwoord heeft gegeven (kan je wel heel gemakkelijk een bruteforce doen...)
    while wachtwoordNietIngevuld:
        kluisWachtwoord = input('Voer uw wachtwoord in!')

        if len(kluisWachtwoord) < 4:
            return "\033[93m" + "Uw wachtwoord moet minstens 4 characters lang zijn!"

        file.write(str(kluisNummer) + ";" + str(kluisWachtwoord) + "\n")
        wachtwoordNietIngevuld = False

    return "\033[92m" + "Uw kluisnummer is: " + str(kluisNummer)

def openKluis():
    file = open("kluizen.txt", 'r')
    kluisNummer = input("Wat is uw kluisnummer? \n")
    kluisWachtwoord = input("Wat is het wachtwoord?")

    for line in file:
        kluisInfo = line.rstrip('\n').split(';')

        if kluisNummer in kluisInfo and kluisWachtwoord in kluisInfo:
            return "\033[92m" + "De kluis is geopend!"
        else:
            return "\033[91m" + "De gegevens van de kluis zijn niet correct!"


run = True
while run:

    task = input("\033[95m" + "Kies 1 van deze opties:\n"
          +  "\033[0m" + "1: Ik wil weten hoeveel kluizen er nog zijn\n"
          + "2: Ik wil een nieuwe kluis\n"
          + "3: Ik wil even iets uit mijn kluis halen\n"
          + "4: Stop het programma\n")

    try:
        eval(task)
    except (NameError):
        print("Je keuze moet een cijfer zijn")
        break

    if int(task) > 5:
        print("\033[91m" + "Die optie bestaat niet!")

    if int(task) == 1:
        print(toonAantalKluizenVrij())

    if int(task) == 2:
        print(newKluis())

    if int(task) == 3:
        print(openKluis())

    if int(task) == 4:
        run = False
        print("Tot de volgende keer o/")
