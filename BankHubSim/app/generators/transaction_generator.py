import random
import uuid

from datetime import datetime, timedelta
from collections import defaultdict

from app.data.merchants import MERCHANTS
from app.data.categories import (
    CREDIT_CATEGORIES,
    DEBIT_CATEGORIES,
)

# =====================================================
# CONFIGURATION
# =====================================================

MONTHS = 12

MIN_DAILY_TXNS = 0
MAX_DAILY_TXNS = 4

SALARY_RANGE = (
    40000,
    100000,
)

SAVING_RATIO = (
    0.18,
    0.35,
)

CATEGORY_SPLIT = {

    "Food":0.18,

    "Shopping":0.10,

    "Travel":0.08,

    "Bills":0.22,

    "Entertainment":0.05,

    "Investment":0.10,

    "Healthcare":0.05,

    "Education":0.04,

    "Cash Withdrawal":0.03,

}

PAYMENT_MODES=[

    "UPI",

    "Debit Card",

    "Credit Card",

    "ATM",

    "IMPS",

    "NEFT",

]

SALARY_COMPANIES=[

    "TCS",

    "Infosys",

    "Capgemini",

    "Google India",

    "Amazon India",

    "Reliance Industries",

]

REFUNDS=[

    "Amazon Refund",

    "Flipkart Refund",

    "Swiggy Refund",

]

FIXED_BILLS={

    "Rent":(18000,28000),

    "Electricity":(900,2500),

    "Internet":(799,1499),

    "Mobile":(299,799),

}

def random_time():

    return (

        random.randint(7,22),

        random.randint(0,59),

        random.randint(0,59),

    )


def build_datetime(day):

    h,m,s=random_time()

    return datetime(

        day.year,

        day.month,

        day.day,

        h,

        m,

        s,

    )


def create_transaction(

    txn_datetime,

    txn_type,

    category,

    merchant,

    amount,

    payment_mode,

    balance,

    account,

):

    return {

        "transaction_id":str(uuid.uuid4()),

        "date":txn_datetime.strftime("%Y-%m-%d"),

        "time":txn_datetime.strftime("%H:%M:%S"),

        "title":merchant,

        "description":merchant,

        "merchant":merchant,

        "category":category,

        "amount":round(amount,2),

        "type":txn_type,

        "payment_method":payment_mode,

        "balance":round(balance,2),

        "status":"SUCCESS",

        "sender":account["customer_name"] if txn_type=="expense" else merchant,

        "receiver":merchant if txn_type=="expense" else account["customer_name"],

        "reference":str(uuid.uuid4())[:12].upper(),

        "source":"bankhub",

    }

    # =====================================================
# MONTHLY BUDGET ENGINE
# =====================================================

def create_month_budget(salary):

    savings = random.uniform(*SAVING_RATIO)

    total_expense_budget = salary * (1 - savings)

    budgets = {}

    for category, ratio in CATEGORY_SPLIT.items():

        budgets[category] = round(total_expense_budget * ratio, 2)

    return budgets


def generate_fixed_transactions(events, month_start, salary):

    # Salary

    salary_day = random.randint(1, 5)

    salary_date = month_start.replace(day=salary_day)

    events.append({

        "datetime": build_datetime(salary_date),

        "type": "income",

        "category": "Salary",

        "merchant": random.choice(SALARY_COMPANIES),

        "amount": salary,

        "payment_mode": "NEFT",

    })

    # Rent

    rent_day = random.randint(2, 6)

    rent = random.randint(*FIXED_BILLS["Rent"])

    events.append({

        "datetime": build_datetime(month_start.replace(day=rent_day)),

        "type": "expense",

        "category": "Bills",

        "merchant": "House Rent",

        "amount": rent,

        "payment_mode": "UPI",

    })

    # Electricity

    bill = random.randint(*FIXED_BILLS["Electricity"])

    events.append({

        "datetime": build_datetime(month_start.replace(day=random.randint(8,15))),

        "type":"expense",

        "category":"Bills",

        "merchant":"Electricity Bill",

        "amount":bill,

        "payment_mode":"UPI",

    })

    # Internet

    internet = random.randint(*FIXED_BILLS["Internet"])

    events.append({

        "datetime":build_datetime(month_start.replace(day=random.randint(12,18))),

        "type":"expense",

        "category":"Bills",

        "merchant":"Jio Fiber",

        "amount":internet,

        "payment_mode":"UPI",

    })

    # Mobile

    recharge=random.randint(*FIXED_BILLS["Mobile"])

    events.append({

        "datetime":build_datetime(month_start.replace(day=random.randint(18,25))),

        "type":"expense",

        "category":"Bills",

        "merchant":"Jio",

        "amount":recharge,

        "payment_mode":"UPI",

    })

    # SIP

    sip=random.choice([2000,3000,5000,10000])

    events.append({

        "datetime":build_datetime(month_start.replace(day=random.randint(5,12))),

        "type":"expense",

        "category":"Investment",

        "merchant":"Mutual Fund SIP",

        "amount":sip,

        "payment_mode":"UPI",

    })

# =====================================================
# DAILY TRANSACTION ENGINE
# =====================================================

def spend(category_budget, category, minimum, maximum):

    remaining = category_budget.get(category, 0)

    if remaining <= minimum:
        return None

    amount = random.randint(minimum, maximum)

    if amount > remaining:
        amount = round(remaining, 2)

    category_budget[category] -= amount

    return amount


def generate_daily_transactions(events, month_start, budgets):

    year = month_start.year
    month = month_start.month

    if month == 12:
        month_end = datetime(year + 1, 1, 1) - timedelta(days=1)
    else:
        month_end = datetime(year, month + 1, 1) - timedelta(days=1)

    current = month_start

    today = datetime.now()

    while current <= month_end:

        # Do not generate transactions for dates ahead of today
        if current.date() > today.date():
            break

        daily_txns = random.randint(
            MIN_DAILY_TXNS,
            MAX_DAILY_TXNS,
        )

        for _ in range(daily_txns):

            category = random.choices(

                population=[
                    "Food",
                    "Shopping",
                    "Travel",
                    "Entertainment",
                    "Healthcare",
                    "Education",
                    "Cash Withdrawal",
                ],

                weights=[
                    35,
                    12,
                    15,
                    8,
                    8,
                    7,
                    15,
                ],

            )[0]

            if category == "Food":

                amount = spend(
                    budgets,
                    "Food",
                    120,
                    650,
                )

            elif category == "Shopping":

                amount = spend(
                    budgets,
                    "Shopping",
                    400,
                    3000,
                )

            elif category == "Travel":

                amount = spend(
                    budgets,
                    "Travel",
                    100,
                    1200,
                )

            elif category == "Entertainment":

                amount = spend(
                    budgets,
                    "Entertainment",
                    250,
                    900,
                )

            elif category == "Healthcare":

                amount = spend(
                    budgets,
                    "Healthcare",
                    300,
                    2500,
                )

            elif category == "Education":

                amount = spend(
                    budgets,
                    "Education",
                    500,
                    3500,
                )

            else:

                amount = spend(
                    budgets,
                    "Cash Withdrawal",
                    500,
                    3000,
                )

            if amount is None:
                continue

            merchant = random.choice(

                MERCHANTS.get(
                    category,
                    [category],
                )

            )

            events.append({

                "datetime": build_datetime(current),

                "type": "expense",

                "category": category,

                "merchant": merchant,

                "amount": amount,

                "payment_mode": random.choice(PAYMENT_MODES),

            })

        # Small chance of refund

        if random.random() < 0.02:

            events.append({

                "datetime": build_datetime(current),

                "type": "income",

                "category": "Refund",

                "merchant": random.choice(REFUNDS),

                "amount": random.randint(150,1200),

                "payment_mode":"UPI",

            })

        current += timedelta(days=1)

# =====================================================
# FINAL GENERATOR
# =====================================================

def generate_transactions(account):

    events = []

    today = datetime.now()

    # Starting month (12 months ago)
    current_month = datetime(
        today.year,
        today.month,
        1,
    ) - timedelta(days=330)

    opening_balance = random.randint(
        5000,
        50000,
    )

    running_balance = opening_balance

    # Generate 12 months
    for _ in range(MONTHS):

        salary = random.randint(
            SALARY_RANGE[0],
            SALARY_RANGE[1],
        )

        budgets = create_month_budget(salary)

        generate_fixed_transactions(
            events,
            current_month,
            salary,
        )

        generate_daily_transactions(
            events,
            current_month,
            budgets,
        )

        # Next month
        if current_month.month == 12:

            current_month = datetime(
                current_month.year + 1,
                1,
                1,
            )

        else:

            current_month = datetime(
                current_month.year,
                current_month.month + 1,
                1,
            )

    # ----------------------------------------------------
    # Sort by date
    # ----------------------------------------------------

    events.sort(
        key=lambda x: x["datetime"]
    )

    # ----------------------------------------------------
    # Reject any event ahead of the current date & time
    # (no transaction may be created in the future)
    # ----------------------------------------------------

    now = datetime.now()

    events = [
        event
        for event in events
        if event["datetime"] <= now
    ]

    transactions = []

    # ----------------------------------------------------
    # Running Balance
    # ----------------------------------------------------

    for event in events:

        if event["type"] == "income":

            running_balance += event["amount"]

        else:

            running_balance -= event["amount"]

        # Prevent impossible balances
        if running_balance < 1000:

            running_balance += random.randint(
                15000,
                60000,
            )

            transactions.append(

                create_transaction(

                    txn_datetime=event["datetime"],

                    txn_type="income",

                    category="Salary",

                    merchant=random.choice(
                        SALARY_COMPANIES
                    ),

                    amount=running_balance,

                    payment_mode="NEFT",

                    balance=running_balance,

                    account=account,

                )

            )

        transactions.append(

            create_transaction(

                txn_datetime=event["datetime"],

                txn_type=event["type"],

                category=event["category"],

                merchant=event["merchant"],

                amount=event["amount"],

                payment_mode=event["payment_mode"],

                balance=running_balance,

                account=account,

            )

        )

    return transactions