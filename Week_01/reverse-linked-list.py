# 206. 反转链表
# 时间复杂度O（n）, 空间O（1)


# class Solution: # 迭代
#     def reverseList(self, head: ListNode) -> ListNode:
#         pre = None
#         cur = head
#         while cur is not None:
#             temp = cur.next
#             cur.next = pre
#             pre = cur
#             cur = temp
#         return pre
class Solution: # 递归 【】-》 2 -》 1 - 》 None
    def reverseList(self, head: ListNode) -> ListNode:
        # 递归终止条件
        if not head or not head.next:
            return head
        # 当前层逻辑，递归下沉
        next_node = self.reverseList(head.next)  # 【】-》 2
        head.next.next = head  # 下面两句2->1 -> None
        head.next = None
        return next_node