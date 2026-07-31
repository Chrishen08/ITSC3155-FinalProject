from sqlalchemy.orm import Session
from fastapi import HTTPException, status, Response
from sqlalchemy.exc import SQLAlchemyError

from ..models import orders as model


def create(db: Session, request):
    new_order = model.Order(
        customer_id=request.customer_id,
        promotion_id=request.promotion_id,
        order_type=request.order_type,
        total_amount=request.total_amount
    )

    try:
        db.add(new_order)
        db.commit()
        db.refresh(new_order)

    except SQLAlchemyError as e:
        db.rollback()
        error = str(e.__dict__.get("orig", e))

        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=error
        )

    return new_order


def read_all(db: Session):
    try:
        return db.query(model.Order).all()

    except SQLAlchemyError as e:
        error = str(e.__dict__.get("orig", e))

        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=error
        )


def read_one(db: Session, order_id: int):
    try:
        order = (
            db.query(model.Order)
            .filter(model.Order.order_id == order_id)
            .first()
        )

        if not order:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Order not found"
            )

        return order

    except SQLAlchemyError as e:
        error = str(e.__dict__.get("orig", e))

        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=error
        )


def update(db: Session, order_id: int, request):
    try:
        order_query = (
            db.query(model.Order)
            .filter(model.Order.order_id == order_id)
        )

        order = order_query.first()

        if not order:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Order not found"
            )

        update_data = request.dict(exclude_unset=True)

        order_query.update(
            update_data,
            synchronize_session=False
        )

        db.commit()
        return order_query.first()

    except SQLAlchemyError as e:
        db.rollback()
        error = str(e.__dict__.get("orig", e))

        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=error
        )


def delete(db: Session, order_id: int):
    try:
        order_query = (
            db.query(model.Order)
            .filter(model.Order.order_id == order_id)
        )

        order = order_query.first()

        if not order:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Order not found"
            )

        order_query.delete(synchronize_session=False)
        db.commit()

    except SQLAlchemyError as e:
        db.rollback()
        error = str(e.__dict__.get("orig", e))

        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=error
        )

    return Response(status_code=status.HTTP_204_NO_CONTENT)