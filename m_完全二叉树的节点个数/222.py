# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def countNodes(self, root: TreeNode) -> int:
        if not root: return 0
        left_height = 0
        left_node = root
        right_height = 0
        right_node = root
        while left_node:
            left_node = left_node.left
            left_height += 1
        while right_node:
            right_node = right_node.right
            right_height += 1
        if left_height == right_height:
            return pow(2,left_height) - 1
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)