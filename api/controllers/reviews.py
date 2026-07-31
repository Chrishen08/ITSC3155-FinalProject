from sqlalchemy.orm import Session
from fastapi import HTTPException, status, Response
from sqlalchemy.exc import SQLAlchemyError

from ..models import reviews as model


def create(db: Session, request):
    new_review = model.Review(
        customer_id=request.customer_id,
        menu_item_id=request.menu_item_id,
        rating=request.rating,
        comment=request.comment
    )

    try:
        db.add(new_review)
        db.commit()
        db.refresh(new_review)

    except SQLAlchemyError as e:
        db.rollback()
        error = str(e.__dict__.get("orig", e))

        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=error
        )

    return new_review


def read_all(db: Session):
    try:
        return db.query(model.Review).all()

    except SQLAlchemyError as e:
        error = str(e.__dict__.get("orig", e))

        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=error
        )


def read_one(db: Session, review_id: int):
    try:
        review = (
            db.query(model.Review)
            .filter(model.Review.review_id == review_id)
            .first()
        )

        if not review:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Review not found"
            )

        return review

    except SQLAlchemyError as e:
        error = str(e.__dict__.get("orig", e))

        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=error
        )


def update(db: Session, review_id: int, request):
    try:
        review_query = (
            db.query(model.Review)
            .filter(model.Review.review_id == review_id)
        )

        if not review_query.first():
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Review not found"
            )

        update_data = request.dict(exclude_unset=True)

        review_query.update(
            update_data,
            synchronize_session=False
        )

        db.commit()
        return review_query.first()

    except SQLAlchemyError as e:
        db.rollback()
        error = str(e.__dict__.get("orig", e))

        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=error
        )


def delete(db: Session, review_id: int):
    try:
        review_query = (
            db.query(model.Review)
            .filter(model.Review.review_id == review_id)
        )

        if not review_query.first():
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Review not found"
            )

        review_query.delete(synchronize_session=False)
        db.commit()

    except SQLAlchemyError as e:
        db.rollback()
        error = str(e.__dict__.get("orig", e))

        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=error
        )

    return Response(status_code=status.HTTP_204_NO_CONTENT)