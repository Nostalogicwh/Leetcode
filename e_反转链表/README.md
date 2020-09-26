# 题目
反转一个单链表。

# 解题思路
首先 pre 指针指向 Null，cur 指针指向 head；  

当 cur != Null，执行循环。  

- 先将 cur.next 保存在 temp 中防止链表丢失：temp = cur.next

- 接着把 cur.next 指向前驱节点 pre：cur.next = pre

- 然后将 pre 往后移一位也就是移到当前 cur 的位置：pre = cur

- 最后把 cur 也往后移一位也就是 temp 的位置：cur = temp

当 cur == Null，结束循环，返回 pre。
