# main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.auth import router as auth_router
from app.products import router as products_router
from app.users import router as cart_router
from app.categories import router as cart_router
from app.database import Base, engine, sync_engine

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI backend!"}

app.include_router(auth_router, tags=["authentication"])
app.include_router(products_router, tags=["products"])
app.include_router(cart_router, tags=["users"])
app.include_router(cart_router, tags=["categories"])

try:
    with sync_engine.connect() as connection_str:
        print('Successfully connected to the PostgreSQL database')
except Exception as ex:
    print(f'Sorry failed to connect: {ex}')

