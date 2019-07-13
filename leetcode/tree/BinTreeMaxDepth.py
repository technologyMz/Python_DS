"""
    问题：给定一个二叉树，找出其最大深度。
         二叉树的深度为根节点到最远叶子节点的最长路径上的节点数。

    说明: 叶子节点是指没有子节点的节点。

    示例：
    给定二叉树 [3,9,20,null,null,15,7]，

        3
       / \
      9  20
        /  \
       15   7
    返回它的最大深度 3 。

    来源：力扣（LeetCode）
    链接：https://leetcode-cn.com/problems/maximum-depth-of-binary-tree
    著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        """
        递归的方式实现，DFS（深度优先搜索）
        :param root:
        :return:
        """

        if not root:
            return 0
        else:
            left_hight = self.maxDepth(root.left)
            right_hight = self.maxDepth(root.right)
        return max(left_hight, right_hight) + 1

    def maxDepth2(self, root: TreeNode):
        """
        DFS 策略访问每个结点，同时在每次访问时更新最大深度
        :param root:
        :return:
        """
        stack = []
        if root:
            stack.append((1, root))

        depth = 0
        while stack:
            current_depth, node = stack.pop()
            if root:
                depth = max(depth, current_depth)
                stack.append((current_depth + 1, root.left))
                stack.append((current_depth + 1, root.right))

        return depth














