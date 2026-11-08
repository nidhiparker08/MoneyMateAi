from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Float
from sqlalchemy import ForeignKey

from app.database import Base


class Account(Base):

    __tablename__ = "accounts"

    id = Column(Integer, primary_key=True)

    bank_id = Column(Integer, ForeignKey("banks.id"))

    customer_name = Column(String)

    account_number = Column(String, unique=True)

    account_type = Column(String)

    branch = Column(String)

    ifsc = Column(String)

    swift = Column(String)

    email = Column(String)

    phone = Column(String)

    balance = Column(Float)

    currency = Column(String, default="INR")