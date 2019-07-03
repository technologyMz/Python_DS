

class StackCustm:
    """
        利用列表数据结构，实现一个栈

    """

    # 用空列表初始化一个栈
    def __init__(self):
        self.__items = []

    def is_empty(self):
        return self.__items == []

    # 返回栈顶元素
    def peek(self):
        return self.__items[len(self.__items) - 1]

    def size(self):
        return len(self.__items)

    # 压栈
    def push(self, item):
        self.__items.append(item)
        return self

    # 出栈
    def pop(self):
        return self.__items.pop()


class GeneralOperator:
    @staticmethod
    def addTwoNum(s1: StackCustm, s2: StackCustm) -> StackCustm:
        flag = 0
        r = StackCustm()
        while s1.size() > 0 and s2.size() > 0:
            temp = s1.pop()+s2.pop()+flag
            if temp > 10:
                flag = 1
                temp -= 10
            else:
                flag = 0
            r.push(temp)

        while s1.size() > 0:
            temp = s1.pop()+flag
            if temp >= 10:
                flag = 1
                temp -= 10
            else:
                flag = 0
            r.push(temp)

        while s2.size() > 0:
            temp = s2.pop()+flag
            if temp >= 10:
                flag = 1
                temp -= 10
            else:
                flag = 0
            r.push(temp)

        if flag:
            r.push(1)

        return r


if __name__ == '__main__':
    # 32
    n1 = StackCustm()
    n1.push(3).push(2)

    # 15
    n2 = StackCustm()
    n2.push(1).push(5)

    r = GeneralOperator.addTwoNum(n1, n2)

    while r.size() > 0:
        print(r.pop())




