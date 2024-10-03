def merge_sort(arr, low, high):
    if low < high:
        mid = (low + high) // 2
        merge_sort(arr, low, mid)
        merge_sort(arr, mid + 1, high)
        merge(arr, low, mid, high)


def merge(arr, low, mid, high):
    left = []
    right = []
    for i in range(low, mid + 1):
        left.append(arr[i])
    for i in range(mid + 1, high + 1):
        right.append(arr[i])

    i = j = 0
    k = low
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1

    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1


# Example usage:
arr = [64, 34, 25, 12, 22, 11, 90]
n = len(arr)
merge_sort(arr, 0, n - 1)
print("Sorted array:", arr)
