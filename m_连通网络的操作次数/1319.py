class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        nums=[]
        for i in connections:
            nums.extend(i)            
        nums=list(set(nums))
        n1=n-len(nums)#未连接的结点的个数
        parent=list(range(0,n))
        def find(x):
            if parent[x]==x:
                return x
            parent[x]=find(parent[x])
            return parent[x]
        count=0#记录多余边的个数
        for i in connections:
            x=find(i[0])
            y=find(i[1])
            if x==y:
                count+=1
            else:   
                parent[x]=y
        count1=-1*n1#记录集合的个数
        for i in range(0,len(parent)):
            if i==parent[i]:
                count1+=1
        if count>=(n1+count1-1):
            return n1+count1-1
        else:
            return -1