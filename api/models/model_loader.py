from . import (
    customers,
    orders,
    order_items,
    menu_items,
    ingredients,
    menu_item_ingredients,
    payments,
    promotions,
    reviews
)

from ..dependencies.database import engine


def index():
    customers.Base.metadata.create_all(engine)
    orders.Base.metadata.create_all(engine)
    order_items.Base.metadata.create_all(engine)
    menu_items.Base.metadata.create_all(engine)
    ingredients.Base.metadata.create_all(engine)
    menu_item_ingredients.Base.metadata.create_all(engine)
    payments.Base.metadata.create_all(engine)
    promotions.Base.metadata.create_all(engine)
    reviews.Base.metadata.create_all(engine)
