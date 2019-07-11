"""
问题：二叉搜索树中的两个节点被错误地交换。请在不改变其结构的情况下，恢复这棵树。

示例 1:

输入: [1,3,null,null,2]

   1
  /
 3
  \
   2

输出: [3,1,null,null,2]

   3
  /
 1
  \
   2

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/recover-binary-search-tree
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


思路：这道题难点,是找到那两个交换节点,把它交换过来就行了.

解决方案：
    1. 中序遍历二叉树
    2. 第一个节点，第一个按照中序遍历时候前一个节点大于后一个节点，选取前一个节点
    3. 第二个节点，在第一个节点找到之后, 后面出现前一个节点大于后一个节点,我们选择后一个节点
    4. 交换这两个结点的位置

"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    @staticmethod
    def recover_tree(root: TreeNode) -> None:
        """
        迭代的方式中序遍历，寻找两个变换位置的结点
        :param root:
        :return:
        """
        first_node = None
        second_node = None
        pre = TreeNode(float("-int"))

        stack = []
        p = root
        while p or stack:
            while p:
                stack.append(p)
                p = p.left

            p = stack.pop()

            if not first_node and pre.val > p.val:
                first_node = pre

            if first_node and pre.val > p.val:
                second_node = p

            pre = p
            p = p.right

        first_node.val, second_node.val = second_node.val, first_node.val

    def __init__(self, x):
        self.val = x
        self.firstNode = None
        self.secondNode = None
        self.preNode = None

    def recover_tree2(self, root: TreeNode) -> None:
        self.firstNode = None
        self.secondNode = None
        self.preNode = TreeNode(float("-inf"))

        def in_order(root):
            if not root:
                return

            in_order(root.left)

            if not self.firstNode and self.preNode >= root.val:
                self.firstNode = self.preNode

            if self.firstNode and self.preNode >= root.val:
                self.secondNode = root

            self.preNode = root
            in_order(root.right)

        in_order(root)
        self.firstNode.val, self.secondNode.val = self.secondNode.val, self.firstNode.val











