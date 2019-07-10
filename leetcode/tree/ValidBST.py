"""
    题目：验证二叉搜索树

    假设一个二叉搜索树具有如下特征：
       1. 节点的左子树只包含小于当前节点的数
       2. 节点的右子树只包含大于当前节点的数
       3. 所有左子树和右子树自身必须也是二叉搜索树
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self, x):
        self.val = x
        self.pre = None
        self.next = None

    def isValidBST(self, root: TreeNode) -> bool:
        """
        利用递归中序遍历
        :param root:
        :return:
        """
        self.pre = None

        def isBST(root):
            if not root:
                return True
            if not isBST(root.left):
                return False
            if self.pre and self.pre.val >= root.val:
                return False
            self.pre = root
            return isBST(root.right)
        return isBST(root)

    def isValidBST2(self, root: TreeNode) -> bool:
        """
        利用迭代
        :param root:
        :return:
        """
        stack = []
        p = root
        pre = None
        while p or stack:
            while p:
                stack.append(p)
                p = p.left
            p = stack.pop()
            if pre and p.val <= pre.val:
                return False
            pre = p
            p = p.right
        return True

    def isValidBST3(self, root: TreeNode) -> bool:
        """
        利用最大值、最小值
        :param root:
        :return:
        """
        def isBST(root_node, min_val, max_val):
            if not root_node:
                return True
            if root_node.val >= max_val or root_node.val <= min_val:
                return False
            return isBST(root_node.left, min_val, root_node.val) and isBST(root_node.right, root_node.val, max_val)
        return isBST(root, float("-inf"), float("inf"))

