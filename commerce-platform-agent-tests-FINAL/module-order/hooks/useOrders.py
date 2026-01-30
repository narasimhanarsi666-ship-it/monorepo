_orders = []

def useOrders(order=None):
    if order:
        _orders.append(order)
    return _orders

def clearOrders():
    _orders.clear()
