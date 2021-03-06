import csv

def is_bearish_candlestick(candle):
    return candle['Close'] < candle['Open']


def is_bullish_engulfing(candles, index):
    current_day = candles[index]
    previous_day = candles[index-1]

    if is_bearish_candlestick(previous_day) \
        and current_day['Close'] > previous_day['Open'] \
        and current_day['Open'] < previous_day['Close']:
        
        return True
    
    return False

with open('StockChartPatternRecognition/btc.csv') as f:
    reader = csv.DictReader(f) # Reads each line into a dictionary to easily reference the open and close data
    candles = list(reader) # convert the DictReader object into a list

for i in range(1, len(candles)): # range starts at one because 0 doesnt have a previous day
    #print(candles[i]) # prints each key in the file


    if is_bullish_engulfing(candles, i):
        print("{} is a bullish engulfing".format(candles[i]['Date']))

