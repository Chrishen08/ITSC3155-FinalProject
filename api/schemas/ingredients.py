from typing import Optional
from pydantic import BaseModel


class IngredientBase(BaseModel):
    ingredient_name: str
    quantity_in_stock: float
    unit_of_measure: str


class IngredientCreate(IngredientBase):
    pass


class IngredientUpdate(BaseModel):
    ingredient_name: Optional[str] = None
    quantity_in_stock: Optional[float] = None
    unit_of_measure: Optional[str] = None


class Ingredient(IngredientBase):
    ingredient_id: int

    class Config:
        from_attributes = True