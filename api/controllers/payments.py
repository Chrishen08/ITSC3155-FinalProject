from sqlalchemy.orm import Session
from fastapi import HTTPException, status, Response
from sqlalchemy.exc import SQLAlchemyError

from ..models import payments as model


def create(db: Session, request):
    new_payment = model.Payment(
        order_id=request.order_id,
        payment_method=request.payment_method,
        payment_status=request.payment_status,
        amount=request.amount
    )

    try:
        db.add(new_payment)
        db.commit()
        db.refresh(new_payment)

    except SQLAlchemyError as e:
        db.rollback()
        error = str(e.__dict__.get("orig", e))

        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=error
        )

    return new_payment


def read_all(db: Session):
    try:
        return db.query(model.Payment).all()

    except SQLAlchemyError as e:
        error = str(e.__dict__.get("orig", e))

        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=error
        )


def read_one(db: Session, payment_id: int):
    try:
        payment = (
            db.query(model.Payment)
            .filter(model.Payment.payment_id == payment_id)
            .first()
        )

        if not payment:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Payment not found"
            )

        return payment

    except SQLAlchemyError as e:
        error = str(e.__dict__.get("orig", e))

        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=error
        )


def update(db: Session, payment_id: int, request):
    try:
        payment_query = (
            db.query(model.Payment)
            .filter(model.Payment.payment_id == payment_id)
        )

        if not payment_query.first():
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Payment not found"
            )

        update_data = request.dict(exclude_unset=True)

        payment_query.update(
            update_data,
            synchronize_session=False
        )

        db.commit()
        return payment_query.first()

    except SQLAlchemyError as e:
        db.rollback()
        error = str(e.__dict__.get("orig", e))

        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=error
        )


def delete(db: Session, payment_id: int):
    try:
        payment_query = (
            db.query(model.Payment)
            .filter(model.Payment.payment_id == payment_id)
        )

        if not payment_query.first():
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Payment not found"
            )

        payment_query.delete(synchronize_session=False)
        db.commit()

    except SQLAlchemyError as e:
        db.rollback()
        error = str(e.__dict__.get("orig", e))

        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=error
        )

    return Response(status_code=status.HTTP_204_NO_CONTENT)