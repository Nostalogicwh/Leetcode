class Solution:
    def addToArrayForm(self, A: List[int], K: int) -> List[int]:
        l = len(A)
        tem1 = 0
        for i in range(l):
            tem1 += A[i] * 10**(l-i-1)
        tem1 += K
        tem1 = str(tem1)
        ans = []
        for i in range(len(tem1)):
            ans.append(tem1[i])
        return ans