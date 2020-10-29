# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        self.res = 0
        def dfs(node, presum):
            if not node:
                return None
            if not node.left and not node.right:
                self.res += presum * 10 + node.val
                return
            presum = 10 * presum + node.val
            dfs(node.left, presum)
            dfs(node.right, presum)
        dfs(root, 0)
        return self.res