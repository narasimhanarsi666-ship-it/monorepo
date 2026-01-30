class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email
        self.active = True

    def deactivate(self):
        self.active = False

    def is_active(self):
        return self.active

    def to_dict(self):
        return {
            "username": self.username,
            "email": self.email,
            "active": self.active
        }
