class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = []
        for i in range(1,numRows+1):
            ans.append([1] * i)
        for i in range(3,numRows+1):
            for j in range(1,i-1):
                ans[i-1][j] = ans[i-2][j-1] + ans[i-2][j]
        return ans