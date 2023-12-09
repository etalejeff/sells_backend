# seed.py
from faker import Faker
from sqlalchemy.orm import Session
from app.models import User, Category, Product
from app.database import async_session, engine

fake = Faker()

def create_user(db: Session):
    user = User(
        username=fake.user_name(),
        email=fake.email(),
        hashed_password=fake.password()
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

def create_category(db: Session):
    category = Category(name=fake.word())
    db.add(category)
    db.commit()
    db.refresh(category)
    return category

def create_product(db: Session, category_id: int):
    product = Product(
        name=fake.word(),
        price=fake.random_number(digits=2),
        category_id=category_id
    )
    db.add(product)
    db.commit()
    db.refresh(product)
    return product

def seed_data():
    with async_session() as db:
        # Create multiple users
        for _ in range(10):
            create_user(db)

        # Create multiple categories
        categories = [create_category(db) for _ in range(5)]

        # Create multiple products with relationships to categories
        for _ in range(20):
            category = fake.random_element(categories)
            create_product(db, category.id)

if __name__ == "__main__":
    # Run the seed data function
    seed_data()
    print("Seed data added successfully.")
