class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        lookup = collections.defaultdict(int)
        res = 0
        for a in A:
            for b in B:
                lookup[a+b] += 1
        for c in C:
            for d in D:
                res += lookup[-(c + d)]
        return res