# products.py
from models import User
from database import get_db, APIRouter, Depends, AsyncSession

router = APIRouter()

@router.get("/products")
def get_products(db: AsyncSession = Depends(get_db)):
    # Your logic to fetch products from the database
    return {"message": "List of products"}

@router.post("/products")
def create_product(db: AsyncSession = Depends(get_db)):
    # Your logic to create a new product
    return {"message": "Product created"}
