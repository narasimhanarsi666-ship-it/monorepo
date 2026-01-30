def Navbar(user=None):
    menu = ["Home", "Shop"]
    if user:
        menu.append("Profile")
    menu.append("Cart")
    return menu
