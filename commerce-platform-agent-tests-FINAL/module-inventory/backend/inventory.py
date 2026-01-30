from shared.state import INVENTORY

def list_inventory():
    return INVENTORY

def is_in_stock(sku, qty):
    if sku not in INVENTORY:
        return False
    return INVENTORY[sku]["stock"] >= qty

def reduce_stock(sku, qty):
    if is_in_stock(sku, qty):
        INVENTORY[sku]["stock"] -= qty
        return True
    return False
