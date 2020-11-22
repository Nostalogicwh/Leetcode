class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        arrs1 = []
        arrs2 = []
        for i in s:
            if i in arrs1:
                continue
            else:
                arrs1.append(i)
        arrs1 = sorted(arrs1)
        for i in t:
            if i in arrs2:
                continue
            else:
                arrs2.append(i)
        arrs2 = sorted(arrs2)
        if arrs1 != arrs2:
            return False
        num1 = []
        num2 = []
        for i in arrs1:
            num1.append(s.count(i))
        for i in arrs1:
            num2.append(t.count(i))
        if num1 == num2:
            return True
        else:
            return False