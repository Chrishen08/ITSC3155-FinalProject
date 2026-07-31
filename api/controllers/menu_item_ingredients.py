from sqlalchemy.orm import Session
from fastapi import HTTPException, status, Response
from sqlalchemy.exc import SQLAlchemyError

from ..models import menu_item_ingredients as model


def create(db: Session, request):
    new_record = model.MenuItemIngredient(
        menu_item_id=request.menu_item_id,
        ingredient_id=request.ingredient_id,
        quantity_required=request.quantity_required
    )

    try:
        db.add(new_record)
        db.commit()
        db.refresh(new_record)

    except SQLAlchemyError as e:
        db.rollback()
        error = str(e.__dict__.get("orig", e))

        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=error
        )

    return new_record


def read_all(db: Session):
    try:
        return db.query(model.MenuItemIngredient).all()

    except SQLAlchemyError as e:
        error = str(e.__dict__.get("orig", e))

        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=error
        )


def read_one(db: Session, menu_item_ingredient_id: int):
    try:
        record = (
            db.query(model.MenuItemIngredient)
            .filter(
                model.MenuItemIngredient.menu_item_ingredient_id
                == menu_item_ingredient_id
            )
            .first()
        )

        if not record:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Record not found"
            )

        return record

    except SQLAlchemyError as e:
        error = str(e.__dict__.get("orig", e))

        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=error
        )


def update(db: Session, menu_item_ingredient_id: int, request):
    try:
        record_query = (
            db.query(model.MenuItemIngredient)
            .filter(
                model.MenuItemIngredient.menu_item_ingredient_id
                == menu_item_ingredient_id
            )
        )

        if not record_query.first():
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Record not found"
            )

        update_data = request.dict(exclude_unset=True)

        record_query.update(
            update_data,
            synchronize_session=False
        )

        db.commit()
        return record_query.first()

    except SQLAlchemyError as e:
        db.rollback()
        error = str(e.__dict__.get("orig", e))

        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=error
        )


def delete(db: Session, menu_item_ingredient_id: int):
    try:
        record_query = (
            db.query(model.MenuItemIngredient)
            .filter(
                model.MenuItemIngredient.menu_item_ingredient_id
                == menu_item_ingredient_id
            )
        )

        if not record_query.first():
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Record not found"
            )

        record_query.delete(synchronize_session=False)
        db.commit()

    except SQLAlchemyError as e:
        db.rollback()
        error = str(e.__dict__.get("orig", e))

        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=error
        )

    return Response(status_code=status.HTTP_204_NO_CONTENT)