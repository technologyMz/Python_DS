"""
    快速排序
"""


def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        base = arr[0]
        less = [v for v in arr[1:] if v <= base]
        more = [v for v in arr[1:] if v > base]
        return quick_sort(less) + [base] + quick_sort(more)


if __name__ == '__main__':
    ls = [1, 3, 9, 7, 11, 2, 1, 3]
    re = quick_sort(ls)
    print(re)
