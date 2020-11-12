class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        odd = []
        even = []
        for i in A:
            if i % 2 == 0:
                even.append(i)
            else:
                odd.append(i)
        ans = []
        o = 0
        e = 0
        for i in range(len(A)):
            if i % 2 == 0:
                ans.append(even[e])
                e += 1
            else:
                ans.append(odd[o])
                o += 1
        return ans