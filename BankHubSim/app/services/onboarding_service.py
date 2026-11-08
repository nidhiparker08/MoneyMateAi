from sqlalchemy.orm import Session

from app.providers.registry import providers

from app.generators.transaction_generator import generate_transactions
from app.generators.investment_generator import generate_investments


class OnboardingService:

    def __init__(self, db: Session):
        self.db = db

    def connect_bank(self,bank_name,customer_name,email,phone):
        # ---------------------------------------
        # Get Provider
        # ---------------------------------------

        provider = providers.get(bank_name.upper())

        if provider is None:
            raise ValueError(f"Unsupported bank: {bank_name}")

        # ---------------------------------------
        # Generate Account
        # ---------------------------------------

        account = provider.generate_account(
            customer_name,
            email,
            phone
        )

        # Random starting balance
        import random

        account["balance"] = round(
            random.uniform(25000, 600000),
            2
        )

        # ---------------------------------------
        # Generate Transactions
        # ---------------------------------------

        transactions = generate_transactions(
            account
        )

        # ---------------------------------------
        # Generate Investments
        # ---------------------------------------

        investments = generate_investments(
            account
        )

        # ---------------------------------------
        # Return JSON
        # ---------------------------------------

        return {

            "success": True,

            "account": account,

            "transactions": transactions,

            "investments": investments

        }