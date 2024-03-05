def binary_search(data, target, low, high):
    """return True if target is in data else False. low = 0 and high = len(data) - 1"""
    if low > high:
        return False
    else:
        mid = (high + low) // 2
        if data[mid] == target:
            return True
        elif target < data[mid]:
            return binary_search(data, target, low, mid - 1)
        else:
            return binary_search(data, target, mid+1, high)
