class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        n = len(intervals)
        if n == 0: 
        	return 0
        dp = [1] * n
        ans = 1
        intervals.sort(key=lambda a: a[0])

        for i in range(len(intervals)):
            for j in range(i - 1, -1, -1):
                if intervals[i][0] >= intervals[j][1]:
                    dp[i] = max(dp[i], dp[j] + 1)
                    break # 由于是按照开始时间排序的, 因此可以剪枝
                
        return n - max(dp)