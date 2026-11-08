from fastapi import FastAPI
from app.database import Base
from app.database import engine
from app.routers.banks import router as bank_router

from app.routers.banks import router as bank_router
from app.routers.accounts import router as account_router
from app.routers.transactions import router as transaction_router
from app.routers.investments import router as investment_router
from app.routers.onboarding import router as onboarding_router


import app.models

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="BankHub API",
    version="1.0.0"
)

app.include_router(onboarding_router)

app.include_router(bank_router)

app.include_router(bank_router)

app.include_router(account_router)

app.include_router(transaction_router)

app.include_router(investment_router)

@app.get("/")
def root():
    return {"message": "BankHub API Running"}