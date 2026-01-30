_inventory = None

def useInventory(data=None):
    global _inventory
    if data is not None:
        _inventory = data
    return _inventory

def clearInventory():
    global _inventory
    _inventory = None
