"""
    给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。
    例如：
        输入: "abcabcbb"
        输出: 3
        解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。

"""


class Solution1:
    """
        使用滑动窗口（队列）
    """
    @staticmethod
    def lengthOfLongestSubstring(s: str) -> int:
        if not s:
            return 0
        left = 0
        lookup = set()
        n = len(s)
        max_len = 0

        cur_len = 0
        for i in range(0, n):
            cur_len += 1
            while s[i] in lookup:
                lookup.remove(s[left])
                left += 1
                cur_len -= 1
            if cur_len > max_len:
                max_len = cur_len
            lookup.add(s[i])
        return max_len


class Solution2:
    """
        *  设定左右双指针l和r，遍历字符串；
        *  哈希表存储某字符s[i]最新在字符串中出现的位置index + 1，key, value对应s[i], i；
        *  左指针在遍历过程中：
            * 若s[i]不在HashMap中，则跳过；
            * 否则，l指针设定为l和dic[s[r]]的最大值，即修改之后，保证新字符串中没有重复字符。
            * 每次更新长度最大值res。
    """

    @staticmethod
    def lengthOfLongestSubstring(s: str) -> int:
        dic = {}
        left, res = 0, 0
        for i in range(0, len(s)):
            if s[i] in dic:
                left = dic[s[i]]
            dic[s[i]] = i + 1
            res = max(res, i + 1 - left)
        return res


if __name__ == '__main__':
    str_test = "abcabcbb"
    le = Solution2.lengthOfLongestSubstring(str_test)
    print(le)


