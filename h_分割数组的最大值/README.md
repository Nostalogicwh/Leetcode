# 题目
给定一个非负整数数组和一个整数 m，你需要将这个数组分成 m 个非空的*连续*子数组。设计一个算法使得这 m 个子数组各自和的最大值最小。

# 解题思路
使用二分查找，查找值即为这个子数组和的最大值的最小值x。  
二分查找范围[max(数组)，sum(数组)]。  
设置中值mid，每一个数组和都应小于mid。  
当前数组和＞mid时，结束该数组，开启一个新数组，并计数加一。  
当数组数量大于m时，mid过小，二分查找右半，同理可得数组数量小于m的情况。  
当查找范围只剩一个数时结束。