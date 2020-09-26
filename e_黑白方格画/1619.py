class Solution:
    def paintingPlan(self, n: int, k: int) -> int:
        if k in (0,n*n):
            return 1
        def get(n,a):
            #计算组合公式迭代版
            res = 1
            for i in range(n,n-a,-1):
                res*=i
            for j in range(1,a+1):
                res/=j
            return res       
        ans=0
        for i in range(n):
            for j in range(n):
                if n*(i+j)-(i*j) ==k:
                    ans+=get(n,i)*get(n,j)             
        return int(ans)