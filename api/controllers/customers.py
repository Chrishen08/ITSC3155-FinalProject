from sqlalchemy.orm import Session
from fastapi import HTTPException, status, Response
from sqlalchemy.exc import SQLAlchemyError

from ..models import customers as model


def create(db: Session, request):
    new_customer = model.Customer(
        first_name=request.first_name,
        last_name=request.last_name,
        email=request.email,
        phone=request.phone,
        address=request.address
    )

    try:
        db.add(new_customer)
        db.commit()
        db.refresh(new_customer)

    except SQLAlchemyError as e:
        db.rollback()
        error = str(e.__dict__.get("orig", e))

        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=error
        )

    return new_customer


def read_all(db: Session):
    try:
        return db.query(model.Customer).all()

    except SQLAlchemyError as e:
        error = str(e.__dict__.get("orig", e))

        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=error
        )


def read_one(db: Session, customer_id: int):
    try:
        customer = (
            db.query(model.Customer)
            .filter(model.Customer.customer_id == customer_id)
            .first()
        )

        if not customer:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Customer not found"
            )

        return customer

    except SQLAlchemyError as e:
        error = str(e.__dict__.get("orig", e))

        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=error
        )


def update(db: Session, customer_id: int, request):
    try:
        customer_query = (
            db.query(model.Customer)
            .filter(model.Customer.customer_id == customer_id)
        )

        customer = customer_query.first()

        if not customer:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Customer not found"
            )

        update_data = request.dict(exclude_unset=True)

        customer_query.update(
            update_data,
            synchronize_session=False
        )

        db.commit()
        return customer_query.first()

    except SQLAlchemyError as e:
        db.rollback()
        error = str(e.__dict__.get("orig", e))

        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=error
        )


def delete(db: Session, customer_id: int):
    try:
        customer_query = (
            db.query(model.Customer)
            .filter(model.Customer.customer_id == customer_id)
        )

        customer = customer_query.first()

        if not customer:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Customer not found"
            )

        customer_query.delete(synchronize_session=False)
        db.commit()

    except SQLAlchemyError as e:
        db.rollback()
        error = str(e.__dict__.get("orig", e))

        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=error
        )

    return Response(status_code=status.HTTP_204_NO_CONTENT)