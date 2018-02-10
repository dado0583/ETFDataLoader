from ETFScraper import DataCleanser, ETFScraper, Validator, DataSaver
import datetime

cleaner = DataCleanser.DataCleanser()
saver = DataSaver.DataSaver()
scraper = ETFScraper.ETFScraper()
validator = Validator.Validator()

if(validator.isDataNew({})):
    print("Going to scrape now")

    current_date = datetime.datetime.today()

    df = scraper.scrape_ETFs()
    saver.save(df, "yyyymmdd-ETFs.csv") #format datetime

    #For each entry above, get the ETF holdings
    df = scraper.scrape_ETF_Holdings("SYMBOL, e.g. SPY")
    saver.save(df, "yyyymmdd-ETFHoldings.csv") #format datetime
