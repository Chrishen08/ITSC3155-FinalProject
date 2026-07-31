from datetime import date
from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from ..controllers import orders as controller
from ..schemas import orders as schema
from ..dependencies.database import get_db


router = APIRouter(
    tags=["Orders"],
    prefix="/orders"
)


@router.post("/", response_model=schema.Order)
def create(
    request: schema.OrderCreate,
    db: Session = Depends(get_db)
):
    return controller.create(
        db=db,
        request=request
    )


@router.get("/", response_model=List[schema.Order])
def read_all(
    db: Session = Depends(get_db)
):
    return controller.read_all(
        db=db
    )


@router.get(
    "/tracking/{tracking_number}",
    response_model=schema.Order
)
def read_by_tracking_number(
    tracking_number: str,
    db: Session = Depends(get_db)
):
    return controller.read_by_tracking_number(
        db=db,
        tracking_number=tracking_number
    )


@router.get(
    "/date-range/",
    response_model=List[schema.Order]
)
def read_by_date_range(
    start_date: date,
    end_date: date,
    db: Session = Depends(get_db)
):
    return controller.read_by_date_range(
        db=db,
        start_date=start_date,
        end_date=end_date
    )


@router.get("/revenue-by-date/")
def revenue_by_date(
    order_date: date,
    db: Session = Depends(get_db)
):
    return controller.revenue_by_date(
        db=db,
        order_date=order_date
    )


@router.get(
    "/{order_id}",
    response_model=schema.Order
)
def read_one(
    order_id: int,
    db: Session = Depends(get_db)
):
    return controller.read_one(
        db=db,
        order_id=order_id
    )


@router.put(
    "/{order_id}",
    response_model=schema.Order
)
def update(
    order_id: int,
    request: schema.OrderUpdate,
    db: Session = Depends(get_db)
):
    return controller.update(
        db=db,
        order_id=order_id,
        request=request
    )


@router.delete(
    "/{order_id}",
    status_code=204
)
def delete(
    order_id: int,
    db: Session = Depends(get_db)
):
    return controller.delete(
        db=db,
        order_id=order_id
    )