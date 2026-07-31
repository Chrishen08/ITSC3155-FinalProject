from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from ..controllers import menu_item_ingredients as controller
from ..schemas import menu_item_ingredients as schema
from ..dependencies.database import get_db


router = APIRouter(
    tags=["Menu Item Ingredients"],
    prefix="/menu-item-ingredients"
)


@router.post("/", response_model=schema.MenuItemIngredient)
def create(
    request: schema.MenuItemIngredientCreate,
    db: Session = Depends(get_db)
):
    return controller.create(
        db=db,
        request=request
    )


@router.get("/", response_model=List[schema.MenuItemIngredient])
def read_all(
    db: Session = Depends(get_db)
):
    return controller.read_all(
        db=db
    )


@router.get("/availability/{menu_item_id}")
def check_ingredient_availability(
    menu_item_id: int,
    db: Session = Depends(get_db)
):
    return controller.check_ingredient_availability(
        db=db,
        menu_item_id=menu_item_id
    )


@router.get(
    "/{menu_item_ingredient_id}",
    response_model=schema.MenuItemIngredient
)
def read_one(
    menu_item_ingredient_id: int,
    db: Session = Depends(get_db)
):
    return controller.read_one(
        db=db,
        menu_item_ingredient_id=menu_item_ingredient_id
    )


@router.put(
    "/{menu_item_ingredient_id}",
    response_model=schema.MenuItemIngredient
)
def update(
    menu_item_ingredient_id: int,
    request: schema.MenuItemIngredientUpdate,
    db: Session = Depends(get_db)
):
    return controller.update(
        db=db,
        menu_item_ingredient_id=menu_item_ingredient_id,
        request=request
    )


@router.delete(
    "/{menu_item_ingredient_id}",
    status_code=204
)
def delete(
    menu_item_ingredient_id: int,
    db: Session = Depends(get_db)
):
    return controller.delete(
        db=db,
        menu_item_ingredient_id=menu_item_ingredient_id
    )