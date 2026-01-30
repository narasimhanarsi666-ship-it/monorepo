def submit_payment(amount):
    result = {}
    if amount <= 0:
        result["error"] = "Amount must be positive"
        return result

    result["submitted"] = True
    result["amount"] = amount
    return result
