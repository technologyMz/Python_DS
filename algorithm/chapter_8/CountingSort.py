"""
    计数排序
"""
import numpy as np


def counting_sort(a, b, k):
    """
    :param a: 原始数组
    :param b: 排序后的输出
    :param k: 临时存储空间大小
    :return:
    """
    c = [0] * k

    # step1：计数，统计元素出现的次数。
    for j in range(len(a)):
        c[a[j]] = c[a[j]] + 1

    # step2：对于每一个元素 i = 0, 1, ... k，有多少个输入元素是小于等于i的。
    for i in range(1, k):
        c[i] = c[i] + c[i-1]

    # step3：将上一步找到的位置关系映射到新的列表中去，顺序输出
    for n in range(len(a)-1, -1, -1):
        b[c[a[n]]-1] = a[n]
        c[a[n]] = c[a[n]] - 1


if __name__ == '__main__':
    arr = [2, 5, 3, 0, 2, 3, 0, 3]
    tmp_k = 6
    out = [2, 5, 3, 0, 2, 3, 0, 3]
    counting_sort(arr, out, tmp_k)
    print(out)
