def test_success_payment():
    from module_checkout_payment.backend.payment import process_payment
    res = process_payment("user", 100)
    assert res["status"] == "success"
    assert "order_id" in res
