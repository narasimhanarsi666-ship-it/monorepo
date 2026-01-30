def test_reset_state():
    from shared.state import USERS, reset_state
    USERS["u"] = {}
    reset_state()
    assert USERS == {}
