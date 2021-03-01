"""
    date:       2021/3/1 4:28 下午
    written by: neonleexiang
"""


# 2021-03-01
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        res = ListNode(0)
        r = res  # recode the head of node
        c = 0    # recode in
        while l1 or l2:
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0
            s = x + y + c
            c = s // 10
            r.next = ListNode(s % 10)
            r = r.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        if c:
            r.next = ListNode(1)
        return res.next




