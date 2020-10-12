# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        arr = []
        def getnum(root):
            if not root:
                return
            arr.append(root.val)
            getnum(root.left)
            getnum(root.right)
        getnum(root)
        num = abs(arr[1] - arr[0])
        l = len(arr)
        for i in range(l):
            for j in range(i+1,l):
                if abs(arr[i] - arr[j]) < num:
                    num = abs(arr[i] - arr[j])
        return num