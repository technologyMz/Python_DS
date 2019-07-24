"""
问题；给定一个二叉树，判断它是否是高度平衡的二叉树。

本题中，一棵高度平衡二叉树定义为：

一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过1。

示例 1:

给定二叉树 [3,9,20,null,null,15,7]

    3
   / \
  9  20
    /  \
   15   7
返回 true 。


来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/balanced-binary-tree
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isBalanceTree1(self, root: TreeNode) -> bool:
        """
        法一：自顶向下
        :param root:
        :return:
        """
        if not root:
            return True
        return abs(self.height(root.right) - self.height(root.left)) < 2 and \
               self.isBalanceTree1(root.left) and self.isBalanceTree1(root.right)

    def height(self, node: TreeNode):
        if not node:
            return 0
        return 1 + max(self.height(node.right), self.height(node.left))

    def isBalanceTree2(self, root: TreeNode) -> bool:
        """
        法二：自底向上
        :param root:
        :return:
        """
        self.res = True

        def helper(node: TreeNode):
            if not root:
                return 0
            left = helper(node.left) + 1
            right = helper(node.right) + 1
            if abs(right - left) > 1:
                return False
            return max(left, right)
        helper(root)
        return self.res
