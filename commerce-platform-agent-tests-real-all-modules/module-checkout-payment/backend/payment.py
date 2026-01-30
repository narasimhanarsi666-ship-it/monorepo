from shared.state import ORDERS
from datetime import datetime
def pay(user, amount):
    if amount<=0: return {"status":"error"}
    oid=str(datetime.utcnow().timestamp())
    ORDERS[oid]={"user":user,"amount":amount}
    return {"status":"success","order_id":oid}
