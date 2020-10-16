class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        if not root:
            return 0
        ans, que = 1, [(0, root)]   #起始坐标为0，节点为根节点
        while que:
            ans = max(ans, que[-1][0] - que[0][0] + 1)
            tmp = []                #下一轮队列
            for i, q in que:        #坐标节点生成
                q.left and tmp.append((i * 2, q.left))
                q.right and tmp.append((i * 2 + 1, q.right))
            que = tmp
        return ans