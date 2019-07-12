"""
    问题：给定一个二叉树，检查它是否是镜像对称的。


    例如： 二叉树 [1,2,2,3,4,4,3] 是对称的。
                                                1
                                               / \
                                              2   2
                                             / \ / \
                                            3  4 4  3
中序遍历结果：[2，3，4，1，2，4，3]
    思路：
        1. 它们的两个根结点具有相同的值
        2. 每个树的右子树都与另一个树的左子树镜像对称
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSymmetric(self, root: TreeNode):
        """
        递归的方式实现
        :param root:
        :return:
        """

        return self.isMirror(root, root)

    def isMirror(self, leftRoot: TreeNode, rightRoot: TreeNode) -> bool:
        if not leftRoot and not rightRoot:
            return True
        if not leftRoot or not rightRoot:
            return False
        if leftRoot.val != rightRoot.val:
            return False
        return self.isMirror(leftRoot.left, rightRoot.right) and self.isMirror(leftRoot.right, rightRoot.left)

    def isSymmetric2(self, root: TreeNode) -> bool:
        """
        迭代的方式实现
        :param root:
        :return:
        """
        if not root:
            return True

        node_queue = [root.left, root.right]
        while node_queue:
            left = node_queue.pop(0)
            right = node_queue.pop(0)

            if not left and not right:
                return True
            if not left or not right:
                return False
            if left.val != right.val:
                return False

            node_queue.extend([left.left, right.right, left.right, right.left])
        return True
