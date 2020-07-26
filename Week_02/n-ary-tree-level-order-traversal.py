# 429. N叉树的层序遍历
# 时间复杂度O（n）, 空间O（n）


"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""


class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return
        from collections import deque
        Layer = deque()
        Layer.append(root)
        result = []
        while Layer:
            result1 = []
            for i in range(len(Layer)):
                root = Layer.popleft()
                if not root:  # 跳过None的节点
                    continue
                result1.append(root.val)
                Layer.extend(root.children[:])
            result.append(result1)
        return result
