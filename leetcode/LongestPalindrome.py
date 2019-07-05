"""
    给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。
    (回文是一个正读和反读都相同的字符串)

    示例 1：
        输入: "babad"
        输出: "bab"
        注意: "aba" 也是一个有效答案。

"""


class Solution:
    def checkPolindrome(self, s: str) -> bool:
        i = 0
        j = len(s) - 1
        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True

    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ''
        # 二分长度, 直接二分长度不行，因为3个成立，2个有可能不成立
        # 但是长度为4成立，则2一定成立，长度为5成立，则3一定成立
        # 因此每次判断两个一奇一偶，不满足才能长度减一。
        ans = ''
        l = 0
        r = len(s)
        while l <= r:
            mid = (l + r) // 2
            find = False

            for i in range(len(s) - mid + 1):
                if self.checkPolindrome(s[i:i + mid]):
                    find = True
                    ans = s[i:i + mid]
                    break

            for i in range(len(s) - mid):
                if self.checkPolindrome(s[i:i + mid + 1]):
                    find = True
                    ans = s[i:i + mid + 1]
                    break
            if find:
                l = mid + 1
            else:
                r = mid - 1
        return ans


if __name__ == '__main__':
    str1 = 'babad'
    s1 = Solution()
    re = s1.longestPalindrome(str1)
    print(re)
