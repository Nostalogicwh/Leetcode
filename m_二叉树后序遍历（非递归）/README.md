# 题目
给定一个二叉树，返回它的 后序 遍历。

# 解题思路
使用while循环，增加一个栈模拟递归，先入后出
> stack.append(node)  
  stack.append(None)  
  stack.append(node.right)  
  stack.append(node.left)
最后在pop出来