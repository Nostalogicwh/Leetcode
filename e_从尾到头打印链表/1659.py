# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reversePrint(self, head: ListNode) -> List[int]:
        lis = head
        arr = []
        while lis:
            arr.append(lis.val)
            lis = lis.next
        arr = arr[::-1]
        return arr