from shared.state import ORDERS
from datetime import datetime
import uuid

def process_payment(user, amount):
    if amount <= 0:
        return {"status": "error", "message": "Invalid amount"}

    order_id = str(uuid.uuid4())
    ORDERS[order_id] = {
        "order_id": order_id,
        "user": user,
        "amount": amount,
        "paid_at": datetime.utcnow().isoformat()
    }
    return {"status": "success", "order_id": order_id}
