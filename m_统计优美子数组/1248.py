class Solution:
    def reverseLeftWords(self, s: str, n: int) -> str:
        a = s[:n]
        b = s[n:]
        return b+a