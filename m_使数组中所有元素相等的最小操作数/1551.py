class Solution:
    def minOperations(self, n: int) -> int:
        arr = []
        b = 0
        summ = 0
        ans = 0
        for i in range(n):
            b = 2*i + 1
            arr.append(b)
            summ = summ + b
        summ = summ // n
        for i in range(n):
            if arr[i] >= summ:
                break
            ans = ans + summ - arr[i]
        return ans