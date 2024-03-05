def mod(a, b):
    """return a mod b"""
    if a < b:
        return a
    else:
        return mod(a-b, b)
