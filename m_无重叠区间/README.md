# 题目
给定一个区间的集合，找到需要移除区间的最小数量，使剩余区间互不重叠。

**注意:**

- 可以认为区间的终点总是大于它的起点。
- 区间 [1,2] 和 [2,3] 的边界相互“接触”，但没有相互重叠。

# 解题思路
动态规划  
在剩下的区间里，相邻区间的后一个区间的开始时间一定不小于前一个区间的结束时间，是一个非严格递增序列  
删除若干区间，从而剩下最长的非严格递增子序列  
先进行排序，比较后面的开始时间和前面的结束