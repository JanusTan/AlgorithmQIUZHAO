# 24. 两两交换链表中的节点
# 时间复杂度O（n）, 空间O（1） 2-》(1—》【】), 递归不要自己在脑里验算全部，只要第一层的子逻辑对了就能递归


class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        res = head.next  # 结果head指向2
        head.next = self.swapPairs(head.next.next)  # (1—》【】)
        res.next = head  # 2 -> 1
        return res  # 2-》1—》【】
