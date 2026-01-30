def test_get_api():
    from module_api_core.api import get
    res = get("/health")
    assert res["status"] == 200
    assert res["method"] == "GET"

def test_post_api():
    from module_api_core.api import post
    res = post("/login", {"user": "admin"})
    assert res["status"] == 201
    assert res["method"] == "POST"
