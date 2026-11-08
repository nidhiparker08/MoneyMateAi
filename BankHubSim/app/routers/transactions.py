from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.transaction import Transaction

router = APIRouter(
    prefix="/transactions",
    tags=["Transactions"]
)

@router.get("/{account_id}")

def account_transactions(
        account_id: int,
        db: Session = Depends(get_db)
):

    return db.query(Transaction).filter(
        Transaction.account_id == account_id
    ).all()

@router.get("/{account_id}/latest")

def latest_transactions(
        account_id: int,
        db: Session = Depends(get_db)
):

    return db.query(Transaction)\
        .filter(
            Transaction.account_id == account_id
        )\
        .order_by(Transaction.date.desc())\
        .limit(20)\
        .all()