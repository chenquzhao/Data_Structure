def counting_sort(alist):
    max_num, min_num = max(alist), min(alist)
    arr_len = max_num - min_num + 1
    arr = []
    for i in range(arr_len):
        arr.append(0)

    for num in alist:
        arr[num - min_num] += 1

    ret = []
    for i in range(arr_len):
        time = arr[i]
        while time > 0:
            ret.append(min_num + i)
            time -= 1
    return ret


can_arr = [0, 9, 3, 5, 6, 4, 2, 8, 1, 7, 2, 3, 9, 8, 3, 2, 0]
print(counting_sort(can_arr))
