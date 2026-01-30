def InventoryTable(items):
    rows = []
    for sku, item in items.items():
        rows.append({
            "sku": sku,
            "name": item["name"],
            "price": item["price"],
            "stock": item["stock"]
        })
    return rows
