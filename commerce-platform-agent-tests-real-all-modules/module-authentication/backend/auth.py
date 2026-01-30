from datetime import datetime
from shared.state import USERS

def login(username, password):
    if not username or not password:
        return {"status": "error", "message": "Missing credentials"}
    USERS.setdefault(username, {"username": username, "created_at": datetime.utcnow().isoformat()})
    return {"status": "success", "token": f"TOKEN-{username}", "user": USERS[username]}
