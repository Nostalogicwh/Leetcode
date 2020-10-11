class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        Sum = sum(nums)
        if Sum % 2!= 0:
            return False
        amount = Sum // 2
        dp = [True] + [False for _ in range(1, amount + 1)]  
        for num in nums:
            for i in range(amount, num - 1, -1):
                dp[i] |= dp[i - num]
        return dp[-1]