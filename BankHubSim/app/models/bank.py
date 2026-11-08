from sqlalchemy import Column, Integer, String
from app.database import Base


class Bank(Base):
    __tablename__ = "banks"

    id = Column(Integer, primary_key=True, index=True)

    name = Column(String, unique=True, nullable=False)

    short_name = Column(String, unique=True)

    ifsc_prefix = Column(String)

    swift_prefix = Column(String)

    account_prefix = Column(String)

    logo = Column(String)

    primary_color = Column(String)