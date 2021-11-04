import requests, json, csv

SYMBOL = 'TWTR'
TOKEN = 'REDACTED'
URL = "https://sandbox.iexapis.com/stable/stock/{}/chart/ytd?token={}".format(SYMBOL, TOKEN)

r = requests.get(URL)



json_data = json.loads(r.content)

csv_file = open('stock.csv', 'w') # w means file is open for writing
csv_writer = csv.writer(csv_file)

csv_writer.writerow(['date', 'open', 'high', 'low', 'close']) # create headers

for item in json_data:
    print(item)
    csv_writer.writerow([item['date'], item['open'], item['high'], item['low'], item['close']])

csv_file.close()
