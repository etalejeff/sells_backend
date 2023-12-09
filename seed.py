# seed.py
from faker import Faker
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.models import User, Category, Product
from app.database import async_session, engine

fake = Faker()

async def delete_data(db: AsyncSession):
    await db.execute(User.__table__.delete())
    await db.execute(Product.__table__.delete())
    await db.execute(Category.__table__.delete())
    await db.commit()

async def create_user(db: AsyncSession):
    user = User(
        username=fake.user_name(),
        email=fake.email(),
        hashed_password=fake.password()
    )
    db.add(user)
    await db.commit()
    await db.refresh(user)
    return user

async def create_category(db: AsyncSession):
    category = Category(
        name=fake.word(),
        image=fake.image_url()
    )
    db.add(category)
    await db.commit()
    await db.refresh(category)
    return category

async def create_product(db: AsyncSession, category_id: int):
    product = Product(
        name=fake.word(),
        price=fake.random_number(digits=2),
        
        image=fake.image_url(),
        category_id=category_id
    )
    db.add(product)
    await db.commit()
    await db.refresh(product)
    return product

async def seed_data():
    async with async_session() as db:
        await delete_data(db)

        # Create multiple users
        for _ in range(10):
            await create_user(db)

        # Create multiple categories and store their IDs
        category_ids = []
        for _ in range(5):
            category = await create_category(db)
            category_ids.append(category.id)

        # Create multiple products with relationships to categories
        for _ in range(20):
            category_id = fake.random_element(category_ids)
            await create_product(db, category_id)

if __name__ == "__main__":
    # Run the seed data function
    import asyncio
    asyncio.run(seed_data())
    print("Seed data added successfully.")
