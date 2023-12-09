# schemas.py
from pydantic import BaseModel
from typing import Optional, List, Union
from datetime import datetime

class UserBase(BaseModel):
    user_name: str
    email: str
    hashed_password: str
   

class UserCreate(UserBase):
    password: str
    id: Union[int, None] = None
    created_at: Union[datetime, None] = None
    updated_at: Union[datetime, None] = None

class UserUpdate(BaseModel):
    user_name: str = None
    email: str = None
    hashed_password: str = None

class UserLogin(BaseModel):
    email: str
    hashed_password: str


class User(UserBase):
    id: Union[int, None] = None
    email: Union[str, None] = None

    class Config:
        from_attributes = True
        orm_mode = True

class CategoryBase(BaseModel):
    name: str

class CategoryCreate(CategoryBase):
    id: Union[int, None] = None
    created_at: Union[datetime, None] = None
    updated_at: Union[datetime, None] = None

class CategoryUpdate(BaseModel):
    name: str = None

class Category(CategoryBase):
    id: Union[int, None] = None

    class Config:
        from_attributes = True
        orm_mode = True

class ProductBase(BaseModel):
    name: str
    price: float
    category_id: int

class ProductCreate(ProductBase):
    id: Union[int, None] = None
    created_at: Union[datetime, None] = None
    updated_at: Union[datetime, None] = None

class ProductUpdate(BaseModel):
    name: str = None
    price: float = None
    category_id: int = None

class Product(ProductBase):
    id: Union[int, None] = None

    class Config:
        from_attributes = True
        orm_mode = True

class CartBase(BaseModel):
    user_id: int
    product_id: int
    quantity: int

class CartCreate(CartBase):
    id: Union[int, None] = None
    created_at: Union[datetime, None] = None
    updated_at: Union[datetime, None] = None

class CartUpdate(BaseModel):
    user_id: int = None
    product_id: int = None
    quantity: int = None

class Cart(CartBase):
    id: Union[int, None] = None

    class Config:
        from_attributes = True
        orm_mode = True

