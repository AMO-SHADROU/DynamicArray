def _sum(n):
    """Add numbers from 1 to n """
    total = 0
    if n == 0:
        return 0
    else:
        total += n + _sum(n-1)
    return total
