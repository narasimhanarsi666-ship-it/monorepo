def ErrorBanner(message=None):
    if not message:
        return None
    return {"error": True, "message": message}
