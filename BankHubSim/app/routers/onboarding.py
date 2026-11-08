from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas.connect_bank import ConnectBankRequest
from app.services.onboarding_service import OnboardingService

router = APIRouter(
    prefix="/onboarding",
    tags=["Onboarding"]
)


@router.post("/connect-bank")
def connect_bank(
    request: ConnectBankRequest,
    db: Session = Depends(get_db)
):

    service = OnboardingService(db)

    return service.connect_bank(
        request.bank,
        request.name,
        request.email,
        request.phone
    )