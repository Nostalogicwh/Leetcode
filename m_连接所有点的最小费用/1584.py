class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        plen = len(points)
        if plen < 2:
            return 0
        f,ans={},0
        def find(x):
            f.setdefault(x,x)
            while f[x]!=x:
                f[x]=f[f[x]]
                x=f[x]
            return x
        def union(x,y):
            f[find(x)]=find(y)
        cost_list=[]
        for i in range(len(points)-1):
            for j in range(1,len(points)):
                xi,yi=points[i]
                xj,yj=points[j]
                cost=abs(xi-xj)+abs(yi-yj)
                cost_list.append((cost,i,j))
        cost_list.sort(key=lambda x:x[0])
        for cost,i,j in cost_list:
            if find(i)!=find(j):
                union(i,j)
                ans+=cost
        return ans