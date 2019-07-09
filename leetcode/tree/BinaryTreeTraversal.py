"""
    二叉树中序遍历
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution1:
    """ 递归的方式 """
    def inorderTraversal(self, root: TreeNode) -> list[int]:
        f = self.inorderTraversal
        return f(root.left) + [root.val] + f(root.right) if root else []


class Solution2:
    """ 迭代的方式 """
    def inorderTraversal(self, root: TreeNode) -> list[int]:
        r, stack = [], []
        while True:
            while root:
                stack.append(root)
                root = root.left
            if not stack:
                return r
            node = stack.pop()
            r.append(node.val)
            root = node.right





