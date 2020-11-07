# 题目
给定一个整数数组 nums，返回区间和在 [lower, upper] 之间的个数，包含 lower 和 upper。
区间和 S(i, j) 表示在 nums 中，位置从 i 到 j 的元素之和，包含 i 和 j (i ≤ j)。  

说明:  
最直观的算法复杂度是 O(n2) ，请在此基础上优化你的算法。

# 解题思路
使用前缀数组pre，然后每个前缀和pre[i]二分查找前面i-1i−1个和的pre[i]-lower和pre[i]−upper的位置得出区间和的数量，然后把pre[i]pre[i]二分插入到数组中保持数组有序