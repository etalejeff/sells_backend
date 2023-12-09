# main.py
from fastapi import FastAPI
from app.auth import router as auth_router
from app.products import router as products_router
from app.cart import router as cart_router
from app.database import Base, engine, async_session

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI backend!"}

app.include_router(auth_router, prefix="/auth", tags=["authentication"])
app.include_router(products_router, prefix="/products", tags=["products"])
app.include_router(cart_router, prefix="/cart", tags=["cart"])

try:
    with engine.connect() as connection_str:
        print('Successfully connected to the PostgreSQL database')
except Exception as ex:
    print(f'Sorry failed to connect: {ex}')

async def get_db():
    db = async_session()
    try:
        yield db
    finally:
        await db.close()
