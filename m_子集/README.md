# 题目
给定一组不含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。  

说明：解集不能包含重复的子集。

# 解题思路
回溯法，用一个index指向每一次的元素，下一层更新index=index+1  
考虑选或不选当前答案，保存当前index指向元素