# 589. N叉树的前序遍历
# 时间复杂度O（n）, 空间O（n）
# 二叉树一般是递归，N叉树要用到栈和队列


"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if not root:
            return []
        stack = [root]
        result = []
        while stack:
            root  = stack.pop()
            result.append(root.val)
            stack.extend(root.children[::-1])
        return result