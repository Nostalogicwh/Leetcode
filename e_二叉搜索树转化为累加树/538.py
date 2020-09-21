# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    
    def convertBST(self, root: TreeNode) -> TreeNode:
        sum = 0
        def des(root):
            nonlocal sum
            if not root:
                return None
            des(root.right)
            sum += root.val 
            root.val = sum
            des(root.left)
            return root
        return des(root)