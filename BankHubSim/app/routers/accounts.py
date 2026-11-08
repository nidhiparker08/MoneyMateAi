from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.account import Account

router = APIRouter(
    prefix="/accounts",
    tags=["Accounts"]
)


@router.get("/")
def get_accounts(db: Session = Depends(get_db)):
    return db.query(Account).all()

@router.get("/{account_id}")
def get_account(account_id: int,
                db: Session = Depends(get_db)):

    return db.query(Account).filter(
        Account.id == account_id
    ).first()