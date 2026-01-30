def test_negative_payment():
    from module_checkout_payment.backend.payment import process_payment
    res = process_payment("user", -10)
    assert res["status"] == "error"
