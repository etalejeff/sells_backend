# products.py
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.ext.asyncio import create_async_engine
from app.models import Product
from app.schemas import Product as ProductSchema, ProductCreate as ProductCreateSchema
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

@router.get("/products", response_model=List[ProductSchema])
async def get_products(db: AsyncSession = Depends(get_db)):
    # Your logic to fetch products from the database
    stmt = select(Product)
    result = await db.execute(stmt)
    products = result.scalars().all()

    return products

@router.post("/products", response_model=ProductSchema)
async def create_product(product: ProductCreateSchema, db: AsyncSession = Depends(get_db)):
    db_product = Product(**product.dict())
    db.add(db_product)
    await db.commit()
    await db.refresh(db_product)
    return db_product
