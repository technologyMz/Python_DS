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
        return self.isMirror(root, root)

    def isMirror(self, leftRoot: TreeNode, rightRoot: TreeNode) -> bool:
        if not leftRoot and not rightRoot:
            return True
        if not leftRoot or not rightRoot:
            return False
        if leftRoot.val != rightRoot.val:
            return False
        return self.isMirror(leftRoot.left, rightRoot.right) and self.isMirror(leftRoot.right, rightRoot.left)



