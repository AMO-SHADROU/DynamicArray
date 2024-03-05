def power(number, n):
    """Return power of given number."""
    total = 1
    if n == 0:
        return 1
    else:
        total *= number * power(number, n-1)
    return total
