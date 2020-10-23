# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        arr = []
        l = head
        while l:
            arr.append(l.val)
            l = l.next
        le = len(arr)
        if le == 1:
            return True
        for i in range(int(le/2)):
            if arr[i] == arr[-1-i]:
                continue
            else:
                return False
        return True