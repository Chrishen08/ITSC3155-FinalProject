from typing import Optional
from pydantic import BaseModel


class MenuItemIngredientBase(BaseModel):
    menu_item_id: int
    ingredient_id: int
    quantity_required: float


class MenuItemIngredientCreate(MenuItemIngredientBase):
    pass


class MenuItemIngredientUpdate(BaseModel):
    quantity_required: Optional[float] = None


class MenuItemIngredient(MenuItemIngredientBase):
    menu_item_ingredient_id: int

    class Config:
        from_attributes = True