
"""
1. 二分查找是有条件的，首先是有序，其次因为二分查找操作的是下标，所以要求是顺序表
2. 最优时间复杂度：O(1)
3. 最坏时间复杂度：O(logn)
"""


def binarySearch(ls, num, l, r):
    if ls is not None:
        mid = (l + r) // 2
        if ls[mid] > num:
            return binarySearch(ls, num, l, mid - 1)
        elif ls[mid] < num:
            return binarySearch(ls, num, mid + 1, r)
        elif ls[mid] == num:
            return mid
    else:
        return 'no result'


def binary_chop(lst, data):
    """
    非递归解决二分查找
    :param lst:
    :param data:
    :return:
    """
    low = 0
    high = len(lst)
    while low <= high:
        mid = (high + low) // 2
        if lst[mid] > data:
            high = mid - 1
        elif lst[mid] < data:
            low = mid + 1
        elif lst[mid] == data:
            return mid
    return -1


if __name__ == '__main__':
    lis = [2, 4, 5, 12, 14, 23]
    print(binarySearch(lis, 23, 0, len(lis)))



