from datetime import datetime
from typing import Optional
from pydantic import BaseModel


class OrderBase(BaseModel):
    customer_id: int
    promotion_id: Optional[int] = None
    order_type: str
    total_amount: float


class OrderCreate(OrderBase):
    pass


class OrderUpdate(BaseModel):
    promotion_id: Optional[int] = None
    order_type: Optional[str] = None
    order_status: Optional[str] = None
    total_amount: Optional[float] = None


class Order(OrderBase):
    order_id: int
    tracking_number: str
    order_status: str
    order_date: datetime

    class Config:
        from_attributes = True
