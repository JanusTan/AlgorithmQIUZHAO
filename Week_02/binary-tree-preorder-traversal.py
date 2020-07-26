# 144. 二叉树的前序遍历
# 时间复杂度O（n）, 空间O（n)


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        result = []
        def traves(root, result):
            if not root:
                return
            result.append(root.val)
            traves(root.left,result)
            traves(root.right,result)
        traves(root, result) # 函数内的函数要写在前
        return result
