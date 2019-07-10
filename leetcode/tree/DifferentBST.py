"""
    给定一个整数 n，生成所有由 1 ... n 为节点所组成的二叉搜索树。

    示例:

        输入: 3
        输出:
        [
          [1,null,3,2],
          [3,2,null,1],
          [3,1,null,null,2],
          [2,1,3],
          [1,null,2,null,3]
        ]
        解释:
        以上的输出对应以下 5 种不同结构的二叉搜索树：

           1         3     3      2      1
            \       /     /      / \      \
             3     2     1      1   3      2
            /     /       \                 \
           2     1         2                 3

"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    """
        * 二叉搜索树, 一节点大于左子树节点, 小于右子树节点
        * 所以我们节点是从1到n,当一个节点为val那么它的左边是<= val,右边是>=val
    """
    def generateTrees(self, n: int) -> list[TreeNode]:
        def generate_trees(start, end):
            if start > end:
                return [None, ]
            all_trees = []
            for i in range(start, end+1):
                # 当i为根节点时，所有可能的左子树
                left_trees = generate_trees(start, i-1)

                # 当i为根节点时， 所有可能的右子树
                right_trees = generate_trees(i+1, end)

                for l in left_trees:
                    for r in right_trees:
                        current_tree = TreeNode(i)
                        current_tree.left = l
                        current_tree.right = r
                        all_trees.append(current_tree)
            return all_trees

        return generate_trees(1, n) if n else []















