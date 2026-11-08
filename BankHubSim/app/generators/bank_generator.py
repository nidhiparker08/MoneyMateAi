from app.models.bank import Bank

from app.providers.registry import providers


def generate_banks(db):

    for provider in providers.values():

        bank = Bank(

            name=provider.bank_name,

            short_name=provider.short_name,

            ifsc_prefix=provider.ifsc_prefix,

            swift_prefix=provider.swift_prefix,

            account_prefix=provider.account_prefix,

            logo="",

            primary_color="#000000"

        )

        db.add(bank)

    db.commit()