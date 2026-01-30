from datetime import datetime

def log(message, level="INFO"):
    entry = {
        "level": level,
        "message": message,
        "timestamp": datetime.utcnow().isoformat()
    }
    return entry

def log_error(message):
    return log(message, level="ERROR")
