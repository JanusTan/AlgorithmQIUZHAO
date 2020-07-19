# 142. 环形链表 II
# 时间复杂度O（n）, 空间O（1）


class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return
        slow = head
        fast = head
        while True:
            if not fast or not fast.next:
                return
            fast, slow = fast.next.next, slow.next
            if fast == slow:
                break
        fast = head
        while slow!=fast:
            fast, slow = fast.next, slow.next
        return fast