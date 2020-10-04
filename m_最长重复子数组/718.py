class Solution:
    def findLength(self, A: List[int], B: List[int]) -> int:
        lenth = 0
        dp = [[0 for _ in range(len(A)+1)] for _ in range(len(B)+1)]
        for i in range(len(A)):
            for j in range(len(B)):
                if A[i] == B[j]:
                    dp[i][j] = dp[i-1][j-1] + 1
                    lenth = max(lenth,dp[i][j])
        return lenth