# 题目
给你一个数组 nums 。数组「动态和」的计算公式为：runningSum[i] = sum(nums[0]…nums[i]) 。  
请返回 nums 的动态和。

# 解题思路
动态规划，dp[i][j]表示[0,i]区间内，到下标为i这一天状态为j时的我们手上拥有的现金数，j：0不持股，1持股  
dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i] - fee)  
dp[i][1] = max(dp[i-1][1], dp[i-1][0] - prices[i])  
第一天不持股初始化为0，持股初始化为-prices[0] - fee
最优值在最后一天，并且不持股