from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.investment import Investment

router = APIRouter(
    prefix="/investments",
    tags=["Investments"]
)
@router.get("/{account_id}")

def investments(
        account_id: int,
        db: Session = Depends(get_db)
):

    return db.query(Investment)\
        .filter(
            Investment.account_id == account_id
        )\
        .all()