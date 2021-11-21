# Web-App-Testing
This repository contains some API clients and other utilities I'm working on.

## AlpacaAPI-PaperTrading
An API Client used to interface with the Alpaca API for trading equities using the requests and json Python libraries.

## CandlestickChartsPython
Contains a simple Yahoo Finance, Alpaca and IEX Cloud API client using the yfinance, requests, json, and csv Python libraries to retrieve the history for equities. and the pandas and plotly libraries to plot the data on a candlestick chart.

## CoinGeckoREST
A simple CoinGecko API client using the requests and json Python libraries to retrieve a specified cryptocurrency price history.

## DynamoDB-and-boto3
Uses the boto3 Python library to create a simple Amazon DynamoDB database.

## FastAPI_Testing
An implementation of FastAPI using Uvicorn, an ASGI server implementation, and the fastapi Python library to serve multiple "Todo" webpages.

## FlaskTesting
An implementation of Flask to serve as a simple stock scanner website using the flask python library.

## KivyTesting
A simple Kivy app using hte kivy Python library to connect to a remote server by prompting the user for an IP Address, Port, and username.

## PythonRobinhood
Another equity trading tool used to purchase assets by following [CNN's Fear vs Greed Index](https://money.cnn.com/data/fear-and-greed/) using the requests and bs4 (BeautifulSoup) Python libraries.

## StockChartPatternRecognition
A program which reads historic asset open and close prices from a csv dataset using the csv Python library.

## StockScanner
A more developed Stock Scanner Dashboard which stores and lists assets by their moving average, divident yield, and forward price-to-earnings using the pydantic, fastapi, sqlalchemy, yfinance, database, and models Python libraries and Jinja2 templates.

## TwitterAPI
A twitter API client which will return tweet information such as the text, username, screen name, and creation date based upon a specified string using the twitter Python library.

## WebsocketPython
This program uses the Coinbase Websocket API to retrieve real-time ticker streaming data with candlestick information using the websocket, json, and dateutil Python libraries.

## robin
This program will use click CLI to return stock prices using the click, json, ui, and robin_stocks python libraries. The robin_stocks library also aparentally supports crypto trading as well, although it may only work on the RobinHood platform.

## stockbot
A simple AWS Chalice application used to serve a serverless website using AWS Lambda and the chalice Python library.
