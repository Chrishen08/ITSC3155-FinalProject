from sqlalchemy import Column, Integer, String, DECIMAL, DateTime, Boolean
from sqlalchemy.orm import relationship
from datetime import datetime

from ..dependencies.database import Base


class Promotion(Base):
    __tablename__ = "promotions"

    promotion_id = Column(
        Integer,
        primary_key=True,
        index=True,
        autoincrement=True
    )
    promo_code = Column(String(50), unique=True, nullable=False)
    description = Column(String(255))
    discount_percentage = Column(DECIMAL(5, 2), nullable=False)
    start_date = Column(DateTime, nullable=False, default=datetime.utcnow)
    end_date = Column(DateTime, nullable=False)
    is_active = Column(Boolean, nullable=False, default=True)

    orders = relationship("Order", back_populates="promotion")