class Solution:
    def totalNQueens(self, n: int) -> int:
        
        ans = 0
        
        def dfs(i,col,dig1,dig2):
            if i == n:
                nonlocal ans
                ans += 1
                return
            for j in range(n):
                if j not in col and i+j not in dig1 and j-i not in dig2:
                    dfs(i+1,col+[j],dig1+[i+j],dig2+[j-i])
        
        dfs(0,[],[],[])
        
        return ans