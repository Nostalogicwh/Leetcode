# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head
        head1 = p = head
        head2 = q = head.next
        i = 0
        tem = head.next.next
        while tem:
            if i % 2 == 0:
                p.next = tem
                p = p.next
            else:
                q.next = tem
                q = q.next
            tem = tem.next
            i += 1
        p.next = head2
        q.next = None
        return head1