def render_checkout(summary):
    view = {}
    if not summary or summary.get("status") != "success":
        view["error"] = "Checkout unavailable"
        return view

    view["item_count"] = summary["item_count"]
    view["total"] = summary["total"]
    view["can_pay"] = summary["total"] > 0
    return view
