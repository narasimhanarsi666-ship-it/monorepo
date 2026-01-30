def test_success():
    from module_authentication.backend.auth import login
    assert login("admin","pass")["status"]=="success"
