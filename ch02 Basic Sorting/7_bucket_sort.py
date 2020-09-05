def bucket_sort(alist, bucket_num):
    max_num, min_num = max(alist), min(alist)
    bucket_size = (max_num - min_num + 1) / bucket_num
    bucket = []
    for i in range(bucket_num):
        bucket.append([])

    # assign elements to buckets
    for num in alist:
        bucket[int((num - min_num) / bucket_size)].append(num)
    print(bucket)

    # merge buckets
    res = []
    for i in range(bucket_num):
        res.extend(sorted(bucket[i]))
    return res


arr = [0, 9, 3, 5, 6, 4, 2, 8, 1, 7]
print(bucket_sort(arr, 5))
