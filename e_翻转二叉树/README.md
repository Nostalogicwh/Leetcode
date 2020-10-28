# 题目
翻转一棵二叉树。

# 解题思路
对每个节点的左右孩子都进行互换。  
不可写在同一行，第一行修改left会影响第二行。  
写在同一行，可保证同时执行  
> root.left,root.right = self.invertTree(root.right),selft.invertTree(root.left)