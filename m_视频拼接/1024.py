class Solution:
    def videoStitching(self, clips: List[List[int]], T: int) -> int:
        # 设定边界条件和初始状态
        dp = [1e5]*(T+1)
        dp[0] = 0
        for i in range(1,T+1):
            # 状态方程的实现
            for c in clips:
                if c[0] < i <= c[1]:
                    dp[i] = min(dp[i],dp[c[0]]+1)

        return dp[T] if dp[T] != 1e5 else -1