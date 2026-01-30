def test_start_app():
    from module_backend_bootstrap.app import start_app
    state = start_app()
    assert state["status"] == "running"
    assert "started_at" in state

def test_health_check():
    from module_backend_bootstrap.app import health_check
    res = health_check()
    assert res["status"] == "ok"
