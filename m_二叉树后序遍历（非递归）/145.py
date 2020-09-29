# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []

        ans = []

        stack = []
        stack.append(root)

        while stack:
            node = stack.pop()
            if node:
                # 如果节点不为空，
                # 当前节点重新入栈
                stack.append(node)
                # 这里添加 None，为了后面处理数据，
                # 标记左右子节点访问结束，可处理当前节点
                stack.append(None)
                # 这里先将右子节点入栈
                if node.right:
                    stack.append(node.right)
                # 再将左子节点入栈
                if node.left:
                    stack.append(node.left)

            else:
                node = stack.pop()
                ans.append(node.val)

        return ans