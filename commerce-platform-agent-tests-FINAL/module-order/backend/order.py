from shared.state import ORDERS
from datetime import datetime
import uuid

def create_order(user, items):
    if not user or not items:
        return {"status": "error", "message": "Invalid order data"}

    order_id = str(uuid.uuid4())
    total = sum(i["qty"] * i["price"] for i in items)

    ORDERS[order_id] = {
        "order_id": order_id,
        "user": user,
        "items": items,
        "total": total,
        "created_at": datetime.utcnow().isoformat()
    }
    return {"status": "success", "order": ORDERS[order_id]}

def list_orders(user):
    return [o for o in ORDERS.values() if o["user"] == user]
