class Order:
    def __init__(self, order_id, user, items):
        self.order_id = order_id
        self.user = user
        self.items = items
        self.total = sum(i["qty"] * i["price"] for i in items)

    def to_dict(self):
        return {
            "order_id": self.order_id,
            "user": self.user,
            "total": self.total,
            "items": self.items
        }
