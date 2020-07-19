# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# 时间复杂度O（n）, 空间O（n）


class Solution:
    # 头指针本身就是下标， 下面和归并排序的递归很像
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode(val=0)
        l3 = dummy
        while l1 and l2:
            if l1.val <= l2.val:
                l3.next = l1
                l3 = l3.next
                l1 = l1.next
            elif l1.val > l2.val:
                l3.next = l2
                l3 = l3.next
                l2 = l2.next
        if l1:
            l3.next = l1
        if l2:
            l3.next = l2
        return dummy.next
