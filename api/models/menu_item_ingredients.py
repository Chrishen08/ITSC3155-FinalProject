from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship

from ..dependencies.database import Base


class MenuItemIngredient(Base):
    __tablename__ = "menu_item_ingredients"

    menu_item_ingredient_id = Column(
        Integer,
        primary_key=True,
        index=True,
        autoincrement=True
    )
    menu_item_id = Column(
        Integer,
        ForeignKey("menu_items.menu_item_id"),
        nullable=False
    )
    ingredient_id = Column(
        Integer,
        ForeignKey("ingredients.ingredient_id"),
        nullable=False
    )
    quantity_required = Column(Integer, nullable=False)

    menu_item = relationship(
        "MenuItem",
        back_populates="menu_item_ingredients"
    )
    ingredient = relationship(
        "Ingredient",
        back_populates="menu_item_ingredients"
    )