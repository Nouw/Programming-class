for lines in open('kaartnummers').read().splitlines():
    line = lines.split(',')
    print(line[1] + ' heeft kaartnummer: ' + line[0])

