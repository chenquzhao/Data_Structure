def radix_sort(alist):
    buckets = []
    for i in range(10):
        buckets.append([])

    for num in alist:
        buckets[num % 10].append(num)

    ret_one = []
    for bucket in buckets:
        if bucket:
            ret_one.extend(bucket)

    buckets = []
    for i in range(10):
        buckets.append([])

    for num in ret_one:
        buckets[num // 10].append(num)

    ret = []
    for bucket in buckets:
        if bucket:
            ret.extend(bucket)
    return ret


can_arr = [62, 14, 59, 88, 16]
print(radix_sort(can_arr))
