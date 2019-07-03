

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:

    @staticmethod
    def addTwoNumbers(l1: ListNode, l2: ListNode) -> ListNode:
        # 用来进位
        flag = 0
        # 保存结果的链表
        out = r = ListNode(0)

        while l1 is not None and l2 is not None:
            temp = l1.val + l2.val + flag
            if temp >= 10:
                flag = 1
                p = temp - 10
            else:
                flag = 0
                p = temp
            l1 = l1.next
            l2 = l2.next
            r.next = ListNode(p)
            r = r.next

        while l1 is not None:
            temp = l1.val + flag
            if temp >= 10:
                flag = 1
                p = temp - 10
            else:
                flag = 0
                p = temp
            l1 = l1.next
            r.next = ListNode(p)
            r = r.next

        while l2 is not None:
            temp = l2.val + flag
            if temp >= 10:
                flag = 1
                p = temp - 10
            else:
                flag = 0
                p = temp
            l2 = l2.next
            r.next = ListNode(p)
            r = r.next
        if flag:
            r.next = ListNode(1)
        out = out.next
        return out


if __name__ == '__main__':
    # 5
    ls1 = ListNode(5)

    # 23
    ls2 = ListNode(3)
    n2 = ListNode(2)
    ls2.next = n2

    sumNum = Solution.addTwoNumbers(ls1, ls2)

    while sumNum is not None:
        print(sumNum.val)
        sumNum = sumNum.next







