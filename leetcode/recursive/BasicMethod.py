

ls = [1, 2, 3, 4, 5]


def sumNum(lst: list):
    """
        列表递归求和
    """
    if not lst:
        return 0
    else:
        return lst[0] + sumNum(lst[1:])


# print(sumNum(ls))


def factorialNum(n: int):
    """
        阶乘
    """
    if n == 0:
        return 1
    else:
        return n * factorialNum(n-1)


# print(factorialNum(5))


