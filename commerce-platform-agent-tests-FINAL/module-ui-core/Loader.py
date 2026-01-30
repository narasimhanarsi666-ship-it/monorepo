def Loader(loading):
    if loading:
        return {"status": "loading", "spinner": True}
    return {"status": "idle", "spinner": False}
