# 题目
和谐数组是指一个数组里元素的最大值和最小值之间的差别正好是1。  

现在，给定一个整数数组，你需要在所有可能的子序列中找到最长的和谐子序列的长度。

# 解题思路
利用哈希表存储数组中元素出现的次数  
遍历哈希表，如果当前元素+1也在哈希表中，那么计算两者次数之和，保留最大值