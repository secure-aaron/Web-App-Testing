# this file stores all of our database models.

from sqlalchemy import Column, String, Numeric, Integer
from database import Base
#from sqlalchemy.orm import relationship        # Not needed since we are currently not relating tables yet, except i may want to in the future.




class Stock(Base):
    __tablename__ = "stocks"

    id = Column(Integer, primary_key=True, index=True)
    symbol = Column(String, unique=True, index=True)
    price = Column(Numeric(10,4))
    forward_pe = Column(Numeric(10,4))
    forward_eps = Column(Numeric(10,4))
    dividend_yield = Column(Numeric(10,4))
    ma50 = Column(Numeric(10,4))
    ma200 = Column(Numeric(10,4))

class Crypto(Base):
    __tablename__ = "crypto"

    id = Column(Integer, primary_key=True, index=True)
    symbol = Column(String, unique=True, index=True)
    price = Column(Numeric(10,4))
    forward_pe = Column(Numeric(10,4))
    forward_eps = Column(Numeric(10,4))
    dividend_yield = Column(Numeric(10,4))
    ma50 = Column(Numeric(10,4))
    ma200 = Column(Numeric(10,4))




    #email = Column(String, unique=True, index=True)
    #hashed_password = Column(String)
    #is_active = Column(Boolean, default=True)

    #items = relationship("Item", back_populates="owner")