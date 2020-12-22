class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [0 for _ in range(len(cost)+2)]
        for i in range(len(cost)):
            dp[i+1] = min(dp[i-1]+cost[i],dp[i]+cost[i])
        dp[-1] = min(dp[-2],dp[-3])
        return dp[-1]