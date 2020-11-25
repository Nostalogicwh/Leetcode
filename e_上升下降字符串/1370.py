class Solution:
    def sortString(self, s: str) -> str:
        t, result = collections.Counter(s), ""
        sort = sorted(t)
        reverse_sort = list(reversed(sort))
        while len(result) < len(s):
            for k in sort:
                if t[k]:
                    result, t[k] = result + k, t[k] - 1
            for k in reverse_sort:
                if t[k]:
                    result, t[k] = result + k, t[k] - 1
        return result