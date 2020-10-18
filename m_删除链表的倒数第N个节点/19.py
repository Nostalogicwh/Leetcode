# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head 
        
        sum = 0
        lis1 = head
        while lis1:
            sum += 1
            lis1 = lis1.next
        if sum == 1:
            return
        lis1 = dummy
        for i in range(sum-n):
            lis1 = lis1.next

        lis1.next = lis1.next.next
        return dummy.next