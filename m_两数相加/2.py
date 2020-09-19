# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        a = ListNode() # 创建链表
        l3 = a  # 
        c = 0  # 进位
        while l1 or l2:
            x=l1.val if l1 else 0  # 没有下一节点时取0
            y=l2.val if l2 else 0
            tmp = x+y
            if tmp+c <10:
                l3.next = ListNode(tmp+c)
                c=0  # 不进位，清零
            else:
                l3.next = ListNode(tmp+c-10)
                c=1  # 进位，进1
            if l1:
                l1 = l1.next  # 进入链表的下一节点
            if l2:
                l2 = l2.next  # 进入链表的下一节点
            l3 = l3.next
        if c==1:
            l3.next = ListNode(1)  # 最后一个进位增加一个末尾节点，元素为1
        return a.next  # a的第一个是0，因此去头节点