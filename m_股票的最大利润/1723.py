class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = len(prices)
        ans = 0
        for i in range(l):
            ans = max(ans,max(prices[i:l])-prices[i])
        return ans