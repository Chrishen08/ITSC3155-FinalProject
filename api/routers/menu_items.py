from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from ..controllers import menu_items as controller
from ..schemas import menu_items as schema
from ..dependencies.database import get_db


router = APIRouter(
    tags=["Menu Items"],
    prefix="/menu-items"
)


@router.post("/", response_model=schema.MenuItem)
def create(
    request: schema.MenuItemCreate,
    db: Session = Depends(get_db)
):
    return controller.create(db=db, request=request)


@router.get("/", response_model=List[schema.MenuItem])
def read_all(db: Session = Depends(get_db)):
    return controller.read_all(db=db)


@router.get("/{menu_item_id}", response_model=schema.MenuItem)
def read_one(
    menu_item_id: int,
    db: Session = Depends(get_db)
):
    return controller.read_one(
        db=db,
        menu_item_id=menu_item_id
    )


@router.put("/{menu_item_id}", response_model=schema.MenuItem)
def update(
    menu_item_id: int,
    request: schema.MenuItemUpdate,
    db: Session = Depends(get_db)
):
    return controller.update(
        db=db,
        menu_item_id=menu_item_id,
        request=request
    )


@router.delete("/{menu_item_id}", status_code=204)
def delete(
    menu_item_id: int,
    db: Session = Depends(get_db)
):
    return controller.delete(
        db=db,
        menu_item_id=menu_item_id
    )