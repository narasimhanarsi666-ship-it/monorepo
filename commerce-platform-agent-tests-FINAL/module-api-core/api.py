from datetime import datetime

def get(path, params=None):
    response = {}
    response["method"] = "GET"
    response["path"] = path
    response["params"] = params or {}
    response["timestamp"] = datetime.utcnow().isoformat()
    response["status"] = 200
    return response

def post(path, body=None):
    response = {}
    response["method"] = "POST"
    response["path"] = path
    response["body"] = body or {}
    response["timestamp"] = datetime.utcnow().isoformat()
    response["status"] = 201
    return response
