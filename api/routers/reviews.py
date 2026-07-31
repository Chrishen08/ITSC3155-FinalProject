from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from ..controllers import reviews as controller
from ..schemas import reviews as schema
from ..dependencies.database import get_db


router = APIRouter(
    tags=["Reviews"],
    prefix="/reviews"
)


@router.post("/", response_model=schema.Review)
def create(
    request: schema.ReviewCreate,
    db: Session = Depends(get_db)
):
    return controller.create(db=db, request=request)


@router.get("/", response_model=List[schema.Review])
def read_all(db: Session = Depends(get_db)):
    return controller.read_all(db=db)


@router.get("/{review_id}", response_model=schema.Review)
def read_one(
    review_id: int,
    db: Session = Depends(get_db)
):
    return controller.read_one(
        db=db,
        review_id=review_id
    )


@router.put("/{review_id}", response_model=schema.Review)
def update(
    review_id: int,
    request: schema.ReviewUpdate,
    db: Session = Depends(get_db)
):
    return controller.update(
        db=db,
        review_id=review_id,
        request=request
    )


@router.delete("/{review_id}", status_code=204)
def delete(
    review_id: int,
    db: Session = Depends(get_db)
):
    return controller.delete(
        db=db,
        review_id=review_id
    )