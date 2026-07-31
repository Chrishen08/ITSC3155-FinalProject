from sqlalchemy.orm import Session
from fastapi import HTTPException, status, Response
from sqlalchemy.exc import SQLAlchemyError

from ..models import ingredients as model


def create(db: Session, request):
    new_ingredient = model.Ingredient(
        ingredient_name=request.ingredient_name,
        quantity_in_stock=request.quantity_in_stock,
        unit_of_measure=request.unit_of_measure
    )

    try:
        db.add(new_ingredient)
        db.commit()
        db.refresh(new_ingredient)

    except SQLAlchemyError as e:
        db.rollback()
        error = str(e.__dict__.get("orig", e))
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=error
        )

    return new_ingredient


def read_all(db: Session):
    try:
        return db.query(model.Ingredient).all()

    except SQLAlchemyError as e:
        error = str(e.__dict__.get("orig", e))
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=error
        )


def read_one(db: Session, ingredient_id: int):
    try:
        ingredient = (
            db.query(model.Ingredient)
            .filter(model.Ingredient.ingredient_id == ingredient_id)
            .first()
        )

        if not ingredient:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Ingredient not found"
            )

        return ingredient

    except SQLAlchemyError as e:
        error = str(e.__dict__.get("orig", e))
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=error
        )


def update(db: Session, ingredient_id: int, request):
    try:
        ingredient_query = (
            db.query(model.Ingredient)
            .filter(model.Ingredient.ingredient_id == ingredient_id)
        )

        if not ingredient_query.first():
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Ingredient not found"
            )

        update_data = request.dict(exclude_unset=True)

        ingredient_query.update(
            update_data,
            synchronize_session=False
        )

        db.commit()
        return ingredient_query.first()

    except SQLAlchemyError as e:
        db.rollback()
        error = str(e.__dict__.get("orig", e))
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=error
        )


def delete(db: Session, ingredient_id: int):
    try:
        ingredient_query = (
            db.query(model.Ingredient)
            .filter(model.Ingredient.ingredient_id == ingredient_id)
        )

        if not ingredient_query.first():
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Ingredient not found"
            )

        ingredient_query.delete(synchronize_session=False)
        db.commit()

    except SQLAlchemyError as e:
        db.rollback()
        error = str(e.__dict__.get("orig", e))
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=error
        )

    return Response(status_code=status.HTTP_204_NO_CONTENT)