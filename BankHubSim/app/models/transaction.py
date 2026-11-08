from sqlalchemy import *

from app.database import Base


class Transaction(Base):

    __tablename__ = "transactions"

    id = Column(Integer, primary_key=True)

    account_id = Column(Integer, ForeignKey("accounts.id"))

    txn_id = Column(String, unique=True)

    date = Column(Date)

    time = Column(Time)

    amount = Column(Float)

    txn_type = Column(String)

    mode = Column(String)

    sender = Column(String)

    receiver = Column(String)

    narration = Column(String)

    category = Column(String)

    balance_after = Column(Float)

    status = Column(String)