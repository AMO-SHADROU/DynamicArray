def insertion_sort(arr):
    """Sort an array using insertion sort in non-decreasing order. O(n^2)"""
    for k in range(1, len(arr)):
        current = arr[k]
        j = k
        while j > 0 and arr[j-1] > current:
            arr[j] = arr[j-1]
            j -= 1
        arr[j] = current
