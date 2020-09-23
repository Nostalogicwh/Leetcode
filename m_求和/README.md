# 题目

求 1+2+...+n ，要求不能使用乘除法、for、while、if、else、switch、case等关键字及条件判断语句（A?B:C）。

# 解题思路
平均计算，乘除法，排除  
迭代 要用while、for，排除
递归 不用if、switch，用逻辑运算  
>n > 0 and n + self.sumNums(n - 1)
