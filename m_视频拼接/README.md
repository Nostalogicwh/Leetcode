# 题目
你将会获得一系列视频片段，这些片段来自于一项持续时长为 T 秒的体育赛事。这些片段可能有所重叠，也可能长度不一。

视频片段 clips[i] 都用区间进行表示：开始于 clips[i][0] 并于 clips[i][1] 结束。我们甚至可以对这些片段自由地再剪辑，例如片段 [0, 7] 可以剪切成 [0, 1] + [1, 3] + [3, 7] 三部分。

我们需要将这些片段进行再剪辑，并将剪辑后的内容拼接成覆盖整个运动过程的片段（[0, T]）。返回所需片段的最小数目，如果无法完成该任务，则返回 -1 。

# 解题思路
动态规划问题  
用dp[i]表示将区间[0,i)覆盖所需的最少子区间的数量。由于我们希望子区间的数目尽可能少，因此可以将所有dp[i]的初始值设为一个大整数，并将dp[0](即空区间)的初始值设为0。  
枚举所有的子区间来依次计算出所有的dp值。首先枚举i，对于任意一个子区间[aj,bj),若其满足aj< i <= bj,那么它就可以覆盖区间[0,i)的后半部分，而前半部分则可以用dp[aj]对应的最优方法进行覆盖，因此我们可以用dp[aj]+1来更新dp[i]。  
状态转移方程： dp[i] = min{dp[aj]} + 1 (aj < i <= bj)  
最终答案即为dp[T]