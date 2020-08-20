from heapq import heappop, heappush
# heapq优先队列最小堆(小顶堆)
# heapq自动从小到大排序，构建小顶堆
a = [5, 3, 1, 6, 4]
priority_queue = []
for i in range(len(a)): heappush(priority_queue, a[i])
for j in range(len(a)): a[j] = heappop(priority_queue)
print(a)  # [1, 3, 4, 5, 6]
