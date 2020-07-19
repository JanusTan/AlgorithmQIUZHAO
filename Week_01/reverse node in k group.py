# 25. K 个一组翻转链表
# 时间复杂度O（n）, 空间O（1）, 遍历整个链表O（n）,每次调换要O（k), c是调换次数，ck常数，O(n*k*c)还是O（n）


class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:  # 分组，子链表排序
        if not head or k < 2:
            return head
        dummy = ListNode(0)
        dummy.next = head
        start = dummy
        end = head
        count = 0
        while end:
            count = count + 1
            if count % k == 0:
                start = self.reverse(start, end.next)
                end = start.next
            else:
                end = end.next
        return dummy.next

    def reverse(self, start, end):  # 倒序子链表
        pre = start
        cur = start.next
        new_start = cur
        while cur != end:
            temp = cur.next
            cur.next = pre
            pre = cur
            cur = temp
        start.next = pre  # 连上前半段
        new_start.next = end  # 连上后半段
        return new_start
