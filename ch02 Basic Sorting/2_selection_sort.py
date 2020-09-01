def selection_sort(alist):
    for i in range(len(alist)):
        print(alist)
        min_index = i
        for j in range(i + 1, len(alist)):
            if alist[j] < alist[min_index]:
                min_index = j
        alist[i], alist[min_index] = alist[min_index], alist[i]
    return alist


unsorted_list = [8, 5, 2, 6, 9, 3, 1, 4, 0, 7]
print(selection_sort(unsorted_list))
