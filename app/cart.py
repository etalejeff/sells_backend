# cart.py
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
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

@router.get("/cart")
def get_cart(db: AsyncSession = Depends(get_db)):
    # Your logic to fetch the user's cart items
    return {"message": "User's shopping cart"}

@router.post("/cart/add")
def add_to_cart(db: AsyncSession = Depends(get_db)):
    # Your logic to add a product to the user's cart
    return {"message": "Product added to the cart"}
