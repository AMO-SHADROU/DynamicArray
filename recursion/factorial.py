def factorial(number):
    """calculate the factorial of a number"""
    if number == 0:
        return 1
    else:
        return number * factorial(number-1)
