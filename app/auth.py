# auth.py
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
# from database import async_session
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import create_async_engine


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

@router.post("/login")
def login(db: AsyncSession = Depends(get_db)):
    # Your login logic here using the database session
    return {"message": "Login successful"}

@router.post("/logout")
def logout(db: AsyncSession = Depends(get_db)):
    # Your logout logic here using the database session
    return {"message": "Logout successful"}


