# 题目
给你两个整数，n 和 start 。  
数组 nums 定义为：nums[i] = start + 2\*i（下标从 0 开始）且 n == nums.length 。  
请返回 nums 中所有元素按位异或（XOR）后得到的结果。

# 解题思路
异或操作  
- 0 ^ x = x
- x ^ x = 0
- 2x ^ (2x+1) = 1  
从第二位逐步与start+2\*i进行异或运算即可