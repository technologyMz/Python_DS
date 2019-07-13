"""
    题目：给定一个二叉树，返回其按层次遍历的节点值。（即逐层地，从左到右访问所有节点）。
    例如:
        给定二叉树: [3,9,20,null,null,15,7],

            3
           / \
          9  20
            /  \
           15   7
        返回其层次遍历结果：

        [
          [3],
          [9,20],
          [15,7]
        ]


【树的常见遍历方式】
    * 深度优先搜索 (DFS)（先序遍历、中序遍历、后序遍历）
    * 宽度优先搜索 (BFS)


【 方法1：递归】
    1. 输出列表称为 levels，当前最高层数就是列表的长度 len(levels)。比较访问节点所在的层次 level 和当前最高层次 len(levels) 的大小，
    如果前者更大就向 levels 添加一个空列表。
    2. 将当前节点插入到对应层的列表 levels[level] 中。
    3. 递归非空的孩子节点：helper(node.left / node.right, level + 1)。


【方法2：迭代】
    1. 初始化队列只包含一个节点 root 和层次编号 0 ： level = 0。
    2. 当队列非空的时候：
        * 在输出结果 levels 中插入一个空列表，开始当前层的算法。
        * 计算当前层有多少个元素：等于队列的长度。
        * 将这些元素从队列中弹出，并加入 levels 当前层的空列表中。
        * 将他们的孩子节点作为下一层压入队列中。
        * 进入下一层 level++。


作者：LeetCode
链接：https://leetcode-cn.com/problems/two-sum/solution/er-cha-shu-de-ceng-ci-bian-li-by-leetcode/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

"""

from collections import deque


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def levelOrder(self, root: TreeNode) -> list[list[int]]:
        """
        使用递归的方式层次遍历，并标记每一层的level
        :param root:
        :return:
        """

        levels = []
        if not root:
            return levels

        def helper(node, level):
            if len(levels) == level:
                levels.append([])

            levels[level].append(node.val)

            if node.left:
                helper(node.left, level+1)

            if node.right:
                helper(node.right, level+1)

        helper(root, 0)
        return levels

    def levelOrder2(self, root):
        """
        使用迭代的方式层次遍历
        :param root:
        :return:
        """
        levels = []
        if not root:
            return levels

        level = 0
        queue = deque([root, ])
        while queue:
            queue.append([])
            level_len = len(queue)

            for i in range(level_len):
                node = queue.popleft()
                levels[level].append(node.val)

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

            level += 1

        return levels
