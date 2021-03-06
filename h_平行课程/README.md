# 题目
已知有 N 门课程，它们以 1 到 N 进行编号。  

给你一份课程关系表 relations[i] = [X, Y]，用以表示课程 X 和课程 Y 之间的先修关系：课程 X 必须在课程 Y 之前修完。  

假设在一个学期里，你可以学习任何数量的课程，但前提是你已经学习了将要学习的这些课程的所有先修课程。  

请你返回学完全部课程所需的最少学期数。  

如果没有办法做到学完全部这些课程的话，就返回 -1。

# 解题思路
有优先级限制的调度问题，使用拓扑排序即可，将这门课所需要的前置课程数量表示为入度  
遍历将所有入度为0的课程上完，并将后置课程的入度减1，重复直到没有课程可上  
入度设置为preClassCount，直接后置课程nextClasses，term表示遍历了几次，将入度为0的课程记录为learn  
时间复杂度O(E+V),E为邻边条数，V为节点个数，空间复杂度同样
