from datetime import datetime
import uuid

USERS = {}
CARTS = {}
ORDERS = {}
INVENTORY = {
    "SKU-1": {"name": "Laptop", "price": 1000, "stock": 5},
    "SKU-2": {"name": "Mouse", "price": 50, "stock": 20}
}

def snapshot():
    return {
        "users": len(USERS),
        "carts": len(CARTS),
        "orders": len(ORDERS),
        "inventory_items": len(INVENTORY),
        "timestamp": datetime.utcnow().isoformat()
    }

def reset_state():
    USERS.clear()
    CARTS.clear()
    ORDERS.clear()

def seed_inventory():
    INVENTORY["SKU-3"] = {"name": "Keyboard", "price": 80, "stock": 15}
    return INVENTORY
