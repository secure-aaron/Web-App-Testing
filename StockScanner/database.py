from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "sqlite:///./assets.db"
# SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver/db" <--- not needed since we are not using this database.

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base() # this is the base model declared, and the models file will extend this model.
