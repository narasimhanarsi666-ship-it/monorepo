from module_checkout_payment.backend.payment import process_payment

def pay(user, amount):
    return process_payment(user, amount)
