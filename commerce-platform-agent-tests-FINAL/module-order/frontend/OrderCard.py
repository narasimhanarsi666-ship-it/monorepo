def OrderCard(order):
    return {
        "id": order["order_id"],
        "total": order["total"],
        "items": len(order["items"])
    }
###
