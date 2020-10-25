class Solution:
    def longestMountain(self, A: List[int]) -> int:
        n = len(A)
        left = [0] * n   #  左边有几个连续递减的数
        right = [0] * n  #  右边有几个连续递减的数

        for i in range(1, n):
            if A[i] > A[i - 1]:
                left[i] = left[i - 1] + 1
        for i in range(n - 2, -1, -1):
            if A[i] > A[i + 1]:
                right[i] = right[i + 1] + 1

        ans = 0
        for i in range(1, n - 1):
            if left[i] > 0 and right[i] > 0:
                ans = max(ans, left[i] + right[i] + 1)
        
        return ans