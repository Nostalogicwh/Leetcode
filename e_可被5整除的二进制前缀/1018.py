class Solution:
    def prefixesDivBy5(self, A: List[int]) -> List[bool]:
        tsum=0
        for i,num in enumerate(A):
            tsum=(tsum*2+num)%5
            A[i]=(tsum%5==0)
        return A