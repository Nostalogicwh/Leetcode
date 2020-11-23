class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        n = len(points)
        if n == 0: return 0
        dp = [1] * n
        cnt = 1
        points.sort(key=lambda a:a[1])

        for i in range(n):
            for j in range(0, i):
                if points[i][0] > points[j][1]:
                    dp[i] = max(dp[i], dp[j] + 1)
                    cnt = max(cnt, dp[i])
        return cnt