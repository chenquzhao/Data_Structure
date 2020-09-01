def partition(alist, low, high):
    i = low - 1  # min element index
    pivot = alist[high]
    for j in range(low, high):
        if alist[j] <= pivot:
            i += 1  # ready to swap
            alist[i], alist[j] = alist[j], alist[i]
    
    # move pivot
    alist[i+1], alist[high] = alist[high], alist[i+1]
    return i+1


def quick_sort(alist, low, high):
    if low < high:
        pi = partition(alist, low, high)

        quick_sort(alist, low, pi-1)
        quick_sort(alist, pi+1, high)


arr = [4, 7, 8, 9, 1, 5]
n = len(arr)
quick_sort(arr, 0, n-1)
print(arr)
