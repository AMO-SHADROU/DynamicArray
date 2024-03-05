def divisor(number, n):
    """count divisors of number"""
    total = 0
    if number < n:
        return 0
    else:
        total += divisor(number-n, n) + 1
    return total


print(divisor(10, 3))
