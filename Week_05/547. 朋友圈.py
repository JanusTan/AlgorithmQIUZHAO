class Solution:
    def findCircleNum(self, M):
        if not M: return 0
        visited = set() # 记录屡过人际关系的人员编号0,1,2...
        nums = len(M)
        result = 0
        for i in range(nums): # 依次屡每个人的人际关系
            if i not in visited: # 之前没屡过才屡
                # BFS
                queue = [i]
                while queue:
                    man_id=queue.pop(0)
                    visited.add(man_id) # 添加到访问过的名单
                    for j in range(nums):
                        if M[man_id][j] == 1 and j not in visited: # 把这个人认识的人且当前未访问过的人加到队列
                            queue.append(j)
                result += 1 # 每一次队空，意味着出现了一个圈
        return result