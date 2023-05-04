from os import environ
from sqlalchemy import create_engine
from dotenv import dotenv_values
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

env = dotenv_values(".env")

URI = f"mysql+pymysql://{env['DB_USERNAME']}:{env['DB_PASSWORD']}@{env['DB_IP']}:{env['DB_PORT']}/{env['DB']}"

engine = create_engine(url=URI, pool_pre_ping=True)
session = sessionmaker(bind=engine)
session = session()
Base = declarative_base()
