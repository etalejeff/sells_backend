#database.py
from sqlalchemy import create_engine
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from fastapi import APIRouter, Depends
from sqlalchemy.ext.declarative import declarative_base
import psycopg2

user = 'sell_user'
password = 'Ll49YhsKgjT50RsDycL82vLxsWs5Zapl'
host = "dpg-clp1kbpoh6hc73br1020-a.frankfurt-postgres.render.com"
port = '5432'
database = 'sell'

connection_str = f'postgresql+asyncpg://{user}:{password}@{host}:{port}/{database}'
sync_connection_str = f'postgresql://{user}:{password}@{host}:{port}/{database}'

engine = create_async_engine(connection_str)
sync_engine = create_engine(sync_connection_str)

Base = declarative_base()

async_session = sessionmaker(autocommit=False, autoflush=False, bind=engine, class_=AsyncSession)

Base.metadata.create_all(bind=sync_engine)