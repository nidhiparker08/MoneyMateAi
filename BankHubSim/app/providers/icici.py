from app.providers.base import BaseProvider
from app.providers.common import CommonProvider


class ICICIProvider(CommonProvider, BaseProvider):

    bank_name = "ICICI Bank"

    short_name = "ICICI"

    ifsc_prefix = "ICICI"

    swift_prefix = "ICICI"

    account_prefix = "99"

    branches = [
        "Mumbai Main",
        "Dombivli",
        "Thane",
        "Pune",
        "Delhi",
        "Bangalore",
        "Hyderabad",
        "Chennai",
        "Ahmedabad",
        "Lucknow"
    ]

    def generate_account(self,customer_name,email,phone):
        return {
            "bank": self.bank_name,
            "short_name": self.short_name,

            "branch": self.random_branch(),
            "ifsc": self.random_ifsc(),
            "swift": self.random_swift(),

            "account_number": self.random_account_number(),

            "customer_name": customer_name,
            "email": email,
            "phone": phone,

            "currency": "INR"
        }

    def generate_transactions(self):
        return []

    def generate_investments(self):
        return []