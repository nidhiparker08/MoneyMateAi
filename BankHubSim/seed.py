from app.database import SessionLocal, Base, engine

import app.models

Base.metadata.create_all(bind=engine)

from app.generators.bank_generator import generate_banks
from app.generators.account_generator import generate_accounts

db = SessionLocal()

generate_banks(db)
generate_accounts(db)

print("Database seeded successfully!")