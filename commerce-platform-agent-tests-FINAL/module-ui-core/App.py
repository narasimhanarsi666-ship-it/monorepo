def app():
    state = {"ready": True}
    state["routes"] = ["home", "login", "cart"]
    state["version"] = "1.0.0"
    state["healthy"] = True
    return state
