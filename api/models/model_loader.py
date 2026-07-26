from . import customers, orders, menu_items, order_items

from ..dependencies.database import engine


def index():
    customers.Base.metadata.create_all(engine)
    orders.Base.metadata.create_all(engine)
    menu_items.Base.metadata.create_all(engine)
    order_items.Base.metadata.create_all(engine)
