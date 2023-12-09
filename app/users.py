# users.py
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.ext.asyncio import create_async_engine
from app.models import User
from app.schemas import User as UserSchema
from typing import List
from sqlalchemy.future import select


router = APIRouter()

user = 'sell_user'
password = 'Ll49YhsKgjT50RsDycL82vLxsWs5Zapl'
host = "dpg-clp1kbpoh6hc73br1020-a.frankfurt-postgres.render.com"
port = '5432'
database = 'sell'

connection_str = f'postgresql+asyncpg://{user}:{password}@{host}:{port}/{database}'

engine = create_async_engine(connection_str)

async_session = sessionmaker(autocommit=False, autoflush=False, bind=engine, class_=AsyncSession)


async def get_db():
    db = async_session()
    try:
        yield db
    finally:
        await db.close()
from sqlalchemy.future import select

@router.get("/users", response_model=List[UserSchema])
async def get_products(db: AsyncSession = Depends(get_db)):
    # Your logic to fetch products from the database
    stmt = select(User)
    result = await db.execute(stmt)
    products = result.scalars().all()

    return products