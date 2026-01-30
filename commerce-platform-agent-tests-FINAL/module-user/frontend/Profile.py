def render_profile(user):
    view = {}
    if not user:
        view["error"] = "User not found"
        return view

    view["username"] = user.get("username")
    view["email"] = user.get("email")
    view["status"] = "Active" if user.get("active") else "Inactive"
    view["can_edit"] = user.get("active")
    return view
