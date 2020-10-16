class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        count = 0
        for j in range(n):
            for i in range(0, j + 1):
                length = j - i + 1
                if length == 1:
                    dp[i][j] = True
                    count += 1
                if length == 2 and s[i] == s[j]:
                    dp[i][j] = True
                    count += 1
                if length > 2 and s[i] == s[j] and dp[i+1][j-1] is True:
                    dp[i][j] = True
                    count += 1
        return count