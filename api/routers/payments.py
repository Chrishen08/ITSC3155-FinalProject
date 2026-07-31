from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from ..controllers import payments as controller
from ..schemas import payments as schema
from ..dependencies.database import get_db


router = APIRouter(
    tags=["Payments"],
    prefix="/payments"
)


@router.post("/", response_model=schema.Payment)
def create(
    request: schema.PaymentCreate,
    db: Session = Depends(get_db)
):
    return controller.create(db=db, request=request)


@router.get("/", response_model=List[schema.Payment])
def read_all(db: Session = Depends(get_db)):
    return controller.read_all(db=db)


@router.get("/{payment_id}", response_model=schema.Payment)
def read_one(
    payment_id: int,
    db: Session = Depends(get_db)
):
    return controller.read_one(
        db=db,
        payment_id=payment_id
    )


@router.put("/{payment_id}", response_model=schema.Payment)
def update(
    payment_id: int,
    request: schema.PaymentUpdate,
    db: Session = Depends(get_db)
):
    return controller.update(
        db=db,
        payment_id=payment_id,
        request=request
    )


@router.delete("/{payment_id}", status_code=204)
def delete(
    payment_id: int,
    db: Session = Depends(get_db)
):
    return controller.delete(
        db=db,
        payment_id=payment_id
    )