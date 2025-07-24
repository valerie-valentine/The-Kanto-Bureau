import os
from sqlalchemy import create_engine
# from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("SQLALCHEMY_DATABASE_URI")

# connecton methods ~
# creates the connection from the api server to my database; this runs when my app starts up. # the initial connecton
# engine = create_async_engine(DATABASE_URL)
engine = create_engine(DATABASE_URL)
# db session - this application has a smaller # of connections to the db; so we do not have to always set up the db connection everytime.
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
# does schema work to check the database types, column names and table names.
Base = declarative_base()
