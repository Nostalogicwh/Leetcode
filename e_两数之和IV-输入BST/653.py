# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        arr = []
        def getarr(root):
            if not root:
                return
            arr.append(root.val)
            getarr(root.left)
            getarr(root.right)
        getarr(root)
        l = len(arr)
        for i in range(l):
            for j in range(i+1,l):
                if arr[i] + arr[j] == k:
                    return True
        return False