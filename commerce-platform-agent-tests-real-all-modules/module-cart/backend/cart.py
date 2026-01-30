from shared.state import CARTS, INVENTORY
import uuid
def add_to_cart(user, sku, qty):
    if sku not in INVENTORY: return {"status":"error"}
    if INVENTORY[sku]["stock"]<qty: return {"status":"error"}
    CARTS.setdefault(user,[]).append({"id":str(uuid.uuid4()),"sku":sku,"qty":qty})
    return {"status":"success"}
