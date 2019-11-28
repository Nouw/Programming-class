import datetime
today = datetime.datetime.today()
stringToday = today.strftime("%a %d %b %Y, %H:%M:%S,")

while True:
    file = open('hardlopers.txt', 'a')
    runner = input('Wat is de naam van de hardloper')
    file.write(stringToday + ' ' + runner + '\n')
