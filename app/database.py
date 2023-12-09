#database.py
from sqlalchemy import create_engine
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from fastapi import APIRouter, Depends
from sqlalchemy.ext.declarative import declarative_base
import psycopg2
# from .config import Config

# DATABASE_URL = Config.DATABASE_URL

# engine = create_engine(
#     DATABASE_URL, connect_args={"check_same_thread": False}
# )

user = 'sell_user'
password = 'Ll49YhsKgjT50RsDycL82vLxsWs5Zapl'
host = "dpg-clp1kbpoh6hc73br1020-a.frankfurt-postgres.render.com"
port = '5432'
database = 'sell'

connection_str = f'postgresql://{user}:{password}@{host}:{port}/{database}'

engine = create_engine(connection_str)

Base = declarative_base()

async_session = sessionmaker(autocommit=False, autoflush=False, bind=engine, class_=AsyncSession)

Base.metadata.create_all(bind=engine)