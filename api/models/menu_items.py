from sqlalchemy import Column, Integer, String, DECIMAL, Boolean
from sqlalchemy.orm import relationship

from ..dependencies.database import Base


class MenuItem(Base):
    __tablename__ = "menu_items"

    menu_item_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    description = Column(String(300))
    price = Column(DECIMAL(10, 2), nullable=False)
    calories = Column(Integer)
    category = Column(String(50), nullable=False)
    is_available = Column(Boolean, nullable=False, default=True)

    order_items = relationship("OrderItem", back_populates="menu_item")