from shared.state import CARTS

def start_checkout(user):
    if not user:
        return {"status": "error", "message": "User required"}

    cart = CARTS.get(user, [])
    if not cart:
        return {"status": "error", "message": "Cart empty"}

    total = sum(i["qty"] * i["price"] for i in cart)
    return {
        "status": "success",
        "item_count": len(cart),
        "total": total
    }
