def ticker(company):
    file = open("ticker.txt", 'r')
    companyToTicker = {}
    tickerToCompany = {}

    for line in file:
        list = line.rstrip("\n").split(':')
        companyToTicker[list[0]] = list[1]
        tickerToCompany[list[1]] = list[0]

    if company in companyToTicker:
        print("Ticker symbol: " + companyToTicker[company])
    else:
        print("Company name: " + tickerToCompany[company])


company = input("Enter Company name:").upper()

ticker(company)
