# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if p.val < q.val:
            s = p.val
            l = q.val
        else:
            s = q.val
            l = p.val
        if s <= root.val <= l:
            return root
        if root.val < s < l:
            return self.lowestCommonAncestor(root.right,p,q)
        if root.val > l > s:
            return self.lowestCommonAncestor(root.left,p,q)