import twint
import pandas as pd
import datetime
localtime = str(datetime.datetime.now()).split('.')[0]
c = twint.Config()
users = ['CNBC','Benzinga','Business','nytimesbusiness','ReutersMoney','ReutersBiz','WSJmarkets','barronsonline','businessinsider','Forbes','MarketWatch','BusinessWire','CNNBusiness','MorningstarInc','PRNewswire','YahooFinance',
         'Deltaone','zerohedge']
for name in users:
    c.Lang = 'en'
    c.Username = name
    #c.Limit = 200
    c.Since = "2020-12-28" # Starting date
    c.Until = "2021-01-05" # not inclusive date
    c.Store_json = True
    c.Output = f"C:\\Users\\mp094\\Desktop\\Twint Jsons\\news_2020-12-28_2021-01-05.json"

    twint.run.Search(c)





#     c.Username = name    -> Twitter Handle or Username
#     #c.Search = "Cannabis"
#     c.Store_object = True
#     c.Limit = 10          Limiting the amount of output responses
#     twint.run.Search(c)
#c.Search = "keyword" -> searching for a tweet that contains X as keyword
#c.Min_likes = 5 -> Searching for tweets with a minimum of 5 likes.

#c.Username = "username"
#c.Format = "ID {id} | Username {username}"



#c.Username = 'Business'
#c.Limit = 100
#c.Hashtags = True        # if hashtags to be present.
#c.Store_object = True
#c.Store_json = True
#c.Output = r"C:\Users\mp094\Desktop\Twint Jsons\news_2020-01-01_2020-12-07.json"
#c.Elasticsearch = "http://35.202.70.31:9200"
# twint.run.Search(c)