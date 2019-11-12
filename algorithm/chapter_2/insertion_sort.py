""" 插入排序

    时间复杂度：n^2

"""


def insert_sort1(arr):
    """
    非降序排序
    :param arr:
    :return:
    """
    for j in range(1, len(arr)):
        i = j - 1
        k = arr[j]
        while i >= 0 and arr[i] > k:
            arr[i+1] = arr[i]  # 元素后移
            i = i - 1
        arr[i+1] = k


def insert_sort2(arr):
    """
    非升序排序
    :param arr:
    :return:
    """
    for j in range(1, len(arr)):
        i = j - 1
        k = arr[j]
        while i >= 0 and arr[i] < k:
            arr[i+1] = arr[i]
            i -= 1
        arr[i+1] = k


if __name__ == '__main__':
    arr = [2, 1, 4, 3, 3, 2, 5, 9, 7]
    insert_sort2(arr)
    print(arr)
