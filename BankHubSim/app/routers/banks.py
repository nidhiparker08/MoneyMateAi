from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.bank import Bank

router = APIRouter(
    prefix="/banks",
    tags=["Banks"]
)


@router.get("/")
def get_banks(db: Session = Depends(get_db)):
    return db.query(Bank).all()

@router.get("/{bank_id}")
def get_bank(bank_id: int, db: Session = Depends(get_db)):

    return db.query(Bank).filter(
        Bank.id == bank_id
    ).first()


@router.get("/{bank}")

def bank_details(bank: str):

    provider = providers.get(bank.upper())

    if not provider:
        return {"error": "Bank not found"}

    return provider.generate_account()