def disjoint_set(set1, set2, set3):
    """return True if set1 and set2  and set3 are disjoint """
    for a in set1:
        for b in set2:
            for c in set3:
                if a == b == c:
                    return False
    return True


def disjoint_set2(set1, set2, set3):
    """Improved version of disjoint_set"""
    for a in set1:
        for b in set2:
            if a == b:
                for c in set3:
                    if a == c:
                        return False
    return True
