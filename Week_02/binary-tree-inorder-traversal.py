# 94. 二叉树的中序遍历
# 时间复杂度O（n）, 空间O（n)
# 树的题一般用递归，现在的运算技术循环和递归速度上已经没啥区别了


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        self.result = []
        self.traverse(root, self.result)
        return self.result

    def traverse(self, root, result):  # 中序（左根右）， 前序（根左右），后序（左右根），按需调换以下三语句顺序即可
        if not root:
            return
        self.traverse(root.left, result)
        self.result.append(root.val)
        self.traverse(root.right, result)
