import requests, json
from config import *

# this program will use the Requests library as our own python client (not using the one thats available) to interface with the alpaca API
BASE_URL = 'https://paper-api.alpaca.markets'
ACCOUNT_URL = "{}/v2/account".format(BASE_URL)
ORDERS_URL = "{}/v2/orders".format(BASE_URL)
HEADERS = {'APCA-API-KEY-ID': API_KEY, 'APCA-API-SECRET-KEY': SECRET_KEY}


def get_account():
    r = requests.get(ACCOUNT_URL, headers=HEADERS)

    return json.loads(r.content) # return the request response as a dictionary so we can access the json keys individually



def create_order(symbol, qty, side, type, time_in_force):
    data = { 
        "symbol": symbol,
        "qty": qty,
        "side": side,
        "type": type,
        "time_in_force": time_in_force
    }
    r = requests.get(ORDERS_URL, json={}, headers=HEADERS) # POST json data from above. could have specified "data", but json={} is a shortcut in requests()
    
    return json.loads(r.content)

def get_orders():

    r = requests.get(ORDERS_URL, headers=HEADERS)

    return json.loads(r.content)


#create_order("AAPL", 100, "buy", "market", "gtc")
#print(response)

orders = get_orders()
print(orders)


#   r = requests.post(ORDERS_URL)

