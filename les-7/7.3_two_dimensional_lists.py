studentencijfers = [ [95, 92, 86],[66, 75, 54],[89, 72, 100],[34, 0, 0] ]


def gemiddelde_per_student(studentencijfers):
    for list in studentencijfers:
        som = 0
        gemiddelde = 0

        for cijfer in list:
            som += cijfer

        gemiddelde += som / len(list)

        return gemiddelde


def gemiddelde_van_alle_studenten(studentencijfers):
    som = 0
    length = 0
    for list in studentencijfers:
        length += len(list)
        for cijfer in list:
            som += cijfer

    return som / length



print(gemiddelde_per_student(studentencijfers))

print(gemiddelde_van_alle_studenten(studentencijfers))
