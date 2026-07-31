from datetime import datetime
from typing import Optional
from pydantic import BaseModel


class PaymentBase(BaseModel):
    order_id: int
    payment_method: str
    payment_status: str
    amount: float


class PaymentCreate(PaymentBase):
    pass


class PaymentUpdate(BaseModel):
    payment_method: Optional[str] = None
    payment_status: Optional[str] = None
    amount: Optional[float] = None


class Payment(PaymentBase):
    payment_id: int
    payment_date: datetime

    class Config:
        from_attributes = True