import random
from datetime import datetime, timedelta

from app.data.stocks import STOCKS
from app.data.mutual_funds import FUNDS

BROKERS = [
    "Groww",
    "Zerodha",
    "Angel One",
    "Upstox",
]

ETF_NAMES = [
    "Nippon India ETF Nifty BeES",
    "Nippon India ETF Gold BeES",
]

FD_BANKS = [
    "State Bank of India",
    "HDFC Bank",
    "ICICI Bank",
    "Axis Bank",
]


def generate_investments(account):

    investments = []

    # ---------------- Stocks ----------------

    for _ in range(random.randint(4, 8)):

        stock = random.choice(STOCKS)

        qty = random.randint(5, 150)

        buy_price = random.randint(200, 3000)

        current_price = round(
            buy_price * random.uniform(0.8, 1.5),
            2
        )

        investments.append({

            "type": "Stock",

            "broker": random.choice(BROKERS),

            "name": stock[0],

            "symbol": stock[1],

            "quantity": qty,

            "buy_price": buy_price,

            "invested_amount": round(qty * buy_price, 2),

            "current_value": round(qty * current_price, 2),

            "purchase_date": (
                datetime.now()
                - timedelta(days=random.randint(30, 1200))
            ).strftime("%Y-%m-%d")

        })

    # ---------------- Mutual Funds ----------------

    for _ in range(random.randint(2, 5)):

        fund = random.choice(FUNDS)

        units = round(random.uniform(25, 500), 3)

        nav = round(random.uniform(20, 250), 2)

        current_nav = round(
            nav * random.uniform(0.9, 1.4),
            2
        )

        investments.append({

            "type": "Mutual Fund",

            "broker": random.choice(BROKERS),

            "name": fund,

            "units": units,

            "purchase_nav": nav,

            "current_nav": current_nav,

            "invested_amount": round(units * nav, 2),

            "current_value": round(units * current_nav, 2),

            "sip": random.choice([True, False])

        })

    # ---------------- Gold ETF ----------------

    investments.append({

        "type": "Gold ETF",

        "broker": random.choice(BROKERS),

        "name": random.choice(ETF_NAMES),

        "invested_amount": random.randint(15000, 120000),

        "current_value": random.randint(18000, 150000)

    })

    # ---------------- Fixed Deposit ----------------

    investments.append({

        "type": "Fixed Deposit",

        "bank": random.choice(FD_BANKS),

        "amount": random.randint(50000, 500000),

        "interest_rate": round(
            random.uniform(6.2, 7.8),
            2
        ),

        "tenure_months": random.choice([
            12,
            24,
            36,
            60
        ])

    })

    return investments