def test_create_and_fetch_user():
    from module_user.backend.user import create_user, get_user
    res = create_user("testuser", "test@mail.com")
    assert res["status"] == "success"

    user = get_user("testuser")
    assert user["email"] == "test@mail.com"

def test_deactivate_user():
    from module_user.backend.user import deactivate_user
    assert deactivate_user("testuser") is True
