def unique(lst):
    """ return True if all elements in lst are unique O(n^2)"""
    for i in range(len(lst)):
        num = lst[i]
        for j in range(i+1, len(lst)):
            if num == lst[j]:
                return False
    return True

def unique2(lst):
    """improved version of unique O(n.logn)"""
    temp = sorted(lst)
    for i in range(1, len(lst)):
        if temp[i] == temp[i-1]:
            return False
    return True
