class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        t = s.split()
        if len(pattern) != len(t):
            return False
        dct = {}
        for i in range(len(pattern)):
            if pattern[i] not in dct:
                if t[i] in dct.values():
                    return False
                dct[pattern[i]] = t[i]
            else:
                if dct[pattern[i]] != t[i]:
                    return False
            print(dct)
        return True