# 题目
字符串 S 由小写字母组成。我们要把这个字符串划分为尽可能多的片段，同一个字母只会出现在其中的一个片段。返回一个表示每个字符串片段的长度的列表。

# 解题思路
找到开头字母的最后一位位置，检查之前的字母是否全在区间内。  
不在则扩充区间，全在则返回当前长度。