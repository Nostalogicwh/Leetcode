# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        # check 是否为叶子结点：
        def helper(root):
            if root is None:
                return False
            if root.left is None and root.right is None:
                return True
            else:
                return False

        # 前序遍历，在遍历过程中，发现叶子结点 and 是左树的，则加入到self.res中。
        def dfs(root,marker):
            if root is None:
                return 0

            if helper(root) and marker:
                self.res += root.val
            dfs(root.left,marker = 1)
            dfs(root.right,marker = 0)

        self.res = 0    
        dfs(root,0)
        return self.res