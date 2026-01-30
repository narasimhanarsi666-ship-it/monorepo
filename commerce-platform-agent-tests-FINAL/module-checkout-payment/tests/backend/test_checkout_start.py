def test_checkout_empty_cart():
    from module_checkout_payment.backend.checkout import start_checkout
    res = start_checkout("nouser")
    assert res["status"] == "error"
