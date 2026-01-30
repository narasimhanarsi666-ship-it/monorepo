def test_fail():
    from module_authentication.backend.auth import login
    assert login("","")["status"]=="error"
