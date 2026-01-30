def test_profile():
    from module_user.backend.user import get_user
    assert get_user("missing") is None
