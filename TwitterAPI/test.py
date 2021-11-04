import twitter

tickerParams = 'AAPL'
#tickers = app.current_request.query_params['tickers'].split(',') # any request that has tickers parameter will be assigned to tickers using TICKER,TICKER format

api = twitter.Api(consumer_key='REDACTED',
                    consumer_secret='REDACTED',
                    access_token_key='REDACTED',
                    access_token_secret='REDACTED')
    
stream = {} # define stream as an empty dict

for ticker in tickerParams:
    stream[ticker] = [] # creating a stream for each ticker

    results = api.GetSearch(raw_query="q={}%20&result_type=popular&count=5".format(ticker)) # replaces {} with ticker

    #results = api.GetSearch(raw_query="q={}%20&result_type=recent&since=2021-03-22&count=100".format(ticker)) # replaces {} with ticker
    for result in results: # each ticker will contain the following data which is retrieved from the line above
        
        tweet = {
            'created': result.created_at,
            'text': result.text,
            'username': result.user.name,
            'screen_name': result.user.screen_name
        }
        print("\n")
        print(tweet['text']) # append each stream to the list of tweets






