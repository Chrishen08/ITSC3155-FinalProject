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


def load_routes(app):
    app.include_router(customers.router)
    app.include_router(orders.router)
    app.include_router(order_items.router)
    app.include_router(menu_items.router)
    app.include_router(ingredients.router)
    app.include_router(menu_item_ingredients.router)
    app.include_router(payments.router)
    app.include_router(promotions.router)
    app.include_router(reviews.router)