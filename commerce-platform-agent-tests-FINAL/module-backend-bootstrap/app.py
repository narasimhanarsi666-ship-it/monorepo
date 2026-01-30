from datetime import datetime

def start_app():
    state = {}
    state["started_at"] = datetime.utcnow().isoformat()
    state["status"] = "running"
    state["checks"] = []

    state["checks"].append("database")
    state["checks"].append("cache")
    state["checks"].append("routes")

    return state

def health_check():
    return {
        "status": "ok",
        "timestamp": datetime.utcnow().isoformat()
    }
