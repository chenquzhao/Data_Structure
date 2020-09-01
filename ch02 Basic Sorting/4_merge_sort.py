def merge_sort(alist):
    if len(alist) <= 1:
        return alist

    mid = int(len(alist)/2)
    left = merge_sort(alist[:mid])
    print("left = " + str(left))
    right = merge_sort(alist[mid:])
    print("right = " + str(right))
    return merge_sorted_array(left, right)


def merge_sorted_array(alist, blist):
    ret = []
    l = 0
    r = 0
    while l < len(alist) and r < len(blist):
        if alist[l] < blist[r]:
            ret.append(alist[l])
            l += 1
        else:
            ret.append(blist[r])
            r += 1
    ret += alist[l:]
    ret += blist[r:]
    return ret


unsortedArray = [6, 5, 3, 1, 8, 7, 2, 4]
print(merge_sort(unsortedArray))
