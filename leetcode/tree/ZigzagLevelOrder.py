"""
    问题：给定一个二叉树，返回其节点值的锯齿形层次遍历。
        （即先从左往右，再从右往左进行下一层遍历，以此类推，层与层之间交替进行）。

    例如：
        给定二叉树 [3,9,20,null,null,15,7],

            3
           / \
          9  20
            /  \
           15   7
        返回锯齿形层次遍历如下：

        [
          [3],
          [20,9],
          [15,7]
        ]

        来源：力扣（LeetCode）
        链接：https://leetcode-cn.com/problems/binary-tree-zigzag-level-order-traversal
        著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> list[list[int]]:
        """
        方法一：BFS 层次遍历
        :param root:
        :return:
        """
        if not root:
            return []
        res = []
        cur_level = [root]
        depth = 0
        while cur_level:
            tmp = []
            next_level = []
            for node in cur_level:
                tmp.append(node.val)
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            if depth % 2 == 1:
                res.append(tmp[::-1])
            else:
                res.append(tmp)
            depth += 1
            cur_level = next_level
        return res

    def zigzagLevelOrder2(self, root: TreeNode) -> list[list[int]]:
        """
        迭代的方式遍历
        :param root:
        :return:
        """
        res = []

        def helper(node, depth):
            if not node:
                return
            if len(res) == depth:
                res.append([])
            if depth % 2 == 0:
                res[depth].append(node.val)
            else:
                res[depth].insert(0, node.val)
            helper(node.left, depth + 1)
            helper(node.right, depth + 1)

        helper(root, 0)
        return res











