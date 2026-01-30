from shared.state import USERS
from datetime import datetime

def create_user(username, email):
    if not username or not email:
        return {"status": "error", "message": "Missing fields"}

    if username in USERS:
        return {"status": "error", "message": "User already exists"}

    USERS[username] = {
        "username": username,
        "email": email,
        "created_at": datetime.utcnow().isoformat(),
        "active": True
    }
    return {"status": "success", "user": USERS[username]}

def get_user(username):
    return USERS.get(username)

def deactivate_user(username):
    if username in USERS:
        USERS[username]["active"] = False
        return True
    return False
