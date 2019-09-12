"""
    二叉树：寻找两个结点的最近祖先结点

"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def pre_order(self, root: TreeNode):
        """
        二叉树的先序遍历
        :param root:
        :return:
        """
        f = self.pre_order
        return [root.val] + f(root.left) + f(root.right) if root else []

    def list2tree(self, root: TreeNode, lst, i):
        """
        通过list创建二叉树
        :param root:
        :param lst:
        :param i:
        :return:
        """
        if i < len(lst):
            if not lst[i]:
                return None
            else:
                root = TreeNode(lst[i])
                root.left = self.list2tree(root.left, lst, 2 * i + 1)
                root.right = self.list2tree(root.right, lst, 2 * i + 2)
                return root
        return root

    def print_tree(self, pRoot):
        """
        打印二叉树
        :param pRoot:
        :return:
        """
        if pRoot is None:
            return []
        if pRoot.left is None and pRoot.right is None:
            return [[pRoot.val]]
        stack = [pRoot]
        output = []
        while stack:
            temp = []
            for i in range(len(stack)):
                out_node = stack.pop(0)
                temp.append(out_node.val)
                if out_node.left is not None:
                    stack.append(out_node.left)
                if out_node.right is not None:
                    stack.append(out_node.right)
            output.append(temp)
        return output

    def lowest_common_ancestor(self, root, A, B):
        """
        LCA,最近公共祖先
        假设给出的两个节点都在树中存在,
        最近公共祖先是两个节点的公共的祖先节点且具有最大深度。

        """
        if (not root) or root.val == A or root.val == B:
            return root  # 若root为空或者root为A或者root为B，说明找到了A和B其中一个

        left = self.lowest_common_ancestor(root.left, A, B)
        right = self.lowest_common_ancestor(root.right, A, B)

        if left and right:
            # 若左子树找到了A，右子树找到了B，说明此时的root就是公共祖先
            return root

        if not left:
            # 若左子树是none右子树不是，说明右子树找到了A或B
            return right

        if not right:
            # 同理
            return left
        return None


if __name__ == '__main__':
    slt = Solution()
    tree = slt.list2tree(None, [1, 3, 4, 5, 6, 7, 8, 9], 0)
    print(slt.print_tree(tree))

    node = slt.lowest_common_ancestor(tree, 5, 6)
    print(node.val)


