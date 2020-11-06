class Solution:
    def transpose(self, A: List[List[int]]) -> List[List[int]]:
        col = len(A)
        row = len(A[0])

        ans = [[0 for _ in range(col)] for j in range(row)]
        print(ans)
        for i in range(col):
            for j in range(row):
                ans[j][i] = A[i][j]
        return ans