from shared.state import ORDERS
def list_orders(user): return [o for o in ORDERS.values() if o["user"]==user]
