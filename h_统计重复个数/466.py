class Solution:
    def getMaxRepetitions(self, s1: str, n1: int, s2: str, n2: int) -> int:
        dp=[]
        for i in range(len(s2)):
            start=i
            end=0
            for j in range(len(s1)):
                if s1[j] == s2[start]:
                    start+=1
                    if start==len(s2):
                        start=0
                        end+=1
            dp.append((start,end))
        res=0
        next=0
        print(dp)
        for _ in range(n1):
            res+=dp[next][1]
            next=dp[next][0]
        return res//n2