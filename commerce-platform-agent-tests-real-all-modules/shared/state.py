from datetime import datetime
import uuid

USERS = {}
CARTS = {}
ORDERS = {}
INVENTORY = {
    "SKU-1": {"name": "Laptop", "price": 1000, "stock": 5},
    "SKU-2": {"name": "Mouse", "price": 50, "stock": 20}
}
