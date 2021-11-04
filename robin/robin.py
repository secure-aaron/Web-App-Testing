import click, json, ui # import our ui file
import robin_stocks.robinhood as rh

# This program will use click CLI to return stock prices using robin_stocks python package
# This package aparentally supports crypto trading, but probably just in RH

@click.group()
def main(): # main function is a click group, so it only executes when any of the subfunctions execute
    content = open('sample_config.json').read() # open the credential file for login and assign it to a string via the .read() funciton.
    config = json.loads(content) # load the json file as a python dictionary and assign it to config

    #rh.login(config['username'], config['password']) # normally accepts username and apssword, but we point each field to the field in our cred file.

@main.command(help='Gets a stock quote for one or more symbols') # attach a command to our main group, which will execute from the main function.
@click.argument('symbols', nargs=-1) # arguements with the quote switch will feed into this function. Accepts -1 (unlimited) amount of args with (number of args) switch
def quote(symbols):


    quotes = rh.stocks.get_quotes(symbols)

    for quote in quotes:
        ui.success("{} | {}".format(quote['symbol'], quote['ask_price'])) # shows just symbol and ask_price split by |
        print(quote)

@main.command(help='Gets quotes for all stocks in your watchlist') # help part returns data for the --help menu
def watchlist():
    print("Getting quotes for watchlist")
    with open('watchlist') as f: # open the file and read all of the lines
        symbols = f.read().splitlines()
    quotes = rh.stocks.get_quotes(symbols)
    for quote in quotes:
        print(quotes)


@main.command(help='Buy quantity of stocks by symbol')
@click.argument('quantity', type=click.INT) # Adds quantity argument
@click.argument('symbol', type=click.STRING) # Adds symbol argument
@click.option('--limit', type=click.FLOAT) # Adds optional limit option
def buy(quantity, symbol, limit): # put parameters into function
    if limit is not None: # so if we DO have a  limit order
        ui.success("Buying {} of {} at {}".format(quantity, symbol, limit)) # pulls the styling defines in the ui.py file.
        result = rh.order_buy_limit(symbol, quantity, limit)

    else # else its a market order
        ui.success("Buying {} of {} at market price".format(quantity, symbol)) # pulls the styling defines in the ui.py file.
        result = rh.order_buy_market(symbol, quantity)

    if 'ref_id' in result: # ref_id parameter is used in robinhood's return message success for purchase, so we use it and format it as an success
        ui.success(result) # print the result
    else:
        ui.error(message)

@main.command(help='Sell quantity of stocks by symbol')
@click.argument('quantity', type=click.INT) # Adds quantity argument
@click.argument('symbol', type=click.STRING) # Adds symbol argument
@click.option('--limit', type=click.FLOAT) # Adds optional limit option
def sell(quantity, symbol, limit):
    if limit is not None: # so if we DO have a  limit order
        ui.success("Selling {} of {} at {}".format(quantity, symbol, limit)) # pulls the styling defines in the ui.py file.
        result = rh.order_sell_limit(symbol, quantity, limit)

    else # else its a market order
        ui.success("Selling {} of {} at market price".format(quantity, symbol)) # pulls the styling defines in the ui.py file.
        result = rh.order_sell_market(symbol, quantity)

    if 'ref_id' in result: # ref_id parameter is used in robinhood's return message success for purchase, so we use it and format it as an success
        ui.success(result) # print the result
    else:
        ui.error(message)




if __name__ == '__main__':
    main() # execute the main function if the name of the app is __main__




