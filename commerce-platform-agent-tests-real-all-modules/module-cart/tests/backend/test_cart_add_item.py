def test_cart():
    from module_cart.backend.cart import add_to_cart
    assert add_to_cart("u","SKU-1",1)["status"]=="success"
