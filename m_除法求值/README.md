# 题目
给你一个变量对数组 equations 和一个实数值数组 values 作为已知条件，其中 equations[i] = [Ai, Bi] 和 values[i] 共同表示等式 Ai / Bi = values[i] 。每个 Ai 或 Bi 是一个表示单个变量的字符串。  

另有一些以数组 queries 表示的问题，其中 queries[j] = [Cj, Dj] 表示第 j 个问题，请你根据已知条件找出 Cj / Dj = ? 的结果作为答案。  

返回 所有问题的答案 。如果存在某个无法确定的答案，则用 -1.0 替代这个答案。

# 解题思路
先构造图，使用dict实现，其天然的hash可以在in判断时做到O(1)复杂度。  

对每个equation如"a/b=v"构造a到b的带权v的有向边和b到a的带权1/v的有向边，  

之后对每个query，只需要进行dfs并将路径上的边权重叠乘就是结果了，如果路径不可达则结果为-1。