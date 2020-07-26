# 95. 不同的二叉搜索树 II
# 时间复杂度O（nlogn）, 空间O（n)


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        if n==0:
            return []
        def findtree(left,right):
            # 递归终止条件
            if left > right:
                return [None]
            res = []
            # 当前层逻辑和递归下沉
            for i in range(left,right+1):
                left_tree = findtree(left, i-1)
                right_tree = findtree(i+1, right)
                for j in left_tree:
                    for k in right_tree:
                        tree_node = TreeNode(i)
                        tree_node.left = j
                        tree_node.right = k
                        res.append(tree_node)
            return res
        result = findtree(1,n)
        return result