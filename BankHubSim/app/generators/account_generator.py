import random

from faker import Faker

from app.models.account import Account
from app.models.bank import Bank

from app.generators.transaction_generator import generate_transactions

fake = Faker("en_IN")


def generate_accounts(db):

    banks = db.query(Bank).all()

    for bank in banks:

        for _ in range(10):

            account = Account(

                bank_id=bank.id,

                customer_name=fake.name(),

                account_number=str(
                    random.randint(100000000000, 999999999999)
                ),

                account_type=random.choice([
                    "Savings",
                    "Current"
                ]),

                branch=random.choice([
                    "Mumbai",
                    "Pune",
                    "Thane",
                    "Delhi",
                    "Bangalore",
                    "Hyderabad"
                ]),

                ifsc=f"{bank.ifsc_prefix}{random.randint(1000,9999)}",

                swift=f"{bank.swift_prefix}INBBXXX",

                email=fake.email(),

                phone=fake.phone_number(),

                balance=round(random.uniform(15000, 500000), 2)

            )

            db.add(account)

            # Generates account.id without committing
            db.flush()

            transactions = generate_transactions(account)

            for transaction in transactions:
                db.add(transaction)

    db.commit()