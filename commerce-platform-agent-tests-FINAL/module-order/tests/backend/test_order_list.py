def test_list_orders():
    from module_order.backend.order import list_orders
    orders = list_orders("user")
    assert isinstance(orders, list)
