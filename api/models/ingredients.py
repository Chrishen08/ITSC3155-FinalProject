from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from ..dependencies.database import Base


class Ingredient(Base):
    __tablename__ = "ingredients"

    ingredient_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    ingredient_name = Column(String(100), nullable=False, unique=True)
    quantity_in_stock = Column(Integer, nullable=False)
    unit_of_measure = Column(String(25), nullable=False)

    menu_item_ingredients = relationship(
        "MenuItemIngredient",
        back_populates="ingredient"
    )