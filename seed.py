# seed.py
from faker import Faker
from sqlalchemy.ext.asyncio import AsyncSession
from app.models import User, Category, Product
from app.database import async_session, engine

fake = Faker()

async def create_user(db: AsyncSession):
    user = User(
        username=fake.user_name(),
        email=fake.email(),
        hashed_password=fake.password()
    )
    db.add(user)
    await db.commit()
    await db.refresh(user)  # Add 'await' here
    return user

async def create_category(db: AsyncSession):
    category = Category(name=fake.word())
    db.add(category)
    await db.commit()
    # await db.flush()
    await db.refresh(category)
    return category

async def create_product(db: AsyncSession, category_id: int):
    product = Product(
        name=fake.word(),
        price=fake.random_number(digits=2),
        category_id=category_id
    )
    db.add(product)
    await db.commit()
    # await db.flush()
    await db.refresh(product)
    return product

async def seed_data():
    async with async_session() as db:
        # Create multiple users
        for _ in range(10):
            await create_user(db)

        # Create multiple categories
        for _ in range(5):
            await create_category(db)

        # Create multiple products with relationships to categories
        for _ in range(20):
            category_id = fake.random_int(min=1, max=5)
            await create_product(db, category_id)

if __name__ == "__main__":
    # Run the seed data function
    import asyncio
    asyncio.run(seed_data())
    print("Seed data added successfully.")
