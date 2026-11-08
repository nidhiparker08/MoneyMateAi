from pydantic import BaseModel


class ConnectBankRequest(BaseModel):

    bank: str

    name: str

    email: str

    phone: str


class ConnectBankResponse(BaseModel):

    success: bool

    account_id: int

    bank: str

    customer_name: str

    dashboard_ready: bool