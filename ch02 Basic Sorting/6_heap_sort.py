import heapq


def heap_sort(alist):
    ret = []
    while alist:
        heapq.heapify(alist)
        ret.append(heapq.heappop(alist))
    return ret


arr = [4, 7, 8, 9, 1, 5]
print(heap_sort(arr))
