# Libraries #
import twint
import pandas as pd
from datetime import datetime,timedelta

# Variables #
date = (datetime.today().strftime('%Y-%m-%d'))
start_date = ((datetime.fromisoformat(date)) - timedelta(days=2)).strftime('%Y-%m-%d')
end_date = ((datetime.fromisoformat(date)) + timedelta(days=2)).strftime('%Y-%m-%d')

users = ['CNBC','Benzinga','Business','nytimesbusiness','ReutersMoney','ReutersBiz',
         'WSJmarkets','barronsonline','businessinsider','Forbes','MarketWatch','BusinessWire',
         'CNNBusiness','MorningstarInc','PRNewswire','YahooFinance','Deltaone','zerohedge']

if __name__ == '__main__':

    data_path = f"C:\\Users\\mp094\\Desktop\\Twint Jsons\\news_{start_date}_{end_date}.json"
    c = twint.Config()

    for name in users:
        c.Lang = 'en'
        c.Username = name
        c.Since = start_date
        c.Until = end_date
        c.Store_json = True
        c.Output = data_path   # Location to save raw twitter data

        twint.run.Search(c)