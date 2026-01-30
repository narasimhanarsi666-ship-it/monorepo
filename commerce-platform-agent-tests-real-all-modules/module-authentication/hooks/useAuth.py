_current = None
def useAuth(user=None):
    global _current
    if user: _current = user
    return _current
