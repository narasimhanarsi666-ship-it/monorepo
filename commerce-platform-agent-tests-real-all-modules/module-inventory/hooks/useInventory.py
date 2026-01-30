_inv=None
def useInventory(i=None):
    global _inv
    if i: _inv=i
    return _inv
