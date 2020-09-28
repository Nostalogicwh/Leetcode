class Solution:
    def minimumOperations(self, leaves: str) -> int:
        n = len(leaves)
        y = [0]
        for i in range(n):
            y.append(y[-1] + (leaves[i] == 'y'))


        t = [None] * (n + 1)
        t[n] = float('INF')
        for i in range(n - 1, -1, -1):
            t[i] = min(t[i + 1], i - 2 * y[i])
        ans = float('INF')
        for p1 in range(n - 2, 0, -1):
            ans = min(ans, y[n] + 2 * y[p1] - p1 + t[p1 + 1])
        return ans