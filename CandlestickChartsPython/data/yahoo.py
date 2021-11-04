import yfinance as yf

bitcoin = yf.Ticker("BTC-USD")

history = bitcoin.history(period="max")

print(history.to_csv())
