from pydantic import BaseModel
from fastapi import FastAPI, Request, Depends, BackgroundTasks
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
import yfinance
from database import SessionLocal, engine
import models


app = FastAPI() # create app object from FastAPI class

models.Base.metadata.create_all(bind=engine) # As per SQLAchemy documentation. Created bind to engine from main file?
"""
We extended the base model for all of the models that we created, then we made another model in the models.py file.
SQLAchemy is aware of these files, adn we created an engine, so
"""

templates = Jinja2Templates(directory="templates")


class StockRequest(BaseModel): # using pydantic to specify the structure of the request and use input validation?
    symbol: str

class CryptoRequest(BaseModel):
    symbol: str


# This will be needed to get a session to the database.
def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


# Root Request
@app.get("/")
async def dashboard(request: Request, forward_pe = None, dividend_yield = None, ma50 = None, ma200 = None, db: Session = Depends(get_db)): # Also add names of query parameters/elements from dashboard. None means its not required.
    """
    Displays the stock/crypto screen.
    """

    stocks = db.query(models.Stock) # Pulls in queried records from the database.

    print(stocks) # prints entered data to web browser console.

    if forward_pe: # previous used "is not None", but it submits an empty string at the end of the URL. Therefore, it was trying to filter the data using code below and is NOT what we want here.
        stocks = stocks.filter(models.Stock.forward_pe < forward_pe) # second forward_pe is the one in the parameter above.
    if dividend_yield:
        stocks = stocks.filter(models.Stock.dividend_yield > dividend_yield) # Greatter than since we want more moooooney
    if ma50:
        stocks = stocks.filter(models.Stock.price > ma50)
    if ma200:
        stocks = stocks.filter(models.Stock.price > ma200)
    
    return templates.TemplateResponse("dashboard.html", {   # this method requires the Request class imported
        "request": request,
        "stocks": stocks,
        "forward_pe": forward_pe, # Takes the data as it comes in and sending it back to the template.
        "dividend_yield": dividend_yield,
        "ma50": ma50,
        "ma200": ma200
    })

def fetch_stock_data(id: int): # this is a FUNCTION
    db = SessionLocal()
    stock = db.query(models.Stock).filter(models.Stock.id == id).first()

    #stock.forward_pe = 10    # this was for teting instead of yfinance

    yahoo_data = yfinance.Ticker(stock.symbol)

    stock.ma200 = yahoo_data.info['twoHundredDayAverage']
    stock.ma50 = yahoo_data.info['fiftyDayAverage']
    stock.price = yahoo_data.info['previousClose']
    stock.forward_pe = yahoo_data.info['forwardPE']
    stock.forward_eps = yahoo_data.info['forwardEps']
    
    if yahoo_data.info['dividendYield'] is not None:
        stock.dividend_yield = yahoo_data.info['dividendYield'] * 100


    db.add(stock)
    db.commit()

@app.post("/stock")
async def create_stock(stock_request: StockRequest, background_tasks: BackgroundTasks, db: Session = Depends(get_db)): #this will force a connection with the database due to the requirement and the method get_db.
    """
    Creates a stock and stores it in the database.
    """
    stock = models.Stock() # Create model from the model to use here.
    stock.symbol = stock_request.symbol

    db.add(stock) # After this object is inserted as a record with sqlalchemy, the object will be populated with the primary key stock.id
    db.commit()

    background_tasks.add_task(fetch_stock_data, stock.id)

    return {
        "code": "success",
        "message": "stock created"
    }

def fetch_crypto_data(id: int): # this is a FUNCTION
    db = SessionLocal()
    crypto = db.query(models.Crypto).filter(models.Crypto.id == id).first()

    crypto.forward_pe = 10

    db.add(crypto)
    db.commit()

@app.post("/crypto")
async def create_crypto(crypto_request: CryptoRequest, background_tasks: BackgroundTasks, db: Session = Depends(get_db)):
    """
    Creates a coin/token and stores it in the database.
    """
    crypto = models.Crypto() # Create model from the model to use here.
    crypto.symbol = crypto_request.symbol

    db.add(crypto)
    db.commit()

    background_tasks.add_task(fetch_crypto_data, crypto.id)


    return {
        "code": "success",
        "message": "crypto created"
    }

#uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True) # ENABLE RELOAD FOR DEBUGGING. DISABLE FOR PRODUCTION.

