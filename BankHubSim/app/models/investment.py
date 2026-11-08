from sqlalchemy import *

from app.database import Base


class Investment(Base):

    __tablename__ = "investments"

    id = Column(Integer, primary_key=True)

    account_id = Column(Integer, ForeignKey("accounts.id"))

    investment_type = Column(String)

    name = Column(String)

    symbol = Column(String)

    quantity = Column(Float)

    invested_amount = Column(Float)

    current_value = Column(Float)

    broker = Column(String)