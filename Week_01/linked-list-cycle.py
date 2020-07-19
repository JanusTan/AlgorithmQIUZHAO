# 141. 环形链表
# 时间复杂度O（n）, 空间O（1）


class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if not head or not head.next:
            return False
        slow = head
        fast = head.next
        while slow != fast:
            if not fast or not fast.next:
                return False
            slow = slow.next
            fast = fast.next.next # 之所以间隔跳是因为上面已经判了fast.next是非空的
        return True