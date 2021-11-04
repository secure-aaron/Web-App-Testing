import websocket, json
import dateutil.parser

# This program uses the Coinbase Websocket API to retrieve real-time ticket streaming data.
# Please see the following for more information: https://docs.pro.coinbase.com/#websocket-feed

minutes_processed = {}
minute_candlesticks = []
current_tick = None
previous_tick = None # store value as the close price of the last candle if we start a new minute.

def on_open(ws): 
    '''
    This function opens the web socket and subscribes to the channel to listen to.
    '''
    print('opened connection') # open websocket

    subscribe_message = { # Coinbase API requires a channel (ticker pair) to be subscribed to for websocket use.
        'type': 'subscribe', 
        'channels': [
            {
                'name': 'ticker',
                'product_ids': [
                    'BTC-USD' # Ticker pair
                ]
            }
        ]
    }
    ws.send(json.dumps(subscribe_message)) # Open the socket, send the python dict from above as json


def on_message(ws, message):
    '''
    This function will return the received message from the websocket.
    '''
    global current_tick, previous_tick # Reference the defined variables at the top of the program

    previous_tick = current_tick
    current_tick = json.loads(message)

    #print('received message') # Used for debugging
    #print(json.loads(message)) # Used for debugging
    print('=== Received Tick ===') # Used for debugging
    print('{} @ ${} USD'.format(current_tick['time'], current_tick['price'])) # Full timestamp
    
    tick_datetime_object = dateutil.parser.parse(current_tick['time'])
    tick_dt = tick_datetime_object.strftime('%m/%d/%Y %H:%M') # Shorter timestamp
    print('Current minute:', tick_datetime_object.minute) # Used to keep track of the minute in case it changes for the new tick/candlestick
    print(tick_dt)

    if not tick_dt in minutes_processed:
        print('starting new candlestick')
        minutes_processed[tick_dt] = True
        print(minutes_processed)

        if len(minute_candlesticks) > 0: # Create previous candlestick close price
            minute_candlesticks[-1]['close'] = previous_tick['price']

        minute_candlesticks.append({ # Create first candlestick
            'minute': tick_dt,
            'open': current_tick['price'],
            'high': current_tick['price'],
            'low': current_tick['price']
        })

    if len(minute_candlesticks) > 0: # Update the candlestick over time
        current_candlestick = minute_candlesticks[-1]
        if current_tick['price'] > current_candlestick['high']:
            current_candlestick['high'] = current_tick['price']
        if current_tick['price'] < current_candlestick['low']:
            current_candlestick['low'] = current_tick['price']

        print('=== Candlesticks ===')
        for candlesticks in minute_candlesticks:
            print(candlesticks)

socket = 'wss://ws-feed.pro.coinbase.com' # Coinbase's API endpoint

ws = websocket.WebSocketApp(socket, on_open=on_open, on_message=on_message)

ws.run_forever() # Run the websocket


