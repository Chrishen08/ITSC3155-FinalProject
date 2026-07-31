from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from ..controllers import customers as controller
from ..schemas import customers as schema
from ..dependencies.database import get_db


router = APIRouter(
    tags=["Customers"],
    prefix="/customers"
)


@router.post("/", response_model=schema.Customer)
def create(
    request: schema.CustomerCreate,
    db: Session = Depends(get_db)
):
    return controller.create(db=db, request=request)


@router.get("/", response_model=List[schema.Customer])
def read_all(db: Session = Depends(get_db)):
    return controller.read_all(db=db)


@router.get("/{customer_id}", response_model=schema.Customer)
def read_one(
    customer_id: int,
    db: Session = Depends(get_db)
):
    return controller.read_one(
        db=db,
        customer_id=customer_id
    )


@router.put("/{customer_id}", response_model=schema.Customer)
def update(
    customer_id: int,
    request: schema.CustomerUpdate,
    db: Session = Depends(get_db)
):
    return controller.update(
        db=db,
        customer_id=customer_id,
        request=request
    )


@router.delete("/{customer_id}", status_code=204)
def delete(
    customer_id: int,
    db: Session = Depends(get_db)
):
    return controller.delete(
        db=db,
        customer_id=customer_id
    )