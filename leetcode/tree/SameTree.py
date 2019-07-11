"""
    问题：给定两个二叉树，编写一个函数来检验它们是否相同。
        （如果两个树在结构上相同，并且节点具有相同的值，则认为它们是相同的）

"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def same_tree(self, p: TreeNode, q: TreeNode) -> bool:
        # 两棵树均为空
        if not p and not q:
            return True

        # 其中一棵树为空
        if not p or not q:
            return False

        # 比较结点的值
        if p.val != q.val:
            return False

        return self.same_tree(p.right, q.right) and self.same_tree(p.left, q.left)

    def same_tree2(self, root1: TreeNode, root2: TreeNode) -> bool:
        """
        比较对应结点上的值是否相同
        :param root1:
        :param root2:
        :return:
        """
        if not root1 and not root2:
            return True

        ls1 = self.inorderTraversal(root1)
        ls2 = self.inorderTraversal(root2)

        if len(ls1) != len(ls2):
            return False

        for i in range(0,len(ls1)):
            if ls1[i] != ls2[i]:
                return False

        return True

    def inorderTraversal(self, root: TreeNode) -> list:
        """
        迭代，中序遍历
        :param root:
        :return:
        """
        if not root:
            return []
        r, stack = [], []
        while True:
            while root:
                stack.append(root)
                root = root.left
            if not stack:
                return r
            p = stack.pop()
            r.append(p.val)
            root = p.right
