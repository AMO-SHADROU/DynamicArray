def max_num(arr):
    """return the maximum number in an array"""
    max_number = arr[0]
    for num in arr:
        if num > max_number:
            max_number = num
    return max_number
