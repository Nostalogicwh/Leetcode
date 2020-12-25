class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        ans = 0
        n = len(g)
        m = len(s)
        i = j = 0
        while i < n and j < m:
            while j < m and g[i] > s[j]:
                j += 1
            if j < m:
                ans += 1
            i += 1
            j += 1
        return ans
