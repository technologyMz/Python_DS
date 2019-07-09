

class Solution:
    """
        约瑟夫环问题

    """
    @staticmethod
    def josephus(ls, skip):
        skip -= 1  # pop automatically skips the dead guy
        idx = skip
        while len(ls) > 1:
            print(ls.pop(idx))  # kill prisoner at idx
            idx = (idx + skip) % len(ls)
        print('survivor: ', ls[0])


if __name__ == '__main__':
    Solution.josephus(["Bill", "David", "Susan", "Jane", "Kent", "Brad"], 3)
