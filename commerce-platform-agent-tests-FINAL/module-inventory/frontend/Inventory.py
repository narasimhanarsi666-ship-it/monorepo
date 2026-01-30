def render_inventory(inventory):
    view = {}
    view["count"] = len(inventory)
    view["items"] = list(inventory.values())
    view["has_items"] = view["count"] > 0
    return view
