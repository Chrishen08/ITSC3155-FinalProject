from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from ..controllers import order_details as controller
from ..schemas import order_items as schema
from ..dependencies.database import get_db


router = APIRouter(
    tags=["Order Items"],
    prefix="/order-items"
)


@router.post("/", response_model=schema.OrderItem)
def create(
    request: schema.OrderItemCreate,
    db: Session = Depends(get_db)
):
    return controller.create(db=db, request=request)


@router.get("/", response_model=List[schema.OrderItem])
def read_all(db: Session = Depends(get_db)):
    return controller.read_all(db=db)


@router.get("/{order_item_id}", response_model=schema.OrderItem)
def read_one(
    order_item_id: int,
    db: Session = Depends(get_db)
):
    return controller.read_one(
        db=db,
        order_item_id=order_item_id
    )


@router.put("/{order_item_id}", response_model=schema.OrderItem)
def update(
    order_item_id: int,
    request: schema.OrderItemUpdate,
    db: Session = Depends(get_db)
):
    return controller.update(
        db=db,
        order_item_id=order_item_id,
        request=request
    )


@router.delete("/{order_item_id}", status_code=204)
def delete(
    order_item_id: int,
    db: Session = Depends(get_db)
):
    return controller.delete(
        db=db,
        order_item_id=order_item_id
    )