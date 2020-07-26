# 236. 二叉树的最近公共祖先


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # 递归终止条件
        if not root or root==p or root == q:
            return root
        # 左右子树递归
        left = self.lowestCommonAncestor(root.left,p,q) # 类别下的成员函数需要用self作为对象调用
        right = self.lowestCommonAncestor(root.right,p,q)
        # 反转当前层的状态
        if not left and not right:
            return
        if not left:
            return right
        if not right:
            return left
        return root