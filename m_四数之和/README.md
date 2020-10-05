# 题目
给定一个包含 n 个整数的数组 nums 和一个目标值 target，判断 nums 中是否存在四个元素 a，b，c 和 d ，使得 a + b + c + d 的值与 target 相等？找出所有满足条件且不重复的四元组。  

*注意：*  

答案中不可以包含重复的四元组。

# 解题思路
常规解法会超时，时间复杂度为O(N^4)  
增加两个判断条件：  
> nums[i]+3\*nums[i+1]>target 此时直接break
> nums[i]+3\*nums[-1]<target 此时continue  

在第二层第三层循环也加入判断即可满足要求