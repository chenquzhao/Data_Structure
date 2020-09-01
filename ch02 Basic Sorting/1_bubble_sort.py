def bubble_sort(alist):
    for i in range(len(alist)):
        print(alist)
        for j in range(1, len(alist) - i):
            if alist[j] < alist[j-1]:
                alist[j], alist[j-1] = alist[j-1], alist[j]
    return alist


unsorted_list = [5, 8, 6, 3, 9, 2, 1, 7]
print(bubble_sort(unsorted_list))
