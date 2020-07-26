# 105. 从前序与中序遍历序列构造二叉树
# 时间复杂度O（n）, 空间O（n）


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder or not inorder:
            return
        root = TreeNode(preorder[0])
        idx = inorder.index(root.val)
        root.left = self.buildTree(preorder[1:idx+1], inorder[0:idx])
        root.right = self.buildTree(preorder[idx+1:], inorder[idx+1:])
        return root