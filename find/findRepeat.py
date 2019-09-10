"""
  给定有序数组，找出其中重复的数字并将其放在数组末尾
  如：[1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 9] 变为 [1,2,3,4,5,6,7,9,4,6,6]
"""


class FindRepeat:
    def __init__(self, x):
        self.lst = x

    @staticmethod
    def sort(lst):
        re_elem = {}
        for i in range(0, len(lst)-1):
            if lst[i] == lst[i+1]:
                re_elem[i] = lst[i]

        count = 0
        for idx in sorted(re_elem.keys()):
            del lst[idx - count]
            count = count + 1

        lst = lst + [re_elem.__getitem__(k) for k in sorted(re_elem.keys())]
        print(lst)


if __name__ == '__main__':
    ls = [1, 2, 3, 4, 4, 5, 5, 6, 6, 6, 7, 8, 9]
    FindRepeat.sort(ls)
