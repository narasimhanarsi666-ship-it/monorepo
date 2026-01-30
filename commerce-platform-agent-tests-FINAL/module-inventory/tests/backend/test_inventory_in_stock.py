def test_inventory_stock():
    from module_inventory.backend.inventory import is_in_stock
    assert is_in_stock("SKU-1", 1) is True
