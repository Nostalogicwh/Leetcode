# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minCameraCover(self, root: TreeNode) -> int:
         
        self.res = 0
        def lrd(node):
            if node is None:
                return 1 #空节点不需要被人拍也不用拍别人，直接返回被拍了就好
            left = lrd(node.left)
            right = lrd(node.right)
            if left == 0 or right == 0: 
                #如果左儿子或者右儿子需要被拍，我就装个摄像机
                self.res += 1
                return 2        
            if left == 2 or right == 2:
                #如果左儿子或者右儿子装了摄像机，那我就被拍了
                return 1
            else:# left == 1 or Null and right == 1 or Null:
                #如果左儿子和右儿子都是被拍的，都没有摄像机，那我就是需要被拍的状态
                return 0

        if lrd(root) == 0:
            ##看看根节点是不是需要被拍
            self.res += 1
        return self.res