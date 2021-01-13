class Solution(object):
    def findRedundantConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        size = len(edges)
        father = [i for i in range(size+1)]#建立集合，每个点一个集合

        def findrootfather(num):#寻找父亲根一直往上找，找到自己指向自己就是根
            while father[num]!=num:
                num = father[num]
            return num

        def union(num1,num2):#合并两个点，找到父亲节点，把父亲合并上去，一旦发现有同一个父亲就是我们要找的环路
            root1 = findrootfather(num1)
            root2 = findrootfather(num2)
            if root1==root2:
                return True
            else:
                father[root2]=root1
                return False
        for s,e in edges:
            if union(s,e):
                return [s,e]