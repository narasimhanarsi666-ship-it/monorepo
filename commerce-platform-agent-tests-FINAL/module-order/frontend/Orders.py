def render_orders(orders):
    view = {}
    view["count"] = len(orders)
    view["orders"] = orders
    view["has_orders"] = view["count"] > 0
    return view
