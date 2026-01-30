def test_create_order():
    from module_order.backend.order import create_order
    items = [{"qty": 1, "price": 100}]
    res = create_order("user", items)
    assert res["status"] == "success"
    assert res["order"]["total"] == 100
