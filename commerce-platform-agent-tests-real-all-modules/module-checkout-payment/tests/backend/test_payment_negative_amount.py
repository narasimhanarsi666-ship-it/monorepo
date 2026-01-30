def test_negative():
    from module_checkout_payment.backend.payment import pay
    assert pay("u",-1)["status"]=="error"
