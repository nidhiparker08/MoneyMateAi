import random
from faker import Faker

fake = Faker("en_IN")


class CommonProvider:

    def random_branch(self):
        return random.choice(self.branches)

    def random_ifsc(self):
        return f"{self.ifsc_prefix}{random.randint(1000,9999)}"

    def random_swift(self):
        return f"{self.swift_prefix}INBBXXX"

    def random_account_number(self):
        return (
            self.account_prefix +
            str(random.randint(1000000000,9999999999))
        )

    def customer_name(self):
        return fake.name()

    def email(self):
        return fake.email()

    def phone(self):
        return fake.phone_number()