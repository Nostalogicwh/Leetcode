class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        l = len(s)
        num = ''
        for i in range(l):
            if i < l//2:
                num = s[i]
                s[i] = s[l-i-1]
                s[l-i-1] = num