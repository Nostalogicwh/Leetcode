class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        f={}
        for a in arr:
            if (a-difference) in f:
                f[a]=f[a-difference]+1
            else:
                f[a]=1
        print(f)
        return max(f.values())