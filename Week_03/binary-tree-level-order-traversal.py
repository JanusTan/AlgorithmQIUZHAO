# 102. 二叉树的层序遍历
# 时间复杂度O（n）, 空间O（n），DFS、BFS都要遍历整个树


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        def dfs(root, level, result):
            if not root: return
            if len(result) == level: result.append([])
            result[level].append(root.val)
            if root.left: dfs(root.left, level + 1, result)
            if root.right: dfs(root.right, level + 1, result)

        result = []
        dfs(root, 0, result)
        return result

        # BFS methods
        # if not root:
        #     return []
        # from collections import deque
        # layer = deque()
        # layer.append(root)
        # result = []
        # while layer:
        #     cur_layer = []
        #     for i in range(len(layer)):
        #         temp = layer.popleft()
        #         cur_layer.append(temp.val)
        #         if temp.left:
        #             layer.append(temp.left)
        #         if temp.right:
        #             layer.append(temp.right)
        #     result.append(cur_layer)
        # return result
