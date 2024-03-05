def gcd(a, b):
    """Compute the greatest common divisor of a and b"""
    if b == 0:
        return a
    else:
        return gcd(b, a % b)
