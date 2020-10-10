# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        fast = slow = head
        while fast and fast.next:
            fast = fast.next.next if fast.next else None
            slow = slow.next
            if fast and fast.next and fast == slow:
                while head != fast:
                    head = head.next
                    fast = fast.next
                return fast             
        return None