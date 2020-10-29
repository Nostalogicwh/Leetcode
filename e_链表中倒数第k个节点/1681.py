# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:
        l = head
        lenth = 0
        while l:
            lenth += 1
            l = l.next
        a = head
        sum = lenth - k
        
        while sum > 0:
            a = a.next
            sum = sum - 1
        return a