def prefix_average(arr):
    """ returns the prefix average of an array """
    list1 = []
    for i in range(len(arr)):
        total = 0
        for j in range(i + 1):
            total += arr[j]
            total /= i + 1
        list1.append(total)
