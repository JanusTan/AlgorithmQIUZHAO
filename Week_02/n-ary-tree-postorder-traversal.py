# 590. N叉树的后序遍历
# 时间复杂度O（n）, 空间O（n)


"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        if not root:
            return []
        stack = [root]
        result = []
        while stack:
            root = stack.pop()
            result.append(root.val)
            stack.extend(root.children[:])
        return result[::-1]