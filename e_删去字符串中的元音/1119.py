class Solution:
    def removeVowels(self, S: str) -> str:
        s = ['a','e','i','o','u']
        a = ''
        for i in range(len(S)):
            if S[i] in s:
                continue
            else:
                a += S[i]
        return a
