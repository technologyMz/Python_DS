"""
问题：给定一个二叉树，找出其最小深度。

最小深度是从根节点到最近叶子节点的最短路径上的节点数量。

说明: 叶子节点是指没有子节点的节点。

示例:

给定二叉树 [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
返回它的最小深度  2.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/minimum-depth-of-binary-tree
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def min_depth1(self, root: TreeNode):
        """
        递归的方式
        :param root:
        :return:
        """
        if not root:
            return 0
        if not root.left and not root.right:
            return 1
        if not root.right:
            return 1+self.min_depth1(root.left)
        if not root.left:
            return 1+self.min_depth1(root.right)
        return 1+min(self.min_depth1(root.left), self.min_depth1(root.right))

    @staticmethod
    def min_depth2(root: TreeNode):
        """
        迭代的方式（层次遍历）
        :param root:
        :return:
        """
        if not root:
            return 0
        ans, count = [root], 1
        while ans:
            n = len(ans)
            for i in range(n):
                r = ans.pop(0)
                if r:
                    if not r.left and not r.right:
                        return count
                    ans.append(r.left if r.left else [])
                    ans.append(r.right if r.right else [])
            count += 1
