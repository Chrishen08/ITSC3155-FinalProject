from sqlalchemy.orm import Session
from fastapi import HTTPException, status, Response
from sqlalchemy.exc import SQLAlchemyError

from ..models import promotions as model


def create(db: Session, request):
    new_promotion = model.Promotion(
        promo_code=request.promo_code,
        description=request.description,
        discount_percentage=request.discount_percentage,
        start_date=request.start_date,
        end_date=request.end_date,
        is_active=request.is_active
    )

    try:
        db.add(new_promotion)
        db.commit()
        db.refresh(new_promotion)

    except SQLAlchemyError as e:
        db.rollback()
        error = str(e.__dict__.get("orig", e))

        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=error
        )

    return new_promotion


def read_all(db: Session):
    try:
        return db.query(model.Promotion).all()

    except SQLAlchemyError as e:
        error = str(e.__dict__.get("orig", e))

        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=error
        )


def read_one(db: Session, promotion_id: int):
    try:
        promotion = (
            db.query(model.Promotion)
            .filter(model.Promotion.promotion_id == promotion_id)
            .first()
        )

        if not promotion:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Promotion not found"
            )

        return promotion

    except SQLAlchemyError as e:
        error = str(e.__dict__.get("orig", e))

        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=error
        )


def update(db: Session, promotion_id: int, request):
    try:
        promotion_query = (
            db.query(model.Promotion)
            .filter(model.Promotion.promotion_id == promotion_id)
        )

        if not promotion_query.first():
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Promotion not found"
            )

        update_data = request.dict(exclude_unset=True)

        promotion_query.update(
            update_data,
            synchronize_session=False
        )

        db.commit()
        return promotion_query.first()

    except SQLAlchemyError as e:
        db.rollback()
        error = str(e.__dict__.get("orig", e))

        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=error
        )


def delete(db: Session, promotion_id: int):
    try:
        promotion_query = (
            db.query(model.Promotion)
            .filter(model.Promotion.promotion_id == promotion_id)
        )

        if not promotion_query.first():
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Promotion not found"
            )

        promotion_query.delete(synchronize_session=False)
        db.commit()

    except SQLAlchemyError as e:
        db.rollback()
        error = str(e.__dict__.get("orig", e))

        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=error
        )

    return Response(status_code=status.HTTP_204_NO_CONTENT)