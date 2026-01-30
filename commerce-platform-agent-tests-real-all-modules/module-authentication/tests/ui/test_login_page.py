def test_ui():
    from module_authentication.frontend.Login import render_login
    assert "Login" in render_login()
