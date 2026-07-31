from sqlalchemy import Column, Integer, String, DateTime, DECIMAL, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime

from ..dependencies.database import Base


class Order(Base):
    __tablename__ = "orders"

    order_id = Column(Integer, primary_key=True, index=True, autoincrement=True)

    customer_id = Column(
        Integer,
        ForeignKey("customers.customer_id"),
        nullable=False
    )

    promotion_id = Column(
        Integer,
        ForeignKey("promotions.promotion_id"),
        nullable=True
    )

    order_date = Column(DateTime, nullable=False, default=datetime.utcnow)
    tracking_number = Column(String(50), unique=True, nullable=False)
    order_status = Column(String(50), nullable=False, default="Pending")
    order_type = Column(String(20), nullable=False)
    total_amount = Column(DECIMAL(10, 2), nullable=False)

    customer = relationship("Customer", back_populates="orders")
    promotion = relationship("Promotion", back_populates="orders")
    order_items = relationship("OrderItem", back_populates="order")
    payments = relationship("Payment", back_populates="order")