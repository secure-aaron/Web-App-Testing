import requests, json

# this program will use the Requests library as our own python client to interface with the coingecko API
BASE_URL = 'https://api.coingecko.com/api/v3'
COIN_NAME = 'bitcoin'
DAY = '1'
OHLC_URL = "{}/coins/{}/ohlc?vs_currency=usd&days={}".format(BASE_URL,COIN_NAME,DAY)

'''
Candle’s body:
1 - 2 days: 30 minutes
3 - 30 days: 4 hours
31 and before: 4 days
'''

def get_ohlc():

    r = requests.get(OHLC_URL) # POST json data from above. could have specified "data", but json={} is a shortcut in requests()
    
    return json.loads(r.content)


print(get_ohlc())