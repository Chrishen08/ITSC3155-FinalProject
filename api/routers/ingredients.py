from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from ..controllers import ingredients as controller
from ..schemas import ingredients as schema
from ..dependencies.database import get_db


router = APIRouter(
    tags=["Ingredients"],
    prefix="/ingredients"
)


@router.post("/", response_model=schema.Ingredient)
def create(
    request: schema.IngredientCreate,
    db: Session = Depends(get_db)
):
    return controller.create(db=db, request=request)


@router.get("/", response_model=List[schema.Ingredient])
def read_all(db: Session = Depends(get_db)):
    return controller.read_all(db=db)


@router.get("/{ingredient_id}", response_model=schema.Ingredient)
def read_one(
    ingredient_id: int,
    db: Session = Depends(get_db)
):
    return controller.read_one(
        db=db,
        ingredient_id=ingredient_id
    )


@router.put("/{ingredient_id}", response_model=schema.Ingredient)
def update(
    ingredient_id: int,
    request: schema.IngredientUpdate,
    db: Session = Depends(get_db)
):
    return controller.update(
        db=db,
        ingredient_id=ingredient_id,
        request=request
    )


@router.delete("/{ingredient_id}", status_code=204)
def delete(
    ingredient_id: int,
    db: Session = Depends(get_db)
):
    return controller.delete(
        db=db,
        ingredient_id=ingredient_id
    )