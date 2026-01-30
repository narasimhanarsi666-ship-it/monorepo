def retry(fn, attempts=3):
    for _ in range(attempts):
        try: return fn()
        except: pass
    return None
